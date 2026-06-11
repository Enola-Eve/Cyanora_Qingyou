# MoodFlow 硬件端
基于树莓派5的实时人脸情绪识别与音乐干预系统。

## 系统架构
[USB摄像头] → 人脸检测 (OpenCV) → 情绪识别 (DeepFace) → 音乐播放 (pygame)

# 硬件组成
| 组件 | 型号 | 用途 |
|------|------|------|
| 主控 | Raspberry Pi 5 | 边缘计算，完全离线 |
| 摄像头 | USB Camera | 实时人脸捕捉 |
| 音频 | 音箱/耳机 | 音乐播放 |

## 技术栈

- Python 3
- OpenCV Haar Cascade — 人脸检测
- DeepFace — 情绪分类，纯本地推理
- pygame.mixer — 音乐播放

## 工作流程

1. USB摄像头捕捉实时画面
2. OpenCV检测人脸区域
3. DeepFace进行情绪分类（愤怒、厌恶、恐惧、高兴、悲伤、惊讶、中性）
4. 播放匹配的原创钢琴曲

## 情绪-音乐映射

| 情绪 | 音乐特征 | 目标 |
|------|----------|------|
| 焦虑 | 缓慢琶音型，C大调，60BPM | 降低唤醒度 |
| 悲伤 | 上行旋律，E大调 | 情绪提振 |
| 愤怒 | 节奏型，降B大调 | 释放压力 |
| 恐惧 | 持续低音，D小调 | 建立安全感 |
| 高兴/中性/惊讶 | 轻爵士，自由速度 | 维持愉悦 |

所有音乐均为原创钢琴演奏。

## 快速开始

```bash
git clone [https://github.com/Enola-Eve/Cyanora_Qingyou]
cd moodflow-hardware
pip install -r requirements.txt
python main.py
```

首次运行自动下载DeepFace模型。

项目结构

```
├── main.py
├── emotion_detector.py
├── music_player.py
├── music/
│   ├── anxiety.mp3
│   ├── sadness.mp3
│   ├── anger.mp3
│   ├── fear.mp3
│   └── neutral.mp3
├── requirements.txt
└── README.md
```

设计原则

· 完全离线，数据不离开设备
· 不记录、不上传面部数据
· 不诊断、不评判，只有音乐

作者

[Yufei Zang] — A-Level学生，AI与心理学交叉方向。HOSA心理学竞赛全国站晋级。独立论文《Face Recognition Technology in the Field of Intelligent Psychological Analysis》。

许可证

MIT

```
```
