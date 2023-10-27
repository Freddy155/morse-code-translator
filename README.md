## Morse Code Translator
### Introduction

The Morse translator is a simple Python web application built using the Flask framework. It allows users to encode text into Morse code and decode Morse code back into text.

### Table of Contents

1. **Getting Started**
   - Prerequisites
   - Installation
   - Running the Application

2. **Usage**
   - Encoding Text
   - Decoding Morse Code

3. **Project Structure**
   - Files and Folders

4. **Troubleshooting**
   - Common Issues

### 1. Getting Started

#### Prerequisites

Before using the application, make sure you have the following installed:

- Python 3
- Flask (you can install it with  `pip install flask` )

#### Installation

1. Clone or download the application from the [GitHub repository](https://github.com/Freddy155/morse-code-translator).
```shell
git clone https://github.com/Freddy155/morse-code-translator.git
```

2. Open your terminal and navigate to the application directory.

```shell
cd morse-code-translator
```

3. Create a virtual environment (recommended) and activate it:

```shell
python3 -m venv venv
source venv/bin/activate
```

#### Running the Application

To run the application, use the following command in your terminal:

```shell 
python app.py
```


The application will start a local web server, and you can access it in your web browser at `http://localhost:5000`.

### 2. Usage

#### Encoding Text

1. Open the application in your web browser at `http://localhost:5000`.

2. In the "Text to Encode" input field, enter the text you want to encode into Morse code.

3. Click the "Encode" button.

4. The encoded Morse code will be displayed below the input field.

#### Decoding Morse Code

1. Open the application in your web browser at `http://localhost:5000`.

2. In the "Morse Code to Decode" input field, enter the Morse code you want to decode into text.

3. Click the "Decode" button.

4. The decoded text will be displayed below the input field.

### 3. Project Structure

The project includes the following files and folders:

- `app.py`: The main application script that runs the Flask web server.
- `templates/index.html`: The HTML template for the web interface.
- `venv/`: A virtual environment folder for isolating project dependencies.

### 4. Troubleshooting

#### Common Issues

- **IndentationError**: Ensure that your code is properly indented as shown in the provided code.

- **Flask Not Installed**: If you encounter an error related to Flask not being installed, make sure you've installed it using  `pip install flask`.
