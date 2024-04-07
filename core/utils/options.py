# Multi-sample Anti-aliasing (might not work)
ANTIALIASING = 0
# Conditional Rendering with Occlusion queries
ADVANCED_OPENGL = False  # Not recommended unless using NVIDIA cards.
# Might cause more slowdowns that speed-ups.
DOUBLE_BUFFER = True
DEPTH_SIZE = 32
WIDTH = 1000
HEIGHT = 562
is_white = False
SMOOTH_FPS = True
VSYNC = False
# Max CPU ahead frames
MAX_CPU_AHEAD_FRAMES = 3  # Number of frames the CPU can be ahead of the GPU until waiting for it to finish rendering.
# Higher values gives higher frame-rate but causes frame-rate instability and higher frame spikes,
# Lower values causes average lower frame-rate but gives smoother frame-rate
# Recommended values are between 0 and 9

# Legacy Smooth FPS
SMOOTH_FPS = True  # Legacy way to force the flushing of command buffer and forces the CPU to wait for the GPU to
# finish rendering.
# Incompatible Max CPU Ahead Frames (it won't be effective)
# Enable this to test whether its impact is better. Similar to Max CPU Ahead frames to 0
"""STARTUP"""
command_line = True
"""DEBUGGING"""
DEBUG = False
MEDIA_DEBUG = False  # lags the program
DEBUG_GL = True
SHADOW_WINDOW = False
"""OPTIONAL MAX FPS"""
OPMAXFPS = True
MAXFPS = float("inf")