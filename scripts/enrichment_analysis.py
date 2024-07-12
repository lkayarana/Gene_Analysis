import pandas as pd
from gprofiler import GProfiler

# Anlamlı genleri yükleyin
significant_genes = pd.read_csv('../results/significant_genes.tsv', sep='\t')

# Doğru sütun ismini kullanarak gen id'lerini alın
gene_ids = significant_genes['converted_alias'].tolist()  # 'gene_id' yerine doğru sütun adı varsa değiştirin

# gProfiler kullanarak enrichment analizi yapın
gp = GProfiler(return_dataframe=True)
results = gp.profile(organism='hsapiens', query=gene_ids, sources=["GO:MF", "GO:BP", "KEGG", "REAC"])

# Enrichment sonuçlarını kaydedin
results.to_csv('../results/enrichment_results.tsv', sep='\t', index=False)
print("Enrichment analizi başarıyla tamamlandı ve sonuçlar kaydedildi.")

# Sonuçları doğrudan terminalde görüntüle
print("GO:BP Sonuçları:")
print(results[results['source'] == 'GO:BP'])

print("\nGO:MF Sonuçları:")
print(results[results['source'] == 'GO:MF'])

print("\nKEGG Sonuçları:")
print(results[results['source'] == 'KEGG'])

print("\nREAC Sonuçları:")
print(results[results['source'] == 'REAC'])
