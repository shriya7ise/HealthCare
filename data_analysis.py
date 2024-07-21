from library_initialize import load_data

# Load the data
df1 = load_data('/Users/shriya/Downloads/healthdata/share-with-mental-or-substance-disorders-by-sex.csv')
df2 = load_data('/Users/shriya/Downloads/healthdata/share-with-mental-and-substance-disorders.csv')
df3 = load_data('/Users/shriya/Downloads/healthdata/share-with-depression.csv')
df4 = load_data('/Users/shriya/Downloads/healthdata/prevalence-of-depression-males-vs-females.csv')
df5 = load_data('/Users/shriya/Downloads/healthdata/prevalence-by-mental-and-substance-use-disorder.csv')
df6 = load_data('/Users/shriya/Downloads/healthdata/mental-and-substance-use-as-share-of-disease.csv')

print(df1)

# Columns in dataset
print(df1.columns)