import time

class FPSTracker:
    def __init__(self):
        self.start_time = time.time()
        self.frame_count = 0

    def update(self):
        self.frame_count += 1
        if self.frame_count % 30 == 0:
            elapsed = time.time() - self.start_time
            fps = self.frame_count / elapsed
            print(f"[INFO] Approx. FPS: {fps:.2f}")

    def stop(self):
        elapsed = time.time() - self.start_time
        fps = self.frame_count / elapsed if elapsed > 0 else 0
        print(f"[INFO] Total frames: {self.frame_count}, Avg FPS: {fps:.2f}")
