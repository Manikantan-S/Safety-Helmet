import cv2
import torch
import numpy as np
import os
import keyboard

path = 'C:/Users/Asus/Desktop/projects/MACHINE LEARNING/yolov5safetyhelmet-main/yolov5safetyhelmet-main/best.pt'

# Load the model
model = torch.hub.load('ultralytics/yolov5', 'custom', path, force_reload=True)

video_path = 'C:/Users/Asus/Desktop/projects/MACHINE LEARNING/yolov5safetyhelmet-main/yolov5safetyhelmet-main/helmet.mp4'
cap = cv2.VideoCapture(video_path)
count = 0
output_folder = 'output_frames'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        count += 1
        if count % 3 != 0:
            continue
        frame = cv2.resize(frame, (1020, 600))
        results = model(frame)
        frame = np.squeeze(results.render())

        # Display the frame
        cv2.imshow('Video Processing', frame)
        key = cv2.waitKey(1) & 0xFF

        # Save the frame as an image in the output folder
        output_path = os.path.join(output_folder, f'frame_{count:04d}.jpg')
        cv2.imwrite(output_path, frame)

        if key == 27:  # Check if 'Esc' key is pressed
            break

finally:
    cap.release()
    cv2.destroyAllWindows()

print("Frames have been saved in the 'output_frames' folder.")






