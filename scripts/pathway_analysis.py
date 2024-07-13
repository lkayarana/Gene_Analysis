import pandas as pd
import json
from bioservices import KEGG


converted_genes = pd.read_csv('../results/converted_significant_genes.tsv', sep='\t')


entrez_ids = converted_genes['converted_entrez_id'].dropna().astype(str).tolist()


kegg = KEGG()
pathways = {}
failed_entrez_ids = []

for entrez_id in entrez_ids:
    try:
        result = kegg.get(f"hsa:{entrez_id}")
        if result:
            pathways[entrez_id] = result
        else:
            failed_entrez_ids.append(entrez_id)
    except Exception as e:
        print(f"Error retrieving pathway for gene {entrez_id}: {e}")
        failed_entrez_ids.append(entrez_id)


with open('../results/kegg_pathways.json', 'w') as f:
    json.dump(pathways, f, indent=4)


with open('../results/failed_entrez_ids.txt', 'w') as f:
    for entrez_id in failed_entrez_ids:
        f.write(f"{entrez_id}\n")

print("Sinyal yolu analizi başarıyla tamamlandı ve sonuçlar kaydedildi.")
print(f"Başarısız olan Entrez ID sayısı: {len(failed_entrez_ids)}")
