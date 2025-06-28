import numpy as np
mileage = np.array([15.2, 16.5, 14.8, 15.9, 16.2, 15.5])
low_mileage_months = np.where(mileage < 15)[0] + 1
print("Months with mileage less than 15:", low_mileage_months)