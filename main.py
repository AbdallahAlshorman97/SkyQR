from video_capture.webcam_stream import WebcamStream
from qr_processing.detector import detect_qrcodes
from qr_processing.qr_parser import parse_qr_content
from utils.logger import log_qr_data
from utils.fps_tracker import FPSTracker
import cv2


def main():
    cap = WebcamStream().start()
    fps = FPSTracker()

    while True:
        frame = cap.read()
        if frame is None:
            break

        decoded_objects, annotated_frame = detect_qrcodes(frame)

        for obj in decoded_objects:
            content = obj.data.decode("utf-8")
            parsed = parse_qr_content(content)
            log_qr_data(parsed)

        cv2.imshow("QR Code Scanner", annotated_frame)
        fps.update()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.stop()
    fps.stop()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
