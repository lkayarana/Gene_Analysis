import pandas as pd

# Enrichment analizi sonuçlarını yükleyin
enrichment_results = pd.read_csv('../results/enrichment_results.tsv', sep='\t')

# KEGG Pathway ile ilişkili olanları filtreleyin
kegg_pathways = enrichment_results[enrichment_results['source'] == 'KEGG']

# İlgili pathway ID'leri ve isimleri alın
pathway_ids = kegg_pathways['native'].tolist()
pathway_names = kegg_pathways['name'].tolist()

# İlgili sinyal yollarını txt dosyasına kaydedin
with open('../results/kegg_pathways.txt', 'w') as f:
    for pathway_id, pathway_name in zip(pathway_ids, pathway_names):
        f.write(f"Pathway ID: {pathway_id}, Pathway Name: {pathway_name}\n")

print("KEGG Pathways başarıyla txt dosyasına kaydedildi.")
