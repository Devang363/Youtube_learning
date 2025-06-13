
with open("log.txt" , "r") as f :
    lines = f.readline()

lineno = 1
for line in lines :
    if ("Python" in lines):
        print(f"Yes we Have Python Present. Line no.{lineno}")
        break
    lineno += 1
else:
    print("Python In The File Is Not Found")