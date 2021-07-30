import cv2
import numpy as np
import warnings
warnings.filterwarnings('ignore')

face_classifier = cv2.CascadeClassifier(
    'C:/Users/Amit/AppData/Local/Programs/Python/Python39/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')


def face_extractor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # This converts RGB image to greyscale image

    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    # detectMultiscale(image,ScalingFactor,MinimumNeighbours(3,6))

    if faces == ():
        return None

    # cropping faces
    # x = x cord ,y = y cord , w = width ,h=height
    for (x, y, w, h) in faces:
        cropped_faces = img[y:y + h, x:x + w]
    return cropped_faces


cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    if face_extractor(frame) is not None:
        count += 1
        face = cv2.resize(face_extractor(frame), (200, 200))
        # resize is used to resize the image

        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        # converts to greyscale

        file_name_path = 'D:/other python projects/FaceRecognition/faces/user' + str(count) + '.jpg'
        cv2.imwrite(file_name_path, face)
        # Here we specify folder where faces will get saved.
        # imwrite writes faces in that folder

        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        # puttext will put count of images taken on screen
        # cv2.putText(img,no,cord,fontface,font_scale,color,font_size

        cv2.imshow('Face Cropper', face)
        # it will show image and will collect also
    else:
        print('Face not found')
        pass

    if cv2.waitKey(1) == 13 or count == 50:
        break
    # Here 13 is break key for enter for stopping it
    # if count is 50 the it will stop

cap.release()
# camera will get closed with release

cv2.destroyAllWindows()
print("Collecting samples Complete")
