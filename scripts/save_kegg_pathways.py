import pandas as pd


enrichment_results = pd.read_csv('../results/enrichment_results.tsv', sep='\t')


kegg_pathways = enrichment_results[enrichment_results['source'] == 'KEGG']


pathway_ids = kegg_pathways['native'].tolist()
pathway_names = kegg_pathways['name'].tolist()


with open('../results/kegg_pathways.txt', 'w') as f:
    for pathway_id, pathway_name in zip(pathway_ids, pathway_names):
        f.write(f"Pathway ID: {pathway_id}, Pathway Name: {pathway_name}\n")

print("KEGG Pathways başarıyla txt dosyasına kaydedildi.")
