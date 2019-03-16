if 3 > 2:
    print('It works')
if 5 > 2:
    print('5 is indeed greater than 2')
else:
    print('5 is not greater than 2')
name = 'sun'
if name == 'meng':
    print("Hey meng!")
elif name == 'sun':
    print('Hey sun!')
else:
    print('Hey anoymous!')
volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting!:(")
# Change the volume if it's too loud or too quiet
if volume < 20 or volume > 80:
    volume = 50
    print("That's better!")
def hi():
    print('Hi there!')
    print('How are you?')

hi()
def hi(name):
    if name == 'meng':
        print('Hi meng!')
    elif name == 'sun':
        print('Hi sun!')
    else:
        print('Hi anonymous!')
hi('sun')
def hi(name):
    print('Hi ' + name + '!')

hi("Rachel")
