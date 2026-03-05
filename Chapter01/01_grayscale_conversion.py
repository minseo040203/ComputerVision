import cv2                      # OpenCV 라이브러리 불러오기 (이미지 처리용)
import matplotlib.pyplot as plt # matplotlib 라이브러리 불러오기 (이미지 시각화용)

# 이미지 불러오기
img = cv2.imread('girl_laughing.jpg')  # 현재 폴더에 있는 girl_laughing.jpg 파일을 읽어와서 img 변수에 저장

# 컬러 이미지 확인 (BGR 형식)
if img is not None:                    # 이미지가 정상적으로 불러와졌는지 확인
    print("이미지 불러오기 성공")      # 이미지 로드 성공 메시지 출력
    print(f"이미지 크기: {img.shape}") # 이미지의 크기 출력 (높이, 너비, 채널 수)

    # 그레이스케일로 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 컬러 이미지를 흑백(그레이스케일) 이미지로 변환
    print(f"그레이스케일 이미지 크기: {gray.shape}") # 변환된 그레이스케일 이미지 크기 출력

    # 결과 이미지 저장
    cv2.imwrite('image_gray.jpg', gray)  # 변환된 그레이스케일 이미지를 image_gray.jpg 파일로 저장

    # 결과 시각화
    plt.figure(figsize=(12, 4))  # 그래프(이미지 표시 창) 크기를 가로12, 세로4로 설정

    # 원본 이미지 (BGR을 RGB로 변환해서 표시)
    plt.subplot(1, 2, 1)  # 1행 2열 중 첫 번째 위치에 이미지 표시
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # OpenCV의 BGR 형식을 matplotlib용 RGB로 변환 후 출력
    plt.title('원본 이미지 (컬러)')  # 이미지 제목 설정
    plt.axis('off')  # 축 눈금 제거 (이미지만 보이게)

    # 그레이스케일 이미지
    plt.subplot(1, 2, 2)  # 1행 2열 중 두 번째 위치에 이미지 표시
    plt.imshow(gray, cmap='gray')  # 그레이스케일 이미지를 gray 컬러맵으로 표시
    plt.title('그레이스케일 이미지')  # 이미지 제목 설정
    plt.axis('off')  # 축 눈금 제거

    plt.tight_layout()  # 그래프 간격 자동 조정
    plt.show()  # 화면에 이미지 출력

else:
    print("이미지를 불러올 수 없습니다. 파일 경로를 확인하세요.")  # 이미지 로드 실패 시 오류 메시지 출력