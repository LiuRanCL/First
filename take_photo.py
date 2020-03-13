




'''
    获取人体照片
    使用方法：点击运行，先拍摄正面照片,按S键拍照,后按Q键转换到背面拍摄；拍摄背面照片，先按S键拍照,再按Q键退出
    照片将保存至sourcImg文件夹中，重复拍照可覆盖
'''

import numpy as np
import cv2
import time




def front():
    print("请拍摄正面照片,先按S键拍照,在按Q键拍摄背面")
    while True:

        success, img = cap.read()

        cv2.imshow("front", img)


        k = cv2.waitKey(1)
        if k == ord("q"):
            cv2.destroyAllWindows()
            break
        elif k == ord("s"):
            cv2.imwrite('./sourceImg/front.jpg', img)
            print("图片已保存到sourceImg文件夹！")


def back():
    print("请拍摄背面照片，先按S键拍照,按Q键退出")
    while True:
        success1, img1 = cap.read()
        cv2.imshow("back", img1)
        k = cv2.waitKey(1)
        if k == ord("q"):

            cv2.destroyAllWindows()
            break
        elif k == ord("s"):
            cv2.imwrite('./sourceImg/back.jpg', img1)
            print("图片已保存到sourceImg文件夹！")


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    cap.set(3, 880)
    cap.set(4, 660)
    front()
    back()
    cap.release()
    cv2.destroyAllWindows()
