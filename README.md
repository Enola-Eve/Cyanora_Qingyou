
# MoodFlow Hardware
Real-time facial emotion recognition and music interaction system on Raspberry Pi 5.
The system captures facial expressions via camera, identifies the user's emotional state, and plays matching original piano pieces for emotional soothing.
## System Architecture

```

[USB Camera] → Face Detection (OpenCV) → Emotion Recognition (DeepFace) → Music (pygame)

```

## Hardware

| Component | Model | Purpose |
|-----------|-------|---------|
| Main Controller | Raspberry Pi 5 | Edge computing, offline |
| Camera | USB Camera | Face capture |
| Audio | Speaker / Headphones | Music playback |

## Tech Stack

- Python 3.11
- OpenCV Haar Cascade — face detection
- DeepFace — emotion classification (local inference)
- pygame.mixer — music playback
- Flask — local API for companion app

## Workflow

1. Camera captures video frames
2. OpenCV detects face region
3. DeepFace classifies emotion (angry, disgust, fear, happy, sad, surprise, neutral)
4. Matching original piano piece plays

## Emotion–Music Mapping

| Emotion | Music | Goal |
|---------|-------|------|
| Anxiety | Slow arpeggios, C major, 60 BPM | Reduce arousal |
| Sadness | Ascending melody, E major | Lift mood |
| Anger | Rhythmic pattern, B-flat major | Release tension |
| Fear | Sustained low notes, D minor | Build safety |
| Happy / Neutral / Surprise | Light jazz, free tempo | Maintain well-being |

All music is original piano performance.

## Getting Started

```bash
git clone [https://github.com/Enola-Eve/Cyanora_Qingyou]
cd moodflow-hardware
pip install -r requirements.txt
python main.py
```

First run downloads DeepFace models automatically.

Local API

Flask server runs on port 5000:

```
http://<raspberry-pi-ip>:5000/api/emotion
```

Project Structure

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

Principles

· Fully offline, no data leaves the device
· No facial data recorded or uploaded
· No diagnosis, no judgment

Author

[Yufei Zang] — A-Level student, AI & psychology. HOSA Psychology National Finalist. Author of Face Recognition Technology in the Field of Intelligent Psychological Analysis.

License

MIT

```
```

