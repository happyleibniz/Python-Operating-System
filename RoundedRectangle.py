from pyglet.shapes import ShapeBase, get_default_shader, _rotate_point
import math
from pyglet.gl import GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA
from pyglet.gl import GL_LINES
from pyglet.graphics import Batch


class RoundedRectangleFill(ShapeBase):

    def __init__(self, x, y, width, height, radius, segments=None, color=(255, 255, 255, 255), batch=None, group=None):

        self._x = x
        self._y = y
        self._w = width
        self._h = height
        self._radius = radius

        self._segments = segments or max(14, int(self._radius / 1.25))
        self._num_triangles = (4 * self._segments) + 6
        self._num_verts = 3 * self._num_triangles

        r, g, b, *a = color
        self._rgba = r, g, b, a[0] if a else 255

        self._rotation = 0  # how do I implement this?

        program = get_default_shader()
        self._batch = batch or Batch()
        self._group = self.group_class(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, program, group)

        self._create_vertex_list()
        self._update_vertices()

    def _create_vertex_list(self):
        self._vertex_list = self._group.program.vertex_list(
            self._num_verts, self._draw_mode, self._batch, self._group,
            colors=('Bn', self._rgba * self._num_verts),
            translation=('f', (0, 0) * self._num_verts))

    def _arc_outer_points(self, cx, cy, start_angle):
        """Calculate the points on perimeter of each corner arc"""
        tau_segs = math.pi / 2 / self._segments  # quarter circle
        return [(cx + self._radius * math.cos(i * tau_segs + start_angle),
                 cy + self._radius * math.sin(i * tau_segs + start_angle)) for i in range(self._segments + 1)]

    def _rect_to_tri(self, left, bottom, right, top):
        """
        Convert rectangle to triangles
        Each rectangle is formed by 2 triangles
        """
        tri_a = [(left, bottom), (right, bottom), (right, top)]
        tri_b = [(right, top), (left, top), (left, bottom)]
        return [tri_a, tri_b]

    def _generate_arcs(self):
        outer_points = []
        for i in range(4):
            cx = self._x + self._radius if i in [1, 2] else self._x + self._w - self._radius
            cy = self._y + self._radius if i in [2, 3] else self._y + self._h - self._radius
            angle = math.pi * (i / 2)
            corner_outer_points = self._arc_outer_points(cx, cy, angle)
            outer_points += corner_outer_points
        return outer_points

    def _generate_rectangles(self):
        rect_a = self._rect_to_tri(self._x + self._radius, self._y + self._h - self._radius,
                                   self._x + self._w - self._radius, self._y + self._h)
        rect_b = self._rect_to_tri(self._x + self._radius, self._y, self._x + self._w - self._radius,
                                   self._y + self._radius)
        rect_c = self._rect_to_tri(self._x, self._y + self._radius, self._x + self._w, self._y + self._h - self._radius)
        return rect_a + rect_b + rect_c

    def _generate_corners(self):
        arcs = self._generate_arcs()
        corners = []
        for i in range(4):
            points = arcs[i * (self._segments + 1):(i + 1) * (self._segments + 1)]
            cx = self._x + self._radius if i in [0, 3] else self._x + self._w - self._radius
            cy = self._y + self._radius if i in [0, 1] else self._y + self._h - self._radius
            corner_triangles = self._partial_arc_to_tri(points, cx, cy)
            corners += corner_triangles
        return corners

    def _partial_arc_to_tri(self, points, cx, cy):
        triangles = []
        for j in range(len(points) - 1):
            first_point = (cx, cy)
            second_point = tuple(points[j])
            third_point = tuple(points[j + 1])
            triangle = [first_point, second_point, third_point]
            triangles.append(triangle)
        return triangles

    def _get_center(self):
        x = self._x + self._w / 2
        y = self._y + self._h / 2
        return x, y

    def _rotate_around_center(self, points):
        """Rotate a list of points around this objects center by self._rotation degrees."""
        center = self._get_center()
        return [_rotate_point(center, point, math.radians(self._rotation)) for point in points]

    def _shape_parts_to_points(self, shape_parts):
        """
        Converts "shape parts" into list of tuples
        In other words, converts [[(), (), ()], [(), ()]] to [(), (), (), (), ()]
        """
        all_points = [point for shape_part in shape_parts for point in shape_part]
        return all_points

    def _points_to_flat(self, points):
        """
        convert a list of tuples to a list of numbers
        In other words, converts [(), (), (), (), ()] to [, , , , , , , ,]
        """
        flat_list = [coordinate for point in points for coordinate in point]
        return flat_list

    def _update_vertices(self):
        if not self._visible:
            vertices = (0, 0) * self._num_verts
        else:
            rectangles = self._generate_rectangles()
            corners = self._generate_corners()
            shape_parts = rectangles + corners
            all_points = self._shape_parts_to_points(shape_parts)
            rotated_points = self._rotate_around_center(all_points)
            vertices = self._points_to_flat(rotated_points)
        self._vertex_list.position[:] = vertices

    def _update_color(self):
        self._vertex_list.colors[:] = self._rgba * self._num_verts

    def __contains__(self, point):
        assert len(point) == 2

        center = self._get_center()
        point = _rotate_point(center, point, -math.radians(self._rotation))
        px, py = point

        inside_bounding = (self._x <= px <= self._x + self._w and self._y <= py <= self._y + self._h)

        if not inside_bounding:
            return False

        # For corners, check if point is inside corner circles
        inside_circle = False
        for i in range(4):
            center_dx = self._radius if i == 0 or i == 1 else self._w - self._radius
            center_dy = self._radius if i == 0 or i == 3 else self._h - self._radius
            center_x, center_y = self._x + center_dx, self._y + center_dy  # center of this corner's circle
            outside_corner_circle = math.sqrt((center_x - px) ** 2 + (center_y - py) ** 2) > self._radius
            if outside_corner_circle:
                inside_circle = True
                break

        if not inside_circle:
            return False

        return True

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = min(max(0, value), self._w / 2, self._h / 2)
        self._update_vertices()

    @property
    def width(self):
        """The width of the rectangle.

        :type: float
        """
        return self._w

    @width.setter
    def width(self, value):
        self._w = max(0, value, self._radius * 2)
        self._update_vertices()

    @property
    def height(self):
        """The height of the rectangle.

        :type: float
        """
        return self._h

    @height.setter
    def height(self, value):
        self._h = max(0, value, self._radius * 2)
        self._update_vertices()

    @property
    def color(self):
        """
        Each color component must be in the range 0 (dark) to 255 (saturated).
        :type: (int, int, int, int)
        """
        return self._rgba

    @color.setter
    def color(self, values):
        r, g, b, *a = values

        if a:
            alpha = a[0]
        else:
            alpha = self._rgba[3]

        self._rgba = r, g, b, alpha
        self._update_color()

    @property
    def rotation(self):
        """in degrees."""
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        self._rotation = rotation
        self._update_vertices()


class RoundedRectangleBorder(ShapeBase):
    _draw_mode = GL_LINES

    # _draw_mode = GL_TRIANGLES
    def __init__(self, x, y, width, height, radius, color=(255, 255, 255, 255), batch=None, group=None):

        self._x = x
        self._y = y
        self._w = max(0, width)
        self._h = max(0, height)
        self._radius = min(max(0, radius), self._w / 2, self._h / 2)

        self._segments = max(14, int(self._radius / 1.25))
        self._num_verts = 8 * (self._segments + 1)

        r, g, b, *a = color
        self._rgba = r, g, b, a[0] if a else 255

        self._rotation = 0  # how do I implement this?

        program = get_default_shader()
        self._batch = batch or Batch()
        self._group = self.group_class(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, program, group)

        self._create_vertex_list()
        self._update_vertices()

    def _create_vertex_list(self):
        self._vertex_list = self._group.program.vertex_list(
            self._num_verts, self._draw_mode, self._batch, self._group,
            colors=('Bn', self._rgba * self._num_verts),
            translation=('f', (self._x, self._y) * self._num_verts))

    def _arc_outer_points(self, cx, cy, start_angle):
        # Calculate the points in each corner arc
        tau_segs = math.pi / 2 / self._segments  # quarter circle
        return [(cx + self._radius * math.cos(i * tau_segs + start_angle),
                 cy + self._radius * math.sin(i * tau_segs + start_angle)) for i in range(self._segments + 1)]

    def _update_vertices(self):
        if not self._visible:
            vertices = (0,) * (self._segments + 1) * 4
        else:
            outer_points = []

            # calculate points for each corner
            for i in range(4):
                dx = self._radius if i == 0 or i == 3 else self._w - self._radius
                dy = self._radius if i == 0 or i == 1 else self._h - self._radius
                angle = math.pi * (i / 2)  # start angle for each corner
                outer_points += self._arc_outer_points(self._x - dx, self._y - dy, angle)

            # Create a list of doubled-up points from outer points:
            vertices = []
            for i in range(-1, len(outer_points) - 1):
                line_points = *outer_points[i], *outer_points[i + 1]
                vertices.extend(line_points)

        print(len(self._vertex_list.position), len(vertices))
        self._vertex_list.position[:] = vertices

    def __contains__(self, point):
        assert len(point) == 2
        px, py = point

        inside_bounding = (self._x <= px <= self._x + self._w and self._y <= py <= self._y + self._h)

        if not inside_bounding:
            return False

        # For corners, check if point is inside corner circles
        inside_circle = False
        for i in range(4):
            center_dx = self._radius if i == 0 or i == 1 else self._w - self._radius
            center_dy = self._radius if i == 0 or i == 3 else self._h - self._radius
            center_x, center_y = self._x + center_dx, self._y + center_dy  # center of this corner's circle
            outside_corner_circle = math.sqrt((center_x - px) ** 2 + (center_y - py) ** 2) > self._radius
            if outside_corner_circle:
                inside_circle = True
                break

        if not inside_circle:
            return False

        return True
