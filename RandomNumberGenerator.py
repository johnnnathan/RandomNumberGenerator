import argparse
import math
import pathlib
import random
import cv2
from pathlib import Path
from PIL import Image

PATH_PRINTED = False
RANDOM_FRAME = "random_frame.jpg"
INFINITY = math.inf
LIMIT = INFINITY
BASE_LIMIT = LIMIT
FILE_PATH = None
VERBOSE = None

def printVideoName(name: str):
    global PATH_PRINTED

    if not PATH_PRINTED and VERBOSE:
        print(f"Video selected: {name}")
        PATH_PRINTED = True


def getChosenColorIndex(listRGB: list) -> int:
    totalValueOfRGB = listRGB[0] + listRGB[1] + listRGB[2]
    index = totalValueOfRGB % 3
    return index


def getFile() -> Path:
    video_folder = Path('Videos')
    video_folder = Path(__file__).resolve().parent / video_folder
    video_files = [file for file in video_folder.iterdir() if
                   file.is_file() and file.suffix in ['.mp4', '.avi', '.mkv']]

    if not video_files and VERBOSE:
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


def resetLimit():
    global LIMIT
    LIMIT = BASE_LIMIT


def setLimit(Limit: int):
    global LIMIT
    LIMIT = Limit


def getNumber() -> int:
    global FILE_PATH
    if not FILE_PATH:
        FILE_PATH = getFile()
    getFrame(FILE_PATH)
    listRGB = getTotalRGB()
    index = getChosenColorIndex(listRGB)
    return int(listRGB[index] % LIMIT)


def main(minAcceptable: int):
    total = ""
    while (len(str(total)) < minAcceptable):
        cur = abs(getNumber())
        total = str(total) + str(cur)
        setLimit(int(len(str(total)) - minAcceptable))
    print(total)
    if VERBOSE:
        print("Length:" + str(len(total)))
    return int(total)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a random number with a specified number of digits.')
    parser.add_argument('digits', type=int, help='The number of digits for the random number')
    parser.add_argument('--verbose', action='store_true', help='Enable print statements')
    args = parser.parse_args()
    VERBOSE = args.verbose
    main(args.digits)
