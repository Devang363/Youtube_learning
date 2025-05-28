letter = ''' Dear <|name|>,\n You Are  Selected! \n <|Date|>'''

print(letter.replace("<|name|>", "Devang").replace("<|Date|>","20 September"))

print(letter.find("  "))

print(letter.replace("  "," "))