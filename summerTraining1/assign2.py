def GetInformation():
    Name = input('What is your name? ')
    Weit = input('What is your weight?(KG) ')
    Heit = input('What is your hegiht?(CM) ')
    return Name,Weit,Heit

Name, Weit, Heit = GetInformation()

BMI = float(Weit) / pow((float(Heit) / 100), 2)
Situation = ''
if BMI <= 18.5: 
    Situation = 'UNDERWEIGHT'
elif BMI <= 24.9: 
    Situation = 'NORMAL WEIGHT'
elif BMI <= 29.9: 
    Situation = 'OVERWEIGHT'
else: 
    Situation = 'OBESE'

print('Your BMI value is {0} and you are: {1}'.format(BMI, Situation))