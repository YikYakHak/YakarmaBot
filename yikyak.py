import requests, uuid

messageID = "R/54267bf93c77b60e5f66beca3bdde"

Ann_Arbor = ['42.2814', "-83.7483"]
Austin = ['30.2861','-97.7394']
Berkeley = ['37.8717', '-122.2728']
Columbus = ['40.0000', '-83.0145']
Philadelphia = ['39.9500', '-75.1900']
State_College = ['40.7914', '-77.8586']

city = Berkeley
lat = city[0]
lng = city[1]

def make_uuids(amount):
	i = 0
	uuids = []
	while i < amount:
		 uuids.append(str(uuid.uuid4()).upper())
		 i += 1
	return uuids

def kill_feed(feed):
	i = 0
	while i < len(feed): 
		n = 0
		while n <= int(feed[i]['numberOfLikes']) + 4:
			dislike_yak(feed[i]['messageID'], downvotes[n])

			if int(feed[i]['numberOfLikes']) - n < - 4:
				n = 999
				print('killed a post')
			else:
				n += 1
		i += 1

def mass_like_yak(m_id, numLikes):
	fake_user_list = make_uuids(numLikes)
	for user_id in fake_user_list:
		like_yak(m_id, user_id)

def like_yak(m_id, user_id):
	yikyak_header =  { "Host": "yikyakapp.com", "Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "en;q=1, fr;q=0.9, de;q=0.8, ja;q=0.7, nl;q=0.6, it;q=0.5", "Connection": "keep-alive", "User-Agent": "Yik Yak/2.0.2.5 (iPhone; iOS 7.0.6; Scale/2.00)" }
	register = requests.post('https://yikyakapp.com/api/registerUser?userID=' + user_id +'&salt=123&hash=abc', headers = yikyak_header)
	send_like = requests.get("https://yikyakapp.com/api/likeMessage?messageID=" + m_id + "&userID=" + user_id + "&salt=1411725084&hash=jxuHrrXzeK1LwTC5JlsQWsUOuzo%3D&userLat=37.873325&userLong=-122.252983")
	print('sent like')

def mass_dislike_yak(m_id, numLikes):
	fake_user_list = make_uuids(numLikes)
	for user_id in fake_user_list:
		dislike_yak(m_id, user_id)

def dislike_yak(m_id, user_id):
	yikyak_header =  { "Host": "yikyakapp.com", "Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "en;q=1, fr;q=0.9, de;q=0.8, ja;q=0.7, nl;q=0.6, it;q=0.5", "Connection": "keep-alive", "User-Agent": "Yik Yak/2.0.2.5 (iPhone; iOS 7.0.6; Scale/2.00)" }
	register = requests.post('https://yikyakapp.com/api/registerUser?userID=' + user_id +'&salt=123&hash=abc', headers = yikyak_header)
	send_downvote = requests.get("https://yikyakapp.com/api/downvoteMessage?messageID=" + m_id + "&userID=" + user_id + "&salt=1411725084&hash=jxuHrrXzeK1LwTC5JlsQWsUOuzo%3D&userLat=37.873325&userLong=-122.252983")
	for message in get_yaks():
		if m_id in message.values():
			print('sent downvote ' + message['message'])

def get_yaks():
	yaks = requests.get("https://yikyakapp.com/api/getMessages?userID=f6bb54ed-d969-4260-b101-9b455e564016&lat="+lat+"&long="+lng+"&salt=1411724954&hash=vuhZnitPbE4p8agZ5sBUub2KUvQ%3D&userLat="+lat+"&userLong="+lng)
	return yaks.json()["messages"]

def terminal_yak():
	yaks_request = requests.get("https://yikyakapp.com/api/getMessages?userID=f6bb54ed-d969-4260-b101-9b455e564016&lat="+lat+"&long="+lng+"&salt=1411724954&hash=vuhZnitPbE4p8agZ5sBUub2KUvQ%3D&userLat="+lat+"&userLong="+lng)
	yaks = []

	for yak in yaks_request.json()["messages"]:
		print(str(yak['numberOfLikes']) + ' ' + yak['message'] + ' ' + yak['messageID'] + '\n ------------------------------------------------')




