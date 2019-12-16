"""Ask the user for a temperature. Then ask them what units
 Celsius or Fahrenheit,the temperature is in Your program should convert
 the temperature  to the other unit """

temp=int(input(' enter the temperature '))
unit=int(input(' enter 1 for Celsius, 2 for Fahrenheit  '))

if unit==1:
    print('The temperature in Fahrenheit is ',((9/5)*temp)+32)
else:
    print('The temperature in Celsius is ', ((5/9)*(temp-32)),  )        
