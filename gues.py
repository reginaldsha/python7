password = "bones"
count = 1
while count <= 3:

    guess = input("enter password :")
    if guess == password:
        print(f"you win")
        break
    if guess != password and count == 3:
        print("u lose")
    count += 1

