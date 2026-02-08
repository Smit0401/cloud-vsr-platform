from preprocess import extract_frames
from dataset import FrameDataset
from model import VSRModel

def run():
    print("Running VSR pipeline...")

    # Step 1: Extract frames (example path)
    extract_frames("sample.mp4", "frames")

    # Step 2: Load dataset
    dataset = FrameDataset("frames")
    print(f"Loaded {len(dataset)} frames")

    # Step 3: Initialize model
    model = VSRModel()
    print("Model initialized")

if __name__ == "__main__":
    run()
