def tricheck(list):
    ones = 0
    twos = 0

    for x in list:
        ones, twos = (ones ^ x) & ~twos, (ones & x) | (twos & ~x)
    assert twos == 0
    return ones

list_1 = [4,4,6,7,3,3,3,7,4,7]
list_2 = [9,7,4,7,4,4,7]

print(tricheck(list_1))
print(tricheck(list_2))