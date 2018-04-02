me = {
    'name': 'Elizabeth Pedley',
    'age': 24,
    'country of birth': 'USA',
    'favorite language': 'JavaScript'
}

def about_me(dict):
    for key, value in dict.items():
        print 'Mgit y {} is {}.'.format(key, value)

about_me(me)