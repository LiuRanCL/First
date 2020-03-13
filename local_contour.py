



import cv2


def contour(ImgPath):

    img = cv2.imread(ImgPath, cv2.IMREAD_COLOR)
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    (y, cr, cb) = cv2.split(ycrcb)

    cr1 = cv2.GaussianBlur(cr, (9, 9), 0)
    _, skin1 = cv2.threshold(cr1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    low = (0, 0, 0)
    high = (180, 255, 46)
    mask = cv2.inRange(hsv, low, high)

    new_img = mask | skin1
    dst = cv2.dilate(new_img, None, iterations=4)
    dst2 = cv2.erode(dst, None, iterations=4)

    cv2.imwrite(ImgPath + '_binary' + '.jpg', dst2)
    return ImgPath + '_binary' + '.jpg'
