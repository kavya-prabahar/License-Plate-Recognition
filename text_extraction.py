import cv2
import easyocr
from ultralytics import YOLO

model = YOLO ("runs/detect/train/weights/best.pt")

reader = easyocr.Reader(['en'])

def extract_text(image):
    results = model.predict(source = image, save = False, imgsz = 640)
    detected_text = ""

    for box in results[0].boxes.xyxy:
        x1, y1, x2, y2 = map(int, box[:4])
        cropped_plate = image[y1:y2, x1:x2]

        ocr_results = reader.readtext(cropped_plate)

        for (bbox, text, confidence) in ocr_results:
            detected_text += text + " "
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return image, detected_text.strip()