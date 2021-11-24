from SCREEN.COLORS.colors import *
import urllib.request
import os, sys, json, time
###############

dict = json.load(open("SCREEN/PACKAGES/screen.json", encoding='UTF-8'))

headers = {
	"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
	"X-requested-with" : "XMLHttpRequest",
	"Accept" : "*/*",
	"Content-type" : "application/json; charset=utf-8"
}



def Flush(Which, Color1, Color2, SleepTime1, SleepTime2):
    for char in Which :
        sys.stdout.write(Color1+char+Color2)
        sys.stdout.flush()
        time.sleep(SleepTime1)
    time.sleep(SleepTime2)

def connect():
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False

def main():
    Flush(dict["IN_OR_OUT"]["IN"], BG_G, W, 0.05, 0.3)
    os.system('clear || cls')
    Banner()

def FalseMain():
    Flush(dict["IN_OR_OUT"]["OUT"], BG_R, W, 0.05, 1)
    print ("                        ", end="\r")
    print (BG_R+dict["IN_OR_OUT"]["OUT"]+W, end="\r")
    Flush(dict["IN_OR_OUT"]["OUT_CHALLENGE"]+" ", Y, W, 0.1, 0)
    Flush(" "+dict["TO_HELP"]["TRY"]+" \n", BG_R, W, 0.1, 0)
    sys.exit()

def Banner():
    Flush("\n\n	     "+dict["DRAWS"]["DRAW_1"]["STEP_1"], Y, W, 0.03, 0)
    Flush("             "+dict["DRAWS"]["DRAW_1"]["STEP_2"], Y, W, 0.03, 0)
    Flush("             "+dict["DRAWS"]["DRAW_1"]["STEP_3"], Y, W, 0.03, 0)
    Flush("             "+dict["DRAWS"]["DRAW_1"]["STEP_4"]+"\n", Y, W, 0.03, 0)
    Flush("        "+dict["DRAWS"]["DRAW_1"]["STEP_5"], Y, W, 0.03, 0)
    Flush("	"+dict["DRAWS"]["DRAW_2"]["STEP_1"], LB, W, 0.03, 0)
    Flush("	"+dict["DRAWS"]["DRAW_2"]["STEP_2"], LB, W, 0.03, 0)
    Flush("		"+dict["DRAWS"]["DRAW_3"], B, W, 0.03, 0)

    Flush("   "+dict["MODES"]["MODE_1"], G, W, 0.03, 0)
    Flush("   "+dict["MODES"]["MODE_2"], G, W, 0.03, 0)
    Flush("   "+dict["MODES"]["MODE_3"]+"\n", G, W, 0.03, 0)

def Screen():
    os.system('clear || cls')

    try :
        Flush(dict["TO_HELP"]["SPACES"]*14, W, W, 0.01, 0)
        Flush("		"+dict["WELCOME_SCREEN"]["FIRSTMSG"]+"\n", B, W, 0.05, 0.1)
        Flush("		"+dict["WELCOME_SCREEN"]["SECONDMSG"], B, W, 0.05, 0.5)
        Flush(" "+dict["WELCOME_SCREEN"]["ANSWER"], G, W, 0.03, 0)
        Flush(dict["TO_HELP"]["SPACES"]*4, W, W, 0.01, 0)

        connect()
        if connect() :
            main()
        else :
            FalseMain()
    except :
        sys.exit()

