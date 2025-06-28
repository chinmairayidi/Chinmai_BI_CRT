# creating pandas series using dictionary and calling indexing
import pandas as pd
calories ={"day1":42,"day2":45,"day3":65}
myvar = pd.Series(calories,index=["day1","day2"])
print(myvar)