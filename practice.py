# #this is comment

# print("hello world \n")
# print("""multi
# line 
# string""")

# print("hello " + "world")
# name=input("what is your name? ")
# print("hello " + name)
# print(type(name)) 
# print(5**7)

camping_stuff=["tent", "sleeping bag", "stove", "food"]
print(camping_stuff[0:2])
camping_stuff.append("flashlight")
camping_stuff.insert(2, "water")
camping_stuff.remove("stove")
print(camping_stuff)
camping_stuff.extend(["matches", "map"])
print(camping_stuff)
camping_stuff.pop(3)
print(camping_stuff)
camping_stuff.clear()
print(camping_stuff)