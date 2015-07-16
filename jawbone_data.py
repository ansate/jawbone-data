from jawbone import Jawbone


client_id = r''
client_secret = r''
redirect_uri = ''

jb = Jawbone(client_id, client_secret, redirect_uri, scope='basic_read extended_read sleep_read move_read')

#if you don't have a token yet, then 
#print jb.auth()
#produces a url, put that url in a browser, you'll get back a page with a code in the url
#mytoken = jb.access_token(code)
#access = mytoken['access_token']

access = u''

#gets first 10 results for these. upgrade to get n sometime
endpoint = 'nudge/api/v.1.1/users/@me/sleeps'
response = jb.api_call(access, endpoint)

sleepjson = response['data']

flat = []
for item in sleepjson['items']:
	flat.append((str(item['details']['asleep_time']), str(item['details']['light']), str(item['details']['sound'])))

sleepfile = "sleep.csv"
target = open(sleepfile, 'w')

for line in flat:
	target.write(','.join(line))
	target.write("\n")

target.close()

endpoint = '/nudge/api/v.1.1/users/@me/moves'
response = jb.api_call(access, endpoint)

mvsjson = response['data']

flat = []
for item in mvsjson['items']:
	flat.append((str(item['date']), str(item['details']['active_time']), 
		str(item['details']['distance']),
		str(item['details']['steps'])))

movesfile = "moves.csv"
target = open(movesfile, 'w')

for line in flat:
	target.write(','.join(line))
	target.write("\n")

target.close()


