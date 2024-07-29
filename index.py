# This script will detect blue frames with in a video and will cut them out
# I am not sure if this is a very niche use case but it works well for me so I will be releasing it to the world

# Imports
from moviepy.editor import VideoFileClip, concatenate_videoclips # Used to actually process the video
from tqdm import tqdm # Used for a cool little progress bar
import numpy as np # Used for mathmatical stuff

# Function to detect blue frames
def is_blue_frame(frame, threshold=200):
    """
    Determine if a frame is predominantly blue.
    
    Parameters:
    - frame: The video frame to analyze.
    - threshold: The intensity threshold for the blue channel to consider the frame as a blue screen.
    
    Returns:
    - True if the frame is predominantly blue, False otherwise.
    """
    blue_channel = frame[:, :, 2]  # Extract the blue channel
    return np.mean(blue_channel) > threshold  # Check if mean blue intensity exceeds the threshold

# Load video
clip = VideoFileClip("input.mp4") # Make sure to change the name to your file name

# Initialize variables
non_blue_segments = []
start = None
is_blue = False

# Create a tqdm progress bar
frame_count = int(clip.fps * clip.duration)  # Total number of frames in the 60-second clip
progress_bar = tqdm(total=frame_count, desc="Processing frames", unit="frame")

# Detect segments without blue screens
for t, frame in clip.iter_frames(with_times=True):
    if is_blue_frame(frame):
        if not is_blue:
            # We've encountered a blue frame after a non-blue segment
            if start is not None:
                non_blue_segments.append((start, t))
            is_blue = True
            start = None
    else:
        if is_blue:
            # We've encountered a non-blue frame after a blue segment
            is_blue = False
            start = t
        elif start is None:
            # Start of a new non-blue segment
            start = t
    
    # Update the progress bar
    progress_bar.update(1)

# Close the progress bar
progress_bar.close()

# Handle the last segment if it is not blue
if not is_blue and start is not None:
    non_blue_segments.append((start, clip.duration))

# Debugging: Print the segments detected
print("Non-blue segments detected:", non_blue_segments)

# Cut and concatenate segments
final_clips = [clip.subclip(start, end) for start, end in non_blue_segments if start != end]

# Check if there are segments to concatenate
if final_clips:
    final_video = concatenate_videoclips(final_clips)
    # Save final video
    final_video.write_videofile("output.mp4", codec="libx264") # You can rename the output filename as you wish
else:
    print("No non-blue segments found.")
