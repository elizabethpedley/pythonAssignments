import random 

def coin_toss():
    heads = 0
    tails = 0
    for i in range(1,5001):
        side = random.randint(1,2)
        print side
        if side == 2:
            heads += 1
            print "Attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far".format( i, heads, tails)
        else:
            tails += 1
            print "Attempt #{}: Throwing a coin... It's a tail! ... Got {} head(s) so far and {} tail(s) so far".format( i, heads, tails)
coin_toss()