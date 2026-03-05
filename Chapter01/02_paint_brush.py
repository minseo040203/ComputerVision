import cv2
import numpy as np
import os

# 전역 변수
drawing = False
brush_size = 5
brush_color = (0, 0, 255)  # BGR 형식 (빨강)
img = None
img_copy = None

def mouse_event(event, x, y, flags, param):
    """마우스 이벤트 처리 함수"""
    global drawing, img, img_copy, brush_size, brush_color
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            # 현재 위치에 원형 브러시로 그리기
            cv2.circle(img, (x, y), brush_size, brush_color, -1)
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

def main():
    global img, img_copy, brush_size, brush_color
    
    # 현재 파일의 디렉토리 경로 가져오기
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, 'girl_laughing.jpg')
    
    # 이미지 불러오기
    img = cv2.imread(image_path)
    
    if img is None:
        print("이미지를 불러올 수 없습니다.")
        return
    
    # 이미지 크기 조정 (너무 크면 조정)
    if img.shape[0] > 600 or img.shape[1] > 800:
        scale = min(600 / img.shape[0], 800 / img.shape[1])
        img = cv2.resize(img, (int(img.shape[1] * scale), int(img.shape[0] * scale)))
    
    img_copy = img.copy()
    
    # 윈도우 생성 및 마우스 콜백 설정
    window_name = 'Paint Brush - 붓 크기 조절'
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, mouse_event)
    
    print("=" * 50)
    print("페인트 붓 프로그램")
    print("=" * 50)
    print("조작 방법:")
    print("  - 마우스 드래그: 그리기")
    print("  - 'w' 키: 붓 크기 증가")
    print("  - 's' 키: 붓 크기 감소")
    print("  - 'r' 키: 리셋 (원본으로 돌아가기)")
    print("  - 'c' 키: 색상 변경 (빨강 ↔ 초록 ↔ 파랑)")
    print("  - 'ESC' 키: 종료")
    print("=" * 50)
    print(f"현재 붓 크기: {brush_size}")
    
    while True:
        cv2.imshow(window_name, img)
        
        # 상태 정보 출력
        info_text = f"Brush Size: {brush_size}"
        print(f"\r{info_text}", end="")
        
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('w'):  # 붓 크기 증가
            brush_size = min(brush_size + 1, 50)
            print(f"\n붓 크기 증가: {brush_size}")
        
        elif key == ord('s'):  # 붓 크기 감소
            brush_size = max(brush_size - 1, 1)
            print(f"\n붓 크기 감소: {brush_size}")
        
        elif key == ord('r'):  # 리셋
            img = img_copy.copy()
            print("\n이미지 리셋!")
        
        elif key == ord('c'):  # 색상 변경
            colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]  # 빨강, 초록, 파랑
            color_names = ["빨강", "초록", "파랑"]
            idx = colors.index(brush_color)
            brush_color = colors[(idx + 1) % 3]
            color_name = color_names[(idx + 1) % 3]
            print(f"\n색상 변경: {color_name}")
        
        elif key == 27:  # ESC 키로 종료
            print("\n프로그램 종료!")
            break
    
    # 결과 이미지 저장
    result_path = os.path.join(current_dir, 'painting_result.jpg')
    cv2.imwrite(result_path, img)
    print(f"결과 이미지가 '{result_path}'로 저장되었습니다.")
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
