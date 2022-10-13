

tweet = input("Introdueix un tweet: ")

i = 0

while i<len(tweet):
    if tweet[i] == "#":
        p = i
        i = i + 1
        while (tweet[i] != " ") and (i<len(tweet)-1):
            i = i + 1
        if (i == len(tweet) -1):
            print (tweet[p:i+1])
        else:
            print(tweet[p:i])
    i = i + 1
        