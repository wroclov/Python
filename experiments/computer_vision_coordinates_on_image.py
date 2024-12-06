from typing import Any

import cv2
from cv2 import Mat
from numpy import ndarray, dtype

# this will print all possible events:
[print(i) for i in dir(cv2) if 'EVENT' in i]

img: Mat | ndarray[Any, dtype[Any]] | ndarray = cv2.imread('1.jpg', 1)

# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN :
        print("left mouse button clicked")
        print(f"location x:{x} and y:{y}")
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x, y), font,
                    1, (255, 0, 0), 2)
        cv2.rectangle(img,(x, y),
                      (x + 50, y + 50), (0, 200, 200),
                      10, 10, 0)
        cv2.imshow('image', img)

        # checking for right mouse clicks
    if event == cv2.EVENT_RBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        print("right mouse button clicked")
        print(f"location x:{x} and y:{y}")

        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x, y), font, 1,
                    (255, 0, 50), 2)
        cv2.circle(img,(x,  y),
                   50, (100, 100, 100),
                   2, 10, 0)
        cv2.imshow('image', img)

    if event == cv2.EVENT_MOUSEMOVE:
        #print("Mouse moved")
        pass

    elif event :
        #print("Other event", event)
        pass


def main():
    # reading the image
    # moved up, as img was not recognized by functions
    #img = cv2.imread('1.jpg', 1)

    # displaying the image
    cv2.imshow('image', img)

    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)

    # close the window
    cv2.destroyAllWindows()
    pass

if __name__ == "__main__":
    main()