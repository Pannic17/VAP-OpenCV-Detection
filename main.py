import math

import cv2

HAAR_CASCADE_PATH = "hc_hand_1.xml"


def detect(filename, cascade_path):
    cascade = cv2.CascadeClassifier(cascade_path)
    origin = cv2.imread(filename)
    gray = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)

    result = cascade.detectMultiScale(gray, scaleFactor=1.02, minNeighbors=5)

    print(result)

    for (x, y, w, h) in result:
        wd = math.ceil(w * 0.1)
        hd = math.ceil(h * 0.1)
        print("##################RESULT")
        print(w, h)
        print(x, y)
        print("END#####################")

        # change the coordinate, increase the rectangle by 10% for each side and move up to include the ears
        x1 = x - wd
        y1 = y - hd * 2
        x2 = x + w + wd
        y2 = y + h

        origin = cv2.rectangle(origin, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("RESULT", origin)
    cv2.waitKey(0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("START")
    camera = cv2.VideoCapture(0)
    while True:
        ret, frame = camera.read()
        cv2.imshow('frame', frame)
        # detect("Test8.png", HAAR_CASCADE_PATH)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
