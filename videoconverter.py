import cv2
import os

def frames_to_video(frames_dir, output_video_path, fps=30):
    # Get the list of frames
    frame_files = sorted(os.listdir(frames_dir))
    
    # Open the first frame to get dimensions
    frame_path = os.path.join(frames_dir, frame_files[0])
    img = cv2.imread(frame_path)
    height, width, _ = img.shape
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
    
    # Write each frame to the video
    for filename in frame_files:
        frame_path = os.path.join(frames_dir, filename)
        img = cv2.imread(frame_path)
        out.write(img)
    
    # Release the VideoWriter
    out.release()

# Example usage:
frames_directory = './output_frames_directory'
output_video_path = 'darkvideo.mp4'
frames_to_video(frames_directory, output_video_path)
