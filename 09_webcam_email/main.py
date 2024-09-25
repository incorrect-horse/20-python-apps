import cv2
import time
import glob
import os
from email_function import send_email
from threading import Thread

video = cv2.VideoCapture(0)
time.sleep(1)

first_frame = None
status_list = []
count = 1


def clean_folder():
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)


while True:
    status = 0
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)
    #cv2.imshow("My Vid", gray_frame_gau)

    if first_frame is None:
        first_frame = gray_frame_gau
    
    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    #cv2.imshow("Delta", delta_frame)

    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    #cv2.imshow("Threshold", thresh_frame)

    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    #cv2.imshow("Dilation", dil_frame)

    contours, check = cv2.findContours(dil_frame,
                                       cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        if rectangle.any():
            status = 1
            cv2.imwrite(f"images/{str(count).zfill(5)}.png", frame)
            count += 1
            all_images = glob.glob("images/*.png")
            index = int(len(all_images) / 2)
            median_image = all_images[index]

    status_list.append(status)
    status_list = status_list[-2:]

    # determines when an image leaves the frame,
    # emails the median image from the set
    if status_list[0] == 1 and status_list[1] == 0:
        email_thread = Thread(target=send_email, args=(median_image, ))
        email_thread.daemon = True
        email_thread.start()

    cv2.imshow("Video - 'q' to quit", frame)
    key = cv2.waitKey(1)

    if key == ord("q"):
        clean_thread = Thread(target=clean_folder)
        clean_thread.daemon = True
        clean_thread.start()
        break

video.release()
