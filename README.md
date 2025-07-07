HEIC to TIFF Converter
A simple, user-friendly desktop application for Windows to batch convert .heic image files to the .tiff format.

Replace the image above with a screenshot of your application.

🌟 Features
Easy-to-Use GUI: A clean graphical interface for selecting folders.

Batch Conversion: Convert all .heic files in a folder at once.

Separate Output: Save converted files to a different folder to keep your source images untouched.

Progress Tracking: A real-time progress bar shows the status of the conversion.

Standalone Executable: No need to install Python or any libraries to run the app.

🎯 Motivation
The .heic format, common on modern iPhones, is not natively supported on all versions of Windows, making it difficult to view or edit these photos. This tool was created to provide a simple, offline solution to convert these images into the widely compatible .tiff format.

🚀 How to Use (for End-Users)
Go to the Releases page of this repository.

Download the latest HEIC_Converter.exe file.

Double-click the .exe file to run it. No installation is needed!

Use the "Browse..." buttons to select your source and destination folders.

Click "Convert" and wait for the process to complete.

🛠️ How to Run from Source (for Developers)
If you want to run the script directly or modify it, follow these steps.

Prerequisites
Python 3.7+

pip (Python package installer)

1. Clone the Repository
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git)
cd YOUR_REPOSITORY

2. Set Up a Virtual Environment (Recommended)
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

(You will need to create a requirements.txt file. See below.)

4. Create requirements.txt
Create a file named requirements.txt with the following content:

pillow
pillow-heif

5. Run the Application
python heic_converter.py

📦 How to Build the .exe from Source
To create your own standalone executable from the Python script:

Install PyInstaller:

pip install pyinstaller

Run the Build Command:
Navigate to the project directory in your terminal and run:

pyinstaller --onefile --windowed --name="HEIC_Converter" heic_converter.py

--onefile: Bundles everything into a single executable.

--windowed: Prevents a console window from appearing when the app runs.

Find Your Executable:
The final HEIC_Converter.exe will be located in the dist folder.

💻 Technologies Used
Python: The core programming language.

Tkinter: Python's standard library for creating the graphical user interface.

Pillow (PIL Fork): A powerful image processing library.

pillow-heif: A library to add HEIF/HEIC support to Pillow.

PyInstaller: A tool to bundle the application into a standalone executable.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.
