import pandas as pd
import matplotlib.pyplot as plt
import json

# Load the data from the JSON file
with open('function_data.json', 'r') as f:
    data = json.load(f)

plt.figure(figsize=(10, 6))

# Loop through each function in the data
for func, func_data in data.items():
    # Convert the function data to a pandas DataFrame
    df = pd.json_normalize(func_data)

    # Convert execution_time to a numeric type, if it's not already
    df['execution_time'] = pd.to_numeric(df['execution_time'])

    # Plot execution_time against list_size for this function
    plt.plot(df['list_size'], df['execution_time'], marker='o', label=func)

plt.title('Execution Time of Sorting Functions')
plt.xlabel('List Size')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.grid(True)
plt.show()