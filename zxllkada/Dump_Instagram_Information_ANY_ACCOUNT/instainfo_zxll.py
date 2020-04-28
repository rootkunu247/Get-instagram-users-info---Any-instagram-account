
#####################################
# BY KADA			    #
# TEXT ME FOR MORE TOOLS :	    #
#       TELEGRAM : @Ghost7_Kada     #
#       FACEBOOK : FB.COM/ZXLLL     #
#                                   #
# Never use this tool for CRACKING* #
#####################################

##### COLORS #####

W = "\033[0m"
G = '\033[32;1m'
Y = '\033[33;1m'
R = '\033[31;1m'

##### LIBS #####
import os, sys, time
try :
    import json
    import requests
    from urllib.request import urlopen
except IOError as msg :
    print ( R + "[!] Error import : please install libraries !!!" + W )
    print ( Y + "[USING]" + W + " This Commands" )
    print ( '''
        pip3 install requests

          * USE pip2 or pip IF PIP3 DOESN'T WORKING
          * if you need help text me on telegram @Ghost7_Kada
          * text me on Facebook fb.com/zxlll
''')
##### I DON NOT KNOW #####

user_info = []
user_img_info = []

##### DUNPS #####
def info():
    try :
        username = input( Y + "zxll " + W + "/" + R + " USERNAME : " + W ).strip()
        print ( G + "[~] Username Accepted " + W )
        time.sleep(0.5)
        print ( R + "[~] Waiting..." + W )
        time.sleep(1.5)
        # GET USER DATA
        url = 'https://www.instagram.com/'+username+'/?__a=1'
        r = requests.get(url)
        data = r.json() ["graphql"]
        info = data ["user"]
        # CREATE FOLDER FOR USER
        ___user_local___ = info ["username"]
        ___media___ = "media"
        os.system('mkdir '+'users/'+___user_local___)
        os.system('mkdir '+'users/'+___user_local___+"/"+___media___)
        print ( G + '[~] USER FOLDER CREATED ' + W )
        ___user_folder___ = ___user_local___
        time.sleep(1)
        print ( '---------------------------' )
        # GET PROFILE NAME
        print ( G + "[ PROFILE NAME ] : " + W + info["full_name"] )
        __profile_name__ =  'PROFILE NAME : ' + info["full_name"]
        user_info.append(__profile_name__)
        time.sleep(1.2)
        # GET USERNAME
        print ( G + "[ USERNAME ] : " + W + info ["username"])
        __username__ =  'USERNAME : ' + info["username"]
        user_info.append(__username__)
        time.sleep(1.2)
        # GET ID
        print ( G + "[ ID ] : " + W + info ["id"] )
        __id__ = 'ID : ' + info["id"]
        user_info.append(__id__)
        time.sleep(1.2)
        # GET BIO
        print ( G + "[ BIO ] : " + W + info ["biography"] )
        __bio__ = 'BIO : ' + info["biography"]
        user_info.append(__bio__)
        time.sleep(1.2)
        # GET FOLLOWERS
        data_followed = info ["edge_followed_by"]
        followed = data_followed ["count"]
        __followed__ = ('FOLLOWERS : ' + str (followed))
        user_info.append(__followed__)
        print ( Y + "[ FOLLOWERS ] : " + W, followed)
        time.sleep(1.2)
        # GET FOLLOWING
        data_following = info ["edge_follow"]
        following = data_following ["count"]
        __following__ = ('FOLLOWING : ' + str (following))
        user_info.append(__following__)
        print ( Y + "[ FOLLOWING ] : " + W , following)
        time.sleep(1.2)
        # GET POSTS
        data_owner_posts = info ["edge_owner_to_timeline_media"]
        count_posts = data_owner_posts ["count"]
        __posts__ = ('POSTS : ' + str (count_posts))
        user_info.append(__posts__)
        print ( Y + "[ POSTS ] : " + W , count_posts)
        time.sleep(1.2)
        # GET IS PRIVATE
        private = info ["is_private"]
        __private__ = ('PRIVATE : ' + str (private))
        user_info.append(__private__)
        print ( Y + "[ Private ] : " + W, private )
        time.sleep(1.2)
        # GET IS VERIFIED
        verified = info ["is_verified"]
        __verified__ = ('VERIFIED : ' + str (verified))
        user_info.append(__verified__)
        print ( Y + "[ Verified ] : " + W, verified )
        time.sleep(1.2)
        # GET IS BUSINESS ACCOUNT
        business = info ["is_business_account"]
        __business__ = ('BUSINESS ACCOUNT : ' + str (business))
        user_info.append(__business__)
        print ( Y + "[ BUSINESS ACCOUNT ] : " + W, business )
        print ( '---------------------------' )
        time.sleep(1)
        # GET PROFILE PIC AND SAVE
        req_img_hd = requests.get(info["profile_pic_url_hd"])
        img_file = open ("users/"+info["username"]+"/"+___media___+"/"+___user_local___+"'s_profile_pic.png","wb")
        img_file.write(req_img_hd.content)
        img_file.close()
        # GET PIC INFO
        url = info["profile_pic_url_hd"]
        run_url = urlopen(url)
        img_info = run_url.info()
        r = img_info["Content-Length"]
        mb = 0.000001
        size_mb = int(r)*mb
        print ( Y + "[ GET PROFILE PIC WITH INFO ] : " + W )
        time.sleep(2)
        print ( G + "        |" + W )
        print ( G + "        ’＿＿ [ DONE ]" + W )
        time.sleep(1.4)
        print ( G + "        、 " + W + Y + "[ LAST MODIFIED ] : " + W + img_info["Last-Modified"] )
        time.sleep(1.7)
        print ( G + "        、 " + W + Y + "[ CONTENT TYPE ] : " + W + img_info["Content-Type"] )
        time.sleep(1.9)
        print ( G + "        、 " + W + Y + "[ SIZE ] : " + W + img_info["Content-Length"],"Byte" )
        time.sleep(1.2)
        print ( G + "        、 " + W + Y + "[ SIZE ] : " + W + ("%.2f" % size_mb), "MB" )
        time.sleep(1.2)
        print ( G + "        、 " + W + Y + "[ DATE ] : " + W + img_info["Date"])
        time.sleep(2)
        # SAVE IMG INFO WITH PIC
        last_modified = img_info["Last-Modified"]
        __last_modified__ = 'LAST MODIFIED : ' + last_modified
        user_img_info.append(__last_modified__)
        content_type = img_info["Content-Type"]
        __content_type__ = 'CONTENT TYPE : '+ str (content_type)
        user_img_info.append(__content_type__)
        content_length = img_info["Content-Length"]
        __content_length__ = 'SIZE : ' + str (content_length) + "byte"
        user_img_info.append(__content_length__)
        __size__ = 'SIZE As MB : ' + str (("%.2f" % size_mb)) + "MB"
        user_img_info.append(__size__)
        date = img_info["Date"]
        __date__ = 'YOU GET THIS INFO AT : ' + str (date)
        user_img_info.append(__date__)
        # SAVING
        print ("")
        print ( Y + '[^] SAVING ' + W )
        with open ('users/'+info["username"]+'/'+info["username"]+'.txt','w', encoding="utf-8") as user_file :
                for info in user_info :
                        user_file.write('%s\n' % info)
                user_file.close()

        with open ("users/"+___user_local___+"/"+___media___+"/"+"PIC_INFO.txt",'w') as pic_info :
                for _info_ in user_img_info :
                        pic_info.write('%s\n' % _info_)
                pic_info.close()
        time.sleep(1)
        print ( " " )
        print ( Y + '[ + -- - ]' + W + ' PROFILE INFO' + G + ' SAVED ' + W )
        time.sleep(2)
        print ( Y + '[ + -- - ]' + W + ' PROFILE PIC' + G + ' SAVED ' + W )
        time.sleep(2)
        print ( Y + '[ + -- - ]' + W + ' PIC INFO' + G + ' SAVED ' + W )
        time.sleep(2)
        info_pwd = 'users/'+___user_folder___+'/'+___user_local___+'.txt'
        pic_pwd = "users/"+___user_local___+"/"+___media___+"/"+___user_local___+"'s_profile_pic.png"
        pic_info_pwd = "users/"+___user_local___+"/"+___media___+"/"+"PIC_INFO.txt"
        print ( " " )
        time.sleep(0.3)
        print ( Y + "LOCAL :" + W )
        print ( " " )
        time.sleep(0.5)
        print ( G + "PROFILE INFO : " + W + info_pwd )
        time.sleep(0.5)
        print ( G + "PROFILE PIC : " + W + pic_pwd )
        time.sleep(0.5)
        print ( G + "PIC INFO : " + W + pic_info_pwd )
        time.sleep(0.4)
        print ( " " )
        print ( G + '[^] DONE ' + W )
        print ( " " )
        again = input( Y + 'zxll ' + W + '/' + R + 'Another username' + W + ' Y / N  : ').strip()
        if again.lower() == "y" :
                os.system('clear')
                user_info.clear()
                user_img_info.clear()
                main()
        elif again.lower() == "n" :
                sys.exit()
        else :
                print ( Y + 'FUNNY MAN ' + W )
                sys.exit()
    except KeyError :
        print ( R + '[~] USERNAME NOT FOUND' + W )
        time.sleep(1.5)
        main()
    except json.decoder.JSONDecodeError :
        print ( R + '[~] JSON DECODE ERROR-- ' + W + 'AM Not Sure What The Fuck Is THAT' )
        time.sleep(4)
        main()
    except KeyboardInterrupt :
        sys.exit()
    except IOError :
        print ( "ERRORS " )
        pass

##### MAIN #####
def main():
    try :
        os.system('clear')
        print ( Y + '''

            + - -- [ BY KADA ]
            + - -- [ v 1.0 ]
            + - -- [ For v2.0 PRO - Telegram : @Ghost7_Kada ]
            + - -- [ Get Instagram users info ]

        //////  EXIT USE : CTRL + C + ENTER  \\\\\\

''' + W )
        info()
    except IOError :
        pass
    except KeyboardInterrupt :
        sys.exit()
#################################### FINISHED
###############################
#########################
###################
#############
#######
################# LUNCHING
main()
