import numpy as np
import cv2

points = []
pointCount = 0


def MouseEventCallBack(_event, _u, _v, _flags, _param):
    global pointCount
    if _event == cv2.EVENT_LBUTTONDOWN:
        points.append([_u, _v])
        print(str(pointCount) + " " + str(_u) + " " + str(_v))
        pointCount += 1


if __name__ == "__main__":
    mapImage = cv2.imread("960x1128.png")
    cv2.namedWindow("Get UV and TM")
    # cv2.setWindowProperty("Get UV and TM", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    # cv2.moveWindow("Get UV and TM", 10, 10)
    # cv2.resizeWindow("Get UV and TM", 4089, 1305)
    cv2.setMouseCallback("Get UV and TM", MouseEventCallBack)
    cv2.imshow("Get UV and TM", mapImage)

    while True:
        inputKey = cv2.waitKey(1)
        if inputKey == ord('r'):
            pointCount = 0
        elif inputKey == ord('q'):
            print("Points selection done.")
            break
