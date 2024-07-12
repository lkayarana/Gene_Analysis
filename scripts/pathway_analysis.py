import pandas as pd
import json
from bioservices import KEGG

# Dönüştürülmüş genleri yükleyin
converted_genes = pd.read_csv('../results/converted_significant_genes.tsv', sep='\t')

# Entrez ID'leri alın
entrez_ids = converted_genes['converted_entrez_id'].dropna().astype(str).tolist()

# KEGG servisinden pathway bilgilerini alın
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

# Sinyal yolu analiz sonuçlarını kaydedin
with open('../results/kegg_pathways.json', 'w') as f:
    json.dump(pathways, f, indent=4)

# Başarısız olan Entrez ID'leri kaydedin
with open('../results/failed_entrez_ids.txt', 'w') as f:
    for entrez_id in failed_entrez_ids:
        f.write(f"{entrez_id}\n")

print("Sinyal yolu analizi başarıyla tamamlandı ve sonuçlar kaydedildi.")
print(f"Başarısız olan Entrez ID sayısı: {len(failed_entrez_ids)}")
