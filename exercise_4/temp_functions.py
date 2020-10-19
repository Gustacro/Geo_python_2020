

def fahrToCelsius(temp_fahrenheit):
    convertedTemp = (temp_fahrenheit - 32) / 1.8
    return convertedTemp


def tempClassifier(tempCelsius):
    """
    Purpose:
    --------
    Reclassify the input temperature based on the criteria on:
         | Return value | Classification criteria                  |
         |---|-----------------------------------------------------|
         | 0 | temperatures below -2 degrees (Celsius)             |
         | 1 | temperatures equal or higher than -2 up to +2 degrees (Celsius)  |
         | 2 | temperatures equal or higher than +2 up to +15 degrees (Celsius)  |
         | 3 | temperatures equal or higher than +15 degrees (Celsius)            |
    The value returned should follow the table above

    Parameter:
    ----------
    tempCelsius: <numeric>
    """
    if tempCelsius < -2:
        criteria = 0
    elif tempCelsius >= -2 and tempCelsius < 2:
        criteria = 1
    elif tempCelsius >= 2 and tempCelsius < 15:
        criteria = 2
    else:
        criteria = 3
    return criteria
