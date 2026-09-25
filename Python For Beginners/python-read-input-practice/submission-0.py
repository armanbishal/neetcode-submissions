def add_two_numbers() -> int:
    list_of_string = input().split(",")
    sum = 0
    for item in list_of_string:
        sum += int(item)
    return sum

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())