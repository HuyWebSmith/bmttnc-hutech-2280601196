from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher

app = Flask(__name__)

#Caesar Cipher
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

#VIGENERE CIPHER ALGORITHM
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text,key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text,key)
    return jsonify({'decrypted_text': decrypted_text})


#railfence
@app.route("/api/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    data = request.json
    text = data.get("plain_text")
    key = int(data.get("key"))

    Railfence = RailFenceCipher()
    encrypted_text = Railfence.railfence_cipher(text, key)

    return jsonify({"encrypted_text": encrypted_text})  # Đổi lại key đúng

@app.route("/api/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    data = request.json
    text = data.get("cipher_text")
    key = int(data.get("key"))

    Railfence = RailFenceCipher()
    decrypted_text = Railfence.railfence_decipher(text, key)

    return jsonify({"decrypted_text": decrypted_text})  # Đổi lại key đúng

#PlayFairCipher
@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    data = request.json
    text = data.get("plain_text")
    key = data.get("key")

    if not text or not key:
        return jsonify({"error": "Missing plain_text or key"}), 400

    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    encrypted_text = playfair.playfair_cipher(text, matrix)

    return jsonify({"encrypted_text": encrypted_text,"matrix": matrix})

@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    data = request.json
    text = data.get("cipher_text")
    key = data.get("key")

    if not text or not key:
        return jsonify({"error": "Missing cipher_text or key"}), 400

    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    decrypted_text = playfair.playfair_decipher(text, matrix)

    return jsonify({"decrypted_text": decrypted_text,"matrix": matrix})

@app.route("/api/playfair/generate_matrix", methods=["POST"])
def playfair_generate_matrix():
    data = request.json
    key = data.get("key")

    if not key:
        return jsonify({"error": "Missing key"}), 400

    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)

    return jsonify({"matrix": matrix})


if __name__ == "__main__":
    app.run(debug=True)

#main function
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
