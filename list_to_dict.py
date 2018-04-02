name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def to_dict(list_a,list_b):
    tuple_list = zip(list_a,list_b)
    new_dict = dict(tuple_list)
    return new_dict

print to_dict(name,favorite_animal)
