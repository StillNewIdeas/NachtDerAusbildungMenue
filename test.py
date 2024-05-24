import os
import sys

# Define the ASCII art as a template with placeholders for text
ascii_art_template = """
 ~-.              \  |\___/|  /              .-~
     ~-.           \ / o o \ /           .-~
        >           \\\\  W  //           <
       /             /~---~\\             \\                       {text}
      /_            |       |            _\\                       {text2}    
         ~-.        |       |        .-~                           {text3}
            ;        \\     /        i                             {text4}
           /___      /\\   /\\      ___\\
                ~-. /  \\_/  \\ .-~
                   V         V
"""

# Function to clear the console
def clear_console():
    os.system('cls')
    
# Function to display the ASCII art with custom text
def display_ascii_art(text, text2,text3,text4,):
    clear_console()
    print(ascii_art_template.format(text=text, text2=text2,text3=text3,text4=text4,))

# Initial display of the ASCII art with text
display_ascii_art("Wow, this Bat is really cool.","","","")

# Simulate updating the text (e.g., after some event or user input)
import time
time.sleep(2)  # Wait for 2 seconds
display_ascii_art("","Bats are fascinating creatures!","","")
