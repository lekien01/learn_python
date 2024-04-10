#print out my name with capital first letter
#use function with output 

def what_is_my_name(first_name, last_name):
    format_first_name = first_name.title()
    format_last_name = last_name.title()
    return f"{format_first_name} , {format_last_name}"

output = what_is_my_name("Angela", "Yu")
print(output)