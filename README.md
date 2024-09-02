
# Object Detection Using Yolov5 : Mobile and Watch Detection

Welcome to my object detection project! This repository contains the code, dataset, and documentation for training a YOLOv5 model to detect two specific objects: mobile phones and watches. This project was developed as part of my internship at Orinson Technologies.


## Table of content

1. [Project Overview](#project-overview)
2. [Dataset](#dataset)
3. [Model Architecture](#model-architecture)
4. [Installation & Setup](#installation)
5. [Training](#training)
6. [Detection](#detection)
7. [Results](#results)


## Project Overview
This project aims to develop a custom object detection model using YOLOv5, a popular deep learning algorithm for real-time object detection. The goal is to accurately detect and classify mobile phones and watches in images, leveraging the speed and efficiency of YOLOv5.

## Dataset

- ***Number of classes:*** 2(Mobile,Watch)
- ***Number of Images:*** *439 images*
- ***Annotation Format:*** YOLO format (txt files with bounding box coordinates)
- ***Training images:*** 339
- ***Validation images:*** 89

## Model Architecture

YOLOv5 (You Only Look Once version 5) is a state-of-the-art, single-stage object detection model. YOLOv5 provides several advantages, including:

- ***Speed:*** Fast inference time suitable for real-time applications.
- ***Accuracy:*** High precision and recall for detecting objects.
- ***Flexibility:*** Easy to fine-tune and adapt to custom datasets.

## Installation and Setup

To set up this project, follow these steps:

**Clone the repository:**
```bash 
git clone https://github.com/ultralytics/yolov5

cd yolov5
```
**Install Dependencies**
```bash
pip install -r requirements.txt
```
## Training

The training process involves several steps:

1. **Data Preparation:** Images are resized, normalized, and augmented to enhance the model's generalization ability.
2. **Model Configuration:** A pre-trained YOLOv5 model is fine-tuned on the custom dataset, adjusting hyperparameters such as learning rate, batch size, and epochs.
3. **Training Execution:** The model is trained using a GPU to speed up the process. The training script monitors loss metrics and adjusts learning rates dynamically.

### Key Parameters

- ***Epochs:*** *30-50*
- ***Batch Size:*** *16*
- ***Data:*** Custom_data.yaml
```bash
python train.py --img 640 --batch 16 --epochs 30 --data custom_data.yaml --weights yolov5s.pt

```
## Detection

After training, the model is used to perform object detection on test images. The detection script reads the input images, applies the trained YOLOv5 model, and outputs images with bounding boxes around detected objects, along with confidence scores.

### Key Parameters
- ***weights:*** Trained data .pt files
- ***Source:*** Path of testing data or either keep source 0 for detection from your systems camera.

**Write Below command for detection**

```bash
python detect.py --weights bestO.pt --img 640 --conf 0.25 --source watch.mp4
```
## Results

The model achieved high accuracy in detecting both mobile phones and watches across a variety of images. Below are some performance metrics:

- ***Accuracy:*** 80-85%
- ***Precision:*** 80%

<p align="center">
  <img src="images/example_detection1.png" alt="Example Detection 1" width="45%">
  <img src="images/example_detection2.png" alt="Example Detection 2" width="45%">
</p>
