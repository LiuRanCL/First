import numpy
from acupoint_front import *
from front_choose_point import front_name

font = ImageFont.truetype('./Font/simhei.ttf', 8)
point_size = 1
point_color = (0, 255, 0)
thickness = 2

if __name__ == '__main__':
    print("正在标注正面穴位点...")

    for i in range(len(front_name)):
        x, y, str = front_name[i]
        cv2.circle(img, (int(x), int(y)), point_size, point_color, thickness)

    img_PIL = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_PIL)

    for i in range(len(front_name)):
        x, y, str = front_name[i]
        draw.text((int(x), int(y)), str, font=font, fill=point_color)

    print("展示正面标注结果")
    img = cv2.cvtColor(numpy.asarray(img_PIL), cv2.COLOR_RGB2BGR)
    window = 'front'

    cv2.imwrite('./generated images/front.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    cv2.imshow(window, img)
    cv2.waitKey(0)

    print("图片已保存！")
