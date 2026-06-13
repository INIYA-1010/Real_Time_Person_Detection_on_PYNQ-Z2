"""
main.py

Real-Time Object Detection on PYNQ-Z2

Main application entry point.
"""

import cv2
import glob
import matplotlib.pyplot as plt
import time

from config import (
    IMAGE_DIR,
    IMAGE_EXTENSIONS,
    RESIZE_WIDTH,
    FIGURE_SIZE,
    NMS_THRESHOLD
)

from detector import HumanDetector
from nms import non_max_suppression
from benchmark import Benchmark


def get_image_paths():
    """
    Load all supported image paths.
    """

    image_paths = []

    for ext in IMAGE_EXTENSIONS:
        image_paths.extend(
            glob.glob(f"{IMAGE_DIR}/{ext}")
        )

    return sorted(image_paths)


def resize_image(image):
    """
    Resize image while maintaining aspect ratio.
    """

    h, w = image.shape[:2]

    scale = RESIZE_WIDTH / w

    return cv2.resize(
        image,
        (RESIZE_WIDTH, int(h * scale))
    )


def draw_boxes(image, boxes):
    """
    Draw detection boxes.
    """

    for (x1, y1, x2, y2) in boxes:

        cv2.rectangle(
            image,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            image,
            "Person",
            (x1, y1 - 6),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

    return image


def display_result(image, title):
    """
    Display detection result.
    """

    image_rgb = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB
    )

    plt.figure(figsize=FIGURE_SIZE)

    plt.imshow(image_rgb)

    plt.title(title)

    plt.axis("off")

    plt.show()


def main():

    image_paths = get_image_paths()

    print(
        f"Total images found: {len(image_paths)}"
    )

    detector = HumanDetector()

    benchmark = Benchmark()

    total_start = time.time()

    for image_path in image_paths:

        image = cv2.imread(image_path)

        if image is None:
            continue

        image = resize_image(image)

        start = time.time()

        boxes = detector.detect(image)

        final_boxes = non_max_suppression(
            boxes,
            overlap_thresh=NMS_THRESHOLD
        )

        latency = time.time() - start

        benchmark.add_latency(latency)

        image = draw_boxes(
            image,
            final_boxes
        )

        display_result(
            image,
            f"{image_path.split('/')[-1]} | Detected: {len(final_boxes)}"
        )

    total_time = time.time() - total_start

    results = benchmark.get_results(
        total_time
    )

    benchmark.print_results(results)


if __name__ == "__main__":
    main()
