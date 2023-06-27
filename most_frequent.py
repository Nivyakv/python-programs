def most_frequent(string):
    frequency = {}
    for letter in string:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1

    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    for letter, count in sorted_frequency:
        print(letter, "-", count)
string = "Mississippi"
most_frequent(string)
