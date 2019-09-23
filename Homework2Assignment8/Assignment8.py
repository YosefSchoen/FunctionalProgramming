def add2Dicts(d1, d2, d3):
    sameKey = list(map(lambda x, y: set(dict(x).values()).union(dict(y).values()) if x == y else 0, range(0, max(len(d1), len(d2)))))

    print(sameKey(d1, d2))
    return 0


d1 = dict([(1, 'a'), (3, 'd'), (5, 'e')])
d2 = dict([(1, 'b'), (3, (11, 22)), (7, 'f'), (4, 'q')])
d3 = dict([(2, 'c'), (3, 'x'), (4, 't'), (8, 'g')])
add2Dicts(d1, d2, d3)

