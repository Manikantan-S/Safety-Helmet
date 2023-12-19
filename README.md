
# Safety Helmet Detector (YOLOv5)

## Overview

This project is a safety helmet detector built using YOLOv5, designed to continuously monitor CCTV footage for individuals not adhering to safety rules by not wearing helmets. The YOLOv5 model is trained to detect the presence or absence of safety helmets in real-time.

## Features

- **Real-time Detection:** The detector operates in real-time, providing instantaneous feedback on safety helmet compliance.
  
- **CCTV Footage Monitoring:** The system is capable of monitoring CCTV footage, making it suitable for surveillance applications.

- **YOLOv5 Model:** The underlying model is based on YOLOv5, a state-of-the-art object detection algorithm, ensuring accurate and efficient helmet detection.

## Requirements

- Python 3.x
- YOLOv5
- OpenCV
- Other dependencies (specified in `requirements.txt`)

## Installation

```bash
https://github.com/Manikantan-S/Safety-Helmet.git
pip install -r requirements.txt

wget https://github.com/ultralytics/yolov5/releases/download/v5.0/yolov5s.pt
