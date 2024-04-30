# Handwritten OCR

## Introduction

Handwritten OCR is a Python-based optical character recognition (OCR) system designed to recognize handwritten text from images.

## Features

- Recognizes handwritten text from images.
- Supports various image formats such as JPEG, PNG, and BMP.
- Uses machine learning algorithms for accurate character recognition.
- Provides easy-to-use APIs for integration into existing applications.

## Installation

1. Clone the repository:
   `git clone https://github.com/21amir21/handwritten-ocr.git`

2. Navigate to the project directory:
   `cd handwritten-ocr`

3. Install dependencies:
   `pip install -r requirements.txt`

## Usage

1. Import the OCR module:

```python
import ocr

image = ocr.load_image("handwritten_text.png")
```

Perform OCR on the image:

```python
text = ocr.recognize_text(image)
```

Print the recognized text:

```python
print(text)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
