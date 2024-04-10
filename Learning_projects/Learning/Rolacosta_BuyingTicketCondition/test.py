height = int(input("what is the height "))


if height >= 120:
    age = int(input("What is your age? "))
    if age <= 10:
        print("$12")
    elif age <= 19:
        print("$15")
    else:
        print("$20")
    
    photo_option = input("Do you want to have a photo?")

    if photo_option == "Y":
        print("Yup")
    else:
        print("Thank you")

else:
    print("Sorry we can not let you in")
