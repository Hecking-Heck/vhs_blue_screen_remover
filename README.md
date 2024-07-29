# Blue Screen Remover

This script processes an MP4 video file to detect and remove segments with a blue screen. It is especially useful for cleaning up old VHS tapes that have been digitized.

## Features

- Detects blue screen segments in a video.
- Removes the detected blue screen segments.
- Outputs a cleaned video without the blue screens.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Hecking-Heck/blue_screen_remover.git
    cd blue_screen_remover
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Place your input video file (`input.mp4`) in the same directory as the script.
2. Run the script:
    ```sh
    python blue_screen_remover.py
    ```

3. The output video (`output.mp4`) will be saved in the same directory.

## Example

```sh
python blue_screen_remover.py
