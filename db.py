

_users = {
    'ivan': {
        'name': 'Ivan Kapustin',
        'age': '25',
        'smoking': 'Yes'
    },

    'igor': {
        'name': 'Igor Lebedev',
        'age': '18',
        'smoking': 'Yes'
    },

    'maria': {
        'name': 'Maria Popova',
        'age': '22',
        'smoking': 'No'
    },

    'olga': {
        'name': 'Olga kravetz',
        'age': '19',
        'smoking': 'Yes'
    }
}

_user_list = []

for login, user_data in _users.items():
    _new_element = {'login': login}
    _new_element.update(user_data)
    _user_list.append(_new_element)




def get_users_by_name(q):
    results = []

    for user in _user_list:
        if q.lower() in user['name'].lower():
            results.append(user)
    return results



def get_user(username):
    return _users.get(username)




