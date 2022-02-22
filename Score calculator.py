def computegrade(score):

    if 0.0 <= score <= 1.0:
        if score >= 0.9:
            return 'A'
        if score >= 0.8:
            return 'B'
        if score >= 0.7:
            return 'C'
        if score >= 0.6:
            return 'D'
        return 'F'
    return 'Entry out of range'


score = input('Enter score between 0 and 1:')

try:
    score = float(score)
except ValueError:
    print('Invalid entry')


print(computegrade(score))
