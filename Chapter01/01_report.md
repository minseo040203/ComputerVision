# 과제 01: 이미지 불러오기 및 그레이스케일 변환

이 과제는 OpenCV 라이브러리를 사용하여 이미지를 불러오고, 그레이스케일(gray scale)로 변환하는 방법을 실습하는 것입니다. PDF에서 제공된 실습 문제를 바탕으로 다음과 같은 내용을 구현해야 합니다.

## 목표

1. 이미지 파일을 OpenCV로 읽어오기 (`cv2.imread`).
2. 불러온 컬러 이미지를 그레이스케일로 변환 (`cv2.cvtColor` + `cv2.COLOR_BGR2GRAY`).
3. 결과를 화면에 표시하고 (`matplotlib` 사용 가능), 변환된 이미지를 파일로 저장하기.
4. 이미지가 정상적으로 로드되지 않는 경우를 처리하는 예외 처리를 포함.

## 구현 내용

- 파일 경로는 상대경로가 아닌 절대경로나, 현재 스크립트 위치를 기준으로 동적으로 설정하도록 구성.
- 컬러 이미지는 OpenCV의 기본 형식인 BGR이므로 `matplotlib`로 표시할 때는 `cv2.COLOR_BGR2RGB`로 변환하여 보여줌.
- 변환된 그레이스케일 이미지는 동일한 디렉토리에 `image_gray.jpg`로 저장.
- 이미지 로드 여부, 크기 등의 정보를 콘솔에 출력.

## 코드
```bash
    import cv2                      # OpenCV 라이브러리 불러오기 (이미지 처리용)
    import matplotlib.pyplot as plt # matplotlib 라이브러리 불러오기 (이미지 시각화용)

    # 이미지 불러오기
    img = cv2.imread('girl_laughing.jpg')  # 현재 폴더에 있는     girl_laughing.jpg 파일을 읽어와서 img 변수에 저장

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
        print("이미지를 불러올 수 없습니다. 파일 경로를 확인하세요.")      # 이미지 로드 실패 시 오류 메시지 출력
```

## 주요코드
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
- cv2.cvtColor()는 이미지 색상 공간을 변환하는 함수이다.
- COLOR_BGR2GRAY 옵션을 사용하여 컬러 이미지를 흑백(그레이스케일)이미지로 변환한다.
- 변환된 이미지는 gray 변수에 저장된다
  
  ```bash
  plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
  ```
- OpenCV는 BGR 색상 순서를 사용한다
- matplotlib은 RGB 색상 순서를 사용한다.
- 따라서 cv2.cvtColor()를 사용하여 BGR을 RGB로 변환해야 정상적인 색상이 출력된다.

    ```bash
    plt.imshow(gray, cmap='gray')
    ```
- gray 이미지를 화면에 출력한다.
- cmap='gray' 옵션을 사용하여 흑백 컬러맵으로 표시한다.

## 실행 방법

1. `c:\ComputerVision\Chapter01` 디렉토리로 이동
2. 필요한 라이브러리 설치:
   ```bash
   pip install opencv-python matplotlib
   ```
3. 아래 명령으로 스크립트 실행:
   ```bash
   python 01_grayscale_conversion.py
   ```
4. 실행 후 `image_gray.jpg` 파일이 생성되는지 확인.

## 결과
![alt text](image.png)![alt text](image-1.png)
