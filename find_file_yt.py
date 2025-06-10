f = open("poem.txt")

content = f.read()

if ("twinkle" in content):
    print("Twinkle is present in the file")

else:
    print("The word Twinkle is not present in the content")
f.close()