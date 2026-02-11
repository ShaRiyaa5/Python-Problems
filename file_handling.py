"""
1) Image Copier
Read an image in "rb" mode.
Write it into a new file using "wb".
Verify that the new file opens correctly.
"""
with open ("image.jpg", "rb") as image:
    data = image.read()
with open("copy_image.jpg", "wb") as image:
    copy_image = image.write(data) #writtens number of bytes and not the binary data
if len(data) == copy_image:
    print("Image copied successfully")
else:
    print("error")
"""
2) Text File in Binary Mode
Open a .txt file in "rb" mode.
Print the raw bytes.
Then open in "wb" mode and write new bytes (like b"Hello Binary World").
Open the file in normal "r" mode to see what it looks like.
"""
with open("text.txt", "rb") as file:
    data = file.read()
    print(data)
with open("text.txt", "wb") as new_file:
    data1 = new_file.write(b"Hello Binary World")
    print(data1)
with open("text.txt", "r") as read_file:
    data2 = read_file.read()
    print(data2)
"""
3) File Splitter
Read a large file in "rb" mode.
Write only the first half of the bytes into a new file using "wb".
Compare the sizes of the original and new file.
"""
with open("HTML - Great Learning.pdf", "rb") as doc:
    data = doc.read()
with open("HTML short", "wb") as new_doc:
    data1 = new_doc.write(data[:len(data)//2])
if len(data)//2 == data1:
    print("half of the file has copied successfully")
"""
4) PDF Reader
Open a PDF in "rb" mode.
Print the first 100 bytes.
Notice how it looks different from text files.
"""
with open("HTML - Great Learning.pdf", "rb") as doc:
    data = doc.read(100)
    print(data)
    print(len(data))

