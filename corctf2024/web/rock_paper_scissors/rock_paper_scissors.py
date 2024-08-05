import requests
from random import choice

# Constants
BASE_URL = 'http://localhost:8080'


def new_game(username):
    response = requests.post(f'{BASE_URL}/new', json={'username': username})
    if response.status_code == 200:
        token = response.cookies.get('session')
        return token
    else:
        print(f"Error creating new game: {response.text}")
        return None


def play_game(token, move):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post(f'{BASE_URL}/play', json={'position': move}, cookies={'session': token}, headers=headers)
    if response.status_code == 200:

        print("token2: ", token)
        return response.json()
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


def optimal(r, p, s):
    moves = ['🪨', '📃', '✂️']

    counts = {'Rock': r, 'Paper': p, 'Scissors': s}
    most_played = max(counts, key=counts.get)

    if most_played == 'Rock':
        if p < s:
            optimal_move = '✂️'
        else:
            optimal_move = '🪨'

    elif most_played == 'Paper':
        if r < s:
            optimal_move = '📃'
        else:
            optimal_move = '🪨'

    elif most_played == 'Scissors':
        if r < p:
            optimal_move = '📃'
        else:
            optimal_move = '✂️'

    print(f"(r,p,s): ({r},{p},{s}) ///// GENERATED OPTIMAL: {optimal_move}\n")

    return optimal_move


def play():
    username = 'LETHIMCOOK'
    token = new_game(username)
    print("token1: ", token)
    if not token:
        return

    moves = ['🪨', '📃', '✂️']

    rock_count = 0
    paper_count = 0
    scissors_count = 0

    move = choice(moves)
    for _ in range(100):  # Try playing multiple rounds

        result = play_game(token, move)
        if result:
            print(f"Played {move}, System chose {result['system']}, Result: {result['state']}")
            if result['state'] == 'end':
                print("Game ended. Score:", result['score'])
                break

        if result['system'] == '🪨':
            rock_count += 1
        elif result['system'] == '📃':
            paper_count += 1
        else:
            scissors_count += 1

        move = optimal(rock_count, paper_count, scissors_count)

        # print(f"(r,p,s): ({rock_count},{paper_count},{scissors_count})\n")

    scores = get_scores()
    if scores:
        print("Scores:", scores)

    flag = get_flag(token)
    if flag:
        print("Flag:", flag)


def main():
    for i in range(1):
        play()


if __name__ == '__main__':
    username = 'FizzBuzz101'
    token = new_game(username)
    print("token1: ", token)
