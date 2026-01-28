import sys
from pyfiglet import Figlet

figlet = Figlet()

font_list = figlet.getFonts()

if len(sys.argv) == 2:
    sys.exit("Invalid usage")

elif len(sys.argv) == 3:

    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in font_list:

        text = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(text))

    else:

        sys.exit("Invalid usage")

else:
    text = input("Input: ")
    print(figlet.renderText(text))
