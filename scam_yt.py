p1 = "Make a lot of money"
p2 = "buy now"
p3 = "Subscribe this "
p4 = "Click here to win prizes"

message = input("Enter a message : ")

if (p1 in message) or (p2 in message ) or (p3 in message ) or (p4 in message):
    print("This message is a scam ")

else :
    print("THis meassage is not scam ")