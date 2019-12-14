
answer = float(input('enter the temperature in celcius  '))

if answer < 0 :
    print('attention low temperature')

elif  0 <= answer <= 35 :
    print ('temperature is fine')

else : print ('attention temperature is high')
