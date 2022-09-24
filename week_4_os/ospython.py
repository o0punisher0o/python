import os

print(os.getcwd())

os.mkdir("papka")
os.chdir("papka")

print(os.getcwd())

text_file = open("TEKSTFILE.txt", "w")
text_file.write("TEKSTFILE")
text_file.close()

print(os.listdir())
os.remove("TEKSTFILE.txt")
print(os.listdir())
