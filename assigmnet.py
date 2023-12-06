# assign 1

num = int (input("Please Enter a Number :") .strip())

if num == 0:
    print(f"Number 0 Is Not Larger Than 0")

else :
    sum = 0
    while num > 1:
        num -= 1
        if num == 6:
            continue
        print(num)
        sum += 1
        
print(f"\n{sum} Numbers Printed Successfully .") 
              
# assign 2

friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
index = 0
count = 1
for x in friends:
    if x.islower():
        count += 1
        index += 1 
        continue
    else:
        print(x)
         
print(f"Friends Printed And Ignored Names Count Is {count}")

# assign 3

skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:
  print(skills.pop(0))


# assign 4

my_friends = []
max_friends = 4


while max_friends > 0:
    friends = input("Enter a name: ")
    if friends.isupper():
        print("Invalid Name")

    else:
        if friends[0].isupper():
            my_friends.append(friends.strip())
            max_friends -= 1
            print(f"Friend {friends.strip()} Is Added")
            print(f"Names Left In List Is {max_friends}")
        else:
            my_friends.append(friends.capitalize().strip())
            max_friends -= 1
            print(f"Friend {friends.capitalize().strip()} Is Added =>> 1st Letter Become Capital")
            print(f"Names Left In List Is {max_friends}")
print(my_friends)    
