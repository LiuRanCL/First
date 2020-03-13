from sympy import *
import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import run_front
from local_base_point import right_yewo, left_yewo
from local_variable_back import *
from local_contour import contour
from PATH_DEFINE import BackPath

img_path = BackPath
img = cv2.imread(img_path)

h, w, a = img.shape
m = 0
n = 0

path = contour(img_path)
binary = cv2.imread(img_path + '_binary' + '.jpg', 0)

print("加载背面正中线X值...")


def mid_back():
    x0, y0, a = run_front.duqi()
    for i in range(w - 1):
        if binary[y0, x0 + i] == 0:
            n = x0 + i
            break
    for i in range(w - 1):
        if binary[y0, x0 - i] == 0:
            m = x0 - i
            break
    mid_x = int((n + m) / 2)
    return mid_x


mid_x = mid_back()

cun_heng = run_front.cun_heng
cun_arm = run_front.cun1
cun_leg = run_front.cun_leg
cun2 = run_front.cun2


def yaoyangguan():
    str = "腰阳关"
    x0, y0, a = run_front.duqi()
    x = mid_x
    return (x0, y0, str)


def taodao():
    str = "陶道"
    x0, y0, a = run_front.xuanji()
    x = mid_x
    return (x, y0, str)


yaoyangguan_x, yaoyangguan_y, yaoyangguan_str = yaoyangguan()
print(yaoyangguan_x, yaoyangguan_y, yaoyangguan_str)
taodao_x, taodao_y, taodao_str = taodao()


def mold():
    x = Symbol('x')
    y = yaoyangguan_y - taodao_y
    result = solve([y - (x * 6 + (50 / 38) * x * 4 + (70 / 38) * x * 5)])
    return result[x]


mold = mold()

vertebra_down = (70 / 38) * mold
vertebra_mid = (50 / 38) * mold
vertebra_up = mold


def dazhui():
    str = "大椎"
    x = taodao_x
    y = taodao_y - round(vertebra_up)
    return (x, y, str)


def mingmen():
    str = "命门"
    x0, y0, z = yaoyangguan()
    y = y0 - round(vertebra_down * 2)
    return (x0, y, str)


def xuanshu():
    str = "悬枢"
    x0, y0, z = yaoyangguan()
    y = y0 - round(vertebra_down * 3)
    return (x0, y, str)


def jizhong():
    str = "脊中"
    x0, y0, z = yaoyangguan()
    y = y0 - round(vertebra_down * 5)
    return (x0, y, str)


def zhongshu():
    str = "中枢"
    x0, y0, z = yaoyangguan()
    y = y0 - round(vertebra_down * 5) - round(vertebra_mid)
    return (x0, y, str)


def jinsuo():
    str = "筋缩"
    x0, y0, z = yaoyangguan()
    y = y0 - round(vertebra_down * 5) - round(vertebra_mid * 2)
    return (x0, y, str)


def zhiyang():
    str = "至阳"
    x0, y0, z = yaoyangguan()
    y = y0 - round(vertebra_down * 5) - round(vertebra_mid * 4)
    return (x0, y, str)


def lingtai():
    str = "灵台"
    x0, y0, z = yaoyangguan()
    y = y0 - round(vertebra_down * 5) - round(vertebra_mid * 4) - round(vertebra_up)
    return (x0, y, str)


def shendao():
    str = "神道"
    x0, y0, z = yaoyangguan()
    y = y0 - round(vertebra_down * 5) - round(vertebra_mid * 4) - round(vertebra_up * 2)
    return (x0, y, str)


def shenzhu():
    str = "身柱"
    x0, y0, z = yaoyangguan()
    y = y0 - round(vertebra_down * 5) - round(vertebra_mid * 4) - round(vertebra_up * 4)
    return (x0, y, str)


def yaoshu():
    str = "腰俞穴"
    x0, y0, z = run_front.qugu()
    x = mid_x
    y = y0 - round(run_front.cun_zong * 1.5)
    return (x, y, str)


def changqiang():
    str = "长强穴"
    x0, y0, z = yaoshu()
    x = mid_x
    y = y0 + round(2 * vertebra_down)
    return (x, y, str)


def shiqizhui():
    str = "十七椎"
    x0, y0, z = yaoyangguan()
    y = y0 + round(vertebra_down * 0.5)
    return (x0, y, str)


def xiajiyu():
    str = "下极俞"
    x0, y0, z = yaoyangguan()
    y = y0 - round(vertebra_down)
    return (x0, y, str)


def jieji():
    str = "接脊"
    x0, y0, z = yaoyangguan()
    y = y0 - round(vertebra_down * 4)
    return (x0, y, str)


def yaoqi():
    str = "腰奇"
    x0, y0, z = yaoshu()
    x = mid_x
    y = y0 + round(vertebra_up)
    return (x, y, str)


def temp1():
    str = "temp1"
    x0, y0, z = yaoyangguan()
    y = y0 - round(vertebra_down * 5) - round(vertebra_mid * 4) - round(vertebra_up * 5)
    return (x0, y, str)


def temp2():
    str = "temp2"
    x0, y0, z = yaoyangguan()
    y = y0 - round(vertebra_down * 5) - round(vertebra_mid * 4) - round(vertebra_up * 3)
    return (x0, y, str)


def temp3():
    str = "temp3"
    x0, y0, z = yaoyangguan()
    y = y0 - round(vertebra_down * 5) - round(vertebra_mid * 3)
    return (x0, y, str)


def dashu():
    str = "大抒穴"
    x0, y0, z0 = taodao()
    x = x0 - round(cun_heng * 1.5)
    return (x, y0, str)


def fengmen():
    str = "风门"
    x0, y0, z0 = taodao()
    y = y0 + vertebra_up
    x = x0 - round(cun_heng * 1.5)
    return (x, y, str)


def feiyu():
    str = "肺俞"
    x0, y0, z0 = shenzhu()
    x = x0 - round(cun_heng * 1.5)
    return (x, y0, str)


def jueyinyu():
    str = "厥阴俞"
    x0, y0, z0 = shenzhu()
    y = y0 + vertebra_up
    x = x0 - round(cun_heng * 1.5)
    return (x, y, str)


def xinyu():
    str = "心俞"
    x0, y0, z0 = shendao()
    x = x0 - round(cun_heng * 1.5)
    return (x, y0, str)


def duyu():
    str = "督俞"
    x0, y0, z0 = lingtai()
    x = x0 - round(cun_heng * 1.5)
    return (x, y0, str)


def geyu():
    str = "膈俞"
    x0, y0, z0 = zhiyang()
    x = x0 - round(cun_heng * 1.5)
    return (x, y0, str)


def weiwanxiashu():
    str = "胃脘下俞"
    x0, y0, z0 = zhiyang()
    y = y0 + vertebra_up
    x = x0 - round(cun_heng * 1.5)
    return (x, y, str)


def ganyu():
    str = "肝俞"
    x0, y0, z0 = jinsuo()
    x = x0 - round(cun_heng * 1.5)
    return (x, y0, str)


def danyu():
    str = "胆俞"
    x0, y0, z0 = zhongshu()
    x = x0 - round(cun_heng * 1.5)
    return (x, y0, str)


def piyu():
    str = "脾俞"
    x0, y0, z0 = jizhong()
    x = x0 - round(cun_heng * 1.5)
    return (x, y0, str)


def weiyu():
    str = "胃俞"
    x0, y0, z0 = jieji()
    x = x0 - round(cun_heng * 1.5)
    return (x, y0, str)


def sanjiaoyu():
    str = "三焦俞"
    x0, y0, z0 = xuanshu()
    x = x0 - round(cun_heng * 1.5)
    return (x, y0, str)


def shenyu():
    str = "肾俞"
    x0, y0, z0 = mingmen()
    x = x0 - round(cun_heng * 1.5)
    return (x, y0, str)


def qihaiyu():
    str = "气海俞"
    x0, y0, z0 = xiajiyu()
    x = x0 - round(cun_heng * 1.5)
    return (x, y0, str)


def dachangyu():
    str = "大肠俞"
    x0, y0, z0 = yaoyangguan()
    x = x0 - round(cun_heng * 1.5)
    return (x, y0, str)


def guanyuanyu():
    str = "关元俞"
    x0, y0, z0 = yaoyangguan()
    y = y0 + vertebra_down
    x = x0 - round(cun_heng * 1.5)
    return (x, y, str)


def xiaochangyu():
    str = "小肠俞"
    x0, y0, z0 = guanyuanyu()
    x = x0
    y = y0 + vertebra_mid
    return (x, y, str)


def pangguangyu():
    str = "膀胱俞"
    x0, y0, z0 = guanyuanyu()
    x = x0
    y = y0 + round(vertebra_mid * 2)
    return (x, y, str)


def zhonglvyu():
    str = "中膂俞"
    x0, y0, z0 = guanyuanyu()
    x = x0
    y = y0 + round(vertebra_mid * 3)
    return (x, y, str)


def baihuanyu():
    str = "白环俞"
    x0, y0, z0 = guanyuanyu()
    x = x0
    y = y0 + round(vertebra_mid * 4)
    return (x, y, str)


def shangliao():
    str = "上髎穴"
    x0, y0, z0 = xiaochangyu()
    x = x0 + round(0.2 * cun_heng)
    y = y0
    return (x, y, str)


def ciliao():
    str = "次髎穴"
    x0, y0, z0 = guanyuanyu()
    x = x0 + int(0.4 * cun_heng)
    y = y0 + round(vertebra_mid * 2)
    return (x, y, str)


def zhongliao():
    str = "中髎"
    x0, y0, z0 = guanyuanyu()
    x = x0 + round(0.6 * cun_heng)
    y = y0 + round(vertebra_mid * 3)
    return (x, y, str)


def xialiaoxue():
    str = "下髎穴"
    x0, y0, z0 = guanyuanyu()
    x = x0 + int(0.8 * cun_heng)
    y = y0 + round(vertebra_mid * 4)
    return (x, y, str)


def huiyang():
    str = "会阳穴"
    x0, y0, z0 = guanyuanyu()
    x = x0 + int(cun_heng)
    y = y0 + round(vertebra_mid * 5)
    return (x, y, str)


def fufen():
    str = "附分穴"
    x0, y0, z0 = taodao()
    y = y0 + vertebra_up
    x = x0 - round(cun_heng * 3)
    return (x, y, str)


def pohu():
    str = "魄户"
    x0, y0, z0 = shenzhu()
    x = x0 - round(cun_heng * 3)
    return (x, y0, str)


def gaohuang():
    str = "膏肓"
    x0, y0, z0 = shenzhu()
    y = y0 + vertebra_up
    x = x0 - round(cun_heng * 3)
    return (x, y, str)


def shentang():
    str = "神堂"
    x0, y0, z0 = shendao()
    x = x0 - round(cun_heng * 3)
    return (x, y0, str)


def yixi():
    str = "譩譆"
    x0, y0, z0 = lingtai()
    x = x0 - round(cun_heng * 3)
    return (x, y0, str)


def geguan():
    str = "膈关穴"
    x0, y0, z0 = zhiyang()
    x = x0 - round(cun_heng * 3)
    return (x, y0, str)


def hunmen():
    str = "魂门"
    x0, y0, z0 = jinsuo()
    x = x0 - round(cun_heng * 3)
    return (x, y0, str)


def yanggang():
    str = "阳纲"
    x0, y0, z0 = zhongshu()
    x = x0 - round(cun_heng * 3)
    return (x, y0, str)


def yishe():
    str = "意舍穴"
    x0, y0, z0 = jizhong()
    x = x0 - round(cun_heng * 3)
    return (x, y0, str)


def weicang():
    str = "胃仓"
    x0, y0, z0 = jieji()
    x = x0 - round(cun_heng * 3)
    return (x, y0, str)


def huangmen():
    str = "肓门穴"
    x0, y0, z0 = xuanshu()
    x = x0 - round(cun_heng * 3)
    return (x, y0, str)


def zhishi():
    str = "志室穴"
    x0, y0, z0 = mingmen()
    x = x0 - round(cun_heng * 3)
    return (x, y0, str)


def baomang():
    str = "胞盲穴"
    x0, y0, z0 = guanyuanyu()
    x = x0 - round(cun_heng * 1.5)
    y = y0 + round(vertebra_mid * 2)
    return (x, y, str)


def zhibian():
    str = "秩边穴"
    x0, y0, z0 = guanyuanyu()
    x = x0 - round(cun_heng * 1.5)
    y = y0 + round(vertebra_mid * 4)
    return (x, y, str)


yewo_left_x, yewo_left_y = right_yewo(mid_x)


def up_yewo():
    yewo_y = 0
    for l in range(h):
        if binary[yewo_left_y - l, yewo_left_x] == 255:
            for k in range(h):
                if binary[yewo_left_y - l - 5 - k, yewo_left_x] == 0:
                    yewo_y = int(yewo_left_y - l - 5 - k + int(cun_arm * 4))
                    break
                else:
                    pass
            break
        else:
            pass
    return yewo_y


yewo_y = up_yewo()


def mid_arm():
    mid_arm1 = 0
    for i in range(w):
        if binary[yewo_y, yewo_left_x - i] == 255:
            for p in range(w):
                if binary[yewo_y, yewo_left_x - 5 - i - p] == 0:
                    mid_arm1 = int((yewo_left_x - i + yewo_left_x - 5 - i - p) / 2)
                    break
                else:
                    pass
            break
        else:
            pass
    return mid_arm1


mid_arm_x = mid_arm()


def naohui():
    str = "臑会穴"
    x = mid_arm_x
    y = yewo_y
    return (x, y, str)


naohui_x, naohui_y, naohui_str = naohui()


def zhoujian():
    str = '肘尖'
    for i in range(w):
        if binary[left_elbow_y, left_elbow_x + 10 + i] == 0:
            m = left_elbow_x + 10 + i
            break

    for i in range(w):
        if binary[left_elbow_y, left_elbow_x + 10 - i] == 0:
            n = left_elbow_x - i + 10
            break
    y = left_elbow_y
    x = int((m + n) / 2)
    return (x, y, str)


zhoujian_x, zhoujian_y, zhoujian_str = zhoujian()


def xiaoluo():
    str = "消泺穴"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - zhoujian_y) / (naohui_y - zhoujian_y) - (x - zhoujian_x) / (naohui_x - zhoujian_x),
                    (((zhoujian_x - x) ** 2 + (zhoujian_y - y) ** 2) ** 0.5) - (5 * cun2)], [x, y])
    x0 = int(result[1][0])
    y0 = int(result[1][1])
    return (x0, y0, str)


def qinglengyuan():
    str = "清冷渊"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - zhoujian_y) / (naohui_y - zhoujian_y) - (x - zhoujian_x) / (naohui_x - zhoujian_x),
                    (((zhoujian_x - x) ** 2 + (zhoujian_y - y) ** 2) ** 0.5) - (2 * cun_arm)], [x, y])
    x0 = int(result[1][0])
    y0 = int(result[1][1])
    return (x0, y0, str)


def tianjing():
    str = "天井"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - zhoujian_y) / (naohui_y - zhoujian_y) - (x - zhoujian_x) / (naohui_x - zhoujian_x),
                    (((zhoujian_x - x) ** 2 + (zhoujian_y - y) ** 2) ** 0.5) - (1 * cun_arm)], [x, y])
    x0 = int(result[1][0])
    y0 = int(result[1][1])
    return (x0, y0, str)


def zuowan():
    str = '左腕'
    m = n = 0
    left_hand = left_hand_x
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


zuowan_x, zuowan_y, zuowan_str, zuowan_n, zuowan_m = zuowan()


def yangchi():
    str = "阳池穴"
    x0 = round((zuowan_m - zuowan_n) / 3)
    x = zuowan_m - x0
    y = zuowan_y
    return (x, y, str)


yangchi_x, yangchi_y, yangchi_str = yangchi()


def sidu():
    str = "四渎穴"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - zuowan_y) / (zhoujian_y - zuowan_y) - (x - zuowan_x) / (zhoujian_x - zuowan_x),
                    (((zhoujian_x - x) ** 2 + (zhoujian_y - y) ** 2) ** 0.5) - (5 * cun2)], [x, y])
    x0 = int(result[0][0])
    y0 = int(result[0][1])
    return (x0, y0, str)


sidu_x, sidu_y, sidu_str = sidu()


def sanyangluo():
    str = "三阳络"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - yangchi_y) / (sidu_y - yangchi_y) - (x - yangchi_x) / (sidu_x - yangchi_x),
                    (((yangchi_x - x) ** 2 + (yangchi_y - y) ** 2) ** 0.5) - (4 * cun2)], [x, y])
    x0 = int(result[1][0])
    y0 = int(result[1][1])
    return (x0, y0, str)


def zhigou():
    str = "支沟穴"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - yangchi_y) / (sidu_y - yangchi_y) - (x - yangchi_x) / (sidu_x - yangchi_x),
                    (((yangchi_x - x) ** 2 + (yangchi_y - y) ** 2) ** 0.5) - (3 * cun2)], [x, y])
    x0 = int(result[1][0])
    y0 = int(result[1][1])
    return (x0, y0, str)


def huizong():
    str = "会宗穴"
    x0, y0, z = zhigou()
    x = x0 + round(0.5 * cun_arm)
    return (x, y0, str)


def waiguan():
    str = "外关穴"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - yangchi_y) / (sidu_y - yangchi_y) - (x - yangchi_x) / (sidu_x - yangchi_x),
                    (((yangchi_x - x) ** 2 + (yangchi_y - y) ** 2) ** 0.5) - (2 * cun2)], [x, y])
    x0 = int(result[1][0])
    y0 = int(result[1][1])
    return (x0, y0, str)


def huiyin():
    str = "裆部"
    for i in range(h):
        if binary[int(yaoyangguan_y) + i, mid_x + 3] == 0:
            y1 = int(yaoyangguan_y) + i
            x1 = mid_x
            break
    return (round(x1), round(y1), str)


huiyin_x, huiyin_y, huiying_str = huiyin()


def chengfu():
    str = "承扶穴"
    y = huiyin_y
    for i in range(w):
        if binary[huiyin_y, huiyin_x - 5 - i] == 0:
            x = round((huiyin_x - 5 - i + huiyin_x) / 2)
            break
    return (x, y, str)


chengfu_x, chengfu_y, chengfu_str = chengfu()


def xizhong():
    str = ''
    for i in range(w):
        if binary[left_knee_y, left_knee_x + 5 + i] == 0:
            m = left_knee_x + 5 + i
            break

    for i in range(w):
        if binary[left_knee_y, left_knee_x + 5 - i] == 0:
            n = left_knee_x + 5 - i
            break
    y = left_knee_y
    x = int((m + n) / 2)
    return (x, y, str, n, m)


xizhong_x, xizhong_y, xizhong_z, xizhong_n, xizhong_m = xizhong()


def weizhong():
    str = "委中穴"
    x = xizhong_x
    y = xizhong_y
    return (x, y, str)


def weiyang():
    str = "委阳穴"
    for i in range(w):
        if binary[xizhong_y, xizhong_x - i] == 0:
            x = round((xizhong_x * 2 - i) / 2)
            break
    y = xizhong_y
    return (x, y, str)


def fuxi():
    str = "浮郄穴"
    x0, y0, z0 = weiyang()
    x = x0
    y = y0 - cun_leg
    return (x, y, str)


fuxi_x, fuxi_y, fuxi_str = fuxi()


def yinmen():
    str = "殷门穴"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - fuxi_y) / (chengfu_y - fuxi_y) - (x - fuxi_x) / (chengfu_x - fuxi_x),
                    (((chengfu_x - x) ** 2 + (chengfu_y - y) ** 2) ** 0.5) - (6 * cun_leg)], [x, y])
    x0 = int(result[0][0])
    y0 = int(result[0][1])
    return (x0, y0, str)


def heyang():
    str = "合阳穴"
    x = xizhong_x
    y = xizhong_y + cun_leg
    return (x, y, str)


def chengjin():
    str = "承筋穴"
    for i in range(w):
        if binary[xizhong_y, xizhong_x + i] == 0:
            m = xizhong_x + i
            break

    for i in range(w):
        if binary[xizhong_y, xizhong_x - i] == 0:
            n = xizhong_x - i
            break
    x = int((m + n) / 2)
    y = xizhong_y + 5 * cun_leg
    return (x, y, str)


def chengshan():
    str = "承山穴"
    for i in range(w):
        if binary[xizhong_y, xizhong_x + i] == 0:
            m = xizhong_x + i
            break

    for i in range(w):
        if binary[xizhong_y, xizhong_x - i] == 0:
            n = xizhong_x - i
            break
    x = int((m + n) / 2)
    y = xizhong_y + 9 * cun_leg
    return (x, y, str)


'''
    来吧，背部右侧的穴位！！！
'''


def dashu1():
    str = "大抒穴"
    x0, y0, z0 = taodao()
    x = x0 + round(cun_heng * 1.5)
    return (x, y0, str)


def fengmen1():
    str = "风门"
    x0, y0, z0 = taodao()
    y = y0 + vertebra_up
    x = x0 + round(cun_heng * 1.5)
    return (x, y, str)


def feiyu1():
    str = "肺俞"
    x0, y0, z0 = shenzhu()
    x = x0 + round(cun_heng * 1.5)
    return (x, y0, str)


def jueyinyu1():
    str = "厥阴俞"
    x0, y0, z0 = shenzhu()
    y = y0 + vertebra_up
    x = x0 + round(cun_heng * 1.5)
    return (x, y, str)


def xinyu1():
    str = "心俞"
    x0, y0, z0 = shendao()
    x = x0 + round(cun_heng * 1.5)
    return (x, y0, str)


def duyu1():
    str = "督俞"
    x0, y0, z0 = lingtai()
    x = x0 + round(cun_heng * 1.5)
    return (x, y0, str)


def geyu1():
    str = "膈俞"
    x0, y0, z0 = zhiyang()
    x = x0 + round(cun_heng * 1.5)
    return (x, y0, str)


def weiwanxiashu1():
    str = "胃脘下俞"
    x0, y0, z0 = zhiyang()
    y = y0 + vertebra_up
    x = x0 + round(cun_heng * 1.5)
    return (x, y, str)


def ganyu1():
    str = "肝俞"
    x0, y0, z0 = jinsuo()
    x = x0 + round(cun_heng * 1.5)
    return (x, y0, str)


def danyu1():
    str = "胆俞"
    x0, y0, z0 = zhongshu()
    x = x0 + round(cun_heng * 1.5)
    return (x, y0, str)


def piyu1():
    str = "脾俞"
    x0, y0, z0 = jizhong()
    x = x0 + round(cun_heng * 1.5)
    return (x, y0, str)


def weiyu1():
    str = "胃俞"
    x0, y0, z0 = jieji()
    x = x0 + round(cun_heng * 1.5)
    return (x, y0, str)


def sanjiaoyu1():
    str = "三焦俞"
    x0, y0, z0 = xuanshu()
    x = x0 + round(cun_heng * 1.5)
    return (x, y0, str)


def shenyu1():
    str = "肾俞"
    x0, y0, z0 = mingmen()
    x = x0 + round(cun_heng * 1.5)
    return (x, y0, str)


def qihaiyu1():
    str = "气海俞"
    x0, y0, z0 = xiajiyu()
    x = x0 + round(cun_heng * 1.5)
    return (x, y0, str)


def dachangyu1():
    str = "大肠俞"
    x0, y0, z0 = yaoyangguan()
    x = x0 + round(cun_heng * 1.5)
    return (x, y0, str)


def guanyuanyu1():
    str = "关元俞"
    x0, y0, z0 = yaoyangguan()
    y = y0 + vertebra_down
    x = x0 + round(cun_heng * 1.5)
    return (x, y, str)


def xiaochangyu1():
    str = "小肠俞"
    x0, y0, z0 = guanyuanyu1()
    x = x0
    y = y0 + vertebra_mid
    return (x, y, str)


def pangguangyu1():
    str = "膀胱俞"
    x0, y0, z0 = guanyuanyu1()
    x = x0
    y = y0 + round(vertebra_mid * 2)
    return (x, y, str)


def zhonglvyu1():
    str = "中膂俞"
    x0, y0, z0 = guanyuanyu1()
    x = x0
    y = y0 + round(vertebra_mid * 3)
    return (x, y, str)


def baihuanyu1():
    str = "白环俞"
    x0, y0, z0 = guanyuanyu1()
    x = x0
    y = y0 + round(vertebra_mid * 4)
    return (x, y, str)


def shangliao1():
    str = "上髎穴"
    x0, y0, z0 = xiaochangyu1()
    x = x0 - round(0.2 * cun_heng)
    y = y0
    return (x, y, str)


def ciliao1():
    str = "次髎穴"
    x0, y0, z0 = guanyuanyu1()
    x = x0 - int(0.4 * cun_heng)
    y = y0 + round(vertebra_mid * 2)
    return (x, y, str)


def zhongliao1():
    str = "中髎"
    x0, y0, z0 = guanyuanyu1()
    x = x0 - round(0.6 * cun_heng)
    y = y0 + round(vertebra_mid * 3)
    return (x, y, str)


def xialiaoxue1():
    str = "下髎穴"
    x0, y0, z0 = guanyuanyu1()
    x = x0 - int(0.8 * cun_heng)
    y = y0 + round(vertebra_mid * 4)
    return (x, y, str)


def huiyang1():
    str = "会阳穴"
    x0, y0, z0 = guanyuanyu1()
    x = x0 - int(cun_heng)
    y = y0 + round(vertebra_mid * 5)
    return (x, y, str)


def fufen1():
    str = "附分穴"
    x0, y0, z0 = taodao()
    y = y0 + vertebra_up
    x = x0 + round(cun_heng * 3)
    return (x, y, str)


def pohu1():
    str = "魄户"
    x0, y0, z0 = shenzhu()
    x = x0 + round(cun_heng * 3)
    return (x, y0, str)


def gaohuang1():
    str = "膏肓"
    x0, y0, z0 = shenzhu()
    y = y0 + vertebra_up
    x = x0 + round(cun_heng * 3)
    return (x, y, str)


def shentang1():
    str = "神堂"
    x0, y0, z0 = shendao()
    x = x0 + round(cun_heng * 3)
    return (x, y0, str)


def yixi1():
    str = "譩譆"
    x0, y0, z0 = lingtai()
    x = x0 + round(cun_heng * 3)
    return (x, y0, str)


def geguan1():
    str = "膈关穴"
    x0, y0, z0 = zhiyang()
    x = x0 + round(cun_heng * 3)
    return (x, y0, str)


def hunmen1():
    str = "魂门"
    x0, y0, z0 = jinsuo()
    x = x0 + round(cun_heng * 3)
    return (x, y0, str)


def yanggang1():
    str = "阳纲"
    x0, y0, z0 = zhongshu()
    x = x0 + round(cun_heng * 3)
    return (x, y0, str)


def yishe1():
    str = "意舍穴"
    x0, y0, z0 = jizhong()
    x = x0 + round(cun_heng * 3)
    return (x, y0, str)


def weicang1():
    str = "胃仓"
    x0, y0, z0 = jieji()
    x = x0 + round(cun_heng * 3)
    return (x, y0, str)


def huangmen1():
    str = "肓门穴"
    x0, y0, z0 = xuanshu()
    x = x0 + round(cun_heng * 3)
    return (x, y0, str)


def zhishi1():
    str = "志室穴"
    x0, y0, z0 = mingmen()
    x = x0 + round(cun_heng * 3)
    return (x, y0, str)


def baomang1():
    str = "胞盲穴"
    x0, y0, z0 = guanyuanyu1()
    x = x0 + round(cun_heng * 1.5)
    y = y0 + round(vertebra_mid * 2)
    return (x, y, str)


def zhibian1():
    str = "秩边穴"
    x0, y0, z0 = guanyuanyu1()
    x = x0 + round(cun_heng * 1.5)
    y = y0 + round(vertebra_mid * 4)
    return (x, y, str)


'''
    手部
'''

yewo_left_x1, yewo_left_y1 = left_yewo(mid_x)


def up_yewo1():
    yewo_y = 0
    for l in range(h):
        if binary[yewo_left_y1 - l, yewo_left_x1] == 255:
            for k in range(h):
                if binary[yewo_left_y1 - l - 5 - k, yewo_left_x1] == 0:
                    yewo_y = int(yewo_left_y1 - l - 5 - k + int(cun_arm * 4))
                    break
                else:
                    pass
            break
        else:
            pass
    return yewo_y


yewo_y1 = up_yewo1()


def mid_arm1():
    mid_arm1 = 0
    for i in range(w):
        if binary[yewo_y1, yewo_left_x1 + i] == 255:
            for p in range(w):
                if binary[yewo_y1, yewo_left_x1 + 5 + i + p] == 0:
                    mid_arm1 = int((yewo_left_x1 + i + yewo_left_x1 + 5 + i + p) / 2)
                    break
                else:
                    pass
            break
        else:
            pass
    return mid_arm1


mid_arm_x1 = mid_arm1()


def naohui1():
    str = "臑会穴"
    x = mid_arm_x1
    y = yewo_y1
    return (x, y, str)


naohui_x1, naohui_y1, naohui_str1 = naohui1()


def zhoujian1():
    str = '肘尖'
    for i in range(w):
        if binary[right_elbow_y, right_elbow_x + i] == 0:
            m = right_elbow_x + i
            break

    for i in range(w):
        if binary[right_elbow_y, right_elbow_x - i] == 0:
            n = right_elbow_x - i
            break
    y = right_elbow_y
    x = int((m + n) / 2)
    return (x, y, str)


zhoujian_x1, zhoujian_y1, zhoujian_str1 = zhoujian1()


def xiaoluo1():
    str = "消泺穴"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - zhoujian_y1) / (naohui_y1 - zhoujian_y1) - (x - zhoujian_x1) / (naohui_x1 - zhoujian_x1),
                    (((zhoujian_x1 - x) ** 2 + (zhoujian_y1 - y) ** 2) ** 0.5) - (5 * cun2)], [x, y])
    x0 = int(result[0][0])
    y0 = int(result[0][1])
    return (x0, y0, str)


def qinglengyuan1():
    str = "清冷渊"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - zhoujian_y1) / (naohui_y1 - zhoujian_y1) - (x - zhoujian_x1) / (naohui_x1 - zhoujian_x1),
                    (((zhoujian_x1 - x) ** 2 + (zhoujian_y1 - y) ** 2) ** 0.5) - (2 * cun_arm)], [x, y])
    x0 = int(result[0][0])
    y0 = int(result[0][1])
    return (x0, y0, str)


def tianjing1():
    str = "天井"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - zhoujian_y1) / (naohui_y1 - zhoujian_y1) - (x - zhoujian_x1) / (naohui_x1 - zhoujian_x1),
                    (((zhoujian_x1 - x) ** 2 + (zhoujian_y1 - y) ** 2) ** 0.5) - (1 * cun_arm)], [x, y])
    x0 = int(result[0][0])
    y0 = int(result[0][1])
    return (x0, y0, str)


def youwan1():
    str = '左腕'
    m = n = 0
    left_hand = right_hand_x
    for i in range(w):
        if binary[right_hand_y, left_hand + i] == 0:
            m = left_hand + i
            break
    for i in range(w):
        if binary[right_hand_y, left_hand - i] == 0:
            n = left_hand - i
            break
    y = right_hand_y + 5
    x = int((m + n) / 2)

    return (x, y, str, n, m)


zuowan_x1, zuowan_y1, zuowan_str1, zuowan_n1, zuowan_m1 = youwan1()


def yangchi1():
    str = "阳池穴"
    x0 = round((zuowan_m1 - zuowan_n1) / 3)
    x = zuowan_m1 - x0
    y = zuowan_y1
    return (x, y, str)


yangchi_x1, yangchi_y1, yangchi_str1 = yangchi1()


def sidu1():
    str = "四渎穴"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - zuowan_y1) / (zhoujian_y1 - zuowan_y1) - (x - zuowan_x1) / (zhoujian_x1 - zuowan_x1),
                    (((zhoujian_x1 - x) ** 2 + (zhoujian_y1 - y) ** 2) ** 0.5) - (5 * cun2)], [x, y])
    x0 = int(result[1][0])
    y0 = int(result[1][1])
    return (x0, y0, str)


sidu_x1, sidu_y1, sidu_str1 = sidu1()


def sanyangluo1():
    str = "三阳络"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - yangchi_y1) / (sidu_y1 - yangchi_y1) - (x - yangchi_x1) / (sidu_x1 - yangchi_x1),
                    (((yangchi_x1 - x) ** 2 + (yangchi_y1 - y) ** 2) ** 0.5) - (4 * cun2)], [x, y])
    x0 = int(result[0][0])
    y0 = int(result[0][1])
    return (x0, y0, str)


def zhigou1():
    str = "支沟穴"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - yangchi_y1) / (sidu_y1 - yangchi_y1) - (x - yangchi_x1) / (sidu_x1 - yangchi_x1),
                    (((yangchi_x1 - x) ** 2 + (yangchi_y1 - y) ** 2) ** 0.5) - (3 * cun2)], [x, y])
    x0 = int(result[0][0])
    y0 = int(result[0][1])
    return (x0, y0, str)


def huizong1():
    str = "会宗穴"
    x0, y0, z = zhigou1()
    x = x0 - round(0.5 * cun_arm)
    return (x, y0, str)


def waiguan1():
    str = "外关穴"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - yangchi_y1) / (sidu_y1 - yangchi_y1) - (x - yangchi_x1) / (sidu_x1 - yangchi_x1),
                    (((yangchi_x1 - x) ** 2 + (yangchi_y1 - y) ** 2) ** 0.5) - (2 * cun2)], [x, y])
    x0 = int(result[0][0])
    y0 = int(result[0][1])
    return (x0, y0, str)


'''
    腿部
'''


def chengfu1():
    str = "承扶穴"
    y = huiyin_y
    for i in range(w):
        if binary[huiyin_y, huiyin_x + 5 + i] == 255:
            m = huiyin_x + 5 + i
            break
    for k in range(w):
        if binary[huiyin_y, m + k] == 0:
            n = m + k
            break
    x = round((m + n) / 2)
    return (x, y, str)


chengfu_x1, chengfu_y1, chengfu_str1 = chengfu1()


def xizhong1():
    str = ''
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


xizhong_x1, xizhong_y1, xizhong_z1, xizhong_n1, xizhong_m1 = xizhong1()


def weizhong1():
    str = "委中穴"
    x = xizhong_x1
    y = xizhong_y1
    return (x, y, str)


def weiyang1():
    str = "委阳穴"
    for i in range(w):
        if binary[xizhong_y1, xizhong_x1 + i] == 0:
            x = round((xizhong_x1 * 2 + i) / 2)
            break
    y = xizhong_y1
    return (x, y, str)


def fuxi1():
    str = "浮郄穴"
    x0, y0, z0 = weiyang1()
    x = x0
    y = y0 - cun_leg
    return (x, y, str)


fuxi_x1, fuxi_y1, fuxi_str1 = fuxi1()


def yinmen1():
    str = "殷门穴z"
    x = Symbol('x')
    y = Symbol('y')
    result = solve([(y - fuxi_y1) / (chengfu_y1 - fuxi_y1) - (x - fuxi_x1) / (chengfu_x1 - fuxi_x1),
                    (((chengfu_x1 - x) ** 2 + (chengfu_y1 - y) ** 2) ** 0.5) - (6 * cun_leg)], [x, y])
    x0 = int(result[1][0])
    y0 = int(result[1][1])
    return (x0, y0, str)


def heyang1():
    str = "合阳穴"
    x = xizhong_x1
    y = xizhong_y1 + cun_leg
    return (x, y, str)


def chengjin1():
    str = "承筋穴"
    for i in range(w):
        if binary[xizhong_y1, xizhong_x1 + i] == 0:
            m = xizhong_x1 + i
            break

    for i in range(w):
        if binary[xizhong_y1, xizhong_x1 - i] == 0:
            n = xizhong_x1 - i
            break
    x = int((m + n) / 2)
    y = xizhong_y1 + 5 * cun_leg
    return (x, y, str)


def chengshan1():
    str = "承山穴"
    for i in range(w):
        if binary[xizhong_y1, xizhong_x1 + i] == 0:
            m = xizhong_x1 + i
            break

    for i in range(w):
        if binary[xizhong_y1, xizhong_x1 - i] == 0:
            n = xizhong_x1 - i
            break
    x = int((m + n) / 2)
    y = xizhong_y1 + 9 * cun_leg
    return (x, y, str)
