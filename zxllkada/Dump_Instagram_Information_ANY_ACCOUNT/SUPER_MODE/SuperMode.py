from SUPER_MODE.SuperLIB.login import *
from SUPER_MODE.SuperLIB.screen.screen import *
import time

# SHOW SUPER MODE BANNER
def RunBanner():
    try :
        os.system("clear || cls")
        Banner()
    except :
        print ("")
        sys.exit()

# LOG IN V1
def Login():
    LoginToInstagram()

# LOG IN V2
def LoginV2():
    LoginToInstagramV2()
    
# REDIRECT
def Redirect():
    k = 3
    for x in range(3):
        print (f" {Y}REDIRECT{W} => {k} {B}Sec{W}", end="\r")
        k -= 1
        time.sleep(1)

    os.system("clear || cls")
    RunBanner()
    MySelf()
