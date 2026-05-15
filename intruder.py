#PYTHON CODE

import cv2, face_recognition, os, serial, time

ser = serial.Serial('COM9',115200); time.sleep(2)
os.makedirs("intruders", exist_ok=True)

# Load known faces
enc, names = [], []
for f in os.listdir("known_faces"):
    e = face_recognition.face_encodings(face_recognition.load_image_file(f"known_faces/{f}"))
    if e: enc.append(e[0]); names.append(os.path.splitext(f)[0])

print("✅ Loaded:", names)

cap, last = cv2.VideoCapture(0), 0

while True:
    _, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    intruder = False
    for (t,r,b,l), e in zip(*[face_recognition.face_locations(rgb), face_recognition.face_encodings(rgb)]):
        d = face_recognition.face_distance(enc, e)
        name = names[d.argmin()] if len(d)>0 and min(d)<0.5 else "Unknown"
        intruder |= (name=="Unknown")

        cv2.rectangle(frame,(l,t),(r,b),(0,0,255),2)
        cv2.putText(frame,name,(l,t-10),0,0.8,(0,255,0),2)

    if intruder and time.time()-last>5:
        print("🚨 INTRUDER DETECTED")
        cv2.imwrite(f"intruders/intruder_{int(time.time())}.jpg", frame)
        ser.write(b'ALERT\n'); last=time.time()

    cv2.imshow("Intruder Detection", frame)
    if cv2.waitKey(1)==27: break

cap.release(); ser.close(); cv2.destroyAllWindows()