import cv2
from local_variable_front import *

img_path = FrontPath
img = cv2.imread(img_path)
binary = cv2.imread(img_path + '_binary' + '.jpg', 0)


def base_point(img1):
    img = cv2.imread(img1)
    h, w, a = img.shape
    canny = cv2.Canny(img, 40, 80)
    _, label, stats, centroids = cv2.connectedComponentsWithStats(canny)

    return label, stats, centroids, h, w


def duqi(img):
    print("正在识别肚脐坐标...")
    duqi = img[left_elbow_y:left_hand_y, right_buttocks_x:left_buttocks_x]
    cv2.imwrite("./generated images/" + "duqi" + '.jpg', duqi)
    img2 = './generated images/duqi.jpg'
    label, stats, centroids, h, w = base_point(img2)
    a = []
    index = 0
    for k in range(len(stats)):
        a.append(stats[k][4])
    centroids = np.delete(centroids, a.index(np.max(a)), axis=0)

    mid_x = w / 2
    min = abs(centroids[0][0] - mid_x)
    for i in range(len(centroids)):
        count = abs(centroids[i][0] - mid_x)
        if min > count:
            min = count
            index = i
    x0 = centroids[index][0] + right_buttocks_x
    y = centroids[index][1] + left_elbow_y
    for k in range(0, w):
        if binary[int(y), int(x0 + k)] == 0:
            max1 = x0 + k
            break
    for j in range(0, w):
        if binary[int(y), int(x0 - j)] == 0:
            min = x0 - j
            break
    x = (min + max1) / 2
    return round(x), round(y)


def A(img):
    n = 5
    r, t = img.shape
    for k in range(n, r - n):
        for l in range(n, t - n):
            point = [
                img[k, l],
                img[k, l + n],
                img[k, l - n],
                img[k - n, l],
                img[k + n, l]
            ]
            if point[1] == point[2] == point[3] == 255 and point[4] == 0:
                print("计算腋窝点成功！")
                print("查找到腋窝点：", k, l)
                flag = 1
                k0 = k
                l0 = l
                return flag, k0, l0


def left_yewo(mid_x):
    print("这是中点坐标", mid_x)
    print("正在计算左边腋窝点...")
    left_yewo1 = binary[left_shoulder_y:left_elbow_y, mid_x: left_elbow_x]
    cv2.imwrite('./generated images/left_yewo.jpg', left_yewo1)
    binary_left_yewo = cv2.imread('./generated images/left_yewo.jpg', 0)
    array = []
    flag, k0, l0 = A(binary_left_yewo)
    if flag == 1:
        array.append([k0, l0])
    left_yuanye_x = array[0][1] + mid_x
    left_yuanye_y = array[0][0] + left_shoulder_y

    return (left_yuanye_x, left_yuanye_y)


def right_yewo(mid_x):
    print("正在计算右边腋窝点...")
    right_yewo = binary[right_shoulder_y:right_elbow_y, right_elbow_x:mid_x]
    cv2.imwrite('./generated images/right_yewo.jpg', right_yewo)
    binary_right_yewo = cv2.imread('./generated images/right_yewo.jpg', 0)
    array = []
    n, h0, w0 = A(binary_right_yewo)
    if n == 1:
        array.append([h0, w0])
    right_yuanye_x = array[0][1] + right_elbow_x
    right_yuanye_y = array[0][0] + right_shoulder_y

    return (right_yuanye_x, right_yuanye_y)


def left_ruzhong(img, mid_x, left_yuanye_x, left_yuanye_y):
    start_x = int((mid_x + left_yuanye_x) / 2)
    img_ruzhong = img[left_shoulder_y:left_yuanye_y, start_x:left_yuanye_x]
    cv2.imwrite('./generated images/' + 'img_ruzhong' + '.jpg', img_ruzhong)
    left_ruzhong = './generated images/img_ruzhong.jpg'
    label, stats, centroids, h, w = base_point(left_ruzhong)
    a = []
    index = 0
    for k in range(len(stats)):
        a.append(stats[k][4])
    centroids = np.delete(centroids, a.index(np.max(a)), axis=0)

    min = abs(centroids[0][0] - 0)
    for i in range(len(centroids)):
        count = abs(centroids[i][0] - 0)
        if min > count:
            min = count
            index = i
    x = centroids[index][0] + start_x
    y = centroids[index][1] + left_shoulder_y
    return round(x), round(y)


def right_ruzhong(img, mid_x, right_yuanye_x, right_yuanye_y):
    print("正在识别右边乳中...")

    start_x = int((mid_x + right_yuanye_x) / 2)
    right_ruzhong1 = img[left_shoulder_y:right_yuanye_y, right_yuanye_x:start_x]
    cv2.imwrite('./generated images/' + 'img_right_ruzhong' + '.jpg', right_ruzhong1)
    right_ruzhong = './generated images/img_right_ruzhong.jpg'
    label, stats, centroids, h, w = base_point(right_ruzhong)
    a = []
    index = 0
    for k in range(len(stats)):
        a.append(stats[k][4])
    centroids = np.delete(centroids, a.index(np.max(a)), axis=0)

    min = abs(centroids[0][0] - w)
    for i in range(len(centroids)):
        count = abs(centroids[i][0] - w)
        if min > count:
            min = count
            index = i
    x = centroids[index][0] + right_yuanye_x
    y = centroids[index][1] + left_shoulder_y
    return round(x), round(y)
