with open("log.txt" , "r") as f :
    content = f.read()

if ("Python" in content):
    print("Yes we Have Python in The Log")

else:
    print("Python In The File Is Not Found")