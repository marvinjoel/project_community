from urllib import parse, request
import json
import requests




url = requests.get('https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=100&q=Programaci%C3%B3n%20ATS&type=playlist&key=AIzaSyBVfmnrZa0h7APydJlDapoiyDH5Kp21FBY')
api = url.json()
items = api['items']

for a in items:
    snippet = a['snippet']
    title = snippet['title']
    print(title)

#api_yt = 'https://youtube.googleapis.com/youtube/v3/search'
#max_result = 100
#q = 'Programacion ATS'
#key='AIzaSyCsJNlNqk20digEKhmbmoMtZG2scTE05JA'
#
#
#'&type=playlist&key=AIzaSyCsJNlNqk20digEKhmbmoMtZG2scTE05JA'
#params_channel = {
#    'part':'snippet',
#    'maxResults':max_result,
#    'q' : q,
#    'type':'playlist',
#    'key':key   
#}
#url_values = parse.urlencode(params_channel)
#with request.urlopen(api_yt+'?'+url_values) as response:
#    json_response = json.loads(response.read())
#items = json_response['items'][0]
##snipp = items['snippet']
#titulo = snipp['channelTitle']
#indent = json.dumps(titulo, indent=4)
