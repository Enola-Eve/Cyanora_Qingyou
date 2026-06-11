# Cyanora_Qingyou
Real-time facial emotion recognition and music interaction system on Raspberry Pi 5.

# System Architecture
USB Camera → Face Detection (OpenCV) → Emotion Recognition (DeepFace) → Music (pygame)

# Hardware
Main Controller | Raspberry Pi 5 | Edge computing, offline
Camera | USB Camera | Face capture
Audio | Speaker / Headphones | Music playback

# Tech Stack
- Python 3.11
- OpenCV Haar Cascade
- DeepFace
- pygame.mixer
- Flask — local API for companion app

# Workflow
1. Camera captures video frames
2. OpenCV detects face region
3. DeepFace classifies emotion (angry, disgust, fear, happy, sad, surprise, neutral)
4. Matching original piano piece plays

# Emotion–Music Mapping
| Emotion | Music | Goal |
| Anxiety | Slow arpeggios, C major, 60 BPM | Reduce arousal |
| Sadness |     Ascending melody, E major   |   Lift mood    |
| Anger   |  Rhythmic pattern, B-flat major | Release tension |
| Fear    |  Sustained low notes, D minor   |   Build safety |
| Happy / Neutral / Surprise | Light jazz, free tempo | Maintain well-being |

All music is original piano performance.
