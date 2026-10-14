import cv2
cap = cv2.VideoCapture(r"C:\Users\Cyrus\Downloads\table_tennis_Bot\WhatsApp Unknown 2026-10-13 at 2.06.24 AM\WhatsApp Video 2026-10-12 at 2.30.27 PM.mp4")
cap.isOpened()
print(cap.get(cv2.CAP_PROP_FPS))
print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap.release()