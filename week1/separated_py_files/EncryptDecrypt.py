def encrypt(file_name = "moby10b.txt", key = 7, print_to_file = False):
    """
    Simple encryption. 
    key is what to shift the letters by
    if there is a symbol it is unchanged

    set print_to_file to false for print to terminal. True will print to "encrypt_" + file_name
    """
    

    def get_char_with_key(char_to_change):
        
        
        offset = 0
        char = ord(char_to_change)

        if char <= ord('Z') and char >= ord('A'):
            offset = char - ord('A')
            result = offset + key if (offset + key < 26) else (offset + key) % 26 
            result += ord('A')
        elif char <= ord('z') and char >= ord('a'):
            offset = char - ord('a')
            result = offset + key if (offset + key < 26) else (offset + key) % 26 
            result += ord('a')
        else:
            return chr(char)

        return chr(result)
    
    file_ = None
    if print_to_file:
            file_ = open("encrypt_" + file_name, 'w')

    # open file and read each line
    text = ""
    try:
        file = open(file_name, 'r')
        text = file.read()
    except:
        print("File is not found, encrypting text entered")
        print("Text entered:")
        print(file_name)
        text = file_name
    

    # go through text and encrypt
    for line in text:
        if print_to_file:
            file_.write(get_char_with_key(line))
        else:
            print(get_char_with_key(line),end="")
    

def decrypt(file_name = "moby10b_encypted.txt", key = 7, print_to_file = False):
    """
    Simple decryption. 
    key is what to shift the letters by
    if there is a symbol it is unchanged
    """
    file_ = None
    if print_to_file:
            file_ = open("decrypt_" + file_name, 'w')
    def get_char_with_key(char_to_change):
        offset = 0
        char = ord(char_to_change)

        if char <= ord('Z') and char >= ord('A'):
            offset = char - ord('A')
            result = offset - key if offset - key >= 0 else 26 - (key - offset)
            result += ord('A')
        elif char <= ord('z') and char >= ord('a'):
            offset = char - ord('a')
            result = offset - key if offset - key >= 0 else 26 - (key - offset)
            result += ord('a')
        else:
            return chr(char)

        return chr(result)
    
    # open file and read each line
    text = ""
    try:
        file = open(file_name, 'r')
        text = file.read()
    except:
        print("File is not found, decrypting text entered")
        print("Text entered:")
        print(file_name)
        text = file_name
    
    # go through text and encrypt
    for line in text:
        if print_to_file:
            file_.write(get_char_with_key(line))
        else:
            print(get_char_with_key(line),end="")

#encrypt("This is a test")
encrypt()
decrypt()