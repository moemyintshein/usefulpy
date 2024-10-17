To export your Python script as an executable program, you can use PyInstaller. This tool allows you to bundle a Python application and all its dependencies into a single package, which can be run on a computer without Python installed. Here's how to do it with your translator app:

1. First, install PyInstaller:
```
pip install pyinstaller
```
2. Make sure all your required libraries are installed in your Python environment:
```
pip install googletrans==3.1.0a0 tkinter
```
3. Navigate to the directory containing your translator_app.py script in the terminal or command prompt. Run PyInstaller with the following command:
```
pyinstaller --name=TranslatorApp --onefile --windowed --icon=icon.icns translator_app.py
```

Note: If you're using a virtual environment, make sure to activate it before running PyInstaller.

To create virtual environment:
```
python3 -m venv translation
source translation/bin/activate
``