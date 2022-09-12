import requests
import json

artists = ["56d6f872139b2166eb000ade",
"4e96f6e23e43de00010050cb",
"4e96f792be2b4e0001002fb1",
"4f0648318501fa10ca000001",
"4f958ec5357afa0001000af3",
"52f16a0e8b3b81a5b3000022",
"548632a7726169516a620100",
"53e126267261692d6bf50100",
"53d8b30672616913c7e40200",
"4f5f64c13b555230ac000007",
"55956e8d72616970d400002b",
"4f552b2e3b55524170000003",
"4f958feaaa701d0001000e3e",
"50208d56f9f2e70002001409",
"505fa4d3e22288000200007d"
]

client_id = '067d7eec58b3e911c139'
client_secret = 'b235ba8f346535712639285dedc69ae0'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
for i in range(len(artists)):
    r = requests.get("https://api.artsy.net/api/artists/" + artists[i], headers=headers)

    # разбираем ответ сервера
    j = json.loads(r.text)

    print(j["birthday"], j["sortable_name"])

