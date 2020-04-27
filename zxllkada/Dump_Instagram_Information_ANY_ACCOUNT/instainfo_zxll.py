
#####################################
# BY KADA			    #
# TEXT ME FOR MORE TOOLS :	    #
#	TELEGRAM : @Ghost7_Kada     #
#	FACEBOOK : FB.COM/ZXLLL     #
#				    #
# Never use this tool for CRACKING* #
#####################################


##### COLORS #####

W = "\033[0m"
G = '\033[32;1m'
Y = '\033[33;1m'
R = '\033[31;1m'
##### LIBS #####
try :
        import requests
        import json
        import os
        import sys
        import time
except IOError as msg :
        print (R + '[!] Error import : please install libraries !!!' + W )
        print Y + '[USING]' + W + ' this command : '
        print '''
        pip3 install requests

          * USE pip2 or pip IF PIP3 DOESN'T WORKING
	  * if you need help text me on telegram @Ghost7_Kada
	  * text me on Facebook fb.com/zxlll
'''
##### I DON'T KNOW ####

user_info = []

######### INFO #########
def info():
        try :
                username = raw_input( Y + 'zxll ' + W + '/' + R + ' USERNAME : ' + W ).strip()
		print G + '[~] Username Accepted ' + W
                time.sleep(0.5)
                print R + '[~] Waiting...' + W
                time.sleep(1.3)
		url = 'https://www.instagram.com/'+username+'/?__a=1'
		print '---------------------------'
		r = requests.get(url)
		# USER INFO
		data = r.json() ["graphql"]
		info = data ["user"]

		print ( G + "PROFILE NAME : " + W + info["full_name"] )
		__profile_name__ =  'PROFILE NAME : ' + info["full_name"]
		user_info.append(__profile_name__)
		time.sleep(0.5)
		print ( G + "USERNAME : " + W + info ["username"])
		__username__ =  'USERNAME : ' + info["username"]
		user_info.append(__username__)
		time.sleep(0.5)
		print ( G + "ID : " + W + info ["id"] )
		__id__ = 'ID : ' + info["id"]
		user_info.append(__id__)
		time.sleep(0.5)
		print ( G + "BIO : " + W + info ["biography"] )
		__bio__ = 'BIO : ' + info["biography"]
		user_info.append(__bio__)
                time.sleep(0.5)
		data_followed = info ["edge_followed_by"]
		followed = data_followed ["count"]
		__followed__ = ('FOLLOWERS : ' + str (followed))
		user_info.append(__followed__)
                print '------------------'
                print Y + "FOLLOWERS : " + W, followed
                time.sleep(0.5)
                data_following = info ["edge_follow"]
		following = data_following ["count"]
		__following__ = ('FOLLOWING : ' + str (following))
		user_info.append(__following__)
                print '------------------'
                print Y + "FOLLOWING : " + W , following
                time.sleep(0.5)
                data_owner_posts = info ["edge_owner_to_timeline_media"]
                count_posts = data_owner_posts ["count"]
		__posts__ = ('POSTS : ' + str (count_posts))
		user_info.append(__posts__)
                print '------------------'
	        print Y + "POSTS : " + W , count_posts
                time.sleep(0.5)
		private = info ["is_private"]
		__private__ = ('PRIVATE : ' + str (private))
		user_info.append(__private__)
		print '------------------'
		print Y + "Private : " + W, private
		time.sleep(0.5)
		verified = info ["is_verified"]
		__verified__ = ('VERIFIED : ' + str (verified))
		user_info.append(__verified__)
		print '------------------'
		print Y + "Verified : " + W, verified
		time.sleep(0.5)
		business = info ["is_business_account"]
		__business__ = ('BUSINESS ACCOUNT : ' + str (business))
		user_info.append(__business__)
		print '------------------'
		print  Y + "Business Account : " + W, business
		print '------------------'
		time.sleep(1)
		print ( Y + '[^] SAVING ' + W)
		with open ('users/'+info["username"]+'.txt','w') as __info__ :
			for _info_ in user_info :
				__info__.write('%s\n' % _info_)
		time.sleep(0.6)
		print ( G + 'SAVED ' + W + 'users/'+info["username"]+'.txt')
		print ''
		time.sleep(0.4)
		print ( G + '[^] DONE ' + W)
		print ' '
		again = raw_input( Y + 'zxll ' + W + '/' + R + 'Another username' + W + ' Y / N  : ').strip()
		if again.lower() == "y" :
			os.system('clear')
			main()
		elif again.lower() == "n" :
			sys.exit()
		else :
			print (Y + 'FUNNY MAN ' + W )
			sys.exit()

	except IOError :
                pass
	except KeyError :
 		print ( R + '[~] USERNAME NOT FOUND' + W )
 	except ValueError :
		print ''
		print Y + 'This account have emoji I can not save it all of it' + W
 		pass
	except KeyboardInterrupt :
		print ( R + '[~] ERRORS' + W + 'something not correct try again')
                sys.exit()

###### MAIN ########
def main():
        try:
                os.system('clear')
                print Y + '''

            + - -- [ BY KADA ]
            + - -- [ v 1.0 ]
	    + - -- [ For v2.0 PRO - Telegram : @Ghost7_Kada ]
            + - -- [ Get Instagram users info ]

	//////  EXIT USER : CTRL + C + ENTER  \\\\\\

''' + W
                info()
        except IOError :
                pass
        except KeyboardInterrupt :
                sys.exit()

main()
