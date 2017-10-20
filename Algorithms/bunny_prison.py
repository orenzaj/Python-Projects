from itertools import combinations
import resource


def answer(plates):
    code = {}
    if not plates or len(plates) > 9:
        return 0
    if not sum(plates) % 3:
        code[len(plates)] = plates
    else:
        for l in range(1, len(plates)+1):
            for c in combinations(plates, l):
                if len(c) in code and sum(c) < sum(code[len(c)]):
                    continue
                if not sum(c) % 3:
                    code[len(c)] = c
    ans = sorted(code[max(code)], reverse=True) if code else [0]
    return int(''.join(map(str, ans)))


# plates = []                                 #0
# plates = [1, 2]                             #21
# plates = [1, 3, 1]                          #3
# plates = [7, 9, 3, 1, 9, 4, 8, 1, 8]        #99874311
# plates = [7, 9, 3, 1, 9, 4, 9, 6, 6]        #999766431
# plates = [7, 9, 3, 1, 9, 7, 0, 2, 2]        #99773220
# print (answer(plates))
for count in xrange(100000):
    var = [int(x) for x in list("{}".format(count))]
    ans = answer(var)
    print("{} : {}".format(count, ans))
print "used:\t{}b".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
