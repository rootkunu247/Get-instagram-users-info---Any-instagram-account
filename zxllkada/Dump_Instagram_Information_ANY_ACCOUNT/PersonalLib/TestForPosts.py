import requests, json, time, sys

#session = requests.Session()

#######################
			# Important #
#######################
# Parts
Part1 = '<script type="text/javascript">window._sharedData = '
Part2 = ';</script>'
IsData = 'window._sharedData = {"config":'
# Query
QU = "https://www.instagram.com/graphql/query/"
QH = "?query_hash="
HC = "003056d32c2554def87228bc3fd9668a"
HV = "&variables="
FP = "&page=2"
QueryJson = {
	"id":"",
	"first":50,
	"after":""
}

# headers
headers = {
	"User-Agent" : "Mozilla/5.0 (Linux; Android 9; SM-J3300) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/46.01.2.5140",
	"Accept" : "*/*",
	"X-requested-with" : "XMLHttpRequest",
	"x-csrftoken" : "",
#	"Content-type" : "application/json; charset=utf-8"
	"referer" : "https://www.instagram.com/taylorswiftfans/"
}
			
# AllMedia
MediaOwner = []
# Rank T@gged
TaggedPeople = []
RankThem = {}
AfterRank = []

#######################
			# Rank T@gged #
#######################

def Tagged() :
	for OwnerPost in MediaOwner :
		OwnerTags = OwnerPost["edge_media_to_tagged_user"]["edges"]
		for Tag in OwnerTags :
			WhoIsThis = Tag["node"]
			ToJson = str(WhoIsThis).replace("'",'"')
			ToJson = ToJson.replace(" ","")
			ToJson = ToJson.replace("False","false")
			ToJson = ToJson.replace("True","true")
			ToJson = json.loads(ToJson)
#			print ("[ User Tagged ] :", ToJson["user"]["username"])
			TaggedPeople.append(ToJson["user"]["username"])

	CountTagged(TaggedPeople)
	
def CountTagged(List) :
	ShadowList = []
	for User in List :
		if User not in ShadowList :
			ShadowList.append(User)
			
	for TaggedUser in ShadowList :
		UserRank = List.count(TaggedUser)
		RankThem.update({str(UserRank) : TaggedUser})
#		print ("[ "+TaggedUser+" ] :", List.count(TaggedUser))
	for user in RankThem :
		AfterRank.append(int(user))

	countT = 1
	for Rank in AfterRank :
		if countT != 10 :
			print ("	[ #0"+str(countT),"]", RankThem[str(Rank)],"  ====>",Rank)
		else :
			print ("	[ #"+str(countT),"]", RankThem[str(Rank)]," ====>",Rank)
		countT += 1
		if countT == 11 :
			break

		

#######################
			# Dump & Json #
#######################
	
def AllPosts(Data, UserId, token, referer, session) :
	headers.update({"x-csrftoken" : token})
	headers.update({"referer" : referer})
	Screen = Data["graphql"]["user"]["edge_owner_to_timeline_media"]
	PostsCount = Screen["count"]
	PostsHasNext = Screen["page_info"]["has_next_page"]
	PostsEndCursor = Screen["page_info"]["end_cursor"]
	print ("[ User Have ] :",PostsCount,"Post")
	for post in Screen["edges"] :
		Post = post["node"]
		MediaOwner.append(Post)
	NextPostsHasNext = True
	while NextPostsHasNext :
		QueryJson.update({"id":UserId})
		QueryJson.update({"after":PostsEndCursor})
		NextUrl = QU+QH+HC+HV+str(QueryJson)+FP
		NextUrl = NextUrl.replace(" ","")
		NextUrl = NextUrl.replace("'",'"')
		NextPosts = session.get(NextUrl, headers=headers)
		Next = json.loads(str(NextPosts.text))
		Media = Next["data"]["user"]["edge_owner_to_timeline_media"]
		NextPostsHasNext = Media["page_info"]["has_next_page"]
		PostsEndCursor = Media["page_info"]["end_cursor"]
		for post in Media["edges"] :
			Post = post["node"]
			MediaOwner.append(Post)
			
	Tagged()

'''
__typename
id
gating_info
fact_check_overall_rating
fact_check_information
media_overlay_info
sensitivity_friction_info
sharing_friction_info
dimensions
display_url
display_resources
is_video
media_preview
tracking_token
edge_media_to_tagged_user
accessibility_caption
edge_media_to_caption
shortcode
edge_media_to_comment
edge_media_to_sponsor_user
comments_disabled
taken_at_timestamp
edge_media_preview_like
owner
location
viewer_has_liked
viewer_has_saved
viewer_has_saved_to_collection
viewer_in_photo_of_you
viewer_can_reshare
thumbnail_src
thumbnail_resources
'''