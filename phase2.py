try:
    file=open("example.txt","r")
    for items in file:
        print(items.strip())
    file.close()
    file=open("example.txt","w")
    file.write(input("enter what you wanna write."))
    file.close()
    file=open("example.txt","a")
    file.write(input("enter what you wanna add."))
    file.close()
except FileNotFoundError:
    print("File not found.")
