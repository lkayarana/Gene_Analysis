import pandas as pd
import json
from bioservices import KEGG

# Dönüştürülmüş genleri yükleyin
converted_genes = pd.read_csv('../results/converted_significant_genes.tsv', sep='\t')

# Entrez ID'leri alın
entrez_ids = converted_genes['converted_entrez_id'].dropna().astype(str).tolist()

# KEGG servisinden pathway bilgilerini alın ve haritalayın
kegg = KEGG()
pathway_maps = {}

# Daha önce kaydettiğimiz pathway ID'leri yükleyin
with open('../results/kegg_pathways.txt', 'r') as f:
    pathway_ids = [line.split(",")[0].split(":")[1].strip() for line in f]

for pathway_id in pathway_ids:
    pathway_maps[pathway_id] = {}
    for entrez_id in entrez_ids:
        try:
            result = kegg.get(f"hsa:{entrez_id}")
            if isinstance(result, str) and pathway_id in result:
                pathway_maps[pathway_id][entrez_id] = result
        except Exception as e:
            print(f"Error retrieving pathway for gene {entrez_id}: {e}")

# Sinyal yolu analiz sonuçlarını kaydedin
output_path = '../results/kegg_pathway_maps.json'
with open(output_path, 'w') as f:
    json.dump(pathway_maps, f, indent=4)

output_path
