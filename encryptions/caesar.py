
def caesar_explanation():
    print('''Die Caesar-Verschlüsselung ist ein einfaches Verschlüsselungsverfahren,
bei dem jeder Buchstabe im Klartext um eine feste Anzahl von Stellen im Alphabet
verschoben wird. 
Zum Beispiel, bei einer Verschiebung um 3:
        
    A -> D
    B -> E
    C -> F
    
    ''')

def caesar_example(message):
    print("Gib eine Nachricht ein: \n")
    message = input("> ")
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


caesar_explanation()