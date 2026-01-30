import cv2
import os

def extract_frames(video_path, output_dir):
    cap = cv2.VideoCapture(video_path)
    count = 0
    os.makedirs(output_dir, exist_ok=True)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imwrite(f"{output_dir}/frame_{count}.jpg", frame)
        count += 1

    cap.release()
    print(f"{count} frames extracted.")

if __name__ == "__main__":
    extract_frames("sample.mp4", "frames")
