import cv2
import os

def extract_frames(video_path, output_dir):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    # Read the video frame by frame
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Save the frame as an image
        frame_name = f"frame_{frame_count:05d}.jpg"
        frame_path = os.path.join(output_dir, frame_name)
        cv2.imwrite(frame_path, frame)
        
        frame_count += 1
    
    # Release the video capture object
    cap.release()

# Example usage:
video_path = './Pick_2_3.mp4'
output_directory = 'output_frames_directory'
extract_frames(video_path, output_directory)
