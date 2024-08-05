'''
		###########
		 Echo Typhoon
		###########
 	Developed by Tanvir		
		
'''

import os
import sys
import time


os.system("clear")

# Color codes
b = '\033[1m'
g = '\033[32m'
c = '\033[36m'
rs = '\033[0m'

# logo
logo = f'''{b+c}

      _______          _                       
     |__   __|        | |                      
        | |_   _ _ __ | |__   ___   ___  _ __  
        | | | | | '_ \| '_ \ / _ \ / _ \| '_ \ 
        | | |_| | |_) | | | | (_) | (_) | | | |
        |_|\__, | .__/|_| |_|\___/ \___/|_| |_|
            __/ | |                            
           |___/|_|                            
                                                                                               
      {g} 
      
     	 #############################
	  [-] Tool Name: Termux setup	 
	  [-] Developer : Tanvir               
	  [-] Team: Echo Typhoon		  
	  [-] TG: @echo_typhoon           
	 #############################
      
                         
    {rs}'''
for i in logo:
	sys.stdout.write(i)
	sys.stdout.flush()
	time.sleep(0.001)


class list:
    pkg= ["termux-setup-storage -y", 
 "apt update && apt upgrade -y", 
 "pkg install python -y", 
 "pkg install python2 -y", 
 "pkg install python3 -y", 
 "pkg install figlet -y", 
 "pkg install pip -y", 
 "pkg install pip2 -y", 
 "pkg install nano -y", 
 "pkg install wget -y", 
 "pkg install bash -y", 
 "pkg install git -y", 
 "pkg install clang -y", 
 "pkg install make -y", 
 "pkg install tar -y", 
 "pkg install zip -y", 
 "pkg install cmatrix -y", 
 "pkg install vim -y", 
 "pkg install unzip -y", 
 "pkg install sudo -y", 
 "pkg install figlet -y", 
 "apt install wget -y", 
 "apt install fonts-noto -y", 
 "apt install fontconfig -y", 
 "pkg install ruby -y", 
 "pkg install fish -y", 
 "pkg install php -y", 
 "pkg install termux-api -y", 
 "pip3 install requests", 
 "pip3 install rich", 
 "gem install lolcat", 
 "pkg update && pkg upgrade -y;apt update && apt upgrade -y"]
 
    def install(self):
       	for i in self.pkg:
                 os.system(i)

x= list()
x.install()

         