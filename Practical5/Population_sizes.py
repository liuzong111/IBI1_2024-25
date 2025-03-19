# ==== Step 1: Define Data ====
# Population data for UK countries (in millions)
uk_countries = [57.11, 3.13, 1.91, 5.45]  # England, Wales, Northern Ireland, Scotland
# Population data for Zhejiang-neighboring provinces (in millions)
china_provinces = [65.77, 41.88, 45.28, 61.27, 85.15]  # Zhejiang, Fujian, Jiangxi, Anhui, Jiangsu

# ==== Step 2: Sort and Print ====
# Sort the population data in ascending order
uk_sorted = sorted(uk_countries)
china_sorted = sorted(china_provinces)

# Print the sorted lists
print("Sorted UK population (ascending):", uk_sorted)
print("Sorted China provinces population (ascending):", china_sorted)

# ==== Step 3: Create Pie Charts ====
import matplotlib.pyplot as plt

# ----- Pie chart for UK countries -----
labels_uk = ["England", "Wales", "Northern Ireland", "Scotland"]
plt.pie(
    uk_countries, 
    labels=labels_uk, 
    autopct="%1.1f%%",  # Display percentages with 1 decimal place
    startangle=90,      # Start the pie chart at 90 degrees (vertical)
)
plt.title("Population Distribution in UK Countries")
plt.show()  # Display the chart

# ----- Pie chart for Zhejiang-neighboring provinces -----
labels_china = ["Zhejiang", "Fujian", "Jiangxi", "Anhui", "Jiangsu"]
plt.pie(
    china_provinces,
    labels=labels_china,
    autopct="%1.1f%%",
    startangle=90,
)
plt.title("Population Distribution in Zhejiang-Neighboring Provinces")
plt.show()

# ==== Step 4 (Optional): Customize Pie Charts ====
# Define custom parameters: colors, explode, shadow
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0"]
explode = (0.1, 0, 0, 0, 0)  # Explode the first slice (Zhejiang)

# Recreate the pie chart for Zhejiang-neighboring provinces with custom styling
plt.pie(
    china_provinces,
    labels=labels_china,
    autopct="%1.1f%%",
    startangle=90,
    explode=explode,    # Explode slices
    colors=colors,      # Custom colors
    shadow=True,        # Add shadow
    wedgeprops={"edgecolor": "black"},  # Add black borders to slices
)
plt.title("Customized Population Distribution in Zhejiang-Neighboring Provinces")
plt.show()