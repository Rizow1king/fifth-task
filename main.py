import random
import string


def id_generator(length=4):
    number = string.digits
    user = ""
    for i in range(length):
        user += random.choice(number)
    return user


while True:
    command = input("buyruq kiriting(add yoki stop):").lower()
    if command == "stop":
        print("Dastur toxtadi!!!")
        break
    elif command == "add":
        while True:
            name = input("ismingizni kiriting:")
            if not name:
                print("Ismni kiritng!!")
                continue
            break
        while True:
            lastname = input("Familiyangizni kiriting:")
            if not lastname:
                print("familiyangizni kiritng!!")
                continue
            break
        while True:
            age = input("yoshingizni kiriting:")
            if not age.isdigit():
                print("yos faqat sonlardan iborat bolishi kerak!!!")
                continue
            break
        while True:
            phone_num = input("telefon raqamni kiriting:")
            if not phone_num.startswith("+998") and len(phone_num) != 13:
                print("telefon raqam '+998' bilan boshlanib 13 ta raqamdan iborat bolishi kerak!!!")
                continue
            break
        while True:
            email = input("email pochtangizni kiriting:")
            if "." and "@" not in email:
                print("emailni ichida '.' va '@' bolishi shart!!")
                continue
            break
        while True:
            address = input("address ni kiriting:")
            if not address:
                print("addresni kiritng!!!")
                continue
            break

        data = f"\n\nID:{id_generator()}\nIsmi:{name} \n Familiyasi:{lastname} \n Yoshi:{age} \n Telefon raqami:{phone_num} \n Emaili:{email} \n addressi:{address}\n\n"
        with open("user_data.txt", "a", encoding='utf-8') as file:
            file.write(data)

