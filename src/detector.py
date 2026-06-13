"""
detector.py

Human detection module using
OpenCV HOG + SVM detector.
"""

import cv2

from config import (
    CONFIDENCE_THRESHOLD,
    WIN_STRIDE,
    PADDING,
    SCALE
)


class HumanDetector:
    """
    Human Detection Engine
    """

    def __init__(self):

        self.hog = cv2.HOGDescriptor()

        self.hog.setSVMDetector(
            cv2.HOGDescriptor_getDefaultPeopleDetector()
        )

    def detect(self, image):
        """
        Detect humans in image.

        Parameters:
            image : Input image

        Returns:
            list : Bounding boxes
        """

        rects, weights = self.hog.detectMultiScale(
            image,
            winStride=WIN_STRIDE,
            padding=PADDING,
            scale=SCALE
        )

        boxes = []

        for (x, y, w, h), weight in zip(rects, weights):

            if weight > CONFIDENCE_THRESHOLD:

                boxes.append(
                    [x, y, x + w, y + h]
                )

        return boxes
