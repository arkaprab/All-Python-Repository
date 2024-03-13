# to demonstrate if else statements:
weather_report="Cloudy"
check=str(input('Enter weather report:'))
if(check == weather_report) :
    print("I will bring umbrella.")
else:
    print('I will bring sunglasses.')

is_male=True
is_female=True
is_transgender=True
if(is_male) :
    print("You are a male.")
else:
    print('You are female.')

if(is_female) :
    print('You are a female')
else:
    print('You are a male.')
if(is_transgender):
    print("Tui ekta chokka.")

is_Tall=False
if(is_male and is_Tall ):
    print('You are a tall handsome male , Congo !!!.')
if(is_male and not is_Tall):
    print('You are of male gender but you are not tall.')