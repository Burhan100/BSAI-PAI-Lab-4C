from flask import Flask, render_template, Response, jsonify
import cv2
import dlib
import numpy as np
from scipy.spatial import distance
import threading
import time

app = Flask(__name__)

# ─── EAR Calculation ───────────────────────────────────────────────────────────
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

# ─── Constants ─────────────────────────────────────────────────────────────────
EAR_THRESHOLD   = 0.25   # below this = eyes closed
CONSEC_FRAMES   = 20     # frames eyes must be closed to trigger alert

# ─── Globals ───────────────────────────────────────────────────────────────────
frame_counter   = 0
drowsy          = False
status_text     = "Monitoring..."
ear_value       = 0.0
lock            = threading.Lock()

# ─── Load dlib models ──────────────────────────────────────────────────────────
detector  = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Landmark indices for eyes
(lStart, lEnd) = (42, 48)
(rStart, rEnd) = (36, 42)

# ─── Video Stream Generator ────────────────────────────────────────────────────
def generate_frames():
    global frame_counter, drowsy, status_text, ear_value

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        success, frame = cap.read()
        if not success:
            break

        gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray, 0)

        with lock:
            if len(faces) == 0:
                status_text = "No face detected"
                drowsy      = False
                ear_value   = 0.0
            else:
                for face in faces:
                    shape     = predictor(gray, face)
                    shape_np  = np.array([[p.x, p.y] for p in shape.parts()])

                    leftEye   = shape_np[lStart:lEnd]
                    rightEye  = shape_np[rStart:rEnd]

                    leftEAR   = eye_aspect_ratio(leftEye)
                    rightEAR  = eye_aspect_ratio(rightEye)
                    ear        = (leftEAR + rightEAR) / 2.0
                    ear_value  = round(ear, 3)

                    # Draw eye contours
                    for eye_pts in [leftEye, rightEye]:
                        hull = cv2.convexHull(eye_pts)
                        cv2.drawContours(frame, [hull], -1, (0, 255, 0), 1)

                    if ear < EAR_THRESHOLD:
                        frame_counter += 1
                        if frame_counter >= CONSEC_FRAMES:
                            drowsy      = True
                            status_text = "DROWSY! WAKE UP!"
                            cv2.putText(frame, "DROWSY ALERT!", (10, 30),
                                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
                    else:
                        frame_counter = 0
                        drowsy        = False
                        status_text   = "Alert & Awake"

                    # EAR text on frame
                    cv2.putText(frame, f"EAR: {ear_value}", (10, 60),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' +
               buffer.tobytes() + b'\r\n')

    cap.release()

# ─── Routes ────────────────────────────────────────────────────────────────────
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/status')
def status():
    with lock:
        return jsonify({
            'drowsy':  drowsy,
            'status':  status_text,
            'ear':     ear_value,
            'frames':  frame_counter
        })

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
