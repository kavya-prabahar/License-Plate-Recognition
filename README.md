# License-Plate-Detection-and-Recogniiton-System

This project uses YOLOv8 for detecting license plates and EasyOCR for optical character recognition (OCR) to recognize the text on the detected plates. The system takes an image as input, detects the license plate, and extracts the text. The project can be integrated into a Streamlit web app for easy use.

## Features
- License Plate Detection using YOLOv8
- Text Recognition from License Plates using EasyOCR
- Image preprocessing and bounding box annotation
- Real-time detection and recognition on images

## Requirements

1. Python 3.x
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
   
## Setup Instructions

- **Clone this repository:**
```
git clone https://github.com/yourusername/license-plate-detection.git
cd license-plate-detection
```

- **Install required dependencies:**

```
pip install -r requirements.txt
```

- **Run the Streamlit app:**

```
streamlit run app.py
```

- **Upload an image to detect and recognize the license plate.**

## How It Works

- The YOLOv8 model is used to detect the license plate from the uploaded image.
- Once the license plate is detected, the image region containing the plate is passed to EasyOCR for text extraction.
- The output is displayed with bounding boxes around the detected plates and the recognized text.

## Model

The YOLOv8 model (yolov8s.pt) is a pre-trained model that has been fine-tuned for detecting license plates. It is part of the YOLOv8 framework, which provides state-of-the-art object detection capabilities.


## Future Enhancements

This project can be further improved and expanded with the following features:

- **Improved Text Recognition**: Enhance the text extraction accuracy by incorporating advanced OCR models or preprocessing techniques to handle low-quality or blurry images effectively.

- **Real-Time Video Integration**: Extend the system to process video feeds in real-time, detecting and recognizing license plates from moving vehicles.

- **Integration with Other Detection Systems**: Combine the license plate recognition system with additional functionalities such as helmet detection or vehicle classification for enhanced traffic surveillance and safety enforcement.

