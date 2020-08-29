import random
import sys
import string
import os

list1 = list(string.ascii_letters)
list2 = list(string.digits)
list3 = list(string.punctuation)


def generate(length, modif):
    '''
    the modifier arguments are "easy"(only letters) 
    "normal"(letters and numbers) 
    "complex"(letters, numbers and punctuation marks
    '''
    endlist = []
    if modif == "complex":
        for i in range(length):
                new_list = []
                random.shuffle(list1)
                x = random.choice(list1)
                random.shuffle(list2)
                y = random.choice(list2)
                random.shuffle(list3)
                z = random.choice(list3)
                new_list.append(x)
                new_list.append(y)
                new_list.append(z)
                endlist.append(random.choice(new_list))

    elif modif == "normal":
        for i in range(length):
                new_list = []
                random.shuffle(list1)
                x = random.choice(list1)
                random.shuffle(list2)
                y = random.choice(list2)
                new_list.append(x)
                new_list.append(y)
                endlist.append(random.choice(new_list))

    elif modif == "easy":
        for i in range(length):
                new_list = []
                random.shuffle(list1)
                x = random.choice(list1)
                new_list.append(x)
                endlist.append(random.choice(new_list))
    
    else:
        print("Possible modifier arguments: easy, normal, complex")
        exit()
    
    end = "".join(endlist)
    print(f"\nYour password is: {end}")

os.system('cls')

try:
    sys._clear_type_cache()
    generate(int(sys.argv[1]),sys.argv[2])
    pass
except:
    print("Give your password a length as the first argument and a modifier as the second argument(easy,normal,complex).")
    sys.exit()
