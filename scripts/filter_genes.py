import pandas as pd

# Veri setini yükleyin
df = pd.read_csv('../data/gene_expression.tsv', sep='\t')

# Hiçbir koşulda ifade göstermeyen genleri filtreleyin
filtered_df = df[(df[['mock_rep1', 'mock_rep2', 'mock_rep3', 'sars_cov_rep1', 'sars_cov_rep2', 'sars_cov_rep3']].sum(axis=1)) > 0]

# Filtrelenmiş veriyi kaydedin
filtered_df.to_csv('../results/filtered_gene_expression.tsv', sep='\t', index=False)
