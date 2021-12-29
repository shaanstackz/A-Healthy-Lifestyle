#Name: Shaan Kohli
#Student Number: 501028410

#This program is meant to advise the user on what different important health conditions and which they should increase or decrease.
#The health conditions include: Headphone Exposure, Step Count, Diets, and overall BMI

#Ask for weekly headphone audio level
dB=float(input('\nPlease input your weekly headphone audio levels (can be found on the health app on your phone)'))
#Function for calculating how much one's headphone exposure should be limited by
def exposure(x):
    difference=0.0
    if x > 85:
        difference = x-70
    else:
        difference=0.0
    return difference
#Displaying how much headphone exposure should be limited by
print ('\nYour headphone exposure should be limited by', exposure(dB),'dB')
#Ask for weekly step count
steps=int(input('\nPlease input the number of steps you walked this week (can be found on the health app on your phone)'))
#Ask for weekly distance walked
distance=float(input('\nPlease input your Walking + Running Distance in kilometres (can be found on the health app on your phone)'))
#Function to determine user's stride length (meant to tell the user how fast they are walking)
def stridelength(steps,distance):
    total=0
    feet=distance*3281
    while steps>distance:
        total=(steps/2)/feet
        print('\nYour stride length is',total,'feet')
        break
#Display stride length
stridelength(steps, distance)
#Function to determine how much the user should increase their weekly step count by
def steplimit(steps):
    dif=0
    if (steps<28000):
        dif=28000-steps
    else:
        dif=0
    return dif
#Display how much the user should increase their step count by
print('\nAs the average adult takes 28,000 steps per week, you should increase your step count by', steplimit(steps),'steps')
#Function to determine if the user follows any diet
def diets():
    diet = str(input('\nDo you follow any diets (y or any other key for no)?'))
    if(diet=="y"):
        #Game to display what diet is recommended for people with a high BMI
        game=str(input('\nWell done! Guess which diet we recommend for people with a high BMI:'))
        if (game=='Weight Watchers Diet'):
            game='Weight Watchers'
            print('\n',game!='Weight Watchers Diet')
        elif (game!='Weight Watchers Diet'):
            game='Weight Watchers Diet'
            print('\n',game!='Weight Watchers Diet')
        print('\nThe Weight Watchers Diet was in fact named the best diet for weight loss, and is recognized as the diet for fastest weight loss')
    else:
        #Game to display what diet is recommended for people who wish to eat healthier
        newdiet=str(input('\nThat is fine, but guess which diet we recommend for healthy eating:'))
        if (newdiet=='Flexitarian Diet'):
            newdiet='Flexitarian Diet'
            print('\n',newdiet=='Flexitarian Diet')
        elif (newdiet!='Flexitarian Diet'):
            newdiet='Flexitarian Diet'
            print('\n',newdiet!='Flexitarian Diet')
        print('\nThe Flexitarian Diet involves fruits, veggies, whole grains, and plant-based proteins therefore creating a great way for healthy eating!')
#Display information about diets
diets()
#Function to determine if BMI is healthy or not
def bmi(value):
    v=True
    #BMI is not healthy
    if value<18.5:
        v=False
        return v
    #BMI is healthy
    if value>=18.5 and value<=24.9:
        v=True
        return v
    #BMI is not healthy
    else:
        v=False
        return v
#BMI values for chart
value=[18.4, 24.9, 29.9, 40.0]
#Display BMI Chart
print('\n--------------BMI CHART------------------')
for v in value:
    print('\nIs a BMI under', v, 'a healthy?', bmi(v))
print('\n--------------BMI CHART------------------')
#Ask user for their weight
weight=float(input('\nPlease enter your weight in lbs'))
#Ask user for their height
height=float(input('\nPlease enter your height in cm'))
#Function to determine the user's BMI
def health(weight, height):
    index=0
    inches=height/2.54
    inches=inches*inches
    index=weight/inches
    index=index*703
    #Underweight
    if (index<18.5):
        print('Your BMI is',index,'meaning you are underweight')
    #Healthy Weight
    elif(index>=18.5 and index<=24.9):
        print('Your BMI is',index,'meaning you are healthy weight')
    #Overweight
    elif(index>=25 and index<=29.9):
        print('Your BMI is',index,'meaning you are overweight')
    #Obese
    elif(index>=30):
        print('Your BMI is',index,'meaning you are obese')
#Display BMI Level
health(weight, height)

