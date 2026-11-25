loop = True
from random import randint
connectors = ['','and','the','but']
tenses = ['will be','is','was']
adjectives = ['handsome','beautiful','happy','lonely','slimy','shiny','pale','cold','flaming','noisy','fat','winsome','']
nouns = ['engineer','gerbil','planet','man','woman','cinnamon roll','jacob','sammy boy','grim reaper','dog','phone','sun','tree','book','reindeer']
verbs = [['hated','loved','ate','killed','fed'],['hates','loves','washes','eats','wakes'],['eating','feeding','duct taping','washing','blasting']]
messageStart = 'Because the '
while loop:
    stimuli = input(': ')
    if stimuli == 'why':
        message = messageStart + adjectives[randint(0,8)] + ' ' + nouns[randint(0,14)] + ' ' + verbs[randint(0,2)][randint(0,4)] + ' ' + 'the' + ' ' + nouns[randint(0,14)] + '.'
        for word in verbs[2]:
            if word in message:
                new_message = list(message.partition(word))
                new_message.insert(new_message.index(word),tenses[randint(0,2)]+' ')
                message = ''.join(new_message)
        print(message)
    elif stimuli == 'exit':
        loop = False
    else:
        print('Meditate futher.')
    