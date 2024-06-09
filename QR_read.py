import cv2
import serial
from pyzbar.pyzbar import decode

def read_qr_code_from_frame(frame):
    decoded_objects = decode(frame)
    for obj in decoded_objects:
        return obj.data.decode('utf-8')
    return None

def send_data_to_serial(serial_port, baudrate, data):
    ser = serial.Serial(serial_port, baudrate, timeout=1)
    try:
        ser.write(data.encode('utf-8'))
        print(f"Sent data: {data}")
    finally:
        ser.close()

def main(serial_port, baudrate):
    cap = cv2.VideoCapture(0)  # 0은 기본 웹캠을 의미
    if not cap.isOpened():
        print("Error: Could not open video capture")
        return
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame")
                break

            qr_data = read_qr_code_from_frame(frame)
            if qr_data:
                print(f"Read data from QR code: {qr_data}")
                send_data_to_serial(serial_port, baudrate, qr_data)

            cv2.imshow('QR Code Scanner', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

# 시리얼 포트와 보드레이트 설정
serial_port = 'COM3'  # 사용하는 시리얼 포트에 맞게 수정
baudrate = 9600

# 웹캠에서 QR 코드를 읽고 시리얼 포트로 데이터를 전송
main(serial_port, baudrate)
