from os import system
from main import nochmalDasGanze

def vigenere_explanation():
    system("cls")
    print('''Die Vigenere-Verschlüsselung ist ein Verschlüsselungsverfahren,
bei dem jeder Buchstabe im Klartext um eine Anzahl von Stellen im Alphabet
verschoben wird. Die jeweiligen Stellen, um die jeder Buchstabe verschoben
wird, werden durch die einzelnen Buchstaben eines Schlüssels festgelegt. 

Hier wird als Beispiel mit dem Schlüssel "Lecos" verschlüsselt:
        
    "A" verschiebt sich um 11 Stellen und wird zu "L"
        -> da der erste Buchstabe in "Lecos" an 11ter Stelle steht.
        -> 0 + 11 = 11 = L
    "B" verschiebt sich um 4 Stellen und wird zu "F"
        -> da der zweite Buchstabe in "Lecos" an 4ter Stelle steht.
        -> 1 + 4 = 5 = F
    "C" verschiebt sich um 14 Stellen und wird zu "R"
        -> da der dritte Buchstabe in "Lecos" an 14ter Stelle steht.
        -> 3 + 14 = 17 = R  
    ''')
    print()
    vigenere_example()

def vigenere_example():
    print("Gib eine Nachricht ein: \n")
    message = input("> ")
    print("\nFür diese Verschlüsselung wird jetzt mit dem Schlüssel 'Lecos GmbH' verschlüsselt.\n")
    key = "lecosgmbh"
    alphabet = 'abcdefghijklmnopqrstuvwxyzöäüß'
    encrypted_text = ''

    key_index = 0
    for char in message.lower():
        if char not in alphabet:
            encrypted_text += char
            if char == " ": 
                print()
        else:        
            # Find the right key character to encode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
             
            print(f'{index}\t+\t{offset}\t=\t{new_index}\t-->\t{char}\t+\t{key_char}\t=\t{alphabet[new_index]}')
    
    print('\nDeine ursprüngliche Nachricht:\t', message)
    print('Die verschlüsselte Nachricht:\t', encrypted_text,"\n")

    if nochmalDasGanze():

        vigenere_explanation()
