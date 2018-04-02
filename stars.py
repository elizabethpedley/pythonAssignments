def stars(arr):
    for indx in range(len(arr)):
        stars = ''
        if isinstance(arr[indx], str):
            for j in range(len(arr[indx])):
                stars += arr[indx][0].lower()
        else:
            for i in range(arr[indx]):
                stars += '*'
        print stars

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
stars(x)
