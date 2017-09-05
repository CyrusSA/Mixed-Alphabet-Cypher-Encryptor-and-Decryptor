def make_key_alpha_dict(key): #creating a dictionary linking the regular alphabet to the encrypted alphabet
    alpha_list, org_alpha_list = [], []
    for a in range(65,91): #creating a list of the regular alphabets
        alpha_list.append(chr(a))
        org_alpha_list.append(chr(a))
    
    key_list = []

    for a in key:
        key_list.append(a)
    
    for a in key_list:
        alpha_list.remove(a)

    key_alpha_list = key_list + alpha_list #list of encrypted alphabets
    key_alpha_dict = {}
    for a in range(26):
        key_alpha_dict[key_alpha_list[a]] = org_alpha_list[a] #creating dictionary

    return key_alpha_dict
def decode(key_alpha_dict, encoded_string):
    decoded_string = ''
    for a in encoded_string:
        try:
            decoded_string+=key_alpha_dict[a]
        except KeyError:
            decoded_string+=a
    return decoded_string

print('Deranged Alphabet Decryptor')
key = input('Enter key(All caps, no digits, no repeating letters): ')
encoded_string = input('Enter string to be descrambled: ')
key_alpha_dict = make_key_alpha_dict(key)
print('Plaintext: ' + decode(key_alpha_dict,encoded_string))
