# Import pprint module
from pprint import pprint
# Import pandas
import pandas as pd

# List of words to pair with products
words = ['cheap', 'discount', 'sale', 'best value', 'bargain', 'affordable', 'promotion', 'budget']

# List of products
products = ['sofas', 'convertible sofas', 'love seats', 'recliners', 'sofa beds']

# Create an empty list
keywords_list = []

# Loop through products
for product in products:
    # Loop through words
    for word in words:
        # Append combinations
        keywords_list.append([product, product + ' ' + word])
        keywords_list.append([product, word + ' ' + product])

# Inspect keyword list
pprint(keywords_list)

# Create a DataFrame from list
keywords_df = pd.DataFrame(keywords_list)

# Print the keywords DataFrame to explore it
print(keywords_df)

# Rename the columns of the DataFrame
keywords_df = keywords_df.rename(columns={0: 'Ad Group', 1: 'Keyword'})

# Add a campaign column
keywords_df['Campaign'] = 'SEM_Sofas'

# Add a criterion type column
keywords_df['Criterion Type'] = 'Exact'

print(keywords_df)
# Make a copy of the keywords DataFrame
keywords_phrase = keywords_df.copy()

# Change criterion type match to phrase
keywords_phrase['Criterion Type'] = 'Phrase'

# Append the DataFrames
keywords_df_final = keywords_df._append(keywords_phrase)

# Save the final keywords to a CSV file
keywords_df_final.to_csv('keywords.csv', index=False)

# View a summary of our campaign work
summary = keywords_df_final.groupby(['Ad Group', 'Criterion Type'])['Keyword'].count()
print(summary)
