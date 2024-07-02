import pathlib
import random
import cv2
from pathlib import Path


def getFile() -> Path:
    video_folder = Path('Videos')
    video_folder = Path(__file__).resolve().parent / video_folder
    video_files = [file for file in video_folder.iterdir() if file.is_file() and file.suffix in ['.mp4', '.avi', '.mkv']]

    if not video_files:
        print("Videos folder is empty")
    else:
        video = random.choice(video_files)
        print(f"Video selected: {video}")
        return video 



def getFrame(file_path: Path):
    file_path_str = str(file_path)
    print(file_path_str)
    vidcap = cv2.VideoCapture(file_path_str)

    totalFrames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    randomFrameNumber=random.randint(0, totalFrames)

    vidcap.set(cv2.CAP_PROP_POS_FRAMES,randomFrameNumber)

    success, image = vidcap.read()

    if success:
        cv2.imwrite("random_frame.jpg", image)


file_path = getFile()
getFrame(file_path)
print("got here")