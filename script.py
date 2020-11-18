import json
import random
import string

import requests

from variables_for_script import number_of_users, max_posts_per_user, max_likes_per_user

user_info = []
user_info_token = []
posts_ids = []


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


def random_int():
    number = random.sample(range(10000, 99999), 1)
    return str(number).strip('[]')


def sign_up_user(number_of_users):
    for user in range(1, number_of_users):
        username = random_char(10)
        phone = f'+3806349{random_int()}'
        if phone in user_info:
            phone = f'+3806349{random_int()}'
        req = requests.post("http://localhost:8000/accounts/sign-up-request",
                            data={'username': username, 'phone': phone, 'password': 'qwe123qwer'})
        if req:
            user_info.append({"phone": phone})
    return print("Users were successfully created")


def login_users():
    for credentials in user_info:
        for key, value in credentials.items():
            req = requests.post("http://localhost:8000/accounts/sign-in-request",
                                data={key: value, 'password': 'qwe123qwer'})
            token = json.loads(req.content)["token"]
            if token:
                user_info_token.append({'token': token})
    return print("Users registered users were logined and got their auth tokens")


def create_posts(max_posts_per_user):
    for token in user_info_token:
        random_amount_of_posts = random.randint(1, max_posts_per_user)
        for post in range(1, random_amount_of_posts):
            req = requests.post("http://localhost:8000/posts/create",
                                headers={'Authorization': f"Token {token.get('token')}"},
                                data={"title": "Any Title", "body": "any body"})
            post = json.loads(req.content)["post"]
            if post:
                posts_ids.append(post.get('id'))
    return print("Logined users created random amount of posts")


def like_post(max_likes_per_user):
    made_likes = 0
    for token in user_info_token:
        for post in posts_ids:
            while made_likes < max_likes_per_user:
                random_bit = random.getrandbits(1)
                random_boolean = bool(random_bit)
                if random_boolean:
                    req = requests.post(f'http://localhost:8000/posts/{str(post)}/like',
                                        headers={'Authorization': f"Token {token.get('token')}"})
                    made_likes = made_likes + 1
            else:
                made_likes = 0
                break

    return print("Random posts were liked by users")


sign_up_user(number_of_users)
login_users()
create_posts(max_posts_per_user)
like_post(max_likes_per_user)

print('When you run this script, firstly we register users, then login them, then create posts and after '
      'randomly liking them ')
