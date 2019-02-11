#!/usr/bin/python

TEST_CASES = [
    [1,1,2,3,4,5,1,5,7,7,8,9,0,0,0,0],
    ['a',1,'b',0,'b',1,'e','r','t','p','q'],
    [],
]

def remove_duplicates(x):
    cleaned = []
    for item in x:
        if not item in cleaned:
            cleaned.append(item)
    return cleaned

for x in TEST_CASES:
    clean = remove_duplicates(x)
    print("{} became {}".format(x, clean))
