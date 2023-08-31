# Ransomeware
# 🔒 File Encryption Program 🗝

This is a simple command-line program that encrypts files in the current directory using Fernet symmetric encryption. It is intended for educational purposes only.

## ⚠️ Disclaimer ⚠️

This software is for authorized testing and educational purposes only. Usage for attacking, infiltrating, or damaging systems or data is strictly prohibited. The author is not responsible for any misuse or damage caused by this code. By using this software, you accept full responsibility for your actions. Do not use for unethical or unlawful purposes. 

## 💡 Usage 💡

To encrypt files:

1. Run the encrypt.py 🏃‍♂️ script
2. It will generate a new cryptographic key 🔑 in thekey.key
3. All files in the current directory will be read in 📝, encrypted 🔒, and overwritten with the encrypted contents, excluding the encrypt.py and thekey.key files.

To decrypt ☠️ the files: 

1. Run the decrypt.py 🏃‍♂️ script  
2. It will load the thekey.key 🗝 to decrypt the file contents
3. Encrypted files will be decrypted 📝 and overwritten with the original plaintext

## About

This program demonstrates basic file encryption 🔒 and decryption ☠️ using the Fernet module in Python 🐍. It generates a new Fernet key 🔑, loads the key to encrypt files in the current directory, and overwrites those files with encrypted contents. 

The encrypted files can be decrypted by running the decrypt.py script which loads the same Fernet key 🗝 and decrypts the file contents.

This serves as a simple example of symmetric encryption 🔒 and decryption ☠️. The key 🗝 should be protected and kept secret. 

## 📜 License

This project is open source and released under the [MIT License](LICENSE) 📜. Feel free to modify and reuse but please retain the disclaimer ⚠️.
## There is more to come in this project, this is still under building.

