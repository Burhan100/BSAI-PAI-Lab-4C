# 🚗 Driver Drowsiness Detector
**4th Semester AI Project | OpenCV + Flask**

---

## Project Overview
Real-time driver drowsiness detection using webcam.
Monitors Eye Aspect Ratio (EAR) — if eyes stay closed too long, an alarm triggers.

---

## Tech Stack
| Tool | Purpose |
|------|---------|
| Flask | Web server & routing |
| OpenCV | Webcam capture & frame processing |
| dlib | 68-point face landmark detection |
| SciPy | Euclidean distance for EAR calculation |
| HTML/CSS/JS | Frontend dashboard |

---

## File Structure
```
drowsiness_detector/
│
├── app.py                        ← Main Flask app
├── requirements.txt              ← Python dependencies
├── shape_predictor_68_face_landmarks.dat  ← dlib model (download separately)
│
├── templates/
│   └── index.html                ← Web UI
│
└── static/
    ├── css/
    │   └── style.css             ← Styling
    ├── js/
    │   └── main.js               ← Status polling & alerts
    └── sounds/
        └── alarm.mp3             ← Alert sound (add your own)
```

---

## Setup Instructions

### Step 1 — Install dependencies
```bash
pip install flask opencv-python dlib numpy scipy
```

> Note: dlib installation needs CMake. If error aaye:
> ```bash
> pip install cmake
> pip install dlib
> ```

### Step 2 — Download dlib landmark model
Download from: https://github.com/italojs/facial-landmarks-recognition/raw/master/shape_predictor_68_face_landmarks.dat

Place it in the root folder (same level as app.py).

### Step 3 — Add alarm sound
Add any `.mp3` file to `static/sounds/` and name it `alarm.mp3`
(Free sounds: https://freesound.org)

### Step 4 — Run the app
```bash
python app.py
```

Open browser: http://127.0.0.1:5000

---

## How It Works (Algorithm)

```
1. Capture webcam frame
2. Convert to grayscale
3. dlib detects face → 68 landmark points
4. Extract 6 points around each eye
5. Calculate EAR = (A + B) / (2 * C)
   where A, B = vertical distances
         C    = horizontal distance
6. If EAR < 0.25 → eyes closed
7. If closed for 20+ frames → DROWSY ALERT!
```

---

## EAR Formula
```
     |p2-p6| + |p3-p5|
EAR = ─────────────────
          2 * |p1-p4|
```
- Open eyes → EAR ≈ 0.30+
- Closed eyes → EAR ≈ 0.20 or below

---

## Made by
Burhan — Lahore Garrison University
Programming for Artificial Intelligence | 4th Semester
