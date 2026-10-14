import cv2
import time
    #for i in range(16):
"""        dog=str(i)+"0cm_test.mp4"
        cap = cv2.VideoCapture(dog)
        print(time.perf_counter())
        print(cap.read())
        cv2.imshow
        cv2.waitKey(1)
        cv2.putText
"""
while True:
    dog="C:\\Users\\Cyrus\\Downloads\\table_tennis_Bot\\table_tennis_bot\\data\\10cm_test.mp4"
    cap = cv2.VideoCapture(dog)
    print(time.perf_counter())
    print(cap.read())
    cv2.imshow("Video", cap.read()[1])
    cv2.waitKey(1)
    cv2.putText(cap.read()[1], "Hello", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)