import random

MAX_PLAYERS = 5
POINTS_TO_WIN = 5
QUESTION_BANK = {
    "Who's the singer of 'Never Gonna Give You Up'?": 'rick astley',
    "What's the capital of Nigeria?": 'abuja',
    'Which of these actors has never won an Oscar?\na) Denzel Washington\nb) Johnny Depp\nc) Tom Hanks': 'b',
    'Which is the country with most FIFA World Cup titles?': 'brazil',
    'Which is the second smallest country in the world?': 'monaco',
    "What's the capital of Brazil?": 'brasilia',
    "What's the capital of India?": 'new delhi',
    'Which of these cities is the capital of Puerto Rico?\na) Ponce\nb) Caguas\nc) San Juan': 'c',
    'Which of these countries is not part of the G7?\na) Italy\nb) Russia\nc) Canada': 'b',
    'When did the Battle of Normandy take place?': '1944',
    'Which of these country has never won Eurovision?\na) Cyprus\nb) Belgium\nc) Luxembourg': 'a',
    'Who is the President of the European Parliament?\na) Christine Lagarde\nb) Charles Michel\nc) Roberta Metsola': 'c',
    'When did Malta become a member of the European Union?\na) 2002\nb) 2003\nc) 2004': 'c',
    'Which of these countries is not a member of the European Union?\na) Czech Republic\nb) Serbia\nc) Cyprus': 'b',
    'Which of these countries is not a NATO member?\na) North Macedonia\nb) Austria\nc) Albania': 'b',
    "What's cynophobia?\na) Fear of snakes\nb) Fear of turtles\nc) Fear of dogs": 'c',
    "What's androphobia?\na) Fear of men\nb) Fear of flowers\nc) Fear of thunder": 'a',
    "What's the currency of Bolivia?": 'boliviano',
    "What's the currency of the Dominican Republic?": 'dominican peso',
    "Who's the Prime Minister of Canada?": 'justin trudeau',
    "Who's the President of France?": 'emmanuel macron',
    "Who's the Prime Minister of Italy?": 'giorgia meloni',
    "Who's the Prime Minister of the United Kingdom?": 'rishi sunak',
    'Which member of The Beatles married Yoko Ono?': 'john lennon',
    'Who was the first president of the United States?': 'george washington',
    'Which of these actors has NOT portrayed James Bond?\na) Pierce Brosnan\nb) Sean Connery\nc) Robert Pattinson': 'c',
    'Which of these films is not directed by Steven Spielberg?\na) Jurassic Park\nb) Catch Me If You Can\nc) Dunkirk': 'c',
    "Who's the singer of 'Watermelon Sugar'?": 'harry styles',
    "Who's the singer of 'Bad Romance'?": 'lady gaga',
    "Who's the singer of 'God's Plan'?": 'drake',
    'How many planets are in our Solar System?': '8',
    'Which is the biggest planet in our Solar System?': 'jupiter',
    'Which is the smallest planet in our Solar System?': 'mercury',
    'Which planet is the closest to Earth?': 'venus',
    'Which planet is the furthest from the Sun?': 'neptune',
    'Which planet is the closest to the Sun?': 'mercury',
    'When did the Western Roman Empire fall?': '476',
    'When did the Byzantine Empire fall?': '1453',
    'Who is the Greek god of wine and feast?': 'dionysius',
    'Who is the Greek King of the Gods?': 'zeus',
    'Mars is a planet, but for the Romans it was a also a...': 'god',
    'Which countries are the most visited in the world?\na) Spain, France & USA\nb) Italy, France & USA\nc) Italy, France & Spain': 'a',
    'Which is the capital of Argentina?': 'buenos aires',
    'Which is the capital of Australia?': 'canberra',
    'Which is the most bought videogame?': 'minecraft',
    'What is the meaning of the initials COD in the videogame world?': 'call of duty',
    'What is the meaning of the initials LoL in the videogame world?': 'league of legends',
    'What is the meaning of the initials CoC in the videogame world?': 'clash of clans',
    'What is the result of this quick operation: 3+2*3+(3-1)/2?': '10',
    "What is the first name of the protagonist of the anime 'Attack on Titans'?": 'eren',
    "What is the first name of the protagonist of the anime 'Demon Slayer'?": 'tanjiro',
    'How many episodes has in total the two series about Naruto?\na) 630\nb) 720\nc) 500\nd) 800': 'b',
    'What is the first name of the protagonist of the original trilogy of Star Wars?': 'luke',
    'What is the surname of Anakin, Luke and Leia in Star Wars?': 'skywalker',
    'If this game was a final project for Programming II, what grade should it have?': '10',
    'When did the 1st World War end?\na) 1914\nb) 1936\nc) 1918\nd) 1921': 'c',
    "In which century was the Thirty Year's War fought? (e.g: IV)": 'xvii',
    'What is the name of the deadliest battle in human history? The battle of ...': 'stalingrad',
    'What is the name of the biggest tank battle of history? The battle of...': 'kursk',
    'How many countries have a permanent seat in the Security Council of the UN?': '5',
    'How many countries are official members of the EU?': '27',
    'Which country won the Eurocup in 2004?': 'greece',
    "What's the capital of Lithuania?": 'vilnius',
    "Who wrote 'Alice in Wonderland'?": 'lewis carroll',
    'When did the French Revolution take place?\na) 1768\nb) 1779 \nc) 1789': 'c',
    'Area 51 is located in which state?': 'nevada',
    'Who painted Las Meninas?': 'diego velazquez',
    "What's the capital of Thailand?": 'bangkok',
    'When did Facebook launch?\na) 2001\nb) 2004\nc) 1999': 'b',
    "What's the symbol for silver?": 'ag',
    'Who painted the sistine chapel?': 'michelangelo',
    "What's the fastest animal on the planet?": 'cheetah',
    "When was 'Stranger Things' released?\na) 2014\nb) 2016\nc) 2017": 'b',
    "Who is Tibet's spiritual leader?": 'the dalai lama',
    "What's the name of the latest 007 movie?": 'no time to die',
    'Who painted The Guernica?': 'pablo picasso',
    "What's the name of the cafe from Friends?": 'central perk',
    'Which is the smallest country in the world?': 'vatican city',
    "Who wrote 'Wuthering Heights'?": 'emily bronte',
    "What's the fruit associated with the state of Georgia?": 'peaches',
    'Where did Sherlock Holmes live?': 'baker street',
    "What's the biggest country in the world?": 'russia',
    'What country formerly ruled Iceland?': 'denmark',
    'Which was the first Disney movie?\na) Snow white\nb) Pinocchio \nc) Sleeping Beauty': 'a',
    'Who was the first democratic-elected president in Spain?': 'adolfo suarez',
    'Where was Mozart born?': 'austria',
    "What's the highest grossing movie of all times?\na) Avatar\nb) Avengers: Endgame\nc) Titanic": 'a',
    "What's the capital of Canada?": 'ottawa',
    "What's the largest ocean in the world?": 'the pacific',
    'What is the capital of France?': 'paris',
    'Who painted the Mona Lisa?': 'leonardo da vinci',
    'What is the chemical symbol for gold?': 'au',
    "Who wrote the novel 'To Kill a Mockingbird'?\na) Harper Lee\nb) J.K. Rowling\nc) F. Scott Fitzgerald\nd) Charles Dickens": 'a',
    'What is the square root of 81?': '9',
    'What is the tallest mountain in the world?': 'mount everest',
    'Who is the Greek god of the sea?': 'poseidon',
    'What is the formula for calculating the area of a circle?\na) A = bh\nb) A = lw\nc) A = πr^2\nd) A = 2πr': 'c',
    'What is the capital of Japan?': 'tokyo',
    'Who is the founder of Microsoft?': 'bill gates',
    'What is the chemical symbol for oxygen?': 'o',
    "Who is the author of 'The Catcher in the Rye'?\na) J.D. Salinger\nb) Ernest Hemingway\nc) Mark Twain\nd) Jane Austen": 'a',
    'Who is the Norse god of thunder?': 'thor',
    'What is the formula for converting Celsius to Fahrenheit?\na) F = (C + 32) × 5/9\nb) F = (C × 9/5) + 32\nc) F = C × 2.20462\nd) F = C + 273.15': 'b',
    "Who is the author of 'Pride and Prejudice'?": 'jane austen',
    'What is the capital of Australia?': 'canberra',
    'Who is the CEO of Tesla?': 'elon musk',
    "Who is the author of 'Harry Potter'?\na) J.R.R. Tolkien\nb) J.K. Rowling\nc) George Orwell\nd) Stephen King": 'b',
    'What is the chemical symbol for hydrogen?': 'h',
    "Who wrote the play 'Hamlet'?": 'william shakespeare',
    'What is the largest continent on Earth?': 'asia',
    'Who is the Greek god of war?': 'ares',
    'What is the formula for calculating speed?\na) Speed = Distance x Time\nb) Speed = Time / Distance\nc) Speed = Distance / Time\nd) Speed = Time - Distance': 'c',
    "Who is the author of 'The Lord of the Rings'?\na) J.R.R. Tolkien\nb) C.S. Lewis\nc) George R.R. Martin\nd) J.K. Rowling": 'a',
}

def shuffle_dictionary(dictionary):  # combining shuffle with .popitem (line 159) prevents from question repetition
    """
    Function to shuffle a dictionary.
    :param dictionary: the dictionary we want to shuffle
    :return: shuffled dictionary
    """
    dictionary = list(dictionary.items())
    random.shuffle(dictionary)
    dictionary = dict(dictionary)
    return dictionary

# def get_random_question():  # with this option there exists the possibility of question repetition
#     questions = {
#         '1+1?': '2',
#         '2+2?': '4',
#         'What is your name? a) Juan / b) Jaun / c) Nuaj': 'a'
#     }
#     return random.choice(list(questions.items()))

# Ask number of players
try:
    total_players = input('How many players? > ')
    total_players = int(total_players)
    if total_players < 1 or total_players > MAX_PLAYERS:
        print(f'Number of players must be between 1 and {MAX_PLAYERS}')
        exit()
except ValueError:
    print("That's not a number 😒")
    exit()

# Main gameplay loop
questions = {}
scores = [0] * total_players
current_player = 0
while True:
    print('')
    print(f'<<< PLAYER {current_player+1} TURN >>>')

    # When no more questions, shuffle again
    if not questions:
        questions = shuffle_dictionary(QUESTION_BANK)

    # Ask current question
    question, solution = questions.popitem()
    print(question)

    # Check answer
    answer = input('> ').lower().strip()  # decapitalize and remove spaces so that the input can coincide with the solution in the dict
    if answer == solution:
        print("SLAYYYY 💅, you're not that stupid!")
        scores[current_player] += 1
        print(f'You win one point, now you have {scores[current_player]} point(s)')
    else:  # to move to next player's turn
        print(f'NOOOO 😭, the correct answer was "{solution}"')
        current_player = (current_player + 1) % total_players  # "%" allows to go back to the first player when the last player fails

    # Has game ended?
    if scores[current_player] == POINTS_TO_WIN:
        break

# Sort final scores
sorted_scores = {}
for index, score in enumerate(scores):
    player_name = 'Player ' + str(index+1)
    sorted_scores[player_name] = score
sorted_scores = dict(sorted(sorted_scores.items(), key=lambda x: x[1], reverse=True))  # sort from highest to lowest score

# Show final scores
print('')
print('<<< GAME OVER >>>')
medals = ['🥇', '🥈', '🥉', '🍪', '💩']
for key, score in sorted_scores.items():
    print(f'{medals.pop(0)} {key} - {score} point(s)')
