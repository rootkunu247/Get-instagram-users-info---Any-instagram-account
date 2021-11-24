from SCREEN.screen import *
from SCREEN.COLORS.colors import *
from SUPER_MODE.SuperMode import *
import os, sys, time


############# CHOOSE MODE ---¬
def WHICHMODE():
    os.system("clear || cls")
    Screen()

    #### MODE FROM USER ---¬
    try :
        MODE = int(input(f"[{R}!{W}] {Y}ENTER MODE TO USE : {W}").strip())
        if MODE == 1:
            print (f"[{Y}...{W}]{LB} Normal Mode Starting Soon...{W}")
            time.sleep(1)
        elif MODE == 2:
            RunBanner()
            Login()
            Redirect()
        elif MODE == 3:
            RunBanner()
            LoginV2()
            Redirect()

        else :
            print (f"{R}--> {MODE}{W} Not on list")

    except ValueError :
        print (f"{R}--> Your Input Is not a number{Y} Select Mode '1' or '2' --¬ {W}")
        sys.exit()
    except KeyboardInterrupt :
        print (f"\n[{G}×{W}] GoodBye..")
        sys.exit()




# RUN SCRIPT --> Select Mode
WHICHMODE()
