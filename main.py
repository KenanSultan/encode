import inquirer
from encript import *

digits = '0123456789'
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
punct = "_ !#$%&'()*+,-./:;<=>?@[]^`{|}~" + '"'  + '\n'
azeriLet = "əƏöÖüÜıİğĞçÇşŞ"

all_keys = digits + letters + punct + azeriLet

while True:
    questions = [
        inquirer.List ('opt',
            message = "What you want? ",
            choices = ['Encode the text','Decode the file','Quit'],
        ),
    ]
    answer = inquirer.prompt(questions)['opt'][0]

    if answer == 'E':
        content = input("Write the text: ")
        file_name = input("Write the file name: ")+'.txt'
        code = int(input("Write the code (100-999): "))
        encode(code, file_name, all_keys, *content)
        print('\n')
    elif answer == 'D':
        options = [
            inquirer.List ('opt',
                message = "Choose file! ",
                choices = [i for i in os.listdir('./secret_files/') if i[-4:] == '.txt'],
            ),
        ]
        file_name = inquirer.prompt(options)['opt']
        code = int(input("Write the code: "))
        print('\n')
        print(decode(code, all_keys, file_name))
        print('\n')
    elif answer == 'Q':
        print("Bye\n")
        exit()
    else:
        exit()