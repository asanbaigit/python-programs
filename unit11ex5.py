"""
 Repeatedly ask the user to enter a team name and the how many games the team won and how many they lost. Store 
 this information in a dictionary where the keys are the team names and the values are lists of the form 
 [wins, losses].(a) Using the dictionary created above, allow the user to enter a team name and print 
 out the team’s winning percentage. (b) Using the dictionary, create a list whose entries are the number of wins 
 of each team. (c) Using the dictionary, create a list of all those teams that have winning records."""
D = {}
m = 0
while True:
    teamname = input('enter the team : ')
    if teamname == '-1':
        break
    w = eval(input('enter number of wins :'))
    l = eval(input('enter number of losses :'))
    if teamname not in D:
        D[teamname] = [w,l,w]
    else :
        m = D[teamname][2]
        if m < w :
            m = w
        D[teamname] = [D[teamname][0]+w,D[teamname][1]+l,m]
        
q = input('enter the team name: ')
if q in D:
    print(q,' wins = ',D[q][0], 'losses = ', D[q][1], 'win % = ','{:.2f}'.format(D[q][0]/(D[q][0]+D[q][1])*100))
    print ('max win of:',q,D[q][2])
else :
    print('No such team')

K = {key:D[key][0] for key in D}
print(K)

