import numpy as np
import matplotlib.pyplot as plt

# Create a dictionary
language_popularity = {
    "JavaScript": 62.3,
    "HTML": 52.9,
    "Python": 51,
    "SQL": 51,
    "TypeScript": 38.5
}
print(language_popularity)

# Extract languages and percentages
languages = list(language_popularity.keys())
percentages = list(language_popularity.values())

# Create the bar chart
plt.bar(languages, percentages, color='blue')
plt.xlabel('Programming Languages')
plt.ylabel('Percentage of Developers')
plt.title('Popularity of Programming Languages')
plt.show()
#Define the query language
selected_language = "Python"
#Retrieve the usage percentage
percentage = language_popularity[selected_language]
#Print the result
print(f"The percentage of developers using {selected_language} is {percentage}%")