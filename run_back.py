import numpy
from acupoint_back import *
from back_choose_point import back_name

jiaji = (
    dazhui(),
    taodao(),
    temp1(),
    shenzhu(),
    temp2(),
    shendao(),
    lingtai(),
    zhiyang(),
    temp3(),
    jinsuo(),
    zhongshu(),
    jizhong(),
    jieji(),
    xuanshu(),
    mingmen(),
    xiajiyu(),
    yaoyangguan(),
    shiqizhui()
)


def jiajixue():
    str = ""
    for i in range(len(jiaji)):
        x0, y0, str = jiaji[i]
        x1 = x0 + round(0.5 * cun_heng)
        x2 = x0 - round(0.5 * cun_heng)
        y = y0
        cv2.circle(img, (int(x1), int(y)), 1, (255, 0, 0), 2)
        cv2.circle(img, (int(x2), int(y)), 1, (255, 0, 0), 2)


font = ImageFont.truetype('./Font/simhei.ttf', 8)
point_size = 1
point_color = (0, 255, 0)
thickness = 2

if __name__ == '__main__':
    print("正在标注背面穴位点...")
    jiajixue()

    for i in range(len(back_name)):
        x, y, str = back_name[i]
        cv2.circle(img, (int(x), int(y)), point_size, point_color, thickness)

    img_PIL = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_PIL)
    print("正在标注背面穴位名称...")

    for i in range(len(back_name)):
        x, y, str = back_name[i]
        draw.text((int(x), int(y)), str, font=font, fill=point_color)

    img = cv2.cvtColor(numpy.asarray(img_PIL), cv2.COLOR_RGB2BGR)

    window = 'back'

    cv2.imwrite('./generated images/back.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    cv2.imshow(window, img)
    print("展示背面面标注结果")

    cv2.waitKey(0)
