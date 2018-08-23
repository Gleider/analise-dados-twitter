import tweepy
import csv
import time
import env

auth = tweepy.OAuthHandler(env.consumer_key, env.consumer_secret)
auth.set_access_token(env.acess_token, env.acess_token_secret)

api = tweepy.API(auth)

status = tweepy.Cursor(api.search, q='#DebateRedeTV', since='2018-08-16', until='2018-08-20', lang='pt').items()

def escrever_arquivo():
  with open('base_teste.csv', 'w') as csv_file:
    arq = csv.writer(csv_file)

    while True:
      try:
        st = status.next()
        row = str(st.user.screen_name), str(st.created_at), str(st.text)
        arq.writerow(row)
        break
      except tweepy.TweepError:
        print('wait 15 minutes')
        time.sleep(60*15)
        continue
      except StopIteration:
        print('Acabou')
        break

# def ler_arquivo():
#   with open('base_teste.csv', 'r') as csv_file:
#     reader = csv.reader(csv_file)
#     for linha in reader:
#       print(linha)

# ------- main ----------- 
escrever_arquivo()