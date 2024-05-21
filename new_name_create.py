import os

# 변경할 폴더 경로 지정
folder_path = r"C:/Users/user/Desktop/Class 1-samples (3)"

# 폴더 안의 파일 리스트 얻기
file_list = os.listdir(folder_path)

# 새로운 파일 이름의 기본
new_name_base = "new_"

# 파일 이름 변경
for i, file_name in enumerate(file_list):
    # 확장자 추출
    file_extension = os.path.splitext(file_name)[1]
    
    # 새 파일 이름 생성
    new_name = f"{new_name_base}_{i+1}{file_extension}"
    
    # 원본 파일 경로
    src = os.path.join(folder_path, file_name)
    
    # 새 파일 경로
    dst = os.path.join(folder_path, new_name)
    
    # 파일 이름 변경
    os.rename(src, dst)
    print(f"{src} -> {dst}")

print("모든 파일 이름이 변경되었습니다.")
