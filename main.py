from os import system
# Define Asciis


def print()

def caesar_explanation():
    print("Die Caesar-Verschlüsselung ist ein einfaches Verschlüsselungsverfahren, \nbei dem jeder Buchstabe im Klartext um eine feste Anzahl \nvon Stellen im Alphabet verschoben wird. \nZum Beispiel, bei einer Verschiebung um 3: \nA -> D, \nB -> E,\nC -> F.")

    to_encrypt = input("Gib eine Nachricht ein: \n")
    #Faktor selbst eingeben
    print("Für diese Verschlüsselung wird jetzt mit dem Faktor 10 verschlüsselt.")
    n=10
    ans = ""
    for i in range(len(to_encrypt)):
        ch = to_encrypt[i]
        
        # check if space is there then simply add space
        if ch==" ":
            ans+=" "
        # check if a character is uppercase then encrypt it accordingly 
        elif (ch.isupper()):
            print(ch, "wird zu", chr((ord(ch) + n-65) % 26 + 65))
            ans += chr((ord(ch) + n-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        
        else:
            print(ch, "wird zu", chr((ord(ch) + n-97) % 26 + 97))
            ans += chr((ord(ch) + n-97) % 26 + 97)
    
        
    print("Und das ist das Ergebnis: ",ans)

    print("\n\n")

    main()

def main():
    usr = ""
    while usr not in ["1", "2"]:
        print ("#######################")
        print ("# LECOS Lama Tour über die Verschlüsselungs-Wiese #")
        print ("# 1. Start #")
        print ('# 2. Exit # ')
        print ("#######################")
        print()
        usr = input("Deine Nummer: ")
    if usr == "1":
        caesar_explanation()
        


if __name__ == "__main__": 
    main()