from PIL import Image
import math
import os
from moviepy.editor import ImageSequenceClip
import imageio
import numpy as np
from PIL import Image
import io
from tqdm import tqdm
from pytube import YouTube


def file_to_binary():
    # get file size
    dir_path = os.getcwd()
    for file_name in os.listdir(dir_path):
        if file_name.endswith('.mkv'):
            print(file_name)
            file_name=file_name
            break
    file_size = os.path.getsize(file_name)

    # read file as binary and convert to string of 0's and 1's
    binary_string = ""
    with open(file_name, "rb") as f:
        for chunk in tqdm(iterable=iter(lambda: f.read(1024), b""), total=math.ceil(file_size/1024), unit="KB"):
            binary_string += "".join(f"{byte:08b}" for byte in chunk)

    return binary_string

    # write binary string to text file


def binary_to_video(bin_string, width=1920, height=1080, pixel_size=4, fps=24):
    # Calculate the total number of pixels needed to represent the binary string
    num_pixels = len(bin_string)

    # Calculate the number of pixels that can fit in one image
    pixels_per_image = (width // pixel_size) * (height // pixel_size)

    # Calculate the number of images needed to represent the binary string
    num_images = math.ceil(num_pixels / pixels_per_image)

    # Create an array to store the frames
    frames = []

    # Loop through each image
    for i in tqdm(range(num_images)):
        # Calculate the range of binary digits needed for this image
        start_index = i * pixels_per_image
        end_index = min(start_index + pixels_per_image, num_pixels)
        binary_digits = bin_string[start_index:end_index]

        # Create a new image object with the given size
        img = Image.new('RGB', (width, height), color='white')

        # Loop through each row of binary digits
        for row_index in range(height // pixel_size):

            # Get the binary digits for the current row
            start_index = row_index * (width // pixel_size)
            end_index = start_index + (width // pixel_size)
            row = binary_digits[start_index:end_index]

            # Loop through each column of binary digits
            for col_index, digit in enumerate(row):

                # Determine the color of the pixel based on the binary digit
                if digit == '1':
                    color = (0, 0, 0)  # Black
                else:
                    color = (255, 255, 255)  # White

                # Calculate the coordinates of the pixel
                x1 = col_index * pixel_size
                y1 = row_index * pixel_size
                x2 = x1 + pixel_size
                y2 = y1 + pixel_size

                # Draw the pixel on the image
                img.paste(color, (x1, y1, x2, y2))

        # Add the frame to the list of frames
        with io.BytesIO() as f:
            img.save(f, format='PNG')
            frame = np.array(Image.open(f))
        frames.append(frame)

    # Create a video from the frames using MoviePy
    clip = ImageSequenceClip(frames, fps=fps)

    # Write the video to a file
    clip.write_videofile('video.mp4', fps=fps)


def process_images(frames):
    # Define the threshold value for determining black pixels
    threshold = 128

    # Create an empty string to store the binary digits
    binary_digits = ''

    # Loop through each frame in the list
    for frame in tqdm(frames, desc="Processing frames"):
        # Convert the frame to grayscale
        gray_frame = np.mean(frame, axis=2).astype(np.uint8)

        # Hardcode the pixel size to 4
        pixel_size = 4

        # Loop through each row of pixels
        for y in range(0, gray_frame.shape[0], pixel_size):
            # Loop through each column of pixels
            for x in range(0, gray_frame.shape[1], pixel_size):
                # Get the color of the current pixel
                color = gray_frame[y:y+pixel_size, x:x+pixel_size]

                # Determine the binary digit based on the color of the pixel
                if color.mean() < threshold:
                    binary_digits += '1'
                else:
                    binary_digits += '0'

    # Store the binary string in a single text file
    return binary_digits


def imageToText():
    # function to convert a file to binary format and store it in a text file
    def file_to_binary(filename):
        # read file as binary
        with open(filename, "rb") as f:
            binary_data = f.read()

        # convert binary data to string of 0's and 1's
        binary_string = "".join(f"{byte:08b}" for byte in binary_data)

        # write binary string to text file
        with open("binary.txt", "w") as f:
            f.write(binary_string)

        print(f"File converted to binary format and stored in binary.txt")

    # prompt user to enter filename
    filename = input("Enter the name of the file to convert: ")

    # call function to convert file to binary format
    file_to_binary(filename)


def binaryToFile(binary_filename):
    # convert binary string to binary data
    binary_data = bytes(int(binary_filename[i:i+8], 2)
                        for i in range(0, len(binary_filename), 8))

    # write binary data to output file
    with open("reverse.mkv", "wb") as f:
        with tqdm(total=len(binary_data), unit='B', unit_scale=True, desc="Writing binary data") as pbar:
            for chunk in range(0, len(binary_data), 1024):
                f.write(binary_data[chunk:chunk+1024])
                pbar.update(1024)

        print(f"Binary data converted to example_reverse.zip")


def ExtractFrames():
    am = []
    dir_path = os.getcwd()
    files = [f for f in os.listdir(dir_path) if f.endswith('.webm')]
    files = [f for f in os.listdir(dir_path) if f.endswith('.mp4')]
    files = files[0]
    # Open the video file
    vid = imageio.get_reader(files, 'ffmpeg')

    # Get the fps of the video
    fps = vid.get_meta_data()['fps']

    # Get the total number of frames in the video
    num_frames = vid.get_length()

    # Use tqdm to create a progress bar
    with tqdm(total=num_frames) as pbar:
        # Iterate over every frame of the video
        for i, frame in enumerate(vid):
            # Append the frame to the list
            am.append(frame)
            # Update the progress bar
            pbar.update(1)

    # Return the list of frames
    return am

def youtube_video_downloader(url):
    # create YouTube object
    yt = YouTube(url)

    # get the video with 1080p resolution
    stream = yt.streams.filter(res="1080p").first()

    # download the video
    stream.download()


input_Data=input("convert file to video press 1 and Enter  \nconvert video to file press 2  and Enter\nDownload video from youtube press 3 and Enter\n" )

if (input_Data=="1"):
    binary_to_video(file_to_binary())
elif(input_Data=="2"):
    binaryToFile(process_images(ExtractFrames()))
elif(input_Data=="3"):
    youtube_video_downloader(input("Enter Url "))
else:
    print("404")
