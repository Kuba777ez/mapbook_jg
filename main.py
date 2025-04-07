users:list[dict] = [
    {'name': 'Kuba', 'location': 'Szczecin', 'posts': 500, },
    {'name': 'Julka', 'location': 'Płońsk', 'posts': 100, },
    {'name': 'Marcin', 'location': 'Poznań', 'posts': 420, }
]

for user in users:
    print(f'Twój znajomy: {user["name"]} z {user["location"]} opublikował {user["posts"]}')
