def alphabet_position(char):
    return ord(char.lower())-97

def rotate_character(charc, rot):
    newchar = chr(((alphabet_position(charc)+rot)%26)+97)
    if charc.isupper():
        newchar = newchar.upper()

    return newchar

def encrypt(string, rot):
    newstring = ""
    for char in string:
        if char.isalpha():
            newstring += rotate_character(char, rot)
        else:
            newstring += char
    return newstring
