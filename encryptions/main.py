from os import system
from time import sleep

def nochmalDasGanze():
    print('Möchtest du eine weitere Nachricht verschlüssel?')
    usr = ""
    while usr not in ["j","n"]:
        try:
            usr = input('j/n: ')
        except KeyboardInterrupt:
            print("Keine gültige Eingabe")
                
    if usr == 'j':
        return True
    else:
        return False 

def main():
    while True: 
        system("cls")
        print('\n\t\t\t\t\t\t###############################')
        print('\t\t\t\t\t\t# Lecos Verschlüsselungs-Tour #')
        print('\t\t\t\t\t\t###############################')
        print('\t\t\t\t\t\t#          1. Caesar          #')
        print('\t\t\t\t\t\t#          2. Atbash          #')
        print('\t\t\t\t\t\t#          3. Vigenere        #')
        print('\t\t\t\t\t\t###############################\n')
        
        chooseEncryption()

def chooseEncryption():
        print('Gib die Nummer der Verschlüsselung ein, die du kennenlernen möchtest.')
        usr = ""
        while usr not in ["1", "2","3"]:
            try:
                usr = input()
            except KeyboardInterrupt:
                print("Keine gültige Eingabe")
        if usr == "1":
            from caesar import caesar_explanation
            caesar_explanation()
            
        elif usr == "2":
            from atbash import atbash_explanation
            atbash_explanation()
            
        else:
            from vigenere import vigenere_explanation
            vigenere_explanation()
            
        
        system("cls")

        


if __name__ == "__main__": 
    main()