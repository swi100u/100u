# Simple plotting script for custody data

import pandas as pd
import matplotlib.pyplot as plt

# Load reconstructed data
df = pd.read_csv('custody_reconstructed_2018_2024.csv')

# Basic checks
print(df.head())

# Compute shares
df['share_razem'] = df['Razem_matce_i_ojcu'] / df['Razem']

# Plot counts
plt.figure(figsize=(9,5))
plt.plot(df['Rok'], df['Razem_matce_i_ojcu'], marker='o', label='Razem (władza)')
plt.plot(df['Rok'], df['Matce'], marker='o', label='Matce (wyłączna)')
plt.plot(df['Rok'], df['Ojcu'], marker='o', label='Ojcu (wyłączna)')
plt.ylabel('Liczba orzeczeń')
plt.xlabel('Rok')
plt.title('Orzeczenia o wykonywaniu władzy rodzicielskiej 2018–2024 (rekonstrukcja)')
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('figures/custody_trends.png', dpi=150)

# Plot shares
plt.figure(figsize=(9,5))
plt.plot(df['Rok'], df['share_razem'], marker='o', label='Udział - wspólna władza')
plt.ylabel('Udział (procent)')
plt.xlabel('Rok')
plt.title('Udział orzeczeń o wspólnej władzy 2018–2024')
plt.grid(alpha=0.3)
plt.savefig('figures/custody_shares.png', dpi=150)
