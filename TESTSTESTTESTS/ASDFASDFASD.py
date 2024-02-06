import pyglet

class ImageButton:
    def __init__(self, x, y, width, height, image_path, on_click):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image_path = image_path
        self.on_click = on_click

        # Load the image
        self.image = pyglet.image.load(image_path)

        # Create a sprite for the image
        self.image_sprite = pyglet.sprite.Sprite(self.image, x=self.x, y=self.y)

        # Flag to track whether the button is currently pressed
        self.is_pressed = False

    def draw(self):
        # Draw the image sprite with a tint based on the button's pressed state
        self.image_sprite.color = (100, 100, 255) if self.is_pressed else (255, 255, 255)
        self.image_sprite.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        # Check if the mouse click is within the button bounds
        if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
            # Set the button as pressed
            self.is_pressed = True
            # Call the on_click function when the button is clicked
            self.on_click()

    def on_mouse_release(self, x, y, button, modifiers):
        # Reset the button's pressed state when the mouse is released
        self.is_pressed = False


# Create a window
window = pyglet.window.Window(width=400, height=300, caption='Pyglet Image Button Example')

# Create a button callback function
def on_image_button_click():
    print("Image button clicked!")

# Set the path to the image file
image_path = ''

# Create an image button instance
image_button = ImageButton(x=150, y=100, width=100, height=50, image_path="C:/Users/leibniz/Pictures/windows icons/Python-Operating-System/TESTSTESTTESTS/image.png", on_click=on_image_button_click)

@window.event
def on_draw():
    window.clear()
    image_button.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    image_button.on_mouse_press(x, y, button, modifiers)

@window.event
def on_mouse_release(x, y, button, modifiers):
    image_button.on_mouse_release(x, y, button, modifiers)

# Run the application
pyglet.app.run()
