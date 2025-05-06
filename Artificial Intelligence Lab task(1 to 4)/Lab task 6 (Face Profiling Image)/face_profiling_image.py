import cv2
import numpy as np
import math
import sys

def calculate_distance(point1, point2):
    
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def measure_facial_features(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) == 0:
        print("No face detected in the image!")
        return
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]  
        eyes = eye_cascade.detectMultiScale(roi_gray)    
        eye_centers = []
        for (ex, ey, ew, eh) in eyes:    
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            eye_center = (x + ex + ew//2, y + ey + eh//2)
            eye_centers.append(eye_center)
            cv2.circle(image, eye_center, 2, (0, 0, 255), -1)
        if len(eye_centers) >= 2:
            ipd = calculate_distance(eye_centers[0], eye_centers[1])
            face_width = w
            face_height = h
            face_ratio = face_height / face_width 
            cv2.putText(image, f'IPD: {ipd:.2f}px', (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(image, f'Face Width: {face_width}px', (10, 60),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(image, f'Face Height: {face_height}px', (10, 90),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(image, f'Face Ratio: {face_ratio:.2f}', (10, 120),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.line(image, eye_centers[0], eye_centers[1], (255, 0, 0), 2) 
            face_center_x = x + w//2
            cv2.line(image, (face_center_x, y), (face_center_x, y+h), (0, 255, 255), 2)


image_path = 'a.jpeg'
image = cv2.imread(image_path)

measure_facial_features(image)


cv2.imshow('Face Profiling', image)

key = cv2.waitKey(0)
if key == ord('s'):
    output_path = 'face_profiling_result.jpg'
    cv2.imwrite(output_path, image)
    print(f"Result saved as: {output_path}")

cv2.destroyAllWindows()
