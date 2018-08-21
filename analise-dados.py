import tweepy
import csv
import time
import env

auth = tweepy.OAuthHandler(env.consumer_key, env.consumer_secret)
auth.set_access_token(env.acess_token, env.acess_token_secret)

api = tweepy.API(auth)

arq = csv.writer(open('base_teste.csv', 'w'))
arq2 = open('base_teste_json.json', 'w')

row = []
status = tweepy.Cursor(api.search, q='#lula', since='2018-08-18', until='2018-08-19', lang='pt').items()

while True:
  try:
    st = status.next()
    row = str(st.user.screen_name), str(st.created_at), str(st.text)
    arq.writerow(row)
    
    arq2.write(str(st))
    arq2.write('/n')

  except tweepy.TweepError:
    print('wait 15 minutes')
    time.sleep(60*15)
    continue
  except StopIteration:
    print('Acabou')
    break