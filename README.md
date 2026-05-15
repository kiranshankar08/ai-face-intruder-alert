## Intruder Detection System (AI + IoT)

An AI-powered real-time intruder detection system using Python (OpenCV + face_recognition) integrated with Arduino hardware alerts via serial communication.
When an unknown person is detected, the system:
Captures and saves the intruder image
Sends an alert signal to Arduino
Triggers a blinking LED alarm system

# Features
1. Real-time face detection using webcam
2. Face recognition using face_recognition library
3. Intruder detection (unknown face classification)
4. Automatic intruder image capture and storage
5. Arduino serial communication alert system
6. LED blinking alarm on detection
7. Cooldown system to avoid repeated alerts

# Tech Stack
Python
OpenCV
face_recognition
PySerial
Arduino (C++)

# Project Structure
intruder-detection/
│
├── intruder.py              # Main Python detection script
├── intruder.ino         # Arduino LED alert code
│
├── known_faces/             # Authorized face images. Capture and keep one using webcam.
├── intruders/               # Saved intruder snapshots
│
└── README.md

# Installation
1. Clone the repository
git clone https://github.com/your-username/intruder-detection.git
cd intruder-detection

3. Install Python dependencies
pip install opencv-python face-recognition pyserial

# How to Run
Step 1: Upload Arduino code
Open intruder.ino

Upload to ESP32 board using Arduino IDE
Step 2: Connect ESP32

Connect ESP via USB
Update port in Python code:
ser = serial.Serial('COM9', 115200) #Port visible while connecting ESP to your system (Available in Boards section of IDE. 115200 is the baud rate.

Step 3: Run Python script
python intruder.py

# Working Flow
Webcam captures live video
Faces are detected and compared with known dataset
If unknown face is detected:
Image is saved in /intruders
ALERT signal sent to Arduino
Arduino blinks LED as warning

# Hardware Requirements
Arduino UNO / ESP32
LED
Resistor (220Ω recommended)
USB cable
PC with webcam

# Arduino Logic
Listens for serial command "ALERT"
Blinks LED 6 times when triggered

# Future Improvements
1. WhatsApp / Telegram alerts
2. Cloud storage for intruder images
3. Buzzer + siren integration
4. IoT dashboard monitoring
5. Multi-face access control system

   
# Author
Kiran Shankar A P - https://github.com/kiranshankar08


If you like this project:
Give it a ⭐ on GitHub and feel free to contribute improvements!
