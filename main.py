import cv2
import os
from os import listdir
import glob 


def images_to_video():
    img_array = []
    for filename in glob.glob('./new_video/*.jpg'):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
 
 
    out = cv2.VideoWriter('new_video.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 30, size)
 
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

def detect_image(folder,name):
    destination_path = './new_video'
    path = f'{folder}/{name}'
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

    img = cv2.imread(path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imwrite(os.path.join(destination_path , name), img)
        print(f'saved file at {destination_path}/{name}')
        cv2.waitKey(0)

def extract_frames(video_file):
    cap = cv2.VideoCapture(video_file)
    
    frame_rate = 30  # Desired frame rate (1 frame every 0.5 seconds)
    frame_count = 0
    
    # Get the video file's name without extension
    video_name = os.path.splitext(os.path.basename(video_file))[0]
    
    # Create an output folder with a name corresponding to the video
    output_directory = f"{video_name}_frames"
    os.makedirs(output_directory, exist_ok=True)
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        frame_count += 1
        

        if frame_count % int(cap.get(5) / frame_rate) == 0:
            output_file = f"{output_directory}/frame_{frame_count}.jpg"
            cv2.imwrite(output_file, frame)
            print(f"Frame {frame_count} has been extracted and saved as {output_file}")
    
    cap.release()
    cv2.destroyAllWindows()

def process_video(video_path):
    extract_frames(video_path)
    folder_dir = "./la_cabra_frames"
    for images in os.listdir(folder_dir):
        detect_image(folder_dir, images)

    images_to_video()

process_video('la_cabra.mp4')