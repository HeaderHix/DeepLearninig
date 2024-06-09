import qrcode

# QR 코드에 넣을 데이터 목록
data_list = ["a4box", "polybag"]

# 데이터에 따라 QR 코드를 생성하고 저장하는 함수
def create_and_save_qr(data, filename):
    qr = qrcode.QRCode(
        version=1,  # QR 코드 버전 (1 ~ 40), 버전이 높을수록 복잡한 QR 코드 생성 가능
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # 오류 수정 수준
        box_size=10,  # QR 코드 상자의 크기
        border=4,  # QR 코드 경계의 두께
    )
    
    
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# 각 데이터에 대해 QR 코드 생성 및 저장
create_and_save_qr("a4box", "qr_code_a4box.png")
create_and_save_qr("polybag", "qr_code_polybag.png")

print("QR 코드 이미지가 'qr_code_a4box.png'와 'qr_code_polybag.png' 파일로 저장되었습니다.")
