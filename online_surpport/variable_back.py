




import cv2
import json
from local_contour import skeleton_point

imgpath = './sourceImg/back.jpg'
img = cv2.imread(imgpath)  
print("正在上传图片获取背面关键点...")

tempoint = skeleton_point(imgpath)
tempoints = json.loads(tempoint)
list = tempoints.get('person_info', 'unknown')
a = list[0]
body_parts = a.get('body_parts', 'unknown')
location = a.get('location', 'unknown')
left = int(location["left"])  
top = int(location["top"])  
width = int(location["width"])
height = int(location["height"])

right_wrist = body_parts["right_wrist"]  
head = body_parts["nose"]  
neck = body_parts["neck"]  
left_shoulder = body_parts["left_shoulder"]  
right_buttocks = body_parts["right_hip"]  
left_knee = body_parts["left_knee"]  
right_elbow = body_parts["right_elbow"]  
right_shoulder = body_parts["right_shoulder"]  
left_buttocks = body_parts["left_hip"]  
left_foot = body_parts["left_ankle"]  
left_elbow = body_parts["left_elbow"]  
left_hand = body_parts['left_wrist']  
right_knee = body_parts["right_knee"]  
right_foot = body_parts["right_ankle"]  



right_hand_x = round(right_wrist["x"])  
right_hand_y = round(right_wrist["y"])  

head_x = round(head["x"])  
head_y = round(head["y"])  

neck_x = round(neck["x"])  
neck_y = round(neck["y"])  

left_shoulder_x = round(left_shoulder["x"])  
left_shoulder_y = round(left_shoulder["y"])  

right_buttocks_x = round(right_buttocks["x"])  
right_buttocks_y = round(right_buttocks["y"])  

left_knee_x = round(left_knee['x'])  
left_knee_y = round(left_knee['y'])  

right_elbow_x = round(right_elbow["x"])  
right_elbow_y = round(right_elbow["y"])  

right_shoulder_x = round(right_shoulder["x"])  
right_shoulder_y = round(right_shoulder["y"])  

left_buttocks_x = round(left_buttocks['x'])  
left_buttocks_y = round(left_buttocks['y'])  

left_foot_x = round(left_foot['x'])  
left_foot_y = round(left_foot['y'])  

left_elbow_x = round(left_elbow["x"])  
left_elbow_y = round(left_elbow["y"])  

left_hand_x = round(left_hand["x"])  
left_hand_y = round(left_hand["y"])  

right_knee_x = round(right_knee["x"])  
right_knee_y = round(right_knee["y"])  

right_foot_x = round(right_foot["x"])  
right_foot_y = round(right_foot["y"])  
print("获取背面关键点成功!")

