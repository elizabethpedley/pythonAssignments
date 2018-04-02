def odd_even():
    for i in range(2001):
        if(i%2 != 0):
            odd_even = 'odd'
        else:
            odd_even = 'even'
        print 'Number is {}. This is an {} number.'.format(i, odd_even)

def multiply(arr, num):
    for index in range(len(arr)):
        arr[index] *= num
    return arr

def layered_multiples(arr):
    new_array = []
    for num in arr:
        nest_array = []
        for one in range(num):
            nest_array.append(1)
        new_array.append(nest_array)
    return new_array
