users = {
    0 : {'username':'username', 'password':'password'},
    1 : {'username':'jilin', 'password':'admin'},
    2 : {'username':'jimbo', 'password':'jimboisreallycool'}
}

users_list = []
for user in users.values():
    users_list.append(user['username'])

print(users_list)
