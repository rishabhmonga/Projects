def reconstruct(people):
    if not people: return []

    # obtain everyone's info
    # key=height, value=k-value, index in original array
    peopledct, height, res = {}, [], []

    for i in range(len(people)):
        p = people[i]
        if p[0] in peopledct:
            peopledct[p[0]] += (p[1], i),
        else:
            peopledct[p[0]] = [(p[1], i)]
            height += p[0],

    print(height)
    height.sort()  # here are different heights we have

    # sort from the tallest group
    for h in height[::-1]:
        peopledct[h].sort()
        for p in peopledct[h]:
            res.insert(p[0], people[p[1]])

    return res


if __name__ == '__main__':
    print(reconstruct([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
