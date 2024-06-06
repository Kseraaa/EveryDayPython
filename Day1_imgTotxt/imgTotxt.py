import pywhatkit
#pip install pywhatkit
pywhatkit.image_to_ascii_art('input.png', "Myart")
read_file = open('Myart.txt', "r")
print(read_file.read())
