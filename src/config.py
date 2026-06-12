"""
config.py

Project configuration settings for
Real-Time Object Detection on PYNQ-Z2
"""

# Dataset Location
IMAGE_DIR = "/home/xilinx/jupyter_notebooks/data_sets"

# Supported Image Formats
IMAGE_EXTENSIONS = ["*.jpg", "*.png", "*.jpeg"]

# Detection Parameters
CONFIDENCE_THRESHOLD = 0.6
NMS_THRESHOLD = 0.4

# HOG Detection Parameters
WIN_STRIDE = (8, 8)
PADDING = (16, 16)
SCALE = 1.03

# Display Parameters
FIGURE_SIZE = (6, 4)

# Resize Width
RESIZE_WIDTH = 640
