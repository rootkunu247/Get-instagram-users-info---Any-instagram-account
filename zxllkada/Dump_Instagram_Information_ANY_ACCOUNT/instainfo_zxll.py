
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

##### DUNPS #####
def info():
    try :
        username = input( Y + "zxll " + W + "/" + R + " USERNAME : " + W ).strip()
        print ( G + "[~] Username Accepted " + W )
        time.sleep(0.5)
        print ( R + "[~] Waiting..." + W )
        time.sleep(1.5)
        url = 'https://www.instagram.com/'+username+'/?__a=1'
        r = requests.get(url)
        data = r.json() ["graphql"]
        info = data ["user"]
        # USER INFO DUMPED
        ___user_local___ = info ["username"]
        print ( '---------------------------' )
        # GET PROFILE NAME
        print ( G + "PROFILE NAME : " + W + info["full_name"] )
        __profile_name__ =  'PROFILE NAME : ' + info["full_name"]
        user_info.append(__profile_name__)
        time.sleep(0.5)
        # GET USERNAME
        print ( G + "USERNAME : " + W + info ["username"])
        __username__ =  'USERNAME : ' + info["username"]
        user_info.append(__username__)
        time.sleep(0.5)
        # GET ID
        print ( G + "ID : " + W + info ["id"] )
        __id__ = 'ID : ' + info["id"]
        user_info.append(__id__)
        time.sleep(0.5)
        # GET BIO
        print ( G + "BIO : " + W + info ["biography"] )
        __bio__ = 'BIO : ' + info["biography"]
        user_info.append(__bio__)
        time.sleep(0.5)
        # GET FOLLOWERS
        data_followed = info ["edge_followed_by"]
        followed = data_followed ["count"]
        __followed__ = ('FOLLOWERS : ' + str (followed))
        user_info.append(__followed__)
        print ( '------------------' )
        print ( Y + "FOLLOWERS : " + W, followed)
        time.sleep(0.5)
        # GET FOLLOWING
        data_following = info ["edge_follow"]
        following = data_following ["count"]
        __following__ = ('FOLLOWING : ' + str (following))
        user_info.append(__following__)
        print ( '------------------' )
        print ( Y + "FOLLOWING : " + W , following)
        time.sleep(0.5)
        # GET POSTS
        data_owner_posts = info ["edge_owner_to_timeline_media"]
        count_posts = data_owner_posts ["count"]
        __posts__ = ('POSTS : ' + str (count_posts))
        user_info.append(__posts__)
        print ( '------------------' )
        print ( Y + "POSTS : " + W , count_posts)
        time.sleep(0.5)
        # GET IS PRIVATE
        private = info ["is_private"]
        __private__ = ('PRIVATE : ' + str (private))
        user_info.append(__private__)
        print ( '------------------' )
        print ( Y + "Private : " + W, private )
        time.sleep(0.5)
        # GET IS VERIFIED
        verified = info ["is_verified"]
        __verified__ = ('VERIFIED : ' + str (verified))
        user_info.append(__verified__)
        print ( '------------------' )
        print ( Y + "Verified : " + W, verified )
        time.sleep(0.5)
        # GET IS BUSINESS ACCOUNT
        business = info ["is_business_account"]
        __business__ = ('BUSINESS ACCOUNT : ' + str (business))
        user_info.append(__business__)
        print ( '------------------' )
        time.sleep(1)
        print ( Y + '[^] SAVING ' + W )
        with open ('users/'+info["username"]+'.txt','w', encoding="utf-8") as user_file :
                for info in user_info :
                        user_file.write('%s\n' % info)
                user_file.close()
        time.sleep(0.6)
        local = 'users/'+___user_local___+'.txt'
        print ( G + 'SAVED ' + W + local )
        print ( " " )
        time.sleep(0.4)
        print ( G + '[^] DONE ' + W )
        print ( " " )
        again = input( Y + 'zxll ' + W + '/' + R + 'Another username' + W + ' Y / N  : ').strip()
        if again.lower() == "y" :
                os.system('clear')
                user_info.remove()
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
        time.sleep(1.5)
        main()
    except KeyboardInterrupt :
        print ( R + '[~] ERRORS' + W + 'something not correct try again')
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
