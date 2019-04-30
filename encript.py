import os

def encode(code, file_name, keys, *content):
    secure_content = []
    
    for i in content:
        if keys.find(i) != -1:
            ind = keys.find(i)-code%108
            secure_content.append(keys[ind])
        
    with open("secret_files/"+file_name, "w") as file:
        file.write("".join(secure_content))

def decode(code, keys, file_name):
    with open("secret_files/"+file_name, "r") as file:
        secure_content = file.read()

    content = []
    
    for i in secure_content:
        if keys.find(i) != '_':
            ind = keys.find(i)+code%108
            if ind > len(keys)-1:
                ind = ind-len(keys)
            content.append(keys[ind])
        
    return "".join(content)