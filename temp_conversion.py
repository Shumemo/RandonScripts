def convert_to_celcius(fahrenheit):
    '''(number) -> float

    Returns the number of Celcius degrees equivalent to Fahrenheit degrees.

    >>>convert_to_celcius(72)
    22.2
    >>>convert_to_celcius(50)
    10.0
    '''
    temp = (fahrenheit - 32) * 5/9
    return print('The temperature is', round(temp, 2), 'in Celcius.')
