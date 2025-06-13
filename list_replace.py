words = ["Donkey" ,"But" , "Ganda"]

with open("replace.txt" , "r") as f :
    content = f.read()
for word in words :
    content = content.replace(word , "#"*len(word))

with open("replace.txt" , "w") as f:
    f.write(content)