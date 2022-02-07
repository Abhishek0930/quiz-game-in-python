import requests as req
import json
import random
import time
ch = False
print('Press 1 for easy \nPress 2 for normal \nPress 3 for hard')
while ch == False:
    difficulty = int(input('enter your choice :-'))
    if difficulty <= 3 and difficulty >= 1:
        ch = True
    else:
        print('please select correct choice')
if difficulty == 1:
    url = 'https://opentdb.com/api.php?amount=1&category=30&difficulty=easy'
    print('So ypu opt for easy. \n\n Lets start the game in \n3')
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
elif difficulty == 2:
    url = 'https://opentdb.com/api.php?amount=1&category=17&difficulty=medium'
    print('So ypu opt for medium. \n\n Lets start the game in \n3')
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
else:
    url = 'https://opentdb.com/api.php?amount=1&category=17&difficulty=hard'
    print('So ypu opt for hard. \n\n Lets start the game in \n3')
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
end_game =''
print('\n')
while (end_game != 'quit'):
    ans_number = 1
    r = req.get(url)
    data = json.loads(r.text)
    question = data['results'][0]['question']
    print(question)
    all_ans = data['results'][0]['incorrect_answers']
    correct_ans = data['results'][0]['correct_answer']
    print('this is correct   ', correct_ans)
    all_ans.append(correct_ans)
    random.shuffle(all_ans)
    for answer in all_ans:
        print(ans_number,'-',answer)
        ans_number = ans_number + 1
    x = False
    while (x != True):
        given_ans = int(input('Type the number of the correct answer :-'))
        if given_ans >0 and given_ans <5:
            x = True
        else:
            print('type the correct number of your answer and it should be a integer :-')
    if (all_ans[given_ans-1] == correct_ans):
        print('\nGreat your answer is correct')
    else:
        print('\nSorry your answer is incorrect.')
    end_game = input('Press enter to play again else print quit to close the game.')
print('\n \n \n Thanks for playing, hope you like it.')