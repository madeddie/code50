import random
import sys

from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    font = random.choices(figlet.getFonts())[0]
elif len(sys.argv) == 3:
    if sys.argv[1] not in ['-f', '--font']:
        sys.exit('Invalid option')
    else:
        if not sys.argv[2] in figlet.getFonts():
            sys.exit('Invalid font')
    font = sys.argv[2]

output_text = input('Input: ')
