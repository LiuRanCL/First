import cv2 as cv
from PIL import Image
from PATH_DEFINE import BackPath

dataset = 'MPI'
if dataset == 'COCO':
    BODY_PARTS = {"Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
                  "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
                  "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
                  "LEye": 15, "REar": 16, "LEar": 17, "Background": 18}

    POSE_PAIRS = [["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
                  ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
                  ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
                  ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"],
                  ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"]]
else:
    assert (dataset == 'MPI')
    BODY_PARTS = {"Head": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
                  "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
                  "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "Chest": 14,
                  "Background": 15}

    POSE_PAIRS = [["Head", "Neck"], ["Neck", "RShoulder"], ["RShoulder", "RElbow"],
                  ["RElbow", "RWrist"], ["Neck", "LShoulder"], ["LShoulder", "LElbow"],
                  ["LElbow", "LWrist"], ["Neck", "Chest"], ["Chest", "RHip"], ["RHip", "RKnee"],
                  ["RKnee", "RAnkle"], ["Chest", "LHip"], ["LHip", "LKnee"], ["LKnee", "LAnkle"]]

inWidth = 368
inHeight = 368
thr = 0.1
protoc = './openpose_pose_coco.prototxt'
model = './pose_iter_440000.caffemodel'
net = cv.dnn.readNetFromCaffe(protoc, model)

frame = cv.imread(BackPath)

frameWidth = frame.shape[1]
frameHeight = frame.shape[0]
inp = cv.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight), (0, 0, 0), swapRB=False, crop=False)
net.setInput(inp)
out = net.forward()


def get_key(dict, value):
    return [k for k, v in dict.items() if v == value]


points = []
for i in range(len(BODY_PARTS)):
    heatMap = out[0, i, :, :]

    _, conf, _, point = cv.minMaxLoc(heatMap)
    x = (frameWidth * point[0]) / out.shape[3]
    y = (frameHeight * point[1]) / out.shape[2]

    points.append((get_key(BODY_PARTS, i)[0], x, y) if conf > thr else None)
    cv.putText(frame, str(i), (int(x), int(y)), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1)
    cv.circle(frame, (int(x), int(y)), 4, (255, 255, 255), 4)

img_PIL = Image.fromarray(cv.cvtColor(frame, cv.COLOR_BGR2RGB))
img_PIL.show()

neck_x = round(points[1][1])
neck_y = round(points[1][2])

left_shoulder_x = round(points[5][1])
left_shoulder_y = round(points[5][2])

right_buttocks_x = round(points[8][1])
right_buttocks_y = round(points[8][2])

left_knee_x = round(points[12][1])
left_knee_y = round(points[12][2])

right_elbow_x = round(points[3][1])
right_elbow_y = round(points[3][2])

right_shoulder_x = round(points[2][1])
right_shoulder_y = round(points[2][2])

left_buttocks_x = round(points[11][1])
left_buttocks_y = round(points[11][2])

left_foot_x = round(points[13][1])
left_foot_y = round(points[13][2])

left_elbow_x = round(points[6][1])
left_elbow_y = round(points[6][2])

left_hand_x = round(points[7][1])
left_hand_y = round(points[7][2])

right_hand_x = round(points[4][1])
right_hand_y = round(points[4][2])

right_knee_x = round(points[9][1])
right_knee_y = round(points[9][2])

right_foot_x = round(points[10][1])
right_foot_y = round(points[10][2])
