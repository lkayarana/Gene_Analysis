import pandas as pd
from scipy import stats


filtered_df = pd.read_csv('../results/filtered_gene_expression.tsv', sep='\t')


numeric_columns = ['mock_rep1', 'mock_rep2', 'mock_rep3', 'sars_cov_rep1', 'sars_cov_rep2', 'sars_cov_rep3']
filtered_df[numeric_columns] = filtered_df[numeric_columns].apply(pd.to_numeric, errors='coerce')


mock = filtered_df[['mock_rep1', 'mock_rep2', 'mock_rep3']]
sars_cov = filtered_df[['sars_cov_rep1', 'sars_cov_rep2', 'sars_cov_rep3']]


p_values = []
for index, row in filtered_df.iterrows():
    # NaN değerleri kontrol et ve kaldır
    mock_values = row[['mock_rep1', 'mock_rep2', 'mock_rep3']].dropna().astype(float)
    sars_cov_values = row[['sars_cov_rep1', 'sars_cov_rep2', 'sars_cov_rep3']].dropna().astype(float)
    t_stat, p_value = stats.ttest_ind(mock_values, sars_cov_values)
    p_values.append(p_value)


filtered_df['p_value'] = p_values


significant_genes = filtered_df[filtered_df['p_value'] < 0.05]


significant_genes.to_csv('../results/significant_genes.tsv', sep='\t', index=False)
