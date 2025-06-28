#loc-to return one or more specified row(s)
import pandas as pd
calories ={"day1":42,"day2":45,"day3":65}
myvar = pd.Series(calories)
print(myvar)
print(myvar.loc["day2"])