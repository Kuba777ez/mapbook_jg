users:list[dict] = [
    {'name': 'Kuba', 'location': 'Szczecin', 'posts': 500, },
    {'name': 'Julka', 'location': 'Płońsk', 'posts': 100, },
    {'name': 'Marcin', 'location': 'Poznań', 'posts': 420, }
]


def get_user_info(users_data: list[dict])->None:
    for user in users_data:
        print(f'Twój znajomy: {user["name"]} z {user["location"]} opublikował {user["posts"]}')

get_user_info(users)