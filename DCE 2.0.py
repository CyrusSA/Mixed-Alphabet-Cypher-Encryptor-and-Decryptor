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
    
    for a in range(26): #creating dictionary
        key_alpha_dict[org_alpha_list[a]] = key_alpha_list[a]

    return key_alpha_dict

def encode(key_alpha_dict, raw_string, punct_choice):
    encoded_string = ''
    for a in raw_string:
        if punct_choice == 'y': 
            try:
                if a.isalnum()==True:
                    encoded_string+=key_alpha_dict[a]
            except KeyError: #punctuation and numbers raise KeyError
                if a.isdigit()==True:
                    encoded_string+=a
        else:
            try:
                encoded_string+=key_alpha_dict[a]
            except KeyError:
                encoded_string+=a
    return encoded_string
                
print('Deranged Alphabet Encryptor')
key = input('Enter key(All caps, no digits, no repeating letters): ')
inp = input('Enter string to be scrambled: ')
punct_choice = input('Remove punctuations and spaces(y/n)? ')
raw_string = inp.upper()
key_alpha_dict = make_key_alpha_dict(key)
print('Scrambled string: ' + encode(key_alpha_dict, raw_string, punct_choice))

    
