# Threshold variables
MIN_THRESHOLD = -2 # Maximum percentage the coin can fall
MAX_THRESHOLD = 5 # Minimum percentage the coin has to rise

# Margin variables
MIN_MARGIN = 1
MAX_MARGIN = 1


# Returns best sell values if given a prediction it is worth to buy
def minmax_interpration(prediction, first_value):
    min = prediction['close'].min()
    max = prediction['close'].max()

    if (min > MIN_THRESHOLD and max > MAX_THRESHOLD):
        return buysell_values(min=min, max=max, first_value=first_value)
    
    return False

# Returns best sell values
def buysell_values(min, max, first_value):
    min -= MIN_MARGIN
    max -= MAX_MARGIN

    return (float(min)*float(first_value)/100) + float(first_value), (float(max)*float(first_value)/100) + float(first_value)

if __name__ == "__main__":
    print("running interpret_data")