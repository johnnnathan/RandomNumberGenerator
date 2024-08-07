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
- Pillow (`PIL`)
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

Run the Python script to generate a random number. You can use the following command-line arguments:

    digits: The number of digits for the random number (required).
    --verbose: Enable verbose output to see additional details (optional).

Example usage:

```bash
python RandomNumberGenerator.py 10 --verbose
```

This command will generate a random number with 10 digits and print additional details if --verbose is enabled.
