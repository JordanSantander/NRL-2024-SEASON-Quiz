print("Welcome to the NRL 2024 Season Quiz!")
print()
print("Lets test how much of an NRL fan you are!")
print()
class Question:
  def __init__(self, prompt, answer,hint):
    self.prompt = prompt
    self.answer = answer
    self.hint = hint
questions = [
  Question("Who finished the season with the most tries in the NRL?\n(a) Alofiana Khan Pereria\n(b) Kyle Feldt\n(c) Ronaldo Mulitalo\n(d) Dominic Young", "a", "He plays for a team finished outside the Top 8"),
  Question("Which team placed first on the NRL ladder?\n(a) Penrith Panthers\n(b) Melbourne Storm\n(c) Cronulla Sharks\n(d)Sydney Roosters", "b", "This team is not from New South Wales"),
  Question("Which player made the most tackles this season?\n(a) Blayke Brailey\n(b) Chris Randall\n(c) Reed Mahoney\n(d) Jacob Liddle", "c", "This player was a former Parramatta Eels player"),
  Question("What club fielded the youngest team in NRL history this season?\n(a) Gold Coast Titans\n(b) Canterbury-Bankstown Bulldogs\n(c) Wests Tigers\n(d) St George Dragons", "c", "This teams home field is in Leichhardt"),
  Question("In their record breaking loss against the Parramatta Eels How many points did the Dragons score?\n(a) 36\n(b) 38\n(c) 40\n(d) 42", "c", "It's a multiple of 4"),
  Question("Which of the following teams finished in the Top 8 of the ladder?\n(a) Dragons\n(b) Dolphins\n(c) Bulldogs\n(d) Raiders", "c", "This team is situated in the West of Sydney"),
  Question("Who won the Wally Lewis Medal in the 2024 State of Origin Series?\n(a) Dylan Edwards\n(b) Jarome Luai\n(c) Ruben Cotter\n(d) Angus Crichton", "d", "This player wears the number 12 jersey"),
  Question("Who was a tryscorer in New South Wales' historic win at Suncorp Stadium?\n(a) Mitchell Moses\n(b) Tom Dearden\n(c) Reece Robson\n(d) Dane Gagai", "a", "This player was injured for the majoirty of the season"),
  Question("Who won the Dally M medal for the 2024 season?\n(a) James Tedesco\n(b) Jahrome Hughes\n(c) Nihcolas Hynes\n(d) Daly Cherry-Evans", "b", "This player is a New Zealand representative player"),
  Question("Who won Dally M coach of the year for the 2024 season?\n(a) Cameron Ciraldo\n(b) Trent Robinson\n(c) Craig Bellamy\n(d) Ivan Cleary", "c", "The coach of the team that finished first"),
  ]
def run_test(questions):
  score = 0
  for question_num, question in enumerate(questions, 1):  
    print(f"Question {question_num}: {question.prompt}") 
    print()
    print ("Do you want a hint (yes/no)")
    hint_choice = input() . lower()
    if hint_choice == 'yes':
      print(f"Hint:{question.hint}")
      hint_choice = 'n'
      answer = input().lower()
      print()
      if answer == question.answer:
        score += 1
        print("Correct!")
        print()
      else:
        print (f"Incorrect. The correct answer is {question.answer}")
        print()
    else: 
      answer = input().lower()
      print() 
      if answer == question.answer:
        score += 1
        print("Correct!")
        print()
      else:
        print (f"Incorrect. The correct answer is {question.answer}") 
        print()
  print(f"You got {score}/{len(questions)} correct!") 
  if score >= 1 and score <= 3:
    print("You're a fake NRL fan!")
  if score >= 4 and score <= 6:
    print("You are a casual NRL fan!")
  if score >= 7 and score <= 9:
    print("You are a huge NRL fan!")
  if score == 10:
    print("You are an NRL superfan!")
run_test(questions)





