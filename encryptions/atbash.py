
def atbash_explanation():
    print('''Die Atbash-Verschlüsselung ist ein Verschlüsselungsverfahren,
bei dem das Alphabet umgedreht wird.
Wenn das Alphabet mit Umlauten so definiert ist:
'abcdefghijklmnopqrstuvwxyzöäüß'
dann findet folgender Tausch statt: 

    "A" wird zu "ß"
    "B" wird zu "ü"
    "C" wird zu "ä"
    ''')

def atbash_example():
    print("Gib eine Nachricht ein: \n")
    message = input("> ")
    
    alphabet = 'abcdefghijklmnopqrstuvwxyzöäüß'
    reversed_alphabet = alphabet[::-1]
    atbash_dictionary = {original: reversed_value for original, reversed_value in zip(alphabet, reversed_alphabet)}

    encrypted_text = ''

    for char in message.lower():
        if char not in alphabet:
            encrypted_text += char
            if char == " ": 
                print()
        else:        
            encrypted_text += atbash_dictionary[char]
            print(f'{char}\t-->\t{atbash_dictionary[char]}')
    
    print('\nDeine ursprüngliche Nachricht:\t', message)
    print('Die verschlüsselte Nachricht:\t', encrypted_text,"\n")


atbash_explanation()
atbash_example()