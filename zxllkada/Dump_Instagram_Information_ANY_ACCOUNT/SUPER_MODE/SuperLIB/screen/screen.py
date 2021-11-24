from SUPER_MODE.SuperLIB.screen.COLORS.colors import *
import os, sys, json, time


dict = json.load(open("SUPER_MODE/SuperLIB/screen/PACKAGES/screen.json"))
os.system("clear || cls")

def Flush(Which, Color1, Color2, SleepTime1, SleepTime2):
    for char in Which :
        sys.stdout.write(Color1+char+Color2)
        sys.stdout.flush()
        time.sleep(SleepTime1)
    time.sleep(SleepTime2)

def Banner():
    Flush("\n\n             "+dict["DRAWS"]["DRAW_1"]["STEP_1"], Y, W, 0, 0)
    Flush("             "+dict["DRAWS"]["DRAW_1"]["STEP_2"], Y, W, 0, 0)
    Flush("             "+dict["DRAWS"]["DRAW_1"]["STEP_3"], Y, W, 0, 0)
    Flush("             "+dict["DRAWS"]["DRAW_1"]["STEP_4"]+"\n", Y, W, 0, 0)
    Flush("     "+dict["DRAWS"]["DRAW_2"]["STEP_1"], G, W, 0.01, 0)
    Flush("     "+dict["DRAWS"]["DRAW_2"]["STEP_2"], G, W, 0.01, 0)
    Flush("     "+dict["DRAWS"]["DRAW_2"]["STEP_3"], G, W, 0.01, 0)
    Flush("     "+dict["DRAWS"]["DRAW_2"]["STEP_4"], G, W, 0.01, 0)
    Flush("     "+dict["DRAWS"]["DRAW_2"]["STEP_5"], G, W, 0.01, 0)
    Flush("     Super Mode is running !\n", LB, W, 0.02, 0)

