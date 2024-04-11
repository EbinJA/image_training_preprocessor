from PIL import Image
import os

def get_image_info(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Get the size of the image
        width, height = img.size
        
        return width, height

# Example usage:
image_path = './output_frames_directory/frame_00011.jpg'
width, height = get_image_info(image_path)
print(f"Image size: {width}x{height}")

