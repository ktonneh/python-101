# play game

def update_score(score):
    with open('high_score.txt','w') as f:
        f.write(str(score))
    print('Score Updated')

def play(score):
    with open('high_score.txt','r') as f:
        current_score = f.read()
        if current_score == '':
            current_score = 0
        print('Current Score: ',current_score)
    if score > int(current_score):
        print('You have broken the high score ', current_score)
        update_score(score)
    else:
        main()

def main():
    score = int(input('Enter a score \n'))
    play(score)

main()