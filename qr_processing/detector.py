import cv2
from pyzbar import pyzbar
import numpy as np


def detect_qrcodes(frame):
    decoded_objects = pyzbar.decode(frame)

    for obj in decoded_objects:
        points = obj.polygon
        if len(points) > 4:  # Fix for irregular polygon shapes
            hull = cv2.convexHull(
                np.array([pt for pt in points], dtype=np.float32)
            )
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points

        # Draw the bounding box
        n = len(hull)
        for j in range(0, n):
            cv2.line(frame, hull[j], hull[(j + 1) % n], (0, 255, 0), 2)

        # Draw the decoded text
        x, y, w, h = obj.rect
        text = obj.data.decode("utf-8")
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    return decoded_objects, frame
