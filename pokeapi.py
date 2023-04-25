import psycopg2
import hidden
import requests
import json

# Load the secrets
secrets = hidden.secrets()

conn = psycopg2.connect(host=secrets['host'],
        port=secrets['port'],
        database=secrets['database'],
        user=secrets['user'],
        password=secrets['pass'],
        connect_timeout=3)

cur = conn.cursor()

# Help functions
def type(k):
    try:
        return js['types'][k]['type']['name']
    except:
        return ' '

def stat(k):
    try:
        return js['stats'][k]['base_stat']
    except:
        return ' '

# Creating pokeapi table
sql = 'DROP TABLE IF EXISTS pokeapi CASCADE;'
print(sql)
cur.execute(sql)

sql = '''
      CREATE TABLE IF NOT EXISTS pokeapi (id SERIAL, name TEXT, type_1 TEXT, type_2 TEXT, hp INTEGER,
      attack INTEGER, defense INTEGER, special_attack INTEGER, special_defense INTEGER, speed INTEGER);
      '''
print(sql)
cur.execute(sql)

conn.commit()

for i in range(1010):
    j = i+1
    j = str(j)
    url = 'https://pokeapi.co/api/v2/pokemon/' + j
    response = requests.get(url).text
    js = json.loads(response)
    sql = 'INSERT INTO pokeapi (name, type_1, type_2, hp, attack, defense, special_attack, special_defense, speed) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);'
    cur.execute(sql, (js['forms'][0]['name'], type(0), type(1), stat(0), stat(1), stat(2), stat(3),stat(4), stat(5), ))
    print(i+1, js['forms'][0]['name'])

conn.commit()
cur.close()
