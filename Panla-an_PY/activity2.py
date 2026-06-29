name = str(input("Input your name Here: "))
score = int(input("Enter Score Here: "))


if (score >= 95 and score <= 100):
    print(name + " Your remarks are " +"Excellent")
elif (score >= 90 and score <= 94):
    print(name + " Your remarks are " +"Very Good")
elif (score >= 85 and score <=89):
    print(name + " Your remarks are " +"Good")
elif (score >=75 and score <= 84):
    print(name + " Your remarks are " +"Satisfactory")
elif (score <=75):
    print(name + " Your remarks " +"Needs Improvement")
else:
    print("Error")