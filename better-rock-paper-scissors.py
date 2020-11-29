from random import randint
want1=0
while want1!=2:

    want1= int(input('To play press 1 to quit press 2: '))

    choices = ['Rock', 'Paper', 'Scissors']
    if want1 == 2:
        print('Game Ended ')
        break
    elif want1 >= 3 :
        print("Invalid Number")
        break
    elif want1 <= 0:
        print('Invalid Number')
        break





    user1 = input(' Enter Rock,Paper or Scissors ').lower()
    computerchoice = choices[randint(0, 2)]
    print('Computer answer is : ', computerchoice)
    if computerchoice=='Scissors'and user1=='scissors':
      print('It is a tie ,PLAY AGAIN')
    elif computerchoice=='Rock' and user1=='rock':
      print("It's a tie,PLAY AGAIN")
    elif computerchoice=='Paper' and user1=='paper':
      print("It's a tie,PLAY AGAIN")
    elif computerchoice=='Rock'and user1=='paper':
        print("Great choice,You WON 😍")
    elif computerchoice=='Paper'and user1=='rock':
        print('Bad move,You LOST 😞')
    elif computerchoice=='Rock' and user1=='scissors':
        print('Good try but bad luck,You LOST 🙃')
    elif computerchoice=='Scissors' and user1=='rock':
        print('Fantastic move,You WON 🤩')
    elif computerchoice=='Paper' and user1=='scissors':
        print('Good job,great move,You WON 🤯')
    elif computerchoice=='Scissors' and user1=='Paper':
        print('Uh OH!,You LOST☹️')
    else:
        print('Oops! Please Check Your Spelling Again')

















