from cash_machine.post_request import post_request

data = {
        "items": [1, 2, 3]
    }

# запуск сервера: python manage.py runserver

post_to_server = post_request(data)
print(post_to_server)
