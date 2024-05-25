from os import system



def main():
    usr = ""
    while usr not in ["start", "exit"]:
        print ("start oder exit")
        usr = input("\n")
    if usr == "start":
        caesar_explanation()
        


if __name__ == "__main__": 
    main()