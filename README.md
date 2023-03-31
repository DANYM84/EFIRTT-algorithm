# EFIRTT - Image Recognition and Translation Tool

EFIRTT (Image Recognition and Translation Tool) is a Python algorithm designed to recognize and translate written text in images, analyze the frequency of each word in English, and provide the results to the user. This tool uses the Tkinter library to create a graphical interface and the OpenCV library for image processing.

## Features

- User-friendly graphical interface for selecting the folder to analyze
- Optical character recognition (OCR) using OpenCV to convert the written text in images to text format
- Translation library for translating the converted text to English
- Natural language processing library for analyzing the frequency of each word in the translated text
- Results displayed to the user in the graphical interface
- Option for the user to export the data

## Installation

To use EFIRTT, follow the steps below:

1. Install Python on your machine. You can download it from the official website: https://www.python.org/downloads/
2. Install the required libraries using pip by running the following command in your terminal:

pip install opencv-python-headless pillow pytesseract googletrans==4.0.0-rc1 nltk

arduino
Copy code

3. Clone the EFIRTT repository using git:

git clone https://github.com/username/EFIRTT.git

arduino
Copy code

4. Open the project directory in your terminal and run the following command:

python main.py

vbnet
Copy code

## Usage

1. Launch the EFIRTT tool by running the above command.
2. Select the folder to analyze using the graphical interface.
3. Wait for the tool to analyze the images and display the results in the interface.
4. Optionally, export the data using the export button.

## Contributing

If you would like to contribute to EFIRTT, please fork the repository, create a new branch, and submit a pull request. All contributions are welcome, including bug fixes, new features, and improvements to the documentation.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as yo

##Project Description:

The goal of this project is to develop a Python algorithm that uses the Tkinter library to create a user-friendly graphical interface and the OpenCV library for image processing. The algorithm will search for a user-selected folder and analyze all images within it, recognizing and translating written words into text. The translated text will then be analyzed for the frequency of each word in English, and the results will be stored for the user.

Algorithm Steps:

- Create a graphical interface using Tkinter that allows the user to select a folder to analyze.
- Use OpenCV to read all images in the selected folder.
- Apply optical character recognition (OCR) using OpenCV to convert the written text in the images to text format.
- Use a translation library to translate the converted text to English.
- Analyze the frequency of each word in the translated text using a natural language processing library.
- Display the frequency analysis results to the user in the graphical interface.
- Store the results in a file and provide an option for the user to export the data.
- This project aims to provide an efficient and user-friendly solution for analyzing written text in images and identifying the frequency of each word in English. It can be useful for tasks such as analyzing text in scanned documents or identifying keywords in marketing materials. 
