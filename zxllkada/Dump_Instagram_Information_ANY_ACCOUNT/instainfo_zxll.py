
#####################################
# BY KADA			    #
# TEXT ME FOR MORE TOOLS :	    #
#       TELEGRAM : @Zkada           #
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
except IOError :
    print ( R + "[!] SOMETHING NOT CORRECT " + W + "TRY AGAIN " )
except ImportError :
    print ( R + "[!] Error import : please install libraries !!!" + W )
    os.system('pip2 install -r requirements.txt')
    print ( G + "[^-^] I HOPE IT IS FIXED TRY TO OPEN IT" + W )
except KeyboardInterrupt :
    print ( R + "[!] ERRORS : " + W + "Try again" )
    sys.exit()

##### I DON NOT KNOW #####

user_info = []
user_img_info = []
last_post = []
a = " None"

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
        ___media_posts__ = "last_post_INFO"
        os.system('mkdir '+'users/'+___user_local___)
        os.system('mkdir '+'users/'+___user_local___+"/"+___media___)
        os.system('mkdir '+'users/'+___user_local___+"/"+___media___+"/"+___media_posts__)
        print ( G + '[~] USER FOLDER CREATED ' + W )
        ___user_folder___ = ___user_local___
        time.sleep(1)
        print ( '-----------------------' )
        # GET PROFILE NAME
        print ( G + "[ PROFILE NAME ] : " + W + info["full_name"] )
        __profile_name__ =  'PROFILE NAME : ' + info["full_name"]
        user_info.append(__profile_name__)
        time.sleep(1.2)
        # GET MORE INFO
        print ( G + "        |" + W )
        print ( G + "        ’＿＿ [ MORE INFO ] " + W )
        time.sleep(2)
        print ( G + "        、 " + Y + "[ LOGGING PAGE ID ] : " + W + r.json() ["logging_page_id"] )
        __logging_page_id__ = '  \ LOGGING PAGE ID : ' + r.json() ["logging_page_id"]
        user_info.append(__logging_page_id__)
        time.sleep(1.6)
        print ( G + "        、 " + Y + "[ SHOW SUGGESTED PROFILES ] : " + W + str( r.json() ["show_suggested_profiles"]) )
        __show_suggested_profiles__ = '  \ SHOW SUGGESTED PROFILES : ' + str( r.json() ["show_suggested_profiles"])
        user_info.append(__show_suggested_profiles__)
        time.sleep(1.6)
        if "True" in str( r.json() ["show_suggested_profiles"]) :
                print ( G + "                |" + W )
                print ( G + "                ’＿＿ SUGGESTED PROFILES SHOWING" + W )
        elif "False" in str( r.json() ["show_suggested_profiles"]) :
                print ( G + "                |" + W )
                print ( G + "                ’＿＿ SUGGESTED PROFILES NOT SHOWING" + W )
        else :
                print ( G + "                |" + W )
                print ( G + "                ’＿＿ NOT SURE" + W )
        time.sleep(2)
        email = a
        print ( G + "        、 " + Y + "[ SHOW FOLLOW DIALOG ] : " + W + str( r.json() ["show_follow_dialog"]))
        __show_follow_dialog__ = '  \ SHOW FOLLOW DIALOG : ' + str( r.json() ["show_follow_dialog"])
        user_info.append(__show_follow_dialog__)
        time.sleep(1)
        print ( '-----------------------' )
        phone = email
        # GET USERNAME
        print ( G + "[ USERNAME ] : " + W + info ["username"])
        __username__ =  'USERNAME : ' + info["username"]
        user_info.append(__username__)
        time.sleep(1.2)
        # GET ID
        print ( G + "        |" + W )
        print ( G + "        ’＿＿ [ GET ID ] " + W )
        time.sleep(2)
        print ( G + "        、 " + Y + "[ ID ] : " + W + info ["id"] )
        __id__ = 'ID : ' + info["id"]
        user_info.append(__id__)
        time.sleep(2)
        # NEXT UPDATE NEED TIME
        # GET EMAIL AND PHONE
        print ( G + "        、 " + Y + "[ EMAIL ] : " + W + email )
        __email__ = 'EMAIL : ' + email
        user_info.append(__email__)
        time.sleep(2)
        print ( G + "        、 " + Y + "[ PHONE ] : " + W + phone )
        __phone__ = 'PHONE : ' + phone
        user_info.append(__phone__)
        time.sleep(1)
        print ( G + "        、 " + Y + "[ JOIM ON INSTGRAM ] : " + W + " None" )
        __data_of_join__ = 'JOIM ON INSTGRAM : None '
        user_info.append(__data_of_join__)
        time.sleep(1.2)
        print ( '-----------------------' )
        # GET LAST ACTIVITY
        print ( G + "[ LAST ACTIVITY ]" + R + " [ ONLINE ] " + W + ": Can't get")
        time.sleep(2)
        # GET LAST POST
        _last_post__ = info["edge_owner_to_timeline_media"]
        __last_post__ = _last_post__["edges"]
        for ____post____ in __last_post__ :
                one_post = ____post____["node"]
                __typename__ = one_post["__typename"]
                add_typename = 'TYPENAME : ' +  __typename__
                last_post.append(add_typename)
                __post__id__ = one_post["id"]
                add_post_id = 'POST ID : ' + __post__id__
                last_post.append(str(add_post_id))
                __short_link__ = one_post["shortcode"]
                add_short_link = 'SHORT LINK : ' + 'https://instagram.com/p/'+__short_link__
                last_post.append(add_short_link)
                get_post_text = one_post["edge_media_to_caption"]
                __post_getting_ = get_post_text["edges"]
                for _post_in_ in __post_getting_ :
                       _post_getting_ = _post_in_["node"]
                try :
                       __post_text__ = _post_getting_["text"]
                       add_posttext = 'POST TEXT : ' +  __post_text__
                       last_post.append(add_posttext)
                except UnboundLocalError :
                       pass
                likes = one_post ["edge_liked_by"]
                __likes__ = likes["count"]
                add_likes = 'LIKES : ' + str(__likes__) + ' Like'
                last_post.append(str(add_likes))
                comments = one_post["edge_media_to_comment"]
                __comments__ = comments["count"]
                add_comments = 'COMMENTS : ' + str(__comments__) + ' Comment'
                last_post.append(str(add_comments))
                if "[]" in str(__last_post__) :
                        pass
                else :
                        __link_to__post__ = one_post["display_url"]
                        url = __link_to__post__
                        web_img = urlopen(url)
                        data = web_img.info()
                        __last_modified__ = data["Last-Modified"]
                        add_last_modified = 'LAST MODIFIED : ' + __last_modified__
                        last_post.append(add_last_modified)
                        __type_of_img__ = data["Content-Type"]
                        add_type_img = 'TYPE : ' + __type_of_img__
                        last_post.append(add_type_img)
                        __size_of_img__ = data["Content-Length"]
                        size_byte = __size_of_img__
                        size_mb = 0.000001
                        final_size_as_mb = int(__size_of_img__)*size_mb
                        add_size = 'SIZE : ' + ("%.2f" % final_size_as_mb) +' MB'
                        last_post.append(str(add_size))
                        date_of_dumps_info = data["date"]
                        add_dumpdate = 'DUMPS THIS INFO AT : ' + date_of_dumps_info
                        last_post.append(add_dumpdate)
                        get_img = requests.get(__link_to__post__)
                        output = open("users/"+___user_local___+"/"+"media/"+___media_posts__+"/"+"last_Image_from_last_post.png",'wb')
                        output.write(get_img.content)
                        output.close()
                break
        with open ("users/"+___user_local___+"/"+"media/"+___media_posts__+"/"+"image_info.txt",'w') as last_img_info :
                for every_info_inlastimg in last_post :
                        last_img_info.write("%s\n" % every_info_inlastimg)
        if "[]" in str(__last_post__) :
                print ( G + "        |" + W )
                print ( G + "        ’＿＿ [ LAST POST WAS ] : " + W + "NO POST OR PRIVATE ACCOUNT" )
        else :
                print ( G + "        |" + W )
                print ( G + "        ’＿＿ [ LAST POST WAS ] : " + W ,__last_modified__ )
                time.sleep(1)
                print ( G + "                |" + W )
                print ( G + "                ’＿＿ [ MORE INFO ABOUT POST ] " + W )
                time.sleep(2)
                print ( Y + "                、    [ IMAGE OR VIDEO OR SIDECAR ] : " + W + __typename__ )
                time.sleep(2)
                print ( Y + "                、    [ POST ID ] : " + W , __post__id__ )
                time.sleep(2)
                print ( Y + "                、    [ LINK TO POST ] : " + W + "https://instagram.com/p/"+__short_link__ )
                time.sleep(2)
                print ( Y + "                、    [ POST TEXT ] : " + W + __post_text__ )
                time.sleep(2)
                print ( Y + "                、    [ LIKES ] : " + W ,__likes__,"Like" )
                time.sleep(2)
                print ( Y + "                、    [ COMMENTS ] : " + W ,__comments__,"Comment" )
                time.sleep(2)
                if "GraphVideo" in str(__typename__) :
                        print ( Y + "                、    [ TYPE ] : " + W + "mp4" )
                else :
                        print ( Y + "                、    [ TYPE ] : " + W + __type_of_img__ )
                time.sleep(2)
                print ( Y + "                、    [ SIZE ] : " + W + ("%.2f" % final_size_as_mb ) + " MB" )
                time.sleep(2)
                print ( Y + "                、    [ DUNPED AT ] : " + W ,date_of_dumps_info )
        time.sleep(2)
        print ( '-----------------------' )
        # GET BIO

        print ( G + "[ BIO ] : " + W + info ["biography"] )
        __bio__ = 'BIO : ' + info["biography"]
        user_info.append(__bio__)
        time.sleep(1.2)
        # SEARCH FOR LINKS IN BIO
        if info["external_url"] == info["external_url"] :
                print ( G + "        |" + W )
                print ( G + "        ’＿＿ [ FIND LINK IN BIO ] " + W )
                time.sleep(2)
                print ( G + "        、 " + Y + "[ LINK ] : " + W + str (info["external_url"]))
                __link_in_bio__ = '  \ BIO LINKS : ' + str (info["external_url"])
                user_info.append(__link_in_bio__)
        else :
                print ( G + "        |" + W )
                print ( G + "        ’＿＿ [ FIND LINK IN BIO ] " + W )
                time.sleep(2)
                print ( G + "        、 " + Y + "[ LINK ] : " + W + "NO LINKS IN BIO " )
        time.sleep(2)
        print ( '-----------------------' )
        # GET FOLLOWERS
        data_followed = info ["edge_followed_by"]
        followed = data_followed ["count"]
        __followed__ = ('FOLLOWERS : ' + str (followed))
        user_info.append(__followed__)
        print ( G + "[ FOLLOWERS ] : " + W, followed)
        time.sleep(2)
        print ( G + "        |" + W )
        print ( G + "        ’＿＿ [ GET FOLLOWERS ] " + W )
        time.sleep(2)
        print ( G + "        ’＿＿ [ DONE ] " + W + ": ",str (followed) + " user" )
        time.sleep(0.5)
#        dump_followers = input( G + ("        ’＿＿＿" + Y + " DO YOU WANT TO SAVE LAST 50 USER ( Y/N ) : " ) + W ).strip()
        time.sleep(2)
        print ( R + "        ’＿＿ [ NEXT UPDATE ] " + W )
        print ( '-----------------------' )
        # GET FOLLOWING
        data_following = info ["edge_follow"]
        following = data_following ["count"]
        __following__ = ('FOLLOWING : ' + str (following))
        user_info.append(__following__)
        print ( G + "[ FOLLOWING ] : " + W , following)
        time.sleep(2)
        print ( G + "        |" + W )
        print ( G + "        ’＿＿ [ GET FOLLOWING ]" + W )
        time.sleep(2)
        print ( G + "        ’＿＿ [ DONE ] " + W + ": ",str (following) + " user" )
        time.sleep(0.5)
#       dump_following = input( G + ("        ’＿＿＿" + Y + " DO YOU WANT TO SAVE LAST 50 USER( Y/N ) : " ) + W ).strip()
        time.sleep(2)
        print ( R + "        ’＿＿ [ NEXT UPDATE ] " + W )

        print ( '-----------------------' )
        time.sleep(2)
        # GET POSTS
        data_owner_posts = info ["edge_owner_to_timeline_media"]
        count_posts = data_owner_posts ["count"]
        __posts__ = ('POSTS : ' + str (count_posts))
        user_info.append(__posts__)
        print ( G + "[ POSTS ] : " + W , count_posts)

        time.sleep(1.2)
        # HIGHLIGHT REEL
        highlight_reel = info["highlight_reel_count"]
        print ( G + "[ HIGHLIGHT REEL ] : " + W , highlight_reel )
        __highlight__ = ('HIGHLIGHT REEL : ' , highlight_reel)
        user_info.append(str (__highlight__))
        time.sleep(2)
        igtv = info["edge_felix_video_timeline"]
        __igtv__ = int(igtv["count"])
        if __igtv__ > 0 :
                print ( G + "[ IGTV ] " + W )
                time.sleep(2)
                print ( G + "        |" + W )
                print ( G + "        ’＿＿THIS ACCOUNT HAS IGTV" + W )
                _igtv_ = 'IGTV : ' + ' THIS ACCOUNT HAS INTG'
                user_info.append(_igtv_)
                time.sleep(2)
                for post_in_igtv in igtv["edges"] :
                        igtv_post = post_in_igtv["node"]
                __title__ = igtv_post["title"]
                title = 'TITLE : ' + __title__
                user_info.append(title)
                __product_type__ = igtv_post["product_type"]
                product_type = 'PRODUCT TYPE : ' + __product_type__
                user_info.append(product_type)
                __igtv_likes__ = igtv_post["edge_liked_by"]
                _get_igtv_likes = __igtv_likes__["count"]
                igtvlikes = 'LIKES : ' + str(_get_igtv_likes) + " LIKE"
                user_info.append(igtvlikes)
                __igtv_comments__ = igtv_post["edge_media_to_comment"]
                _get_igtv_comments = __igtv_comments__["count"]
                igtvcomments = 'COMMENTS : ' + str(_get_igtv_comments) + ' Comment'
                user_info.append(igtvcomments)
                igtv_id = igtv_post["id"]
                __igtvid__ = 'ID : ' + str(igtv_id)
                user_info.append(__igtvid__)
                __igtv_shortlink__ = igtv_post["shortcode"]
                igtvshort = 'SHORT LINK :' + 'https://instagram.com/p/'+__igtv_shortlink__
                user_info.append(igtvshort)
                print ( G + "           '＿＿ [ LAST POST WITH INFO ] :" + W )
                time.sleep(2)
                print ( Y + "             、 [ TITLE ] : " + W + title )
                time.sleep(2)
                print ( Y + "             、 [ PRODUCT TYPE ] :" + W + __product_type__ )
                time.sleep(2)
                print ( Y + "             、 [ LIKES ] : " + W + str(_get_igtv_likes) + " Like" )
                time.sleep(2)
                print ( Y + "             、 [ COMMENTS ] : " + W + str(_get_igtv_comments) + " Comment" )
                time.sleep(2)
                print ( Y + "             、 [ ID ] : " + W + str(igtv_id) )
                time.sleep(2)
                print ( Y + "             、 [ SHORT LINK ] : " + W + "htpps://instagram.com/p/"+__igtv_shortlink__ )
        else :
                print ( G + "[ IGTV ] " + W )
                time.sleep(2)
                print ( G + "        |" + W )
                print ( G + "        ’＿＿THIS ACCOUNT HAS NOT IGTV" + W )
        time.sleep(3)
        print ( '-----------------------' )
        # GET IS PRIVATE
        private = info ["is_private"]
        print ( G + "[ Private ] : " + W, private )
        time.sleep(2)
        print ( G + "        |" + W )
        if "True" in str (private) :
                print ( G + "        ’＿＿ IT'S A PRIVATE ACCOUNT" + W )
                __private__ = ('  \ PRIVATE : ' + "IT'S A PRIVATE ACCOUNT ")
                user_info.append(__private__)
        elif "False" in str (private) :
                print ( G + "        ’＿＿ IT'S NOT A PRIVATE ACCOUNT" + W )
                __private__ = ('  \ PRIVATE : ' + "IT'S NOT A PRIVATE ACCOUNT ")
                user_info.append(__private__)
        else :
                print ( G + "        ’＿＿ NOT SURE" + W )
        time.sleep(2)
        print ( '-----------------------' )
        # GET IS VERIFIED
        verified = info ["is_verified"]
        __verified__ = ('VERIFIED : ' + str (verified))
        user_info.append(__verified__)
        print ( G + "[ Verified ] : " + W, verified )
        time.sleep(2)
        print ( G + "        |" + W )
        if "True" in str (verified) :
                print ( G + "        ’＿＿ THE ACCOUNT HAS BEEN VERIFIED" + W )
                __verified__ = ('  \ VERIFIED : ' + "THE ACCOUNT HAS BEEN VERIFIED ")
                user_info.append(__verified__)
        elif "False" in str (verified) :
                print ( G + "        ’＿＿ THE ACCOUNT HAS NOT BEEN VERIFIED " + W )
                __verified__ = ('  \ VERIFIED : ' + "THE ACCOUNT HAS NOT BEEN VERIFIED ")
                user_info.append(__verified__)
        else :
                print ( G + "        ’＿＿ NOT SURE" + W )
        time.sleep(1.2)
        # GET IS BUSINESS ACCOUNT
        business = info ["is_business_account"]
        __business__ = ('BUSINESS ACCOUNT : ' + str (business))
        user_info.append(__business__)
        print ( G + "[ BUSINESS ACCOUNT ] : " + W, business )
        time.sleep(2)
        print ( G + "        |" + W )
        if "True" in str (business) :
                print ( G + "        ’＿＿ THIS IS A BUSINESS ACCOUNT" + W )
                __business__ = ('BUSINESS ACCOUNT : ' + "THIS IS A BUSINESS ACCOUNT")
                user_info.append(__business__)
                business_name = info["business_category_name"]
                category_id = info["category_id"]
                time.sleep(2)
                print ( G + "                |" + W )
                print ( Y + "                ’＿＿ [ BUSINESS CATEGORY NAME ] : " + W , business_name )
                time.sleep(2)
                print ( Y + "                ’＿＿ [ CATEGORY ID ] : " + W , category_id )
                user_info.append(str (business_name))
                user_info.append(str (category_id))

        elif "False" in str (business) :
                print ( G + "        ’＿＿ THIS IS NOT A BUSINESS ACCOUNT " + W )
                __business__ = ('BUSINESS ACCOUNT : ' + "THIS IS NOT A BUSINESS ACCOUNT ")
                user_info.append(__business__)
        else :
                print ( G + "        ’＿＿ NOT SURE" + W )
        print ( '---------------------------' )
        time.sleep(3)
        # GET PROFILE PIC AND SAVE
        req_img_hd = requests.get(info["profile_pic_url_hd"])
        __profile_pic__ = "PRIFILE_PIC"
        os.system('mkdir '+"users/"+___user_local___+"/"+___media___+"/"+__profile_pic__)
        img_file = open ("users/"+info["username"]+"/"+___media___+"/"+__profile_pic__+"/"+"profile_pic.png","wb")
        img_file.write(req_img_hd.content)
        img_file.close()
        # GET PIC INFO
        url = info["profile_pic_url_hd"]
        run_url = urlopen(url)
        img_info = run_url.info()
        r = img_info["Content-Length"]
        mb = 0.000001
        size_mb = int(r)*mb
        print ( G + "[ GET PROFILE PIC WITH INFO ] : " + W )

        time.sleep(2)
        print ( G + "        |" + W )
        print ( G + "        ’＿＿ [ DONE ]" + W )
        time.sleep(1.4)
        print ( G + "        、 " + Y + "[ LAST MODIFIED ] : " + W + img_info["Last-Modified"] )
        time.sleep(1.7)
        print ( G + "        、 " + Y + "[ CONTENT TYPE ] : " + W + img_info["Content-Type"] )
        time.sleep(1.9)
        print ( G + "        、 " + Y + "[ SIZE ] : " + W + img_info["Content-Length"],"Byte" )
        time.sleep(1.2)
        print ( G + "        、 " + Y + "[ SIZE ] : " + W + ("%.2f" % size_mb), "MB" )
        time.sleep(1.2)
        print ( G + "        、 " + Y + "[ DATE ] : " + W + img_info["Date"])
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
        with open ("users/"+___user_local___+"/"+___media___+"/"+__profile_pic__+"/"+"PIC_INFO.txt",'w') as pic_info :
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
        print ( Y + '[ + -- - ]' + W + ' LAST POST ' + G + ' SAVED ' + W )
        time.sleep(2)
        print ( Y + '[ + -- - ]' + W + ' LAST POST INFO ' + G + ' SAVED ' + W )
        time.sleep(2)
        print ( " " )
        time.sleep(1)
        print ( G + "PROFILE INFO : " + W + "Check --> " + "users/"+___user_local___)
        time.sleep(1)
        print ( G + "PROFILE PIC : " + W + "Check --> " + "users/"+___user_local___+"/"+"media/"+__profile_pic__ )
        time.sleep(1)
        print ( G + "PIC INFO : " + W + "Check --> " + "users/"+___user_local___+"/"+"media/"+__profile_pic__ )
        time.sleep(1)
        print ( G + "LAST POST : " + W + "Check --> " + "users/"+___user_local___+"/"+"media/"+___media_posts__ )
        time.sleep(1)
        print ( G + "LAST POST INFO : " + W + "users/"+___user_local___+"/"+"media/"+___media_posts__ )
        time.sleep(1)
        print ("")
        print ( Y + '[!]' + G + ' TIPS : ' + Y + " MOVE USER FOLDER TO SDCARD AND CHECK IT FROM 'MY FILES' " + W )
        time.sleep(0.5)
        print ( Y + '[!]' + G + ' USER TO MOVE : ' + W + 'mv '+"users/"+___user_local___+" /sdcard" )
        time.sleep(0.4)
        print ( " " )
        print ( G + '[^] DONE ' + W )
        print ( " " )
        again = input( Y + 'zxll ' + W + '/' + R + 'Another username' + W + ' Y / N  : ').strip()
        if again.lower() == "y" :
                os.system('clear')
                user_info.clear()
                user_img_info.clear()
                last_post.clear()
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
        print ( "ERRORS Please check your internet." )
        pass

##### MAIN #####
def main():
    try :
        os.system('clear')
        print ( Y + '''

            + - -- [ BY KADA ]
            + - -- [ V 12.7 ]
            + - -- [ For V 27.6 PRO - Telegram : @Ghost7_Kada ]
            + - -- [ Get Instagram users info ]

        //////  EXIT USE : CTRL + C + ENTER  \\\\\\

''' + W )
        print ( G + "         、[ DOWNLOAD ALL POSTS FROM INSTAGRAM USER ]" + W )
        print ( G + "         、[ GET USERS FROM ANY HASHTAG ]" + W )
        print ( R + "                   、[ ONLY ON TELEGRAM CHANNEL ] " + W )

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
