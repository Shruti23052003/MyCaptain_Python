# To print the letters in decreasing order of frequency using most_frequent function

x = str(input("Enter the string "))

def most_frequent(x):
    d = dict()
    for key in x:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

y = most_frequent(x)

print(y)
