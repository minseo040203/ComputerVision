import cv2                 # OpenCV 라이브러리 (이미지 처리, GUI 창, 마우스 이벤트 등)
import numpy as np         # 배열 연산을 위한 NumPy 라이브러리
import os                  # 파일 경로 및 운영체제 관련 기능 사용

# ---------------------------
# 전역 변수 설정
# ---------------------------

drawing = False            # 현재 그림을 그리고 있는지 여부 (마우스 클릭 상태)
brush_size = 5             # 붓 크기 기본값
brush_color = (0, 0, 255)  # 붓 색상 (BGR 형식) → 빨강색
img = None                 # 현재 작업 중인 이미지
img_copy = None            # 원본 이미지 복사본 (리셋 기능용)

# ---------------------------
# 마우스 이벤트 처리 함수
# ---------------------------

def mouse_event(event, x, y, flags, param):
    """마우스 이벤트 처리 함수"""
    
    global drawing, img, img_copy, brush_size, brush_color  # 전역 변수 사용
    
    # 마우스 왼쪽 버튼 눌렀을 때
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True   # 그림 그리기 시작
    
    # 마우스 이동
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:      # 마우스를 누른 상태라면
            # 현재 마우스 위치(x, y)에 원형 브러시로 그림 그리기
            cv2.circle(img, (x, y), brush_size, brush_color, -1)
            # -1 → 원을 채우기(fill)
    
    # 마우스 왼쪽 버튼을 뗐을 때
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False  # 그림 그리기 종료

# ---------------------------
# 메인 함수
# ---------------------------

def main():
    
    global img, img_copy, brush_size, brush_color
    
    # 현재 실행 중인 파일의 폴더 경로 가져오기
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 이미지 파일 경로 생성
    image_path = os.path.join(current_dir, 'girl_laughing.jpg')
    
    # 이미지 불러오기
    img = cv2.imread(image_path)
    
    # 이미지 로드 실패 시
    if img is None:
        print("이미지를 불러올 수 없습니다.")
        return
    
    # ---------------------------------
    # 이미지 크기 조정 (너무 큰 경우)
    # ---------------------------------
    
    # 이미지 높이가 600보다 크거나 너비가 800보다 크면
    if img.shape[0] > 600 or img.shape[1] > 800:
        
        # 비율 유지하면서 크기 줄이기
        scale = min(600 / img.shape[0], 800 / img.shape[1])
        
        # 이미지 리사이즈
        img = cv2.resize(
            img,
            (int(img.shape[1] * scale), int(img.shape[0] * scale))
        )
    
    # 원본 이미지 복사 (리셋 기능용)
    img_copy = img.copy()
    
    # ---------------------------
    # OpenCV 윈도우 생성
    # ---------------------------
    
    window_name = 'Paint Brush - 붓 크기 조절'
    
    cv2.namedWindow(window_name)                 # 창 생성
    cv2.setMouseCallback(window_name, mouse_event)  # 마우스 이벤트 연결
    
    # ---------------------------
    # 프로그램 사용 설명 출력
    # ---------------------------
    
    print("=" * 50)
    print("페인트 붓 프로그램")
    print("=" * 50)
    print("조작 방법:")
    print("  - 마우스 드래그: 그리기")          # 마우스 드래그하면 그림 그리기
    print("  - 'w' 키: 붓 크기 증가")           # w → 붓 크기 커짐
    print("  - 's' 키: 붓 크기 감소")           # s → 붓 크기 작아짐
    print("  - 'r' 키: 리셋 (원본으로 돌아가기)") # r → 원본 이미지 복구
    print("  - 'c' 키: 색상 변경 (빨강 ↔ 초록 ↔ 파랑)") # c → 색상 변경
    print("  - 'ESC' 키: 종료")                # ESC → 프로그램 종료
    print("=" * 50)
    
    print(f"현재 붓 크기: {brush_size}")
    
    # ---------------------------
    # 메인 반복 루프
    # ---------------------------
    
    while True:
        
        # 현재 이미지 화면에 표시
        cv2.imshow(window_name, img)
        
        # 현재 붓 크기 정보 출력
        info_text = f"Brush Size: {brush_size}"
        print(f"\r{info_text}", end="")
        
        # 키 입력 대기 (1ms)
        key = cv2.waitKey(1) & 0xFF
        
        # ---------------------------
        # 키보드 입력 처리
        # ---------------------------
        
        # w 키 → 붓 크기 증가
        if key == ord('w'):
            brush_size = min(brush_size + 1, 50)  # 최대 50 제한
            print(f"\n붓 크기 증가: {brush_size}")
        
        # s 키 → 붓 크기 감소
        elif key == ord('s'):
            brush_size = max(brush_size - 1, 1)   # 최소 1 제한
            print(f"\n붓 크기 감소: {brush_size}")
        
        # r 키 → 이미지 리셋
        elif key == ord('r'):
            img = img_copy.copy()                 # 원본 이미지 복사
            print("\n이미지 리셋!")
        
        # c 키 → 색상 변경
        elif key == ord('c'):
            
            # 사용할 색상 목록 (BGR)
            colors = [
                (0, 0, 255),   # 빨강
                (0, 255, 0),   # 초록
                (255, 0, 0)    # 파랑
            ]
            
            color_names = ["빨강", "초록", "파랑"]
            
            # 현재 색상의 인덱스 찾기
            idx = colors.index(brush_color)
            
            # 다음 색상으로 변경
            brush_color = colors[(idx + 1) % 3]
            
            color_name = color_names[(idx + 1) % 3]
            
            print(f"\n색상 변경: {color_name}")
        
        # ESC 키 → 프로그램 종료
        elif key == 27:
            print("\n프로그램 종료!")
            break
    
    # ---------------------------
    # 결과 이미지 저장
    # ---------------------------
    
    result_path = os.path.join(current_dir, 'painting_result.jpg')
    
    cv2.imwrite(result_path, img)  # 최종 이미지 저장
    
    print(f"결과 이미지가 '{result_path}'로 저장되었습니다.")
    
    # 모든 OpenCV 창 닫기
    cv2.destroyAllWindows()


# ---------------------------
# 프로그램 시작 지점
# ---------------------------

if __name__ == "__main__":
    main()   # main 함수 실행