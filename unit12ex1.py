L = [line.strip() for line in open('scores.txt')]

S = []
for l in L:
    s = l.split()
    #D = {s[0] : int(s[1])+5}
    D = {'name': s[0], 'score': int(s[1])+5}
    S.append(D)

print(S)


f = open('scores2.txt','w')
for k in S:
    print(k['name'], k['score'], file=f)
    #for key in k:
    #   print(key, k[key], file=f)

f.close()