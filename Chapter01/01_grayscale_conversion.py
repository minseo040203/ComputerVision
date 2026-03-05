import cv2
import matplotlib.pyplot as plt

# 이미지 불러오기
img = cv2.imread('girl_laughing.jpg')  # 이미지 파일 경로 입력

# 컬러 이미지 확인 (BGR 형식)
if img is not None:
    print("이미지 불러오기 성공")
    print(f"이미지 크기: {img.shape}")
    
    # 그레이스케일로 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(f"그레이스케일 이미지 크기: {gray.shape}")
    
    # 결과 이미지 저장
    cv2.imwrite('image_gray.jpg', gray)
    
    # 결과 시각화
    plt.figure(figsize=(12, 4))
    
    # 원본 이미지 (BGR을 RGB로 변환해서 표시)
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('원본 이미지 (컬러)')
    plt.axis('off')
    
    # 그레이스케일 이미지
    plt.subplot(1, 2, 2)
    plt.imshow(gray, cmap='gray')
    plt.title('그레이스케일 이미지')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
    
else:
    print("이미지를 불러올 수 없습니다. 파일 경로를 확인하세요.")
