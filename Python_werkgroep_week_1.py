#ik heb hier wat aangepast, nummer twee 
#nog een hele hoop leuke oplossingen 

#ik ga hier nog even typen, 

#dit is een volgende regel 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Lees csv file als DataFrame
df = pd.read_csv('datasets.csv')

# 2. Print aantal unieke datasets
print(f"Aantal datasets: {df['dataset'].nunique()}")

# 3. Print namen van datasets
print(f"Namen van datasets: {df['dataset'].unique()}")

# print statistieken per dataset 
statestiek_per_dataset = df.groupby('dataset').agg(['count', 'mean', 'var', 'std'])
print(statestiek_per_dataset)

# plotten van de dataset (violin plot)
# 1. Violin plot voor x-coördinaten per dataset
plt.figure(figsize=(10, 6)) # Optioneel: maakt het scherm iets groter
sns.violinplot(data=df, x='dataset', y='x')
plt.title('Violin plot van x-coördinaten per dataset')
plt.show()

# 2. Violin plot voor y-coördinaten per dataset
plt.figure(figsize=(10, 6))
sns.violinplot(data=df, x='dataset', y='y')
plt.title('Violin plot van y-coördinaten per dataset')
plt.show()

#correltatie tussen x en y berekenen 
for name, group in df.groupby('dataset'):
    correlatie = group['x'].corr(group['y'])
    print(f"Dataset {name}: de correlatie tussen x en y is {correlatie:.3f}")

#Bepaal en print de covariantie matrix voor elke dataset
for name, group in df.groupby('dataset'):
    print(f"\n--- Covariantie Matrix voor dataset: {name} ---")
    # We selecteren alleen de kolommen x en y
    cov_matrix = group[['x', 'y']].cov()
    print(cov_matrix)


#scatterplot 
# col_wrap=4 zorgt voor een nette verdeling over meerdere rijen
g = sns.FacetGrid(df, col="dataset", col_wrap=4)

# Map de scatterplot functie op elk deel van het raster
g.map_dataframe(sns.scatterplot, x="x", y="y")

# Optioneel: voeg titels toe
g.set_titles(col_template="{col_name}")
plt.show()

#scatterplot met regressielijn --> lmplot combineert de facetgrid en regplot samen
sns.lmplot(data=df, x='x', y='y', col='dataset', col_wrap=4, ci=None)

plt.suptitle("Scatterplots met Regressielijnen", y=1.02)
plt.show()