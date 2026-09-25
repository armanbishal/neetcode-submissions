from typing import List

def read_integers() -> List[int]:
    list_of_string = input().split(",")
    list_of_int = []
    for item in list_of_string:
        list_of_int.append(int(item))
    return list_of_int

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())