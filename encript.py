import os

letters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !#$%&'()*+,-./:;<=>?@[]^_`{|}~" + '"' + "əƏöÖüÜıIğĞçÇşŞ"


def encode(surf, file_name, *content):
    secure_content = []
    
    for i in content:
        ind = letters.find(i)-surf
        secure_content.append(letters[ind])
        
    with open(file_name, "w") as file:
        file.write("".join(secure_content))


def decode(surf, file_name):
    with open(file_name, "r") as file:
        secure_content = file.read()

    content = []
    
    for i in secure_content:
        ind = letters.find(i)+surf
        if ind > len(letters)-1:
            ind = ind-len(letters)
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
    