import cv2

filename = 'path_to_video'

cap = cv2.VideoCapture(filename)
i = 0

while cap.isOpened():
    ret, frame = cap.read()

    ''' Writing the frames '''
    cv2.imwrite('Image_' + str(i) + '.jpg', frame)
    i += 1

    cv2.imshow('main', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        break

cv2.destroyAllWindows()
