import hashlib
import datetime
import requests
import pandas as pd

pub_key = 'your public key'
priv_key = 'your private key'
ts = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')

def hash_md5_params():
    hash_md5 = hashlib.md5()
    hash_md5.update(f'{ts}{priv_key}{pub_key}'.encode('utf-8'))
    final_hash = hash_md5.hexdigest()
    return final_hash
'''
A hash MD5 encryption was made acording to the site requests:
The public key, the private key and the TimeStamp were concatenated on bytes and encode to a 8-bit Unicode-based(UTF) format;
The parameter hexdigest returned a hexdecimal string-object, identified as final_hash.
'''

df1 = pd.DataFrame()
jump_offset = 0

for i in range(16):
    params = {'ts': ts, 'apikey': pub_key, 'hash': hash_md5_params()};
    request = requests.get(f'https://gateway.marvel.com:443/v1/public/characters?limit=100&offset={jump_offset}', params=params)
    response = request.json()

    df0 = pd.DataFrame(response['data'])
    df1 = pd.concat([df1, df0])
    jump_offset += 100

df2 = df1.results
'''
A loop was created to make the pagination of the API:
The limit of pagination is 100, so the "for" loop was used to get the data one hundred by one hundred;
The data has been converted to json and concatened in a DataFrame.
'''


lista_id = []
lista_name = []
lista_description = []
lista_comics = []
lista_series = []
lista_stories = []
lista_events = []

for i in df2:
    id = i['id']
    name = i['name']
    description = i['description']
    comics = i['comics']['available']
    series = i['series']['available']
    stories = i['stories']['available']
    events = i['events']['available']
    
    lista_id.append(id)
    lista_name.append(name)
    lista_description.append(description)
    lista_comics.append(comics)
    lista_series.append(series)
    lista_stories.append(stories)
    lista_events.append(events)
'''
To manipulate the data it was chosen to receive them in lists:
Using a loop, the lists traverse each row of the DataFrame and stored the specified data.
'''


df = pd.DataFrame(data = {'id':lista_id,
                          'name':lista_name,
                          'discription':lista_description,
                          'comics':lista_comics,
                          'series':lista_series,
                          'stories':lista_stories,
                          'events':lista_events})
'''
The final DataFrame was created:
The DataFrame was made using a dictionary shape;
The colum names were used as keys and the lists as values.
'''

         
print(df)
'''
The 'print' comand showed the final DataFrame.
''' 

df.to_csv('MarvelAPI')
'''
Used to created a ".csv" file.
'''
