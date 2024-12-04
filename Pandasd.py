import os 
import csv

 try:
        # Check if the file exists
        if not os.path.existselection_data.csv):
            print(f"File 'election_data.csv}' does not exist. Creating it...")
            # Create and write to the file
            with open('election_data.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            print(f"File 'election_data.csv}' created successfully with election data.")
        else:
            print(f"File 'election_data.csv}' already exists.")
    except OSError as e:
        print(f"An error occurred while handling the file: {e}")



import pandas as pd

# Create the dataset
data = {
    "State": [
        "Madhya Pradesh", "Madhya Pradesh", "Madhya Pradesh", "Madhya Pradesh",
        "Rajasthan", "Rajasthan", "Rajasthan", "Rajasthan"
    ],
    "Party": ["BJP", "INC", "BSP", "Others", "BJP", "INC", "BSP", "Others"],
    "Seats_Won": [163, 66, 0, 1, 115, 69, 2, 13],
    "Total_Seats": [230, 230, 230, 230, 200, 200, 200, 200],
    "Voter_Turnout (%)": [72.1, 72.1, 72.1, 72.1, 74.2, 74.2, 74.2, 74.2]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Group by state and determine the party with the maximum seats
result = df.loc[df.groupby("State")["Seats_Won"].idxmax(), ["State", "Party", "Seats_Won"]]

# Display the result
print("Party with the highest number of seats in each state:")
print(result)


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create the DataFrame with the given data
data = {
    "State": ["Madhya Pradesh", "Madhya Pradesh", "Madhya Pradesh", "Madhya Pradesh",
              "Rajasthan", "Rajasthan", "Rajasthan", "Rajasthan"],
    "Party": ["BJP", "INC", "BSP", "Others", "BJP", "INC", "BSP", "Others"],
    "Seats_Won": [163, 66, 0, 1, 115, 69, 2, 13]
}

df = pd.DataFrame(data)

# Set up the figure
plt.figure(figsize=(10, 6))

# Create a barplot
sns.barplot(x="State", y="Seats_Won", hue="Party", data=df, palette="tab10")

# Add labels and title
plt.title("Seats Won by Each Party in Each State", fontsize=16)
plt.xlabel("State", fontsize=12)
plt.ylabel("Seats Won", fontsize=12)
plt.legend(title="Party", fontsize=10)

# Display the plot
plt.tight_layout()
plt.show()
