def convertCtoF(temperatureCelsus : float) -> float:
    """
    ## convertir temperature de  celsus en farenheit
    [](https://github.com/webdevproformation/python-h3-sept-2024/blob/main/jour02/12-exercise-11.png)
    - c / 5 = (f - 32) / 9
    - c / 5 * 9= (f - 32) 
    - c / 5 * 9 + 32 = f 
    """
    return  temperatureCelsus / 5 * 9 + 32

print(convertCtoF(0))  # 32.0
print(convertCtoF(50)) # 122.0
print(help(convertCtoF))

