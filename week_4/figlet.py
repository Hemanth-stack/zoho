
import sys as s
import pyfiglet as pyf

try:
    if len(s.argv) == 3:
        if s.argv[1] == '-f' or s.argv[1] == '--font':
            string = input('give the text')
            pyf.print_figlet(string,font=s.argv[2])
except:
    print('Invalid usage')
    s.exit()
    
    

