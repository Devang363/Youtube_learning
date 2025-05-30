marks = {"Devang" : 100 , "Shubham" : 56 , "Rohan" : 23}

marks.update({"Devang" : 99,"Renuka" : 88})

print(marks.items())

print(marks.keys())

print(marks.get("Devang") )  #retuns none if key not found

print(marks["Devang"]) #returns error if key not found

