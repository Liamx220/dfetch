#import module as a
import platform
import distro
import psutil
import os

import sys
from termcolor import colored

distro_Printed = False
class dfetch:
    def convertTuple(self,tup):
        str =  ' '.join(tup)
        return str
    

    def printAscii(self):
        global distro_Printed 
        if distro.linux_distribution()[0] == "Pop!_OS":
    
            distro_Printed = True
            print (colored("""
/$$$$$$$                            /$$$$$$   /$$$$$$ 
| $$__  $$                          /$$__  $$ /$$__  $$
| $$  \ $$ /$$$$$$   /$$$$$$       | $$  \ $$| $$  \__/
| $$$$$$$//$$__  $$ /$$__  $$      | $$  | $$|  $$$$$$ 
| $$____/| $$  \ $$| $$  \ $$      | $$  | $$ \____  $$
| $$     | $$  | $$| $$  | $$      | $$  | $$ /$$  \ $$
| $$     |  $$$$$$/| $$$$$$$/      |  $$$$$$/|  $$$$$$/
|__/      \______/ | $$____/        \______/  \______/ 
                   | $$                                
                   | $$                                
                   |__/                                
""", 'cyan'))


        if distro.linux_distribution()[0] == "Ubuntu":
    
            distro_Printed = True
            print (colored("""
/$$   /$$ /$$                             /$$              
| $$  | $$| $$                            | $$              
| $$  | $$| $$$$$$$  /$$   /$$ /$$$$$$$  /$$$$$$   /$$   /$$
| $$  | $$| $$__  $$| $$  | $$| $$__  $$|_  $$_/  | $$  | $$
| $$  | $$| $$  \ $$| $$  | $$| $$  \ $$  | $$    | $$  | $$
| $$  | $$| $$  | $$| $$  | $$| $$  | $$  | $$ /$$| $$  | $$
|  $$$$$$/| $$$$$$$/|  $$$$$$/| $$  | $$  |  $$$$/|  $$$$$$/
\______/ |_______/  \______/ |__/  |__/   \___/   \______/ 
""", 'yellow'))


        if distro.linux_distribution()[0] == "Arch":
            distro_Printed = True
            print (colored("""

  /$$$$$$                      /$$             /$$       /$$                              
 /$$__  $$                    | $$            | $$      |__/                              
| $$  \ $$  /$$$$$$   /$$$$$$$| $$$$$$$       | $$       /$$ /$$$$$$$  /$$   /$$ /$$   /$$
| $$$$$$$$ /$$__  $$ /$$_____/| $$__  $$      | $$      | $$| $$__  $$| $$  | $$|  $$ /$$/
| $$__  $$| $$  \__/| $$      | $$  \ $$      | $$      | $$| $$  \ $$| $$  | $$ \  $$$$/ 
| $$  | $$| $$      | $$      | $$  | $$      | $$      | $$| $$  | $$| $$  | $$  >$$  $$ 
| $$  | $$| $$      |  $$$$$$$| $$  | $$      | $$$$$$$$| $$| $$  | $$|  $$$$$$/ /$$/\  $$
|__/  |__/|__/       \_______/|__/  |__/      |________/|__/|__/  |__/ \______/ |__/  \__/
""", 'blue'))

        if distro.linux_distribution()[0] == "Fedora":
            distro_Printed = True
            print (colored("""

 /$$$$$$$$              /$$                             
| $$_____/             | $$                             
| $$     /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$  /$$$$$$ 
| $$$$$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$|____  $$
| $$__/| $$$$$$$$| $$  | $$| $$  \ $$| $$  \__/ /$$$$$$$
| $$   | $$_____/| $$  | $$| $$  | $$| $$      /$$__  $$
| $$   |  $$$$$$$|  $$$$$$$|  $$$$$$/| $$     |  $$$$$$$
|__/    \_______/ \_______/ \______/ |__/      \_______/
""", 'blue'))

        if distro.linux_distribution()[0] == "Debian GNU/Linux":
            distro_Printed = True
            print (colored("""

 /$$$$$$$            /$$       /$$                    
| $$__  $$          | $$      |__/                    
| $$  \ $$  /$$$$$$ | $$$$$$$  /$$  /$$$$$$  /$$$$$$$ 
| $$  | $$ /$$__  $$| $$__  $$| $$ |____  $$| $$__  $$
| $$  | $$| $$$$$$$$| $$  \ $$| $$  /$$$$$$$| $$  \ $$
| $$  | $$| $$_____/| $$  | $$| $$ /$$__  $$| $$  | $$
| $$$$$$$/|  $$$$$$$| $$$$$$$/| $$|  $$$$$$$| $$  | $$
|_______/  \_______/|_______/ |__/ \_______/|__/  |__/
""", 'red'))

        elif platform.system() == 'Linux' and distro_Printed == False:
                
                print (colored("""

  /$$$$$$  /$$   /$$ /$$   /$$      /$$ /$$       /$$$$$$ /$$   /$$ /$$   /$$ /$$   /$$
 /$$__  $$| $$$ | $$| $$  | $$     /$$/| $$      |_  $$_/| $$$ | $$| $$  | $$| $$  / $$
| $$  \__/| $$$$| $$| $$  | $$    /$$/ | $$        | $$  | $$$$| $$| $$  | $$|  $$/ $$/
| $$ /$$$$| $$ $$ $$| $$  | $$   /$$/  | $$        | $$  | $$ $$ $$| $$  | $$ \  $$$$/ 
| $$|_  $$| $$  $$$$| $$  | $$  /$$/   | $$        | $$  | $$  $$$$| $$  | $$  >$$  $$ 
| $$  \ $$| $$\  $$$| $$  | $$ /$$/    | $$        | $$  | $$\  $$$| $$  | $$ /$$/\  $$
|  $$$$$$/| $$ \  $$|  $$$$$$//$$/     | $$$$$$$$ /$$$$$$| $$ \  $$|  $$$$$$/| $$  \ $$
 \______/ |__/  \__/ \______/|__/      |________/|______/|__/  \__/ \______/ |__/  |__/
""", 'yellow'))
    
        elif platform.system() == 'BSD' and distro_Printed == False:
            print (colored("""

 /$$$$$$$   /$$$$$$  /$$$$$$$ 
| $$__  $$ /$$__  $$| $$__  $$
| $$  \ $$| $$  \__/| $$  \ $$
| $$$$$$$ |  $$$$$$ | $$  | $$
| $$__  $$ \____  $$| $$  | $$
| $$  \ $$ /$$  \ $$| $$  | $$
| $$$$$$$/|  $$$$$$/| $$$$$$$/
|_______/  \______/ |_______/ 
""", 'red'))
    
    
    def printInfo(self):
        
        sys.stdout.write(colored("OS: ", 'red' ,attrs=['bold']))
        print(x.convertTuple(distro.linux_distribution()))
        

        sys.stdout.write(colored("OS TYPE: ", 'yellow' ,attrs=['bold']))
        print (platform.system())
        
        
        sys.stdout.write(colored("CPU ARCHITECTURE: ", 'green' ,attrs=['bold']))
        print (platform.processor())
        
        sys.stdout.write(colored("HOSTNAME: " , 'cyan' ,attrs=['bold']))
        print (platform.node())
        
        sys.stdout.write(colored("PYTHON VERSION: " , 'blue' ,attrs=['bold']))
        print (platform.python_version())

        sys.stdout.write(colored("CPU USAGE: " , 'magenta' ,attrs=['bold']))
        print(str(psutil.cpu_percent()) + "%")
        
        sys.stdout.write(colored("MEMORY USAGE: " , 'white' ,attrs=['bold']))
        print(str(psutil.virtual_memory()[2]) + "%")

        





x = dfetch()
x.printAscii()
x.printInfo()






