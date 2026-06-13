# coding=utf-8
# 实时摄像头表情识别
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import cv2
from tensorflow.keras.models import load_model
import numpy as np
import chineseText

# 加载模型
print("正在加载模型...")
emotion_classifier = load_model('classifier/emotion_models/simple_CNN.530-0.65.hdf5')
print("模型加载成功！")

emotion_labels = {
    0: '生气', 1: '厌恶', 2: '恐惧',
    3: '开心', 4: '难过', 5: '惊喜', 6: '平静'
}

# 加载人脸检测器
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 打开摄像头 (0代表默认摄像头)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("错误：无法打开摄像头！请检查权限或是否被其他软件占用。")
else:
    print("摄像头已启动，按 q 键退出...")
    while True:
        ret, frame = cap.read()  # 读取一帧画面
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(40, 40))

        color = (255, 255, 0)  # 字体颜色 BGR格式(蓝色)

        for (x, y, w, h) in faces:
            # 截取人脸区域并预处理
            gray_face = gray[y:y + h, x:x + w]
            try:
                gray_face = cv2.resize(gray_face, (48, 48))
            except:
                continue
            gray_face = gray_face / 255.0
            gray_face = np.expand_dims(gray_face, 0)
            gray_face = np.expand_dims(gray_face, -1)

            # 预测表情
            emotion_label_arg = np.argmax(emotion_classifier.predict(gray_face))
            emotion = emotion_labels[emotion_label_arg]

            # 画框和写中文
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            frame = chineseText.cv2ImgAddText(frame, emotion, x, y - 20, color, 30)

        cv2.imshow("Real-time Emotion Detection", frame)

        # 按 'q' 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()  # 【注意】关闭窗口资源的代码应该放在这里