weight=float(input('Weight? '))
measurement=input('(K)g or (L)bs? ').upper()
result = 0.0
if measurement == 'K':
    result = weight*2.2
    print(f'Weight in Lbs is {result}')
elif measurement == 'L':
    result = weight*0.45
    print(f'Weight in Kg is {result}')
else: 
    print ('You have provided an incorrect input')
    
    
