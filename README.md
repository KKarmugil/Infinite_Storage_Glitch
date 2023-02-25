# Infinite_Storage_Glitch
 YouTube as Cloud Storage: Store Any Files You Want

![ezgif-1-0299af809c](https://user-images.githubusercontent.com/86147453/221376499-1e7e894a-1d76-4d59-90ec-90ccf7fb6fd0.gif)

How to use
-------------
Install Requirments


1. Archive to zip all the files you will be uploading
2. Run the executable
3. It will give you three options file to video , video to file , download video from youtube select option you need and program will start executing 
4. Upload the video to your YouTube channel. You probably want to keep it up as unlisted
5. Use the download option to get the video back
6. Use the dislodge option to get your files back from the downloaded video
7. PROFIT
 

input file should be zipped (.zip) file 

keep only one zip file in same directery 



This program inspired from DvorakDwarf Infinite-Storage-Glitch 
https://github.com/DvorakDwarf/Infinite-Storage-Glitch check out his project

I dont know rust so I recreated the same project in python 

# Demo 
 [YouTube Link](https://youtu.be/wsbZO4kmXFI)

To reduce the risk of corruption, the program uses larger pixel blocks in binary mode, typically 2x2 blocks.

This program consists of several functions that allow for the conversion of files to binary format, and for the creation of videos from a file.

## file_to_binary()
This function takes no parameters and returns a string of 0's and 1's representing the binary data of a file with a .zip extension. It does this by first determining the file size and reading the file as binary data. The binary data is then converted to a string of 0's and 1's and returned.

## binary_to_video(bin_string, width=1920, height=1080, pixel_size=4, fps=24)
This function takes a string of binary data as bin_string and several optional parameters that determine the size and framerate of the resulting video. It returns a video file in .mp4 format. The function first calculates the total number of pixels needed to represent the binary data and the number of pixels that can fit in one image. It then creates an array of frames, each of which corresponds to one image that contains the binary data. The frames are created by iterating through each row and column of binary digits and determining the color of each pixel based on the binary digit. The frames are then added to the array of frames. Finally, the frames are used to create a video file using the MoviePy library and written to disk.

## process_images(frames)
This function takes an array of frames as input and returns a string of 0's and 1's representing the binary data contained in the frames. It does this by iterating through each frame and converting it to grayscale. It then iterates through each row and column of pixels and determines the binary digit based on the color of each pixel. The binary digits are concatenated into a single string and returned.

## imageToText()
This function takes no parameters and prompts the user to enter the name of a file to convert to binary format. It then calls the file_to_binary() function and stores the resulting binary data in a file named binary.txt.

## binaryToFile(binary_filename)
This function takes a string of binary data as binary_filename and writes it to a file named output.zip. It does this by first converting the binary data to binary format and then writing the binary data to the output file.

Overall, this program provides a simple way to convert files to binary format and create videos from binary data, as well as convert binary data back to files.



