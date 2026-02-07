import os
import cv2
from torch.utils.data import Dataset

class FrameDataset(Dataset):
    def __init__(self, frames_dir):
        self.frames_dir = frames_dir
        self.frames = os.listdir(frames_dir)

    def __len__(self):
        return len(self.frames)

    def __getitem__(self, idx):
        frame_path = os.path.join(self.frames_dir, self.frames[idx])
        frame = cv2.imread(frame_path)
        return frame
