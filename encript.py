import os

def encode(code, file_name, keys, *content):
    surfing = "".join([keys[keys.find(i)-code%len(keys)] if keys.find(i) != -1 else i for i in content])
    part = code//len(keys)+2
    surfing += (part - len(surfing)%part)*' '
    secure_content = ''.join([surfing[i::part] for i in range(part)])
        
    with open("secret_files/"+file_name, "w") as file:
        file.write(secure_content)

def decode(code, keys, file_name):
    with open("secret_files/"+file_name, "r") as file:
        secure_content = file.read()
    
    part = len(secure_content)//(code//len(keys)+2)
    surfing = ''.join([secure_content[i::part] for i in range(part)]).strip()

    content = []
    
    for i in surfing:
        if keys.find(i) != -1:
            ind = keys.find(i)+code%len(keys)
            if ind > len(keys)-1:
                ind = ind-len(keys)
            content.append(keys[ind])
        else:
            content.append(i)
        
    return "".join(content)