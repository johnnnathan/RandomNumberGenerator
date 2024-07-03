# RNG by Dimitrios Tsiplakis

**RandomNumberGenerator** is a Python tool that generates random numbers using audio-visual mediums such as video files. Future updates will include support for images and audio tracks.

## Features

- **Video Support:** Selects a random frame from a randomly chosen video file to generate a random number.
- **Planned Features:**
  - **Image Support:** Generate random numbers using images (Under Development).
  - **Audio Support:** Generate random numbers using audio tracks (Under Development).

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- pathlib
- random

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/RandomNumberGenerator.git
    cd RandomNumberGenerator
    ```

2. Install the required Python libraries:

    ```bash
    pip install opencv-python
    pip install pillow
    ```

3. Populate the `Videos` folder with your video files (`.mp4`, `.avi`, `.mkv`).

## Usage

Run the Python script to generate a random number:

```bash
python RandomNumberGenerator.py
