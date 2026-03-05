import cv2
import os

# 전역 변수
x_start, y_start = 0, 0
x_end, y_end = 0, 0
drawing = False
img = None
img_copy = None
roi = None

def mouse_event(event, x, y, flags, param):
    """마우스 이벤트 처리 함수 - ROI 선택"""
    global x_start, y_start, x_end, y_end, drawing, img, img_copy, roi
    
    if event == cv2.EVENT_LBUTTONDOWN:
        # 마우스 왼쪽 버튼 누름
        drawing = True
        x_start, y_start = x, y
        img = img_copy.copy()
    
    elif event == cv2.EVENT_MOUSEMOVE:
        # 마우스 이동 중
        if drawing:
            img = img_copy.copy()
            # 현재 좌표까지 사각형 그리기
            cv2.rectangle(img, (x_start, y_start), (x, y), (0, 255, 0), 2)
    
    elif event == cv2.EVENT_LBUTTONUP:
        # 마우스 왼쪽 버튼 뗌
        drawing = False
        x_end, y_end = x, y
        
        # 좌표 정렬 (시작점이 끝점보다 작도록)
        x1 = min(x_start, x_end)
        y1 = min(y_start, y_end)
        x2 = max(x_start, x_end)
        y2 = max(y_start, y_end)
        
        # ROI 추출
        roi = img_copy[y1:y2, x1:x2].copy()
        
        # 최종 선택 영역 그리기
        img = img_copy.copy()
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
        
        print(f"ROI 선택 완료!")
        print(f"좌표: ({x1}, {y1}) ~ ({x2}, {y2})")
        print(f"크기: {x2-x1} x {y2-y1}")

def main():
    global img, img_copy, roi
    
    # 현재 파일의 디렉토리 경로 가져오기
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 사용 가능한 이미지 찾기
    image_names = ['girl_laughing.jpg', 'soccer.jpg', 'image_gray.jpg']
    img_path = None
    
    for img_name in image_names:
        potential_path = os.path.join(current_dir, img_name)
        if os.path.exists(potential_path):
            img_path = potential_path
            break
    
    if img_path is None:
        print("사용 가능한 이미지가 없습니다.")
        print(f"다음 파일 중 하나를 {current_dir}에 저장하세요:")
        for name in image_names:
            print(f"  - {name}")
        return
    
    # 이미지 불러오기
    img = cv2.imread(img_path)
    
    if img is None:
        print("이미지를 불러올 수 없습니다.")
        return
    
    # 이미지 크기 조정 (너무 크면 조정)
    if img.shape[0] > 600 or img.shape[1] > 800:
        scale = min(600 / img.shape[0], 800 / img.shape[1])
        img = cv2.resize(img, (int(img.shape[1] * scale), int(img.shape[0] * scale)))
    
    img_copy = img.copy()
    
    # 윈도우 생성 및 마우스 콜백 설정
    window_name = 'ROI Extraction - 마우스로 영역 선택'
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, mouse_event)
    
    print("=" * 60)
    print("ROI(Region of Interest) 추출 프로그램")
    print("=" * 60)
    print("조작 방법:")
    print("  - 마우스 드래그: ROI 영역 선택")
    print("  - 's' 키: 선택된 ROI 저장")
    print("  - 'r' 키: 선택 취소 (원본 이미지로 리셋)")
    print("  - 'ESC' 키: 종료")
    print("=" * 60)
    
    roi_count = 0
    
    while True:
        cv2.imshow(window_name, img)
        
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('s'):  # ROI 저장
            if roi is not None and roi.size > 0:
                roi_count += 1
                roi_path = os.path.join(current_dir, f'roi_{roi_count}.jpg')
                cv2.imwrite(roi_path, roi)
                print(f"\n✓ ROI가 '{roi_path}'로 저장되었습니다.")
                print(f"  크기: {roi.shape[1]} x {roi.shape[0]} (너비 x 높이)")
            else:
                print("\n선택된 ROI가 없습니다. 먼저 마우스로 영역을 선택하세요.")
        
        elif key == ord('r'):  # 리셋
            img = img_copy.copy()
            roi = None
            print("\n영역 선택이 취소되었습니다.")
        
        elif key == 27:  # ESC 키로 종료
            print("\n프로그램을 종료합니다.")
            break
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
