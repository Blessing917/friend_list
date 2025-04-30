# Program: Friends List
# Author: Blessing Glory Tsikey
# Description: This program collects names of friends from the user until they type "end".
# It then displays the list of entered friends.

friends = []

while True:
    name = input("Type the name of a friend: ").strip()  

    if name.lower() == "end":
        break

    friends.append(name)

print("\nYour friends are:")
for friend in friends:
    print(friend)
