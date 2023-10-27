from flask import Flask, request, render_template

app = Flask(__name__)

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

def encode_morse(text):
    morse_code = []
    for char in text.upper():
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            morse_code.append(' ')
    
    return ' '.join(morse_code)

def decode_morse(morse_code):
    morse_code = morse_code.split(' ')
    decoded_message = []
    for code in morse_code:
        if code in morse_code_dict.values():
            decoded_message.append(list(morse_code_dict.keys())[list(morse_code_dict.values()).index(code)])
        else:
            decoded_message.append(' ')
    
    return ''.join(decoded_message)

@app.route("/", methods=["GET", "POST"])
def home():
    encoded_message = ""
    decoded_message = ""
    
    if request.method == "POST":
        if "encode" in request.form:
            text_to_encode = request.form["text_to_encode"]
            encoded_message = encode_morse(text_to_encode)
        elif "decode" in request.form:
            morse_to_decode = request.form["morse_to_decode"]
            decoded_message = decode_morse(morse_to_decode)
    
    return render_template("index.html", encoded_message=encoded_message, decoded_message=decoded_message)

if __name__ == "__main__":
    app.run(debug=True)
