import pandas as pd
import sqlite3

# Loading CVS file
df = pd.read_csv('/Users/wilson/AttentionLab/data/cleaned_attentionlab_data.csv')

# Create a connection to the SQLite database
conn = sqlite3.connect('/Users/wilson/AttentionLab/data/attentionlab.db')

# Save the DataFrame to a SQL table named 'attentionlab'
df.to_sql('attentionlab', conn, if_exists='replace', index=False)

print("Database created and data inserted successfully.")   

# Close the database connection
conn.close()

