print('Hello, world!\n')
#Counting loop example
#countWhile
i = int(input("Give me next number it'll start a counting journey until 10: "))
while i < 11:
  print(i)
  i += 1
#countFor
print("\nSecond \n")
for x in range(1,11):
  print(x)
#Accumulator pattern
#Have the python ask the user how many numbers are in the sequence(How many numbers do you have to average? 12 for example),
quizNumber = int(input("\n Please enter the amount of quizzes you will like to average: "))
#repeats N times
scoresCollector = 0
saverQuizNumber = quizNumber
while quizNumber > 0:
  quizScores = int(input("\nEnter a quiz score: "))
  quizNumber -= 1
  scoresCollector = scoresCollector + quizScores
  if quizScores == quizNumber:
    break
#When all the numbers have been entered (after your loop), have python print the average of those numbers.
print("\nYour average: ",scoresCollector/saverQuizNumber, "%")
#having python ask the user in advance how many numbers are in the sequence, have python (and each float(input(""))) tell the user to enter a special value(e.g., -999) to end the summing of numbers
starter = 1
counter = 0
holder = 0
print("\n \nEnter quiz scores to average. However, if you enter a negative number the loop will end and you'll get your average.")
while starter > 0.0:
  quizScores = int(input("\n Enter a quiz score to average: "))
  if quizScores < 0:
    break
  counter = counter + quizScores
  holder += 1
print("\nYour Average: ",counter/holder, "%")
