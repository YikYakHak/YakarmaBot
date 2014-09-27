import requests

with open('upvote.txt', 'r') as f:
	upvotes = f.read().split()

with open('downvote.txt', 'r') as f:
	downvotes = f.read().split()

messageID = "R/5426622e13f82822d9c4e69b9bb27"

Ann_Arbor = ['42.2814', "-83.7483"]
Austin = ['30.2861','-97.7394']
Berkeley = ['37.8717', '-122.2728']
Columbus = ['39.9833', '-82.9833']
Philadelphia = ['39.9500', '-75.1900']
State_College = ['40.7914', '-77.8586']



city = Berkeley
lat = city[0]
lng = city[1]

def like_yak():
	for line in upvotes:
		yikyak_header =  { "Host": "yikyakapp.com", "Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "en;q=1, fr;q=0.9, de;q=0.8, ja;q=0.7, nl;q=0.6, it;q=0.5", "Connection": "keep-alive", "User-Agent": "Yik Yak/2.0.2.5 (iPhone; iOS 7.0.6; Scale/2.00)" }
		register = requests.post('https://yikyakapp.com/api/registerUser?userID=' + line.upper() +'&salt=123&hash=abc', headers = yikyak_header)
		send_like = requests.get("https://yikyakapp.com/api/likeMessage?messageID=" + messageID + "&userID=" + line.upper() + "&salt=1411725084&hash=jxuHrrXzeK1LwTC5JlsQWsUOuzo%3D&userLat=37.873325&userLong=-122.252983")
		print('sent like')
	f.close()

def dislike_yak():
	for line in downvotes: 
		yikyak_header =  { "Host": "yikyakapp.com", "Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "en;q=1, fr;q=0.9, de;q=0.8, ja;q=0.7, nl;q=0.6, it;q=0.5", "Connection": "keep-alive", "User-Agent": "Yik Yak/2.0.2.5 (iPhone; iOS 7.0.6; Scale/2.00)" }
		register = requests.post('https://yikyakapp.com/api/registerUser?userID=' + line.upper() +'&salt=123&hash=abc', headers = yikyak_header)
		send_downvote = requests.get("https://yikyakapp.com/api/downvoteMessage?messageID=" + messageID + "&userID=" + line.upper() + "&salt=1411725084&hash=jxuHrrXzeK1LwTC5JlsQWsUOuzo%3D&userLat=37.873325&userLong=-122.252983")
		print('sent downvotes')
	f.close()


def get_yaks():
	yaks = requests.get("https://yikyakapp.com/api/getMessages?userID=f6bb54ed-d969-4260-b101-9b455e564016&lat="+lat+"&long="+lng+"&salt=1411724954&hash=vuhZnitPbE4p8agZ5sBUub2KUvQ%3D&userLat="+lat+"&userLong="+lng)
	print(yaks.json()["messages"])