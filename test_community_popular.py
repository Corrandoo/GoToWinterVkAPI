import requests, json

result = requests.get("https://api.vk.com/method/groups.getMembers?group_id=80270762&v=5.60")
result2 = requests.get("https://api.vk.com/method/groups.getMembers?group_id=80270762&offset=1000&v=5.60")
json_result = json.loads(result.text)
json_result2 = json.loads(result2.text)
subscribers = json_result["response"]["items"] + json_result2["response"]["items"]
popular_subs = {} # ключ - Id пользователя, значение - количество друзей в сообществе
list_of_ids = []
list_of_numfriends = []

for i in subscribers:
    popular_subs[i] = 0
    try:
        result_user = requests.get("https://api.vk.com/method/friends.get?user_id=" + str(i) + "&v=5.60")
        json_result_user = json.loads(result_user.text)
        friends = json_result_user["response"]["items"]
        for friend in subscribers:
            if friend in friends:
                popular_subs[i] += 1
    except:
        popular_subs[i] = -1
for i in subscribers:
    print("id: " + str(i) + " friends: " + str(popular_subs.get(i)))
