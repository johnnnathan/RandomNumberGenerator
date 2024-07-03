import pathlib
import random
import cv2
from pathlib import Path
from PIL import Image


RANDOM_FRAME = "random_frame.jpg"
LIMIT = 1000

def printVideoName(name: str):
    print(f"Video selected: {name}")


def getChosenColorIndex(listRGB: list) -> int:
    totalValueOfRGB = listRGB[0] + listRGB[1] + listRGB[2]
    index = totalValueOfRGB % 3
    return index


def getFile() -> Path:
    video_folder = Path('Videos')
    video_folder = Path(__file__).resolve().parent / video_folder
    video_files = [file for file in video_folder.iterdir() if
                   file.is_file() and file.suffix in ['.mp4', '.avi', '.mkv']]

    if not video_files:
        print("Videos folder is empty")
    else:
        video = random.choice(video_files)
        printVideoName(video)
        return video


def getFrame(file_path: Path):
    file_path_str = str(file_path)
    vidcap = cv2.VideoCapture(file_path_str)

    totalFrames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    randomFrameNumber = random.randint(0, totalFrames)

    vidcap.set(cv2.CAP_PROP_POS_FRAMES, randomFrameNumber)

    success, image = vidcap.read()

    if success:
        cv2.imwrite(RANDOM_FRAME, image)


def getTotalRGB() -> list[int]:
    im = Image.open(RANDOM_FRAME)
    listRGB = [0, 0, 0]
    width, height = im.size
    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x, y))
            listRGB[0] += r
            listRGB[1] += g
            listRGB[2] += b

    return listRGB


def main():
    file_path = getFile()
    getFrame(file_path)
    listRGB = getTotalRGB()
    index = getChosenColorIndex(listRGB)
    print(listRGB[index] % LIMIT)


if __name__ == "__main__":
    main()
