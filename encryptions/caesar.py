from os import system
from main import nochmalDasGanze

def caesar_explanation():
    system("cls")

    print('''Die Caesar-Verschlüsselung ist ein einfaches Verschlüsselungsverfahren,
bei dem jeder Buchstabe im Klartext um eine feste Anzahl von Stellen im Alphabet
verschoben wird. 
Zum Beispiel, bei einer Verschiebung um 3:
        
    A -> D
    B -> E
    C -> F
    
    ''')

    print()
    caesar_example()

def caesar_example():
    try:
        print("Gib eine Nachricht ein: \n")
        message = input("> ")
    except KeyboardInterrupt:
        print("Keine gültige Eingabe")
        caesar_example()

    print("\nFür diese Verschlüsselung wird jetzt mit dem Faktor 10 verschlüsselt.\n")
    offset = 10
    alphabet = 'abcdefghijklmnopqrstuvwxyzöäüß'
    encrypted_text = ''

    for char in message.lower():
        if not char.isalpha():
            encrypted_text += char
            if char ==" ": 
                print()
        else:
            index = alphabet.find(char)
            encrypted_text += alphabet[(index + offset) % len(alphabet)]
            print(f'{char} --> {alphabet[(index + offset) % len(alphabet)]}')
         
    print('\nDeine ursprüngliche Nachricht:\t', message)
    print('Die verschlüsselte Nachricht:\t', encrypted_text,"\n")

    if nochmalDasGanze():
        caesar_explanation()
    

