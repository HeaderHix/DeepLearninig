import cv2
import os

# 사진 저장 폴더 생성
save_dir = "captured_images_4"
os.makedirs(save_dir, exist_ok=True)

# 저장할 파일 번호 초기화
file_index = 0

# 웹캠 열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # 화면에 프레임 표시
    cv2.imshow("Webcam Feed", frame)

    # 키 입력 대기
    key = cv2.waitKey(1) & 0xFF

    # 's' 키가 눌린 경우
    if key == ord('s'):
        # 파일 이름 생성
        filename = os.path.join(save_dir, f"{file_index}.jpg")

        # 프레임 저장
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")

        # 파일 번호 증가
        file_index += 1

    # 'q' 키를 누르면 종료
    if key == ord('q'):
        break

# 웹캠 및 창 닫기
cap.release()
cv2.destroyAllWindows()
