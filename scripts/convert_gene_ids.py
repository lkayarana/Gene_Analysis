import pandas as pd

# Converter dosyasını yükleyin
converter = pd.read_csv('../data/converter.tsv', sep=',')

# Anlamlı genleri yükleyin
significant_genes = pd.read_csv('../results/significant_genes.tsv', sep='\t')

# Sütun isimlerini kontrol etme
print("Converter Sütun İsimleri:", converter.columns)
print("Anlamlı Genler Sütun İsimleri:", significant_genes.columns)

# Boşlukları temizleme ve sütunları aynı veri türüne dönüştürme
converter['initial_alias'] = converter['initial_alias'].astype(str).str.strip()
converter['converted_alias'] = converter['converted_alias'].astype(str).str.strip()
significant_genes['converted_alias'] = significant_genes['converted_alias'].astype(str).str.strip()

# NaN değerleri kaldırma
converter = converter.dropna(subset=['initial_alias', 'converted_alias'])
significant_genes = significant_genes.dropna(subset=['converted_alias'])

# Anlamlı genlerle converter'ı doğru eşleştirme sağlamak için birleştirin
# Eşleşme için kullanılan sütunları kontrol edin
merged = significant_genes.merge(converter, left_on='converted_alias', right_on='converted_alias', how='inner')

# Birleşmiş DataFrame'in sütun isimlerini kontrol etme
print("Birleşmiş Sütun İsimleri:", merged.columns)

# Gerekli sütunları seçin ve adlandırın
selected_columns = ['converted_alias', 'mock_rep1', 'mock_rep2', 'mock_rep3',
                    'sars_cov_rep1', 'sars_cov_rep2', 'sars_cov_rep3', 'p_value', 'initial_alias']

# Seçili sütunları kullanarak veriyi yeniden düzenleyin ve kaydedin
cleaned_merged = merged[selected_columns].copy()
cleaned_merged.rename(columns={'initial_alias': 'converted_entrez_id'}, inplace=True)

cleaned_merged.to_csv('../results/converted_significant_genes.tsv', sep='\t', index=False)

print("Gen ID dönüşümü ve veri temizleme başarıyla tamamlandı ve sonuçlar kaydedildi.")
