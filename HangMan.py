Word_list=['apple','banana','mango','orange','grape','pineapple','apricot','lemon']
lives =5
Chosen_word = random.choice (Word_list)
print(Chosen_word)
display=[]

for i in range (len(Chosen_word)):  
    display += '_'
print(display)

Game_Over = False

while not Game_Over:
    gussed_letter = input('Guess a letter : ').lower()
    for position in range (len(Chosen_word)):
        letter = Chosen_word [position]
        if letter == gussed_letter :
            display [position]=gussed_letter

    print(display)
    if gussed_letter not in Chosen_word:
        lives -=1 
        if lives == 0:
            Game_Over = True
            print('You Loose !!!!')

    if '_' not in display:

        Game_Over = True 
        print('~~~You win ~~~~')
