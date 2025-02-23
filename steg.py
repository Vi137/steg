import cv2
import os
import string

img_path = input("Enter the path to the image (e.g., mypic.jpg or C:/path/to/mypic.jpg): ")

img = cv2.imread(img_path)

if img is None:
    print(f"Error: Unable to load the image file '{img_path}'.")
    exit(1)

height, width, channels = img.shape

msg = input("Enter secret message: ")

password = input("Enter password: ")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

msg_len = len(msg)
max_pixels = height * width * channels

if msg_len > max_pixels:
    print("Message is too long for the image!")
    exit(1)

for i in range(msg_len):
    img[n, m, z] = d[msg[i]]
    n += 1
    if n >= height:
        n = 0
        m += 1
    if m >= width:
        m = 0
    z = (z + 1) % 3

cv2.imwrite("Encryptedmsg.jpg", img)

os.system("start Encryptedmsg.jpg")

message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption: ")

if password == pas:
    for i in range(msg_len):
        message = message + c[img[n, m, z]]
        n += 1
        if n >= height:
            n = 0
            m += 1
        if m >= width:
            m = 0
        z = (z + 1) % 3
    print("Decrypted message:", message)
else:
    print("Invalid key!")
