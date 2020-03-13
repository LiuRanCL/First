





import json
from local_contour import img_mainpart_detect

from local_variable_front import *
import cv2

img_path = './generated images/cut_img.jpg'
img = cv2.imread(img_path)
binary = cv2.imread(img_path + '_binary' + '.jpg', 0)
h, w, p = img.shape



def duqi(img):
    print("正在识别肚脐坐标...")
    duqi = img[left_elbow_y:left_hand_y, right_buttocks_x:left_buttocks_x]
    cv2.imwrite("./generated images/" + "duqi" + '.jpg', duqi)  
    img2 = './generated images/duqi.jpg'
    content = img_mainpart_detect(img2)
    content1 = json.loads(content)
    print("肚脐坐标检测：", content1)
    result = content1['result']
    width = result['width']
    top = result['top']
    height = result['height']
    left = result['left']
    x = right_buttocks_x + left + int(width / 2)
    y = left_elbow_y + top + int(height / 2)
    
    return (x, y)



def mid_x():
    print("加载中线X坐标...")
    neck_left_x = neck_right_x = 0
    for l in range(w):
        if binary[neck_y, neck_x + l] == 0:
            neck_left_x = neck_x + l
            break
    for j in range(w):
        if binary[neck_y, neck_x - j] == 0:
            neck_right_x = neck_x - j
            break
    mid_x1 = round((neck_left_x + neck_right_x) / 2)
    print("加载中线X坐标成功！")
    return mid_x1





def A(img):
    n = 5
    r, t = img.shape
    print(r, t)
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




def left_yewo(imgmid_x):
    print("正在计算左边腋窝点...")
    left_yewo1 = binary[left_shoulder_y:left_elbow_y, imgmid_x: left_elbow_x]
    cv2.imwrite('./generated images/left_yewo.jpg', left_yewo1)
    binary_left_yewo = cv2.imread('./generated images/left_yewo.jpg', 0)
    array = []  
    flag, k0, l0 = A(binary_left_yewo)
    if flag == 1:
        array.append([k0, l0])
    print(array)
    left_yuanye_x = array[0][1] + imgmid_x  
    left_yuanye_y = array[0][0] + left_shoulder_y
    
    return (left_yuanye_x, left_yuanye_y)



def right_yewo(imgmid_x):
    print("正在计算右边腋窝点...")
    right_yewo = binary[right_shoulder_y:right_elbow_y, right_elbow_x:imgmid_x]
    cv2.imwrite('./generated images/right_yewo.jpg', right_yewo)
    binary_right_yewo = cv2.imread('./generated images/right_yewo.jpg', 0)
    array = []  
    n, h0, w0 = A(binary_right_yewo)
    if n == 1:
        array.append([h0, w0])
    print(array)
    right_yuanye_x = array[0][1] + right_elbow_x  
    right_yuanye_y = array[0][0] + right_shoulder_y
    
    return (right_yuanye_x, right_yuanye_y)



def left_ruzhong(img, mid_x, left_yewo_x, left_yewo_y):
    print("正在识别左边乳中...")
    
    start_x = int((mid_x + left_yewo_x) / 2)
    img_ruzhong = img[left_shoulder_y:left_yewo_y, start_x:left_yewo_x]
    cv2.imwrite('./generated images/' + 'img_ruzhong' + '.jpg', img_ruzhong)
    ruzhong = './generated images/img_ruzhong.jpg'
    content = img_mainpart_detect(ruzhong)
    content1 = json.loads(content)
    result = content1['result']
    width = result['width']
    top = result['top']
    height = result['height']
    left = result['left']
    x = start_x + left + int(width / 2)
    y = left_shoulder_y + top + int(height / 2)
    
    return (x, y)



def right_ruzhong(img, mid_x, yewo_right_x, yewo_right_y):
    print("正在识别右边乳中...")
    
    start_x = int((mid_x + yewo_right_x) / 2)
    img_ruzhong = img[left_shoulder_y:yewo_right_y, yewo_right_x:start_x]
    cv2.imwrite('./generated images/' + 'img_right_ruzhong' + '.jpg', img_ruzhong)
    ruzhong = './generated images/img_right_ruzhong.jpg'
    content = img_mainpart_detect(ruzhong)
    content1 = json.loads(content)
    result = content1['result']
    width = result['width']
    top = result['top']
    height = result['height']
    left = result['left']
    x = yewo_right_x + left + int(width / 2)
    y = left_shoulder_y + top + int(height / 2)
    
    return (x, y)



