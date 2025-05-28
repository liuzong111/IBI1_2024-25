import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir(r"C:\Users\Liu\Desktop\IBI1\Practical10")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

first_ten_lines = dalys_data.iloc[0:10, 2]
# the 10th year is 1999 which was recorded in Afghanistan and data s 82624.94
print(first_ten_lines)


list = []
column = dalys_data.iloc[:, 2]
for i in column:
    if i == 1990:
        list.append(True)
    else:
        list.append(False)
# To out put the entity and dalys in all 1990 years
list1990 = dalys_data.loc[list, [True, False, False, True]]
print(list1990)


uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["DALYs", "Year"]]
uk_average = uk.DALYs.mean()
print("UK's average DALYs: ", uk_average)
fra = dalys_data.loc[dalys_data.Entity == "France", ["DALYs", "Year"]]
fra_average = fra.DALYs.mean()
print("France's average DALYs: ", fra_average)
if uk_average > fra_average:
    print("UK's average DALYs is higher than France's average DALYs")
elif uk_average < fra_average:
    print("UK's average DALYs is lower than France's average DALYs")
else:
    print("UK's average DALYs is equal to France's average DALYs")
# UK' average DALYs is higher than France's average DALYs

plt.plot(uk.Year, uk.DALYs, 'b+')
plt.xticks(np.arange(1990, 2021, 2), rotation=-20)
# to give the plot a title and x and y lables
plt.title("DALYs in UK", fontsize=18,
          fontweight='bold', color='blue', alpha=0.5)
plt.xlabel("Year", fontsize=10)
plt.ylabel("DALYs")
plt.show()

# To find out in each year, which country had the highest DALYs.
for year in range(1990, 2020):
    dalys_in_same_year = dalys_data.loc[dalys_data.Year == year, [
        "Entity", "DALYs"]]
    max_dalys = dalys_in_same_year.DALYs.max()
    country = dalys_in_same_year.loc[dalys_in_same_year.DALYs ==
                                     max_dalys, "Entity"]
    print(
        f"In {year}, the country with the highest DALYs is {country} with {max_dalys} DALYs.")
