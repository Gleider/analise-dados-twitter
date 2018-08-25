import tweepy
import csv
import time
import env

auth = tweepy.OAuthHandler(env.consumer_key, env.consumer_secret)
auth.set_access_token(env.acess_token, env.acess_token_secret)

api = tweepy.API(auth)

status = tweepy.Cursor(api.search, q='#DebateRedeTV', since='2018-08-17', until='2018-08-18', lang='pt').items()

data = []

def escrever_arquivo():
  with open('base_teste2.csv', 'w') as csv_file:
    arq = csv.writer(csv_file)

    while True:
      try:
        st = status.next()
        row = str(st.user.screen_name), str(st.created_at), str(st.text)
        arq.writerow(row)

      except tweepy.TweepError:
        print('wait 15 minutes')
        time.sleep(60*15)
        continue
        
      except StopIteration:
        print('Acabou')
        break

def ler_arquivo():
  with open('base_teste.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    i = 0
    for linha in reader:
      l = linha[0].split(' ')
      if l[0] not in data:
        data.append(l[0])
        i += 1

  return i

def gerarAmostra(qtd):
  amostra = []
  with open('base_teste.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    i = 0
    for linha in reader:
      amostra.append(linha)
      i += 1
      if i == qtd:
        break

  with open('amostra.csv', 'w') as csv_file:
    arq = csv.writer(csv_file)
    for linha in amostra:
      arq.writerow(linha)

# ------- main ----------- 
#escrever_arquivo()
#print(ler_arquivo())
gerarAmostra(100)
#print(data)