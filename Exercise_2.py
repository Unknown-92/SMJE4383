#Calculate rainfall in gallons for saome number of inches on 1 acre
inches = float(input("How many inches of rain have fallen: "))
volume = (inches/12) * 43560
gallons = volume * 7.48051945
print(inches, " in. rain on 1 acre is", gallons, "gallons")
