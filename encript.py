import string
import os

letters = string.ascii_letters

def encode(surf, file_name, *content):
    secure_content = []
    
    for i in content:
        if i == ' ':
            secure_content.append(' ')
        else:
            ind = letters.find(i)-surf
            secure_content.append(letters[ind])
        
    with open(file_name, "w") as file:
        file.write("".join(secure_content))


def decode(surf, file_name):
    with open(file_name, "r") as file:
        secure_content = file.read()

    content = []
    
    for i in secure_content:
        if i == ' ':
            content.append(' ')
        else:
            ind = letters.find(i)+surf
            if ind > 51:
                ind = ind-52
            content.append(letters[ind])
        
    return "".join(content)

while True:
    option = input("Sechim et [e, d, q]: ")

    if option == 'e':
        content = input("Metni girin: ")
        file_name = input("Faylin adini sechin: ")+'.txt'
        surf = int(input("Surushdurme sayi: "))
        encode(surf, file_name, *content)
    elif option == 'd':
        print(", ".join(os.listdir()))
        file_name = input("Faylin adini sechin: ")+'.txt'
        surf = int(input("Surushdurme sayi: "))
        print(decode(surf, file_name))
    elif option == 'q':
        print("Program sonlandi")
        break
    else:
        print("Yanlish sechim")
    