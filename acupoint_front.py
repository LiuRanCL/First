'''
本文件包含身体正面所有函数以及实现方法，
可自行添加穴位函数。
编写之后需添加至front_choose_point.py的dict_front中，
在array_front中调用。
'''

from local_base_point import *
import numpy as np
from PIL import Image, ImageDraw, ImageFont

from local_variable_front import *
from sympy import *
from local_contour import contour
import cv2
from PATH_DEFINE import FrontPath

imgpath = FrontPath
img = cv2.imread(imgpath)
h, w, a = img.shape
m = 0
n = 0
path = contour(imgpath)
binary = cv2.imread(path, 0)


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


mid_x = mid_x()
left_yuanye_x, left_yuanye_y = left_yewo(mid_x)
right_yuanye_x, right_yuanye_y = right_yewo(mid_x)

yewoup = 0
print("正在计算腋前纹头纵坐标...")
for l in range(h):
    if binary[int(left_yuanye_y) - 5 - l, left_yuanye_x] == 0:
        yewoup = left_yuanye_y - 5 - l
        break

yeqianwen_y = int((left_yuanye_y + yewoup) / 2)
for i in range(w):
    if binary[yeqianwen_y, left_yuanye_x + 5 + i] == 0:
        m = left_yuanye_x + 5 + i
        break
leg_mid = int((left_yuanye_x + m) / 2)


def chize():
    str = '尺泽穴'
    m = n = 0
    for i in range(w):
        if binary[left_elbow_y, left_elbow_x + i] == 0:
            m = left_elbow_x + i
            break
    for i in range(w):
        if binary[left_elbow_y, left_elbow_x - i] == 0:
            n = left_elbow_x - i
            break
    else:
        print("请检查左肘")
    y = left_elbow_y

    x = int((m + n) / 2)
    return (x, y, str)


def zuowan():
    print("计算左腕关键点...")
    str = '左腕'
    m = n = 0
    left_hand = left_hand_x
    if binary[left_hand_y, left_hand_x] == 0:
        for j in range(w):
            if binary[left_hand_y, left_hand_x + j] == 255:
                left_hand = left_hand_x + j
                break
            elif binary[left_hand_y, left_hand_x - j] == 255:
                left_hand = left_hand_x - j
                break
    for i in range(w):
        if binary[left_hand_y, left_hand + i] == 0:
            m = left_hand + i
            break
    for i in range(w):
        if binary[left_hand_y, left_hand - i] == 0:
            n = left_hand - i
            break
    y = left_hand_y + 5
    x = int((m + n) / 2)
    return (x, y, str, n, m)


def youwan():
    print("计算右腕关键点...")
    str = '测试点'
    for i in range(w):
        if binary[right_hand_y, right_hand_x + i] == 0:
            m = right_hand_x + i
            break

    for i in range(w):
        if binary[right_hand_y, right_hand_x - i] == 0:
            n = right_hand_x - i
            break
    y = right_hand_y
    x = int((m + n) / 2)
    return (x, y, str)


def left_quze():
    str = '曲泽穴'
    xx = 0
    x0, y0, z0 = chize()
    y = y0 + 5
    for j in range(w):
        if binary[y0, x0 - j] == 0:
            xx = x0 - j
            break
    x = int((x0 + xx) / 2)
    return (x, y, str)


def left_shaohai():
    str = '少海穴'
    x = 0
    x0, y0, z0 = chize()
    y = y0 + 10
    for j in range(w):
        if binary[y0, x0 - j] == 0:
            x = x0 - j + 5
            break
    return (x, y, str)


zuozhou_x, zuozhou_y, str = chize()

cun1 = int((((mid_x - zuozhou_x) ** 2 + (left_yuanye_y - zuozhou_y) ** 2) ** 0.5) / 9)


def tianquan():
    str = "天泉穴"
    x = leg_mid
    y = yeqianwen_y + 2 * cun1
    return (x, y, str)


def tianfu():
    str = '天府穴'
    x0, y0, str1 = tianquan()
    for i in range(w):
        if binary[y0, x0 + i] == 0:
            x = x0 + i
            break
    y = y0 + cun1
    return (x, y, str)


def xiabai():
    str = '侠白穴'
    x0, y0, str1 = tianfu()
    x = x0 + int((pow(2, 0.5) * cun1) / 2)
    y = y0 + int((pow(2, 0.5) * cun1) / 2)
    return (x, y, str)


zuowan_x, zuowan_y, zuowan_str, n, m = zuowan()
cun2 = int((((zuowan_x - zuozhou_x) ** 2 + (zuowan_y - zuozhou_y) ** 2) ** 0.5) / 12)


def dalin():
    str = '大陵穴'
    y = zuowan_y + 5
    x = m - int((m - n) / 3)
    return (x, y, str)


def shenmen():
    str = '神门穴'
    y = zuowan_y + 10
    x = n + int((m - n) / 3)
    return (x, y, str)


def taiyuan():
    str = '太渊穴'
    x = m
    y = zuowan_y
    return (x, y, str)


def xinbaojing():
    x1, y1, str1 = dalin()
    x2, y2, str2 = left_quze()
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 1)


def xinjing():
    x1, y1, str1 = shenmen()
    x2, y2, str2 = left_shaohai()
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 1)


def feijing():
    x1, y1, str1 = chize()
    x2, y2, str2 = taiyuan()
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 1)


def neiguanxue():
    str = '内关穴'
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - zuozhou_y) / (zuowan_y - zuozhou_y) - (x - zuozhou_x) / (zuowan_x - zuozhou_x),
                    (((zuowan_x - x) ** 2 + (zuowan_y - y) ** 2) ** 0.5) - (2 * cun2)], [x, y])
    x0 = int(result[0][0])
    y0 = int(result[0][1])
    return (x0, y0, str)


def jianshi():
    str = '间使穴'
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - zuozhou_y) / (zuowan_y - zuozhou_y) - (x - zuozhou_x) / (zuowan_x - zuozhou_x),
                    (((zuowan_x - x) ** 2 + (zuowan_y - y) ** 2) ** 0.5) - (3 * cun2)], [x, y])
    x0 = int(result[0][0])
    y0 = int(result[0][1])
    return (x0, y0, str)


def ximen():
    str = '郄门穴'
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - zuozhou_y) / (zuowan_y - zuozhou_y) - (x - zuozhou_x) / (zuowan_x - zuozhou_x),
                    (((zuowan_x - x) ** 2 + (zuowan_y - y) ** 2) ** 0.5) - (5 * cun2)], [x, y])
    x0 = int(result[0][0])
    y0 = int(result[0][1])
    return (x0, y0, str)


shenmen_x, shenmen_y, shenmen_str = shenmen()
shaohai_x, shaohai_y, shaohai_str = left_shaohai()


def yinxi():
    str = '阴郄穴'
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - shenmen_y) / (shaohai_y - shenmen_y) - (x - shenmen_x) / (shaohai_x - shenmen_x),
                    (((shenmen_x - x) ** 2 + (shenmen_y - y) ** 2) ** 0.5) - (0.5 * cun2)], [x, y])
    x0 = int(result[0][0])
    y0 = int(result[0][1])
    return (x0, y0, str)


def tongli():
    str = '通里穴'
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - shenmen_y) / (shaohai_y - shenmen_y) - (x - shenmen_x) / (shaohai_x - shenmen_x),
                    (((shenmen_x - x) ** 2 + (shenmen_y - y) ** 2) ** 0.5) - (1 * cun2)], [x, y])
    x0 = int(result[0][0])
    y0 = int(result[0][1])
    return (x0, y0, str)


def lingdao():
    str = '灵道穴'
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - shenmen_y) / (shaohai_y - shenmen_y) - (x - shenmen_x) / (shaohai_x - shenmen_x),
                    (((shenmen_x - x) ** 2 + (shenmen_y - y) ** 2) ** 0.5) - (1.5 * cun2)], [x, y])
    x0 = int(result[0][0])
    y0 = int(result[0][1])
    return (x0, y0, str)


chize_x, chize_y, chize_str = chize()
taiyuan_x, taiyuan_y, taiyaun_str = taiyuan()


def kongzui():
    str = '孔最穴'
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - chize_y) / (taiyuan_y - chize_y) - (x - chize_x) / (taiyuan_x - chize_x),
                    (((taiyuan_x - x) ** 2 + (taiyuan_y - y) ** 2) ** 0.5) - (7 * cun2)], [x, y])
    x0 = int(result[0][0])
    y0 = int(result[0][1])
    return (x0, y0, str)


def jingqu():
    str = '经渠穴'
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - chize_y) / (taiyuan_y - chize_y) - (x - chize_x) / (taiyuan_x - chize_x),
                    (((taiyuan_x - x) ** 2 + (taiyuan_y - y) ** 2) ** 0.5) - (1 * cun2)], [x, y])
    x0 = int(result[0][0])
    y0 = int(result[0][1])
    return (x0, y0, str)


def lieque():
    str = '列缺穴'
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - chize_y) / (taiyuan_y - chize_y) - (x - chize_x) / (taiyuan_x - chize_x),
                    (((taiyuan_x - x) ** 2 + (taiyuan_y - y) ** 2) ** 0.5) - (1.5 * cun2)], [x, y])
    x0 = int(result[0][0])
    y0 = int(result[0][1])
    return (x0, y0, str)


'''

left_ruzhong_x, left_ruzhong_y = left_ruzhong(img, mid_x, left_yuanye_x, left_yuanye_y)  
right_ruzhong_x, right_ruzhong_y = right_ruzhong(img, mid_x, right_yuanye_x, right_yuanye_y)  
duqi_x, duqi_y = duqi(img)  


cun_heng = int(abs(left_ruzhong_x - right_ruzhong_x) / 9)

cun_zong = int(((duqi_y - left_ruzhong_y) * 0.915) / 8)

jianxiong_y = left_ruzhong_y + int((duqi_y - left_ruzhong_y) * 0.085)

jianjian_y = yewoup

cun_xiong = int(abs(jianxiong_y - jianjian_y) / 5)





def duqi():
    str = "神阙"
    x = duqi_x
    y = duqi_y
    return (int(x), int(y), str)





def shuifen():
    str = "水分穴"
    x, y0, a = duqi()
    y = y0 - cun_zong
    return (x, y, str)



def xiawan():
    str = "下脘穴"
    x, y0, a = duqi()
    y = y0 - cun_zong * 2
    return (x, y, str)



def jianli():
    str = "建里穴"
    x, y0, a = duqi()
    y = y0 - cun_zong * 3
    return (x, y, str)



def zhongwan():
    str = "中脘穴"
    x, y0, a = duqi()
    y = y0 - cun_zong * 4
    return (x, y, str)



def shangwan():
    str = "上脘穴"
    x, y0, a = duqi()
    y = y0 - cun_zong * 5
    return (x, y, str)



def juque():
    str = "巨阙穴"
    x, y0, a = duqi()
    y = y0 - cun_zong * 6
    return (x, y, str)



def jiuwei():
    str = "鸠尾穴"
    x, y0, a = duqi()
    y = jianxiong_y + cun_zong
    return (x, y, str)



def zhongting():
    str = "中庭穴"
    x, y0, a = duqi()
    y = jianxiong_y
    return (x, y, str)



def tanzhong():
    str = "膻中穴"
    x = duqi_x
    y = right_ruzhong_y
    return (x, y, str)



def yutang():
    str = "玉堂穴"
    x, y0, a = tanzhong()
    y = y0 - cun_xiong
    return (x, y, str)



def zigong():
    str = "紫宫穴"
    x, y0, a = tanzhong()
    y = y0 - cun_xiong * 2
    return (x, y, str)



def huagai():
    str = "华盖穴"
    x, y0, a = tanzhong()
    y = y0 - cun_xiong * 3
    return (x, y, str)



def xuanji():
    str = "璇玑穴"
    x, y0, a = tanzhong()
    y = y0 - cun_xiong * 4
    return (x, y, str)



def tiantu():
    str = '天突穴'
    x = duqi_x
    y = jianjian_y
    return (x, y, str)





def yinjiao():
    str = "阴交穴"
    x, y0, a = duqi()
    y = y0 + cun_zong
    return (x, y, str)



def qihai():
    str = "气海穴"
    x, y0, a = duqi()
    y = y0 + int(cun_zong * 1.5)
    return (x, y, str)



def shimen():
    str = "石门穴"
    x, y0, a = duqi()
    y = y0 + cun_zong * 2
    return (x, y, str)



def guanyuan():
    str = "关元穴"
    x, y0, a = duqi()
    y = y0 + cun_zong * 3
    return (x, y, str)



def zhongji():
    str = "中极穴"
    x, y0, a = duqi()
    y = y0 + cun_zong * 4
    return (x, y, str)



def qugu():
    str = "曲骨穴"
    x, y0, a = duqi()
    y = y0 + int(cun_zong * 4.5)
    return (x, y, str)






def henggu():
    str = "横骨穴"
    x0, y, a = qugu()
    x = x0 + int(0.5 * cun_heng)
    return (x, y, str)



def dahe():
    str = "大赫穴"
    x0, y, a = zhongji()
    x = x0 + int(cun_heng * 0.5)
    return (x, y, str)



def qixue():
    str = "气穴"
    x0, y, a = guanyuan()
    x = x0 + int(cun_heng * 0.5)
    return (x, y, str)



def siman():
    str = "四满穴"
    x0, y, a = shimen()
    x = x0 + int(cun_heng * 0.5)
    return (x, y, str)



def zhongzhu():
    str = "中注穴"
    x0, y, a = yinjiao()
    x = x0 + int(cun_heng * 0.5)
    return (x, y, str)



def huangshu():
    str = "肓俞穴"
    x0, y, a = duqi()
    x = x0 + int(cun_heng * 0.5)
    return (x, y, str)



def shangqu():
    str = "商曲穴"
    x0, y, a = xiawan()
    x = x0 + int(cun_heng * 0.5)
    return (x, y, str)



def shiguan():
    str = "石关穴"
    x0, y, a = jianli()
    x = x0 + int(cun_heng * 0.5)
    return (x, y, str)



def yindu():
    str = "阴都穴"
    x0, y, a = zhongwan()
    x = x0 + int(cun_heng * 0.5)
    return (x, y, str)



def futonggu():
    str = "腹通谷"
    x0, y, a = shangwan()
    x = x0 + int(cun_heng * 0.5)
    return (x, y, str)



def youmen():
    str = "幽门穴"
    x0, y, a = juque()
    x = x0 + int(cun_heng * 0.5)
    return (x, y, str)



def bulang():
    str = "步廊穴"
    x0, y, a = zhongting()
    x = x0 + int(cun_heng * 2)
    return (x, y, str)



def shenfeng():
    str = "神封穴"
    x0, y, a = tanzhong()
    x = x0 + int(cun_heng * 2)
    return (x, y, str)



def lingxu():
    str = "灵虚穴"
    x0, y, a = yutang()
    x = x0 + int(cun_heng * 2)
    return (x, y, str)



def shenzang():
    str = "神藏穴"
    x0, y, a = zigong()
    x = x0 + int(cun_heng * 2)
    return (x, y, str)



def yuzhong():
    str = "彧中穴"
    x0, y, a = huagai()
    x = x0 + int(cun_heng * 2)
    return (x, y, str)



def yufu():
    str = "俞府穴"
    x0, y, a = xuanji()
    x = x0 + int(cun_heng * 2)
    return (x, y, str)






def qichong():
    str = "气冲穴"
    x0, y, a = qugu()
    x = x0 + 2 * cun_heng
    return (x, y, str)



def guilai():
    str = "归来穴"
    x0, y, a = zhongji()
    x = x0 + int(cun_heng * 2)
    return (x, y, str)



def shuidao():
    str = "水道穴"
    x0, y, a = guanyuan()
    x = x0 + int(cun_heng * 2)
    return (x, y, str)



def daju():
    str = "大巨穴"
    x0, y, a = shimen()
    x = x0 + int(cun_heng * 2)
    return (x, y, str)



def wailing():
    str = "外陵穴"
    x0, y, a = yinjiao()
    x = x0 + int(cun_heng * 2)
    return (x, y, str)



def tianshu():
    str = "天枢穴"
    x0, y, a = duqi()
    x = x0 + int(cun_heng * 2)
    return (x, y, str)



def huaroumen():
    str = "滑肉门"
    x0, y, a = shuifen()
    x = x0 + int(cun_heng * 2)
    return (x, y, str)



def taiyi():
    str = "太乙"
    x0, y, a = xiawan()
    x = x0 + int(cun_heng * 2)
    return (x, y, str)



def guanmen():
    str = "关门"
    x0, y, a = jianli()
    x = x0 + int(cun_heng * 2)
    return (x, y, str)



def liangmen():
    str = "梁门穴"
    x0, y, a = zhongwan()
    x = x0 + int(cun_heng * 2)
    return (x, y, str)



def chengman():
    str = "承满穴"
    x0, y, a = shangwan()
    x = x0 + int(cun_heng * 2)
    return (x, y, str)



def burong():
    str = "不容"
    x0, y, a = juque()
    x = x0 + int(cun_heng * 2)
    return (x, y, str)



def rugen():
    str = "乳根"
    x0, y, a = ruzhong()
    x1, y1, b = zhongting()
    x = x0 - round(cun_heng * 0.5)
    return (x, y1, str)



def ruzhong():
    str = '乳中'
    x = left_ruzhong_x
    y = left_ruzhong_y
    return (x, y, str)




def tianchi():
    str = "天池"
    x0, y0, a = ruzhong()
    y = y0
    x = x0 + round(0.5 * cun_heng)
    return (x, y, str)



def yingchuang():
    str = "膺窗穴"
    x0, y, a = ruzhong()
    y = y - cun_xiong
    x = x0 - round(cun_heng * 0.5)
    return (x, y, str)



def wuyi():
    str = "屋翳穴"
    x0, y, a = ruzhong()
    y = left_ruzhong_y - cun_xiong * 2
    x = x0 - round(cun_heng * 0.5)
    return (x, y, str)



def kufang():
    str = "库房"
    x0, y, a = ruzhong()
    y = left_ruzhong_y - cun_xiong * 3
    x = x0 - round(cun_heng * 0.5)
    return (x, y, str)



def qihu():
    str = "气户穴"
    x0, y, a = ruzhong()
    y = left_ruzhong_y - cun_xiong * 4
    x = x0 - round(cun_heng * 0.5)
    return (x, y, str)






def fujie():
    str = "腹结穴"
    x0, y0, a = duqi()
    x = x0 + cun_heng * 4
    y = y0 + int(cun_zong * 1.3)
    return (x, y, str)



def daheng():
    str = "大横穴"
    x0, y0, a = duqi()
    x = x0 + cun_heng * 4
    y = y0
    return (x, y, str)



def fuai():
    str = "腹哀穴"
    x0, y0, a = duqi()
    x = x0 + cun_heng * 4
    y = y0 - int(cun_zong * 3)
    return (x, y, str)



def shidou():
    str = "食窦穴"
    x0, y0, a = zhongting()
    x = x0 + cun_heng * 6
    y = y0
    return (x, y, str)



def tianxi():
    str = "天溪穴"
    x0, y0, a = shidou()
    x = x0
    y = y0 - cun_xiong
    return (x, y, str)



def xiongxiang():
    str = "胸乡穴"
    x0, y0, a = shidou()
    x = x0
    y = y0 - cun_xiong * 2
    return (x, y, str)



def zhourong():
    str = "周荣穴"
    x0, y0, a = shidou()
    x = x0
    y = y0 - cun_xiong * 3
    return (x, y, str)






def sanjiaojiu1():
    str = "三角灸(左)"
    x0, y0, z = qihai()
    y = y0
    x = x0 + cun_heng
    return (x, y, str)


def sanjiaojiu2():
    str = "三角灸(右)"
    x0, y0, z = qihai()
    y = y0
    x = x0 - cun_heng
    return (x, y, str)



def liniao():
    str = "利尿"
    x0, y0, z = duqi()
    y = y0 + int(cun_zong * 3.5)
    return (x0, y, str)



def dome():
    str = "子宫（女）"
    x0, y0, z = zhongji()
    y = y0
    x = x0 + cun_heng * 4
    return (x, y, str)





guanyuan_x, guanyuan_y, guangyuan_str = guanyuan()
cun_leg = int((left_knee_y - guanyuan_y) / 19)



def huiyin():
    str = "裆部"
    for i in range(h):
        if binary[int(duqi_y) + i, int(duqi_x)] == 0:
            y1 = duqi_y + i
            x1 = duqi_x
            break
    return (int(x1), int(y1), str)


huiyin_x, huiyin_y, huiyin_str = huiyin()



def mid_leg():
    str = "大腿根中点"
    x = y = 0
    for i in range(h):
        if binary[huiyin_y, huiyin_x + 10 + i] == 0:
            x = int((huiyin_x * 2 + 10 + i) / 2)
            y = huiyin_y
            break
    return (x, y, str)


mid_leg_x, mid_leg_y, mid_leg_str = mid_leg()






def chongmen():
    str = "冲门穴"
    x0, y0, a = qugu()
    x = x0 + int(cun_heng * 3.5)
    y = y0
    return (x, y, str)



def yinglian():
    str = '阴廉穴'
    x, y0, a = qichong()
    y = y0 + cun_leg * 2
    return (x, y, str)



def zuwuli():
    str = '足五里'
    x, y0, a = qichong()
    y = y0 + cun_leg * 3
    return (x, y, str)



def jimai():
    str = '急脉'
    x0, y0, a = qichong()
    x = mid_x + int(cun_heng * 2.5)
    y = y0 + cun_leg
    return (x, y, str)



def biguan():
    str = "髀关穴"
    x0, y0, a = qichong()
    x = mid_leg_x
    y = y0 + cun_leg
    return (x, y, str)



def knee():
    m = n = 0
    for i in range(w):
        if binary[left_knee_y, left_knee_x + i] == 0:  
            m = left_knee_x + i
            break
    for i in range(w):
        if binary[left_knee_y, left_knee_x - i] == 0:  
            n = left_knee_x - i
            break
    y = left_knee_y  
    x = int((m + n) / 2)  
    return (x, y, str, n, m)


knee_x, knee_y, knee_str, n1, m1 = knee()



def xiya1():
    str = "膝眼1"
    x = n1 + int((m1 - n1) / 3)
    y = left_knee_y
    return (x, y, str)


def xiya2():
    str = "膝眼2"
    x = m1 - int((m1 - n1) / 3)
    y = left_knee_y
    return (x, y, str)



def dubi():
    str = "犊鼻穴"
    x0, y, a = xiya2()
    x = x0 + 10
    return (x, y, str)



dubi_x, dubi_y, dubi_str = dubi()




def jiexi():
    for i in range(w):
        if binary[left_foot_y, left_foot_x + i] == 0:
            foot_m = left_foot_x + i
            break
    for i in range(w):
        if binary[left_foot_y, left_foot_x - i] == 0:
            foot_n = left_foot_x - i
            break
    foot_mid_x = int((foot_n + foot_m) / 2)
    return (foot_mid_x)


foot_mid_x = jiexi()



def heding():
    str = "鹤顶穴"
    x = knee_x
    y = knee_y - int(cun_leg * 1.5)
    return (x, y, str)



def liangqiu():
    str = "梁丘穴"
    x, y0, a = xiya2()
    y = y0 - int(cun_leg * 3.5)
    return (x, y, str)



def kuangu1():
    str = "髋骨"
    x0, y0, a = xiya2()
    x = x0 + int(cun_heng * 1.5)
    y = y0 - int(cun_leg * 3.5)
    return (x, y, str)



def kuangu2():
    str = "髋骨"
    x0, y0, a = xiya2()
    x = x0 - int(cun_heng * 1.5)
    y = y0 - int(cun_leg * 3.5)
    return (x, y, str)



def xuehai():
    str = "血海穴"
    x0, y0, a = xiya2()
    x = x0 - int(cun_heng * 3)
    y = y0 - int(cun_leg * 3.5)
    return (x, y, str)



def baichongwo():
    str = "百虫窝"
    x0, y0, a = xiya2()
    x = x0 - int(cun_heng * 3)
    y = y0 - int(cun_leg * 4.5)
    return (x, y, str)



def yinshi():
    str = "阴市穴"
    x, y0, a = xiya2()
    y = y0 - int(cun_leg * 4.5)
    return (x, y, str)



def futu():
    str = "伏兔穴"
    x, y0, a = xiya2()
    y = y0 - int(cun_leg * 7.5)
    return (x, y, str)





def zusanli():
    str = "足三里"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - left_foot_y) / (dubi_y - left_foot_y) - (x - foot_mid_x) / (dubi_x - foot_mid_x),
                    (((dubi_x - x) ** 2 + (dubi_y - y) ** 2) ** 0.5) - (3 * cun_leg)], [x, y])
    x0 = int(result[1][0])  
    y0 = int(result[1][1])
    return (x0, y0, str)



def lanwei():
    str = "阑尾"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - left_foot_y) / (dubi_y - left_foot_y) - (x - foot_mid_x) / (dubi_x - foot_mid_x),
                    (((dubi_x - x) ** 2 + (dubi_y - y) ** 2) ** 0.5) - (5 * cun_leg)], [x, y])
    x0 = int(result[1][0])  
    y0 = int(result[1][1])
    return (x0, y0, str)



def shangjuxu():
    str = "上巨虚"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - left_foot_y) / (dubi_y - left_foot_y) - (x - foot_mid_x) / (dubi_x - foot_mid_x),
                    (((dubi_x - x) ** 2 + (dubi_y - y) ** 2) ** 0.5) - (6 * cun_leg)], [x, y])
    x0 = int(result[1][0])  
    y0 = int(result[1][1])
    return (x0, y0, str)



def tiaokou():
    str = "条口"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - left_foot_y) / (dubi_y - left_foot_y) - (x - foot_mid_x) / (dubi_x - foot_mid_x),
                    (((dubi_x - x) ** 2 + (dubi_y - y) ** 2) ** 0.5) - (8 * cun_leg)], [x, y])
    x0 = int(result[1][0])  
    y0 = int(result[1][1])
    return (x0, y0, str)



def xiajuxu():
    str = "下巨虚"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - left_foot_y) / (dubi_y - left_foot_y) - (x - foot_mid_x) / (dubi_x - foot_mid_x),
                    (((dubi_x - x) ** 2 + (dubi_y - y) ** 2) ** 0.5) - (9 * cun_leg)], [x, y])
    x0 = int(result[1][0])  
    y0 = int(result[1][1])
    return (x0, y0, str)



def fenglong():
    str = "丰隆穴"
    x0, y0, a = tiaokou()
    x = x0 + cun_leg
    y = y0
    return (x, y, str)



def jiexi():
    str = "解溪穴"
    x = foot_mid_x
    y = left_foot_y
    return (x, y, str)



def jimen():
    str = "箕门穴"
    x0, y0, z = chongmen()
    x1, y1, z1 = qichong()
    y = y0 + int((left_knee_y - y0) / 3)
    x = x1
    return (x, y, str)


'''
右半身穴位点来袭！！！！！！！！！！！！！！！！！
'''





def henggu1():
    str = "横骨穴"
    x0, y, a = qugu()
    x = x0 - int(0.5 * cun_heng)
    return (x, y, str)



def dahe1():
    str = "大赫穴"
    x0, y, a = zhongji()
    x = x0 - int(cun_heng * 0.5)
    return (x, y, str)



def qixue1():
    str = "气穴"
    x0, y, a = guanyuan()
    x = x0 - int(cun_heng * 0.5)
    return (x, y, str)



def siman1():
    str = "四满穴"
    x0, y, a = shimen()
    x = x0 - int(cun_heng * 0.5)
    return (x, y, str)



def zhongzhu1():
    str = "中注穴"
    x0, y, a = yinjiao()
    x = x0 - int(cun_heng * 0.5)
    return (x, y, str)



def huangshu1():
    str = "肓俞穴"
    x0, y, a = duqi()
    x = x0 - int(cun_heng * 0.5)
    return (x, y, str)



def shangqu1():
    str = "商曲穴"
    x0, y, a = xiawan()
    x = x0 - int(cun_heng * 0.5)
    return (x, y, str)



def shiguan1():
    str = "石关穴"
    x0, y, a = jianli()
    x = x0 - int(cun_heng * 0.5)
    return (x, y, str)



def yindu1():
    str = "阴都穴"
    x0, y, a = zhongwan()
    x = x0 - int(cun_heng * 0.5)
    return (x, y, str)



def futonggu1():
    str = "腹通谷"
    x0, y, a = shangwan()
    x = x0 - int(cun_heng * 0.5)
    return (x, y, str)



def youmen1():
    str = "幽门穴"
    x0, y, a = juque()
    x = x0 - int(cun_heng * 0.5)
    return (x, y, str)



def bulang1():
    str = "步廊穴"
    x0, y, a = zhongting()
    x = x0 - int(cun_heng * 2)
    return (x, y, str)



def shenfeng1():
    str = "神封穴"
    x0, y, a = tanzhong()
    x = x0 - int(cun_heng * 2)
    return (x, y, str)



def lingxu1():
    str = "灵虚穴"
    x0, y, a = yutang()
    x = x0 - int(cun_heng * 2)
    return (x, y, str)



def shenzang1():
    str = "神藏穴"
    x0, y, a = zigong()
    x = x0 - int(cun_heng * 2)
    return (x, y, str)



def yuzhong1():
    str = "彧中穴"
    x0, y, a = huagai()
    x = x0 - int(cun_heng * 2)
    return (x, y, str)



def yufu1():
    str = "俞府穴"
    x0, y, a = xuanji()
    x = x0 - int(cun_heng * 2)
    return (x, y, str)






def qichong1():
    str = "气冲穴"
    x0, y, a = qugu()
    x = x0 - 2 * cun_heng
    return (x, y, str)



def guilai1():
    str = "归来穴"
    x0, y, a = zhongji()
    x = x0 - int(cun_heng * 2)
    return (x, y, str)



def shuidao1():
    str = "水道穴"
    x0, y, a = guanyuan()
    x = x0 - int(cun_heng * 2)
    return (x, y, str)



def daju1():
    str = "大巨穴"
    x0, y, a = shimen()
    x = x0 - int(cun_heng * 2)
    return (x, y, str)



def wailing1():
    str = "外陵穴"
    x0, y, a = yinjiao()
    x = x0 - int(cun_heng * 2)
    return (x, y, str)



def tianshu1():
    str = "天枢穴"
    x0, y, a = duqi()
    x = x0 - int(cun_heng * 2)
    return (x, y, str)



def huaroumen1():
    str = "滑肉门"
    x0, y, a = shuifen()
    x = x0 - int(cun_heng * 2)
    return (x, y, str)



def taiyi1():
    str = "太乙"
    x0, y, a = xiawan()
    x = x0 - int(cun_heng * 2)
    return (x, y, str)



def guanmen1():
    str = "关门"
    x0, y, a = jianli()
    x = x0 - int(cun_heng * 2)
    return (x, y, str)



def liangmen1():
    str = "梁门穴"
    x0, y, a = zhongwan()
    x = x0 - int(cun_heng * 2)
    return (x, y, str)



def chengman1():
    str = "承满穴"
    x0, y, a = shangwan()
    x = x0 - int(cun_heng * 2)
    return (x, y, str)



def burong1():
    str = "不容"
    x0, y, a = juque()
    x = x0 - int(cun_heng * 2)
    return (x, y, str)



def ruzhong1():
    str = '乳中'
    x = right_ruzhong_x
    y = right_ruzhong_y
    return (x, y, str)



def rugen1():
    str = "乳根"
    x0, y, a = ruzhong1()
    x1, y1, b = zhongting()
    x = x0 + round(cun_heng * 0.5)
    return (x, y1, str)






def tianchi1():
    str = "天池"
    x0, y0, a = ruzhong1()
    y = y0
    x = x0 - round(0.5 * cun_heng)
    return (x, y, str)



def yingchuang1():
    str = "膺窗穴"
    x0, y, a = ruzhong1()
    y = y - cun_xiong
    x = x0 + round(cun_heng * 0.5)
    return (x, y, str)



def wuyi1():
    str = "屋翳穴"
    x0, y, a = ruzhong1()
    y = left_ruzhong_y - cun_xiong * 2
    x = x0 + round(cun_heng * 0.5)
    return (x, y, str)



def kufang1():
    str = "库房"
    x0, y, a = ruzhong1()
    y = left_ruzhong_y - cun_xiong * 3
    x = x0 + round(cun_heng * 0.5)
    return (x, y, str)



def qihu1():
    str = "气户穴"
    x0, y, a = ruzhong1()
    y = left_ruzhong_y - cun_xiong * 4
    x = x0 + round(cun_heng * 0.5)
    return (x, y, str)





def chongmen1():
    str = "冲门穴"
    x0, y0, a = qugu()
    x = x0 - int(cun_heng * 3.5)
    y = y0
    return (x, y, str)


def fujie1():
    str = "腹结穴"
    x0, y0, a = duqi()
    x = x0 - cun_heng * 4
    y = y0 + int(cun_zong * 1.3)
    return (x, y, str)



def daheng1():
    str = "大横穴"
    x0, y0, a = duqi()
    x = x0 - cun_heng * 4
    y = y0
    return (x, y, str)



def fuai1():
    str = "腹哀穴"
    x0, y0, a = duqi()
    x = x0 - cun_heng * 4
    y = y0 - int(cun_zong * 3)
    return (x, y, str)



def shidou1():
    str = "食窦穴"
    x0, y0, a = zhongting()
    x = x0 - cun_heng * 6
    y = y0
    return (x, y, str)



def tianxi1():
    str = "天溪穴"
    x0, y0, a = shidou1()
    x = x0
    y = y0 - cun_xiong
    return (x, y, str)



def xiongxiang1():
    str = "胸乡穴"
    x0, y0, a = shidou1()
    x = x0
    y = y0 - cun_xiong * 2
    return (x, y, str)



def zhourong1():
    str = "周荣穴"
    x0, y0, a = shidou1()
    x = x0
    y = y0 - cun_xiong * 3
    return (x, y, str)





def dome1():
    str = "子宫（女）"
    x0, y0, z = zhongji()
    y = y0
    x = x0 - cun_heng * 4
    return (x, y, str)


def liniao1():
    str = "利尿"
    x0, y0, z = duqi()
    y = y0 - int(cun_zong * 3.5)
    return (x0, y, str)



def mid_leg1():
    str = "大腿根中点"
    x = y = 0
    for i in range(h):
        if binary[huiyin_y, huiyin_x - 10 - i] == 0:
            x = int((huiyin_x * 2 - 10 - i) / 2)
            y = huiyin_y
            break
    return (x, y, str)


mid_leg_x1, mid_leg_y1, mid_leg_str1 = mid_leg1()






def chongmen1():
    str = "冲门穴"
    x0, y0, a = qugu()
    x = x0 - int(cun_heng * 3.5)
    y = y0
    return (x, y, str)



def yinglian1():
    str = '阴廉穴'
    x, y0, a = qichong1()
    y = y0 + cun_leg * 2
    return (x, y, str)



def zuwuli1():
    str = '足五里'
    x, y0, a = qichong1()
    y = y0 + cun_leg * 3
    return (x, y, str)



def jimai1():
    str = '急脉'
    x0, y0, a = qichong1()
    x = mid_x - int(cun_heng * 2.5)
    y = y0 + cun_leg
    return (x, y, str)



def biguan1():
    str = "髀关穴"
    x0, y0, a = qichong1()
    x = mid_leg_x1
    y = y0 + cun_leg
    return (x, y, str)



def knee1():
    m = n = 0
    for i in range(w):
        if binary[right_knee_y, right_knee_x + i] == 0:  
            m = right_knee_x + i
            break
    for i in range(w):
        if binary[right_knee_y, right_knee_x - i] == 0:  
            n = right_knee_x - i
            break
    y = right_knee_y  
    x = int((m + n) / 2)  
    return (x, y, str, n, m)


knee_x1, knee_y1, knee_str1, n11, m11 = knee1()



def xiya11():
    str = "膝眼1"
    x = n11 + int((m11 - n11) / 3)
    y = knee_y1
    return (x, y, str)


def xiya21():
    str = "膝眼2"
    x = m11 - int((m11 - n11) / 3)
    y = knee_y1
    return (x, y, str)



def dubi1():
    str = "犊鼻穴"
    x0, y, a = xiya11()
    x = x0 - 10
    return (x, y, str)



dubi_x1, dubi_y1, dubi_str1 = dubi1()




def jiexi1():
    for i in range(w):
        if binary[right_foot_y, right_foot_x + i] == 0:
            foot_m1 = right_foot_x + i
            break
    for i in range(w):
        if binary[right_foot_y, right_foot_x - i] == 0:
            foot_n1 = right_foot_x - i
            break
    foot_mid_x = int((foot_n1 + foot_m1) / 2)
    return (foot_mid_x)


foot_mid_x1 = jiexi1()



def heding1():
    str = "鹤顶穴"
    x = knee_x1
    y = knee_y1 - int(cun_leg * 1.5)
    return (x, y, str)



def liangqiu1():
    str = "梁丘穴"
    x, y0, a = xiya11()
    y = y0 - int(cun_leg * 3.5)
    return (x, y, str)



def kuangu11():
    str = "髋骨"
    x0, y0, a = xiya11()
    x = x0 - int(cun_heng * 1.5)
    y = y0 - int(cun_leg * 3.5)
    return (x, y, str)



def kuangu21():
    str = "髋骨"
    x0, y0, a = xiya11()
    x = x0 + int(cun_heng * 1.5)
    y = y0 - int(cun_leg * 3.5)
    return (x, y, str)



def xuehai1():
    str = "血海穴"
    x0, y0, a = xiya11()
    x = x0 + int(cun_heng * 3)
    y = y0 - int(cun_leg * 3.5)
    return (x, y, str)



def baichongwo1():
    str = "百虫窝"
    x0, y0, a = xiya11()
    x = x0 + int(cun_heng * 3)
    y = y0 - int(cun_leg * 4.5)
    return (x, y, str)



def yinshi1():
    str = "阴市穴"
    x, y0, a = xiya21()
    y = y0 - int(cun_leg * 4.5)
    return (x, y, str)



def futu1():
    str = "伏兔穴"
    x, y0, a = xiya11()
    y = y0 - int(cun_leg * 7.5)
    return (x, y, str)





def zusanli1():
    str = "足三里"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - right_foot_y) / (dubi_y1 - right_foot_y) - (x - foot_mid_x1) / (dubi_x1 - foot_mid_x1),
                    (((dubi_x1 - x) ** 2 + (dubi_y1 - y) ** 2) ** 0.5) - (3 * cun_leg)], [x, y])
    x0 = int(result[0][0])  
    y0 = int(result[0][1])
    return (x0, y0, str)



def lanwei1():
    str = "阑尾"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - right_foot_y) / (dubi_y1 - right_foot_y) - (x - foot_mid_x1) / (dubi_x1 - foot_mid_x1),
                    (((dubi_x1 - x) ** 2 + (dubi_y1 - y) ** 2) ** 0.5) - (5 * cun_leg)], [x, y])
    x0 = int(result[0][0])  
    y0 = int(result[0][1])
    return (x0, y0, str)



def shangjuxu1():
    str = "上巨虚"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - right_foot_y) / (dubi_y1 - right_foot_y) - (x - foot_mid_x1) / (dubi_x1 - foot_mid_x1),
                    (((dubi_x1 - x) ** 2 + (dubi_y1- y) ** 2) ** 0.5) - (6 * cun_leg)], [x, y])
    x0 = int(result[0][0])  
    y0 = int(result[0][1])
    return (x0, y0, str)



def tiaokou1():
    str = "条口"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - right_foot_y) / (dubi_y1 - right_foot_y) - (x - foot_mid_x1) / (dubi_x1 - foot_mid_x1),
                    (((dubi_x1 - x) ** 2 + (dubi_y1 - y) ** 2) ** 0.5) - (8 * cun_leg)], [x, y])
    x0 = int(result[0][0])  
    y0 = int(result[0][1])
    return (x0, y0, str)



def xiajuxu1():
    str = "下巨虚"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - right_foot_y) / (dubi_y1 - right_foot_y) - (x - foot_mid_x1) / (dubi_x1 - foot_mid_x1),
                    (((dubi_x1 - x) ** 2 + (dubi_y1 - y) ** 2) ** 0.5) - (9 * cun_leg)], [x, y])
    x0 = int(result[0][0])  
    y0 = int(result[0][1])
    return (x0, y0, str)



def fenglong1():
    str = "丰隆穴"
    x0, y0, a = tiaokou1()
    x = x0 - cun_leg
    y = y0
    return (x, y, str)



def jiexi1():
    str = "解溪穴"
    x = foot_mid_x1
    y = right_foot_y
    return (x, y, str)



def jimen1():
    str = "箕门穴"
    x0, y0, z = chongmen1()
    x1, y1, z1 = qichong1()
    y = y0 + int((knee_y1 - y0) / 3)
    x = x1
    return (x, y, str)



yewoupp = 0
print("正在计算腋前纹头纵坐标...")
for l in range(h):
    if binary[int(right_yuanye_y) - 5 - l, right_yuanye_x] == 0:
        yewoupp = right_yuanye_y - 5 - l
        break

m3 = 0
yeqianwen_y1 = int((right_yuanye_y + yewoupp) / 2)  
for i in range(w):
    if binary[yeqianwen_y1, right_yuanye_x - 5 - i] == 0:  
        m3 = right_yuanye_x - 5 - i
        break
leg_mid3 = int((right_yuanye_x + m3) / 2)  




def chize1():
    str = '尺泽穴'
    m = n = 0
    if binary[right_elbow_y, right_elbow_x] == 255:
        for i in range(w):
            if binary[right_elbow_y, right_elbow_x + 10 + i] == 0:  
                m = right_elbow_x + 10 + i
                break
        for i in range(w):
            if binary[right_elbow_y, right_elbow_x + 10 - i] == 0:  
                n = right_elbow_x + 10 - i
                break
    elif binary[right_elbow_y, right_elbow_x] == 0:
        for i in range(w):
            if binary[right_elbow_y, right_elbow_x  + i] == 255:  
                m = right_elbow_x + i
                break
        for k in range(w):
            if binary[right_elbow_y, m + k] == 0:
                n = m + k
                break

    y = right_elbow_y  
    x = int((m + n) / 2)  
    return (x, y, str)





def youwan1():
    print("计算左腕关键点...")
    str = '左腕'
    m = n = 0
    for i in range(w):
        if binary[right_hand_y, right_hand_x + 10 + i] == 0:  
            m = right_hand_x + 10 + i
            break
    for i in range(w):
        if binary[right_hand_y, right_hand_x + 10 - i] == 0:
            n = right_hand_x + 10 - i
            break
    y = right_hand_y + 5  
    x = int((m + n) / 2)  
    return (x, y, str, n, m)  






def left_quze1():
    str = '曲泽穴'
    xx = 0
    x0, y0, z0 = chize1()
    y = y0 + 5
    for j in range(w):
        if binary[y0, x0 + j] == 0:
            xx = x0 + j
            break
    x = int((x0 + xx) / 2)
    return (x, y, str)



def left_shaohai1():
    str = '少海穴'
    x = 0
    x0, y0, z0 = chize1()
    y = y0 + 10
    for j in range(w):
        if binary[y0, x0 + j] == 0:
            x = x0 + j
            break
    return (x, y, str)



zuozhou_x1, zuozhou_y1, strqwe1 = chize1()  




def tianquan1():
    str = "天泉穴"
    x = leg_mid3
    y = yeqianwen_y1 + 2 * cun1
    return (x, y, str)



def tianfu1():
    str = '天府穴'
    x0, y0, str1 = tianquan1()
    for i in range(w):
        if binary[y0, x0 - i] == 0:
            x = x0 - i
            break
    y = y0 + cun1
    return (x, y, str)



def xiabai1():
    str = '侠白穴'
    x0, y0, str1 = tianfu1()
    x = x0 - int((pow(2, 0.5) * cun1) / 2)
    y = y0 + int((pow(2, 0.5) * cun1) / 2)
    return (x, y, str)




zuowan_x1, zuowan_y1, zuowan_str1, n0, m0 = youwan1()  
cun2 = int((((zuowan_x1 - zuozhou_x1) ** 2 + (zuowan_y1 - zuozhou_y1) ** 2) ** 0.5) / 12)  



def dalin1():
    str = '大陵穴'
    y = zuowan_y1 + 5
    x =n0 + int((m0 - n0) / 3)
    return (x, y, str)



def shenmen1():
    str = '神门穴'
    y = zuowan_y1 + 10
    x = m0 - int((m0 - n0) / 3)
    return (x, y, str)



def taiyuan1():
    str = '太渊穴'
    x = n0
    y = zuowan_y1
    return (x, y, str)



def xinbaojing1():
    x1, y1, str1 = dalin1()
    x2, y2, str2 = left_quze1()
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 1)  






def xinjing1():
    x1, y1, str1 = shenmen1()
    x2, y2, str2 = left_shaohai1()
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 1)






def feijing1():
    x1, y1, str1 = chize1()
    x2, y2, str2 = taiyuan1()
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 1)










def neiguanxue1():
    str = '内关穴'
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - zuozhou_y1) / (zuowan_y1 - zuozhou_y1) - (x - zuozhou_x1) / (zuowan_x1 - zuozhou_x1),
                    (((zuowan_x1 - x) ** 2 + (zuowan_y1 - y) ** 2) ** 0.5) - (2 * cun2)], [x, y])
    x0 = int(result[1][0])  
    y0 = int(result[1][1])
    return (x0, y0, str)



def jianshi1():
    str = '间使穴'
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - zuozhou_y1) / (zuowan_y1 - zuozhou_y1) - (x - zuozhou_x1) / (zuowan_x1 - zuozhou_x1),
                    (((zuowan_x1 - x) ** 2 + (zuowan_y1 - y) ** 2) ** 0.5) - (3 * cun2)], [x, y])
    x0 = int(result[1][0])
    y0 = int(result[1][1])
    return (x0, y0, str)



def ximen1():
    str = '郄门穴'
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - zuozhou_y1) / (zuowan_y1 - zuozhou_y1) - (x - zuozhou_x1) / (zuowan_x1 - zuozhou_x1),
                    (((zuowan_x1 - x) ** 2 + (zuowan_y1 - y) ** 2) ** 0.5) - (5 * cun2)], [x, y])
    x0 = int(result[1][0])
    y0 = int(result[1][1])
    return (x0, y0, str)



shenmen_x1, shenmen_y1, shenmen_str1 = shenmen1()
shaohai_x1, shaohai_y1, shaohai_str1 = left_shaohai1()




def yinxi1():
    str = '阴郄穴'
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - shenmen_y1) / (shaohai_y1 - shenmen_y1) - (x - shenmen_x1) / (shaohai_x1 - shenmen_x1),
                    (((shenmen_x1 - x) ** 2 + (shenmen_y1 - y) ** 2) ** 0.5) - (0.5 * cun2)], [x, y])
    x0 = int(result[1][0])  
    y0 = int(result[1][1])
    return (x0, y0, str)



def tongli1():
    str = '通里穴'
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - shenmen_y1) / (shaohai_y1 - shenmen_y1) - (x - shenmen_x1) / (shaohai_x1 - shenmen_x1),
                    (((shenmen_x1 - x) ** 2 + (shenmen_y1 - y) ** 2) ** 0.5) - (1 * cun2)], [x, y])
    x0 = int(result[1][0])  
    y0 = int(result[1][1])
    return (x0, y0, str)



def lingdao1():
    str = '灵道穴'
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - shenmen_y1) / (shaohai_y1 - shenmen_y1) - (x - shenmen_x1) / (shaohai_x1 - shenmen_x1),
                    (((shenmen_x1 - x) ** 2 + (shenmen_y1 - y) ** 2) ** 0.5) - (1.5 * cun2)], [x, y])
    x0 = int(result[1][0])  
    y0 = int(result[1][1])
    return (x0, y0, str)




chize_x1, chize_y1, chize_str1 = chize1()
taiyuan_x1, taiyuan_y1, taiyaun_str1 = taiyuan1()





def kongzui1():
    str = '孔最穴'
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - chize_y1) / (taiyuan_y1 - chize_y1) - (x - chize_x1) / (taiyuan_x1 - chize_x1),
                    (((taiyuan_x1 - x) ** 2 + (taiyuan_y1 - y) ** 2) ** 0.5) - (7 * cun2)], [x, y])
    x0 = int(result[1][0])  
    y0 = int(result[1][1])
    return (x0, y0, str)



def jingqu1():
    str = '经渠穴'
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - chize_y1) / (taiyuan_y1 - chize_y1) - (x - chize_x1) / (taiyuan_x1 - chize_x1),
                    (((taiyuan_x1 - x) ** 2 + (taiyuan_y1 - y) ** 2) ** 0.5) - (1 * cun2)], [x, y])
    x0 = int(result[1][0])  
    y0 = int(result[1][1])
    return (x0, y0, str)



def lieque1():
    str = '列缺穴'
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - chize_y1) / (taiyuan_y1 - chize_y1) - (x - chize_x1) / (taiyuan_x1 - chize_x1),
                    (((taiyuan_x1 - x) ** 2 + (taiyuan_y1 - y) ** 2) ** 0.5) - (1.5 * cun2)], [x, y])
    x0 = int(result[1][0])  
    y0 = int(result[1][1])
    return (x0, y0, str)
