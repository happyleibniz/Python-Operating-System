import pyglet
from core.exceptions.exceptions_ import *
from tkinter.filedialog import askopenfilename


class Program:  # Must be the class name Program
    def __init__(self):
        if pyglet.media.have_ffmpeg():
            self.video_path = askopenfilename(
                title='Open a file',
                initialdir='/',
                filetypes=(("mp4 video files", ".mp4"),
                           ("mkv files", ".mkv"),)
            )
            self.player = pyglet.media.Player()
            self.source = pyglet.media.StreamingSource()
            print(self.video_path)
            self.Media = pyglet.media.load(self.video_path)
        else:
            raise No_FFMPEG_Exception(
                "You have not installed ffmpeg, please see "
                "https://pyglet.readthedocs.io/en/latest/programming_guide/media.html#ffmpeg-installation"
            )

    def blit_media(self):
        self.player.queue(self.Media)
        self.player.play()
        if self.player.source and self.player.source.video_format:
            self.player.get_texture().blit(0, 0)

    def pause(self):
        self.player.pause()

    def queue_media(self):
        self.player.queue(self.Media)

    def resume(self):
        self.player.play()
