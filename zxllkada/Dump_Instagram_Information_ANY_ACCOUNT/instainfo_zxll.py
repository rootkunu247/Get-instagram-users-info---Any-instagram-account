from PersonalLib.Total import JoinedWork as AgeDef
from PersonalLib.Total import GetData as TotalDef
from PersonalLib.Total import Location as LocationDef
import urllib.request
import json
import sys
import os
import time

########### I DON'T KNOW

W = "\033[0m"
G = '\033[32;1m'
Y = '\033[33;1m'
R = '\033[31;1m'
B = '\033[1;34;40m'
LB = '\033[1;36;40m'
BG_R = '\033[0;37;41m'
BG_G = '\033[0;37;42m'
BG_P = '\033[0;37;44m'
BG_K = '\033[0;37;45m'

###########

try :
    import requests
    from igql import InstagramGraphQL
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install igql')
    print (G+"[~]"+BG_P+" OPEN THE TOOL AGAIN "+W)
    sys.exit()

###########

dict = {
	"FirstMsg" :   "		Welcome Here\n		How Are You Doing ? ",
	"Answer" : " I Hope You're Good",
	"Spaces" : "\n",
	"No Internet" : " You Are Not Connected ",
	"Check" : "You Must Be Connected With Internet ",
	"Connected" : "You Are Connected\n",
	"Try" : "Try Again\n",
	"GoodBye" : "[~] See You Later ",
	"IK" : '"',
	"Help" : '''
	 ----------------------------------------------------
	| Command                | For What                  |
	 ----------------------------------------------------
	| Help                   | Show Help Table           |
	······················································
	| CTRL + C + ENTER       | EXIT FROM THE TOOL        |
	······················································
	| Exit                   | EXIT FROM THE TOOL	     |
	······················································
        | Enter A Username       | Dump All User Information |
	 ----------------------------------------------------

''',
	"Draw" : '''
	##        ###        ##
	###      #####      ###
	####    #######    ####
	#######################
	#######################  + - -- [ BY KADA ]
	###      #####      ###  + - -- [ BEGINNERS VERISION ]
	###  @@  #####  @@  ###  + - -- [ V 13.7 ]
	###      #####      ###  + - -- [ Get Instagram Users Info ]
	#######################  [!] FOR HELP ENTER : Help 
	#######################

''',
	"Target" : {
		  	 "USERNAME" : "",
		   },
	"Headers" :   {
		 	 "content-type" : "application/json",
			 "User-agent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 Instagram 50.0.0.52.188 (iPhone7,2; iOS 11_4_1; es_CO; es; scale=2.00; gamut=normal; 750x1334",
		   }
}

# MAIN
def main():
    for char in dict["Connected"] :
        sys.stdout.write(BG_G+char+W)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(0.3)
    os.system('clear')
    Banner()

# FALSE MAIN
def FalseMain():
    for char in dict["No Internet"] :
        sys.stdout.write(BG_R+char+W)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    print ("                        ", end="\r")
    print (BG_R+dict["No Internet"]+W, end="\r")
    for char in dict["Check"] :
        sys.stdout.write(Y+char+W)
        sys.stdout.flush()
        time.sleep(0.1)
    for char in dict["Try"] :
        sys.stdout.write(BG_R+char+W)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.exit()

# FLUSH
def Flush(Which):
    for char in Which :
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(1)

# DUMP
class DumpFromJsonFile :
    USERNAME = ""


    def GetUser(self):
        URL = 'https://www.instagram.com/'+self.USERNAME+'/?__a=1'
        req = requests.get(url=URL, headers=dict["Headers"])
        data = req.json()
        STORY_URL = 'https://www.instagram.com/graphql/query/?query_hash=c9100bf9110dd6361671f113dd02e7d6&variables={'+dict["IK"]+'user_id'+dict["IK"]+':'+dict["IK"]+data["graphql"]["user"]["id"]+dict["IK"]+','+dict["IK"]+'include_reel'+dict["IK"]+':true,'+dict["IK"]+'include_logged_out_extras'+dict["IK"]+':true}'
        req_story = requests.get(url=STORY_URL, headers=dict["Headers"])
        story = req_story.json() ["data"]["user"]["has_public_story"]


        print (BG_R+" EXTRACTING DATA FROM : "+BG_P+" ", end='')
        Flush((data["graphql"]["user"]["username"]).upper())
        print (' '+W)
        # SUREFACE DATA
        print (BG_G+"、SURFACE DATA "+W)
        print (Y+"	、__ [~] "+LB+"FULL NAME : "+W, end='')
        Flush(data["graphql"]["user"]["full_name"])
        print ('')
        print (Y+"	、__ [~] "+LB+"PRIVATE ACCOUNT : "+W, end='')
        Flush(str(data["graphql"]["user"]["is_private"]))
        print ('')
        print (Y+"	、__ [~] "+LB+"VERIFIED ACCOUNT : "+W, end='')
        Flush(str(data["graphql"]["user"]["is_verified"]))
        print ('')
        print (Y+"	、__ [~] "+LB+"BUSINESS ACCOUNT : "+W, end='')
        Flush(str(data["graphql"]["user"]["is_business_account"]))
        print ('')
        try :
            print (Y+"		 、__ [~] "+LB+"BUSINESS CATEGORY NAME : "+W, end='')
            Flush(str(data["graphql"]["user"]["business_category_name"]))
            print ('')
        except :
            pass
        print (Y+"	、__ [~] "+LB+"SHOW SUGGESTED PROFILES : "+W, end='')
        Flush(str(data["show_suggested_profiles"]))
        print ('')
        print (Y+"	、__ [~] "+LB+"SHOW VIEW SHOP : "+W, end='')
        Flush(str(data["show_view_shop"]))
        print ('')
        print (Y+"	、__ [~] "+LB+"SHOW ACCOUNT CATEGORY : "+W, end='')
        Flush(str(data["graphql"]["user"]["should_show_category"]))
        print ('')
        # NOT YET
        print (Y+"		 、__ [~] "+LB+"ACCOUNT CATEGORY NAME : "+W, end='')
        Flush("It can't be known right now.")
        print ('')
        #########
        print (Y+"	、__ [~] "+LB+"BIO : "+W, end='')
        Flush(data["graphql"]["user"]["biography"])
        print ('')
        try :
            print (Y+"	、__ [~] "+LB+"LINK IN BIO : "+W, end='')
            Flush(data["graphql"]["user"]["external_url"])
            print ('')
            print (Y+"	、__ [~] "+LB+"INSIDE THIS LINK : "+W, end='')
            Flush(data["graphql"]["user"]["external_url_linkshimmed"])
        except :
            pass
        print ('')
        print (Y+"	、__ [~] "+LB+"POSTS COUNT : "+W, end='')
        Flush(str(data["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]))
        print ('')
        print (Y+"	、__ [~] "+LB+"FELIX VIDEOS COUNT : "+W, end='')
        Flush(str(data["graphql"]["user"]["edge_felix_video_timeline"]["count"]))
        print ('')
        print (Y+"	、__ [~] "+LB+"FOLLOWERS COUNT : "+W, end='')
        Flush(str(data["graphql"]["user"]["edge_follow"]["count"]))
        print ('')
        print (Y+"	、__ [~] "+LB+"FOLLOWING COUNT : "+W, end='')
        Flush(str(data["graphql"]["user"]["edge_followed_by"]["count"]))
        print ('')
        print (Y+"	、__ [~] "+LB+"HIGHLIGHT REEL COUNT : "+W, end='')
        Flush(str(data["graphql"]["user"]["highlight_reel_count"]))
        print ('')
        print (Y+"	、__ [~] "+LB+"HAS PUBLIC STORY : "+W, end='')
        Flush(str(story))
        print ('')
        print (Y+"	、__ [~] "+LB+"HAS AR EFFECTS : "+W, end='')
        Flush(str(data["graphql"]["user"]["has_ar_effects"]))
        print ('')
        print (Y+"	、__ [~] "+LB+"HAS CLIPS : "+W, end='')
        Flush(str(data["graphql"]["user"]["has_clips"]))
        print ('')
        print (Y+"	、__ [~] "+LB+"HAS GUIDES : "+W, end='')
        Flush(str(data["graphql"]["user"]["has_guides"]))
        print ('')
        print (Y+"	、__ [~] "+LB+"HAS CHANNEL : "+W, end='')
        Flush(str(data["graphql"]["user"]["has_channel"]))
        print ('')

        # DEEP DATA
        print (BG_K+"、DEEP DATA "+W)
        print (Y+"	、__ [~] "+LB+"LOGGING PAGE ID : "+W, end='')
        Flush(str(data["logging_page_id"]))
        print ('')
        print (Y+"	、__ [~] "+LB+"ID : "+W, end='')
        Flush(data["graphql"]["user"]["id"])
        print ('')

        # ALL LIKES AND COMMENTS
        print (Y+"		、__ [~] "+LB+"TOTAL LIKES AND COMMENTS ON ALL ACCOUNT POSTS : "+W)
        print ("		"+BG_P+" START THE CALCULATION "+W)
        try :
            TotalDef(data["graphql"]["user"]["username"])
        except :
            print ("                	"+BG_R+" [!] WIRNING : "+"CALCUATION FAILD"+W)
            pass
        print ("		"+BG_G+" FINISH THE CALCULATION "+W)

        # DARK DATA
        print (BG_R+"、DARK DATA "+W)
        print (Y+"	、__ [~] "+LB+"IS JOINED RECENTLY : "+W, end='')
        Flush(str(data["graphql"]["user"]["is_joined_recently"]))
        print ('')
        print (Y+"	、__ [~] "+LB+"ACCOUNT AGE : "+W)
        print (Y+"	"+BG_P+"LOOKING FOR ACCOUNT AGE "+W)
        try :
            AgeDef()
        except :
            print ("		"+BG_R, end='')
            Flush(" Can't See It Right Now. ")
        print (W+'')
        print (Y+"	、__ [~] "+LB+"FB ID : "+W, end='')
        Flush(str(data["graphql"]["user"]["fbid"]))
        print ('')
        print (Y+"	、__ [~] "+LB+"COUNTRY BLOCK : "+W, end='')
        Flush(str(data["graphql"]["user"]["country_block"]))
        print ('')

        #####
        print (Y+"	、__ [~] "+LB+"EMAIL : "+W, end='')
        Flush("It can't be known right now.")
        print ('')
        print (Y+"	、__ [~] "+LB+"PHONE : "+W, end='')
        Flush("It can't be known right now.")
        print ('')
        #####

        print (Y+"	   、__ [~] "+LB+"LOCATIONS : "+W)
        try :
            LocationDef()
        except :
            print (Y+"	      、__ [~] "+LB+"LOCATIONS : "+W, end='')
            Flush("No Locations Right Now.")
        print ('')

# ASK
def Ask():
    try :
        command = input (LB+"Zxll "+R+"/ "+LB+"USERNAME "+R+"> "+W)
        if command.lower() == "help" :
            print (dict["Help"])
            Ask()
        elif command.lower() == "exit" :
            print (BG_P+dict["GoodBye"]+W)
            sys.exit()
        else :
            dict["Target"]["USERNAME"] = command
            GetAll = DumpFromJsonFile()
            GetAll.USERNAME = dict["Target"]["USERNAME"]
            GetAll.GetUser()
    except KeyboardInterrupt :
        print (BG_P+dict["GoodBye"]+W)
        sys.exit()

# BANNER
def Banner():
    for char in dict["Draw"] :
        sys.stdout.write(BG_P+char+W)
        sys.stdout.flush()
        time.sleep(0.03)
    Ask()

# CHECK INTERNET
def connect():
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False

# SCREEN
def Screen():
    os.system('clear')
    for space in dict["Spaces"]*14 :
        sys.stdout.write(space)
        sys.stdout.flush()
        time.sleep(0.01)
    for char in dict["FirstMsg"] :
        sys.stdout.write(B+char+W)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(0.5)
    for char in dict["Answer"] :
        sys.stdout.write(G+char+W)
        sys.stdout.flush()
        time.sleep(0.1)
    for space in dict["Spaces"]*4 :
        sys.stdout.write(space)
        sys.stdout.flush()
        time.sleep(0.01)
    connect()
    if connect() :
        main()
    else :
        FalseMain()
# RUN
Screen()
