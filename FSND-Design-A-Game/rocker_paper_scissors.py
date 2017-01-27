import random

HANDS = ['paper', 'scissors', 'rock']

def random_hand():
    return random.choice(HANDS)

def rock_paper_scissors(player_hand, computer_hand):
    if computer_hand == player_hand:
        return 'draw'
    elif computer_hand == 'paper':
        if player_hand == 'scissors':
            return 'player'
        elif player_hand == 'rock':
            return 'computer'
    elif computer_hand == 'scissors':
        if player_hand == 'paper':
            return 'computer'
        elif player_hand == 'rock':
            return 'player'
    elif computer_hand == 'rock':
        if player_hand == 'paper':
            return 'player'
        elif player_hand == 'scissors':
            return 'computer'

def game():
    result = 'draw'
    while result == 'draw':
        player_hand = random_hand()
        computer_hand = random_hand()
        result = rock_paper_scissors(player_hand, computer_hand)
        # print "player:", player_hand
        # print "computer:", computer_hand
        # print "result:", result
        # print ""
    return result


player_score = 0
computer_score = 0

for i in range(100):
    # print 'GAME', i
    winner = game()
    if winner == 'player':
        player_score += 1
    elif winner == 'computer':
        computer_score += 1

# print '================================='
print 'Player wins: ', player_score
print 'Computer wins: ', computer_score
