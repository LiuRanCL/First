





import base64
import urllib.parse
import urllib.request
import json
import numpy as np
import cv2

'''
人像分割
'''


host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id="官网获取的AK"_secret="官网获取的SK"'
request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
token_new = json.loads(content)
refresh_token = token_new['access_token']



def contour(img_path):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_seg"
    
    f = open(img_path, 'rb')
    img = base64.b64encode(f.read())
    img1 = cv2.imread(img_path)
    height,width,a = img1.shape

    params = {"image":img}
    params = urllib.parse.urlencode(params).encode(encoding='UTF-8')

    access_token = refresh_token
    request_url = request_url + "?access_token=" + access_token
    request = urllib.request.Request(url=request_url, data=params)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib.request.urlopen(request)
    content = json.loads(response.read())
    if content:
        labelmap = base64.b64decode(content['labelmap'])  
        nparr = np.fromstring(labelmap, np.uint8)
        labelimg = cv2.imdecode(nparr, 1)
        
        labelimg = cv2.resize(labelimg, (width, height), interpolation=cv2.INTER_NEAREST)
        im_new = np.where(labelimg == 1, 255, labelimg)
        print("识别人体轮廓成功!")
        cv2.imwrite(img_path + '_binary' + '.jpg', im_new)
        return img_path + '_binary' + '.jpg'


def img_mainpart_detect(img_path):
    
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id="官网获取的AK"&client_secret="官网获取的SK"'
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read()
    token_new = json.loads(content)
    refresh_token = token_new['access_token']

    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/object_detect"
    
    f = open(img_path, 'rb')
    img = base64.b64encode(f.read())
    params = {"image": img, "with_face": 1}
    params = urllib.parse.urlencode(params).encode(encoding='UTF-8')
    access_token = refresh_token
    request_url = request_url + "?access_token=" + access_token
    request = urllib.request.Request(url=request_url, data=params)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib.request.urlopen(request)
    content1 = response.read()
    if content1:
        print("识别成功！")
        return content1


def skeleton_point(img_path):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_analysis"
    
    f = open(img_path, 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img}
    params = urllib.parse.urlencode(params).encode(encoding='UTF-8')

    access_token = refresh_token
    request_url = request_url + "?access_token=" + access_token
    request = urllib.request.Request(url=request_url, data=params)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib.request.urlopen(request)
    content = response.read()
    if content:
        return content




