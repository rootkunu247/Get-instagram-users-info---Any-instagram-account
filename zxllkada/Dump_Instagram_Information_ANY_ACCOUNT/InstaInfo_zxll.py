from PersonalLib.Shadow import *
from PersonalLib.Fast import *
from PersonalLib.More import *
from PersonalLib.TestForPosts import *
from bs4 import BeautifulSoup
import requests
import json
import sys

######################
session = requests.Session()
######################

def AskUser(session):
    try :
        command = input (LB+"Zxll "+R+"/ "+LB+"USERNAME "+R+"> "+W)
        if command.lower() == "help" :
            print (f'{dict["Help"]}')	
            AskUser()
        elif command.lower() == "exit" :
            print (f'{BG_P} {dict["GoodBye"]} {W}')
            sys.exit()
        else :
            try :
            	DumpUser(command, session)
            except :
            	print (f'{BG_P} {command} {BG_R} NOT ON INSTAGRAM OR TOO MANY REQUESTS {W}')
            	sys.exit()
    except KeyboardInterrupt :
        print (f'{BG_P} {dict["GoodBye"]} {W}')
        sys.exit()
        
def DumpUser(User, session):
	BaseUrl = "https://www.instagram.com/"+User+"/channel"
	data = session.get(BaseUrl, headers=dict["Headers"])
	csrftoken = data.cookies["csrftoken"]
	referer = "https://www.instagram.com/"+User+"/"
	soup = BeautifulSoup(data.text, 'html.parser')
	for i in range(0, 50) :
		script = soup.find_all('script')[i]
		if isData in str(script) :
			script = soup.find_all('script')[i]
			break
	ToJson(script, csrftoken, referer, session)
	
def ToJson(Script, csrftoken, referer, session) :
	JsonFile = str(Script).split(Ghost1)[1]
	JsonFile = JsonFile.split(Ghost2)[0]
	JsonFile = json.loads(str(JsonFile))
	UserId = JsonFile["entry_data"]["ProfilePage"][0]["graphql"]["user"]["id"]
	AllData = JsonFile["entry_data"]["ProfilePage"][0]
	HasStoryIsLive(UserId, AllData, csrftoken, referer, session)
	
	
def HasStoryIsLive(UserId, Data, csrftoken, referer, session):
	try :
		QueryJson.update({"user_id": UserId})
		TargetUrl = QueryUrl+QueryHash+HashContent+QueryVariables+str(QueryJson)+FixParameter
		TargetUrl = TargetUrl.replace("'",'"')
		TargetUrl = TargetUrl.replace(" ","")
		TargetUrl = TargetUrl.replace("False","false")
		TargetUrl = TargetUrl.replace("True","true")
		try :
			data = session.get(TargetUrl, headers=dict["Headers"])
			StoryAnswer = data.json()["data"]["user"]["has_public_story"]
			LiveAnswer = data.json()["data"]["user"]["is_live"]
		except :
			StoryAnswer = "I Dont Know"
			LiveAnswer = "I Dont Know"
#		AllPosts(Data, UserId, csrftoken, referer, session)
		MirrorInfo(StoryAnswer, LiveAnswer, Data)
		
	except :
		print ("[ Error : HasPublicStoryLive ]")
		AllPosts(Data, UserId, csrftoken, referer, session)
		MirrorInfo(Failed, Failed, Data)

def main(session):
	os.system("clear")
	Screen()
	AskUser(session)
	
##############################
def MirrorInfo(StoryAnswer, LiveAnswer, Data):
	UserName = Data["graphql"]["user"]["username"]
	#### SURE FACE DATA ####
	print (f"{Y}INFO :{W}\n			{G}True{W} >>>>> Yes.\n			{G}False{W} >>>>> No.\n")
	print ("= "*25)
	print (f'{BG_G} SURE FACE DATA {W}')
	time.sleep(2)
	Username(Data["graphql"]["user"], UserName)
	FullName(Data["graphql"]["user"], UserName)
	Biography(Data["graphql"]["user"], UserName)
	ExternalUrl(Data["graphql"]["user"], UserName)
	ExternalUrlLinkshimmed(Data["graphql"]["user"], UserName)
	EdgeFollowedBy(Data["graphql"]["user"], UserName)
	EdgeFollow(Data["graphql"]["user"], UserName)
	isPrivate(Data["graphql"]["user"], UserName)
	isVerified(Data["graphql"]["user"], UserName)
	CategoryEnum(Data["graphql"]["user"], UserName)
	ProfilePicUrlHd(Data["graphql"]["user"], UserName)
	ShowSuggestedProfiles(Data, UserName)
	ShowFollowDialog(Data, UserName)
	ShowViewShop(Data, UserName)
	HighlightReelCount(Data["graphql"]["user"], UserName)
	EdgeFelixVideoTimeline(Data["graphql"]["user"], UserName)
	EdgeOwnerToTimelineMedia(Data["graphql"]["user"], UserName)
	HasClips(Data["graphql"]["user"], UserName)
	HasGuides(Data["graphql"]["user"], UserName)
	HasArEffects(Data["graphql"]["user"], UserName)
	HasChannel(Data["graphql"]["user"], UserName)
	
	####  DEEP DATA ####
	print (f'{BG_K} DEEP DATA {W}')
	time.sleep(2)
	id(Data["graphql"]["user"], UserName)
	isJoinedRecently(Data["graphql"]["user"], UserName)
	HasPublicStory(StoryAnswer, UserName)
	isLiveNow(LiveAnswer, UserName)
	OverallCategoryName(Data["graphql"]["user"], UserName)
	CategoryName(Data["graphql"]["user"], UserName)
	isBusinessAccount(Data["graphql"]["user"], UserName)
	ShouldShowCategory(Data["graphql"]["user"], UserName)
	BusinessCategoryName(Data["graphql"]["user"], UserName)
	CountryBlock(Data["graphql"]["user"], UserName)
	ToastContentOnLoad(Data, UserName)
	ProfilePicEditSyncProps(Data, UserName)
	
	####  DARK DATA ####
	print (f'{BG_R} DARK DATA {W}')
	time.sleep(2)
	LogginPageId(Data, UserName)
	Fbid(Data["graphql"]["user"], UserName)
	ConnectedFbPage(Data["graphql"]["user"], UserName)
	
# RUN
main(session)