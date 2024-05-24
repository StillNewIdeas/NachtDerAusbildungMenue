

def caesar_explanation():
    print("Wow, hier eine voll krasse Erklärung über die Caesar verschlüsselungsmethode")



    to_encrypt = input("Gib eine Nachricht ein: \n")
    #encryption stuff
    print("Und das ist das Ergebnis: ",to_encrypt)

    print("")

    main()

def main():
    usr = ""
    while usr not in ["start", "exit"]:
        print ("start oder exit")
        usr = input("\n")
    if usr == "start":
        caesar_explanation()
        


if __name__ == "__main__": 
    main()