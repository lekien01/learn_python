class_infor = [
    {
        "firstname": "Stephen",
        "lastname": "Dinh",
        "class_number": "10a1",
        "friend_name": ["Nam", "Vuong"]
    },
    {
        "firstname": "Sarah",
        "lastname": "Dinh",
        "class_number": "10a1",
        "friend_name": ["Stephen", "Dinh"]
    },
]

#create input function
#function that do input

def input_new_record():
    print("What is your first name?")
    input_fist_name = input().title()

    print("what is your last name?")
    input_last_name = input().title()

    print("What is your class?")
    input_class_number = input().title()

    print("who is your friend?")
    input_first_friend = input().title()

    print(f"{input_fist_name} + {input_last_name} + {input_class_number} +{input_first_friend}")


