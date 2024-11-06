print("Welcome to the NRL 2024 Season Quiz!")
print()
print("Let's test how much of an NRL fan you are!")
print()
class Question:
    def __init__(self, prompt, answer, hint): #defined the key features of the quiz, was the same structure used by makeuseof.com in their tutorial
        self.prompt = prompt
        self.answer = answer
        self.hint = hint
questions = [
    Question("Who finished the season with the most tries in the NRL?\n(a) Alofiana Khan Pereria\n(b) Kyle Feldt\n(c) Ronaldo Mulitalo\n(d) Dominic Young", "a", "He plays for a team finished outside the Top 8"),
    Question("Which team placed first on the NRL ladder?\n(a) Penrith Panthers\n(b) Melbourne Storm\n(c) Cronulla Sharks\n(d) Sydney Roosters", "b", "This team is not from New South Wales"),
    Question("Which player made the most tackles this season?\n(a) Blayke Brailey\n(b) Chris Randall\n(c) Reed Mahoney\n(d) Jacob Liddle", "c", "This player was a former Parramatta Eels player"),
    Question("What club fielded the youngest team in NRL history this season?\n(a) Gold Coast Titans\n(b) Canterbury-Bankstown Bulldogs\n(c) Wests Tigers\n(d) St George Dragons", "c", "This team's home field is in Leichhardt"),
    Question("In their record-breaking loss against the Parramatta Eels, how many points did the Dragons score?\n(a) 36\n(b) 38\n(c) 40\n(d) 42", "c", "It's a multiple of 4"),
    Question("Which of the following teams finished in the Top 8 of the ladder?\n(a) Dragons\n(b) Dolphins\n(c) Bulldogs\n(d) Raiders", "c", "This team is situated in the West of Sydney"),
    Question("Who won the Wally Lewis Medal in the 2024 State of Origin Series?\n(a) Dylan Edwards\n(b) Jarome Luai\n(c) Ruben Cotter\n(d) Angus Crichton", "d", "This player wears the number 12 jersey"),
    Question("Who was a try-scorer in New South Wales' historic win at Suncorp Stadium?\n(a) Mitchell Moses\n(b) Tom Dearden\n(c) Reece Robson\n(d) Dane Gagai", "a", "This player was injured for the majority of the season"),
    Question("Who won the Dally M medal for the 2024 season?\n(a) James Tedesco\n(b) Jahrome Hughes\n(c) Nihcolas Hynes\n(d) Daly Cherry-Evans", "b", "This player is a New Zealand representative player"),
    Question("Who won Dally M coach of the year for the 2024 season?\n(a) Cameron Ciraldo\n(b) Trent Robinson\n(c) Craig Bellamy\n(d) Ivan Cleary", "c", "The coach of the team that finished first"),
]
def run_quiz(questions): # defining what happens when the quiz is run
    score = 0
    for question_num, question in enumerate(questions, 1): #enumerate is used to get the numerical value of the question
        print(f"Question {question_num}: {question.prompt}") #f strings embed key expressions to set a command 
        print()
        print("Do you want a hint (yes/no)")
        hint_choice = input().lower()         # input gernerates a place for the user to answer and lower keeps it lowercase
        if hint_choice == 'yes':
            print(f"Hint: {question.hint}") # here i commanded the program to print the hint if the user answered yes

        answer = input("Your answer: ").lower()
        print()                                  # this was used various times to make the code more clean and easy to read

        if answer == question.answer:
            score += 1                # allowed me to track the score of the user by adding 1 to the score when correct
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {question.answer}") # this code was completed with the help of the bro code youtube video on how to set correct and incorrect answers
        print()
    print(f"You got {score}/{len(questions)} correct!") # gave the user their score out of the total number of questions

    if score >= 1 and score <= 3:
        print("You are a fake NRL fan!")
    if score >= 4 and score <= 6:          # if statments to produce a response to the score the user obtains
        print("You are a casual NRL fan!") 
    if score >= 7 and score <= 9:
        print("You are a huge NRL fan!")
    if score == 10:
        print("You are an NRL superfan!")
run_quiz(questions)





