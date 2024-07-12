# Gene_Analysis

Bu proje, Sars-CoV-2 enfekte ve kontrol grupları arasındaki genetik ve biyolojik farklılıkları transkripsiyon verilerini kullanarak belirlemek amacıyla oluşturulmuştur.

## Proje Yapısı

Gene_Analysis/
│
├── data/ # Veri dosyaları
│ ├── gene_expression.tsv
│ └── converter.tsv.tsv
├── results/ # Analiz sonuçları
│ ├── filtered_gene_expression.tsv
│ ├── significant_genes.tsv
│ ├── enrichment_results.tsv
│ ├── converted_significant_genes.tsv
│ ├── kegg_pathways.txt
│ └── kegg_pathway.json
├── scripts/ # Python script dosyaları
│ ├── filter_genes.py
│ ├── differential_expression_analysis.py
│ ├── enrichment_analysis.py
│ ├── convert_gene_ids.py
│ ├── save_kegg_pathways.py
│ └── pathway_analysis.py
└── README.md 

# Proje açıklamaları ve kurulum adımları

## Gereksinimler

- Python 3.7+
- pandas
- numpy
- scipy
- statsmodels
- requests
- bioservices

## Kurulum

1. Sanal ortamı oluşturun ve etkinleştirin:

    - Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

    - macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

2. Gerekli paketleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

## Adımlar

### 1. Filtreleme

İlk adımda, hiçbir koşulda ifade göstermeyen (read içermeyen) genleri veri setinden çıkardım.

**Kod Dosyası:** `scripts/filter_genes.py`

Bu adımda, pandas kullanarak veri setini yükledim ve hiçbir koşulda ifade göstermeyen genleri filtreledim. Filtrelenmiş veriyi `results/filtered_gene_expression.tsv` dosyasına kaydettim.

### 2. Diferansiyel İfade Analizi

İki koşul arasında anlamlı olarak değişen genleri belirledim. Bunun için p-value 0.05 sınır değerini kullandım.

**Kod Dosyası:** `scripts/differential_expression_analysis.py`

Bu adımda, scipy kullanarak diferansiyel ifade analizi yaptım ve p-value'leri hesapladım. Anlamlı değişen genleri `results/significant_genes.tsv` dosyasına kaydettim.

### 3. Enrichment Analizi

Anlamlı değişmiş gen listesine gProfiler kullanarak enrichment analizi uyguladım ve GO:MF, GO:BP, KEGG ve REAC sonuçlarını raporladım.

**Kod Dosyası:** `scripts/enrichment_analysis.py`

Bu adımda, gProfiler kullanarak anlamlı genlerin zenginleştirme analizini yaptım ve sonuçları `results/enrichment_results.tsv` dosyasına kaydettim.

### 4. Gen ID Dönüşümü

Anlamlı değişen genlerin Ensembl ID'lerini Entrez ID'lere dönüştürdüm.

**Kod Dosyası:** `scripts/convert_gene_ids.py`

Bu adımda, pandas kullanarak gen ID dönüşümünü gerçekleştirdim ve sonuçları `results/converted_significant_genes.tsv` dosyasına kaydettim.

### 5. Sinyal Yolu Analizi

Enrichment analizi sonucundan elde edilen ilişkili sinyal yollarını listeledim ve anlamlı değişen genleri KEGG Pathway kullanarak haritaladım.

**Kod Dosyası:** `scripts/save_kegg_pathways.py` ve `scripts/pathway_analysis.py`

Bu adımda, KEGG Pathway ile ilişkili sinyal yollarını listeledim ve pathway bilgilerini `results/kegg_pathways.txt` dosyasına kaydettim. Daha sonra bu pathway'leri KEGG Pathway sitesinde manuel olarak haritaladım.

### 6. Sonuçların Yorumlanması

Elde edilen sonuçların yorumlanması ve ilgili soruların yanıtlanması:

SARS-CoV-2 enfekte ve kontrol grupları arasındaki genetik ve biyolojik farklılıkları belirlemek amacıyla yapılan bu analiz, enfeksiyonun hücresel düzeyde çeşitli biyolojik süreçleri ve sinyal yollarını nasıl etkilediğini ortaya koymaktadır. Elde edilen sonuçlar, SARS-CoV-2 enfeksiyonunun hücrelerde ciddi biyolojik değişikliklere yol açtığını göstermektedir. Aşağıda, genel olarak elde edilen sonuçların yorumlanması yer almaktadır:

1. **Anlamlı Değişen Genler**
Analiz sonucunda, SARS-CoV-2 enfeksiyonuna maruz kalmış hücrelerde ifade düzeyleri anlamlı şekilde değişen birçok gen belirlenmiştir. Bu genler, enfeksiyonun hücresel yanıtı üzerinde önemli roller oynayabilir.

2. **Enrichment Analizi**
Anlamlı değişen genlerin zenginleştirme analizi, belirli biyolojik süreçlerin ve sinyal yollarının enfeksiyondan etkilendiğini göstermektedir. Özellikle aşağıdaki alanlar dikkat çekicidir:

3. **Bağışıklık Yanıtı ve İnflamasyon**

   - TNF signaling pathway (KEGG:04668)
   - IL-17 signaling pathway (KEGG:04657)
   - NF-kappa B signaling pathway (KEGG:04064)
   - Cytokine-cytokine receptor interaction (KEGG:04060)

Bu pathway'ler, enfeksiyon sırasında aktif hale gelen bağışıklık yanıtları ve inflamatuar süreçlerle ilgilidir. SARS-CoV-2 enfeksiyonu, hücrelerin inflamatuar yanıtlarını tetikleyebilir ve bu da hastalığın şiddetini etkileyebilir.

4. **Viral Enfeksiyon Mekanizmaları**

   - Influenza A (KEGG:05164)
   - Epstein-Barr virus infection (KEGG:05169)
   - Kaposi sarcoma-associated herpesvirus infection (KEGG:05167)
   - Hepatitis B (KEGG:05161)
   - Measles (KEGG:05162)

Bu pathway'ler, viral enfeksiyon mekanizmalarıyla ilgilidir ve SARS-CoV-2 enfeksiyonunun, diğer viral enfeksiyonlarla ortak biyolojik süreçleri etkilediğini göstermektedir. Bu, SARS-CoV-2'nin hücreleri enfekte etme ve yayılma yolları hakkında önemli ipuçları sağlayabilir.

5. **Metabolik Süreçler ve Hücresel Stres**

   - Lipid and atherosclerosis (KEGG:05417)
   - Fluid shear stress and atherosclerosis (KEGG:05418)
   - Alcoholic liver disease (KEGG:04936)
   - Apoptosis (KEGG:04210)
   - 
Bu pathway'ler, enfeksiyon sonrası hücrelerin metabolik süreçlerinin ve hücresel stres tepkilerinin etkilendiğini göstermektedir. Özellikle lipid metabolizması ve hücre ölümü (apoptoz) gibi süreçlerdeki değişiklikler, enfeksiyonun hücresel homeostaz üzerinde nasıl etkili olduğunu göstermektedir.

6. **Hücre Büyümesi ve Kanser**
*Bladder cancer (KEGG:05219)*
Bu pathway, SARS-CoV-2 enfeksiyonunun hücre büyümesi ve kanserle ilişkili biyolojik süreçleri nasıl etkileyebileceğine dair ipuçları sunmaktadır. Enfeksiyonun, hücre proliferasyonunu ve kanser gelişimini etkileyebileceği göz önünde bulundurulmalıdır.

Analiz sonuçları, SARS-CoV-2 enfeksiyonunun hücrelerde geniş kapsamlı biyolojik değişikliklere neden olduğunu göstermektedir. Bu değişiklikler, enfeksiyonun bağışıklık yanıtı, inflamasyon, viral enfeksiyon mekanizmaları, metabolik süreçler ve hücre büyümesi üzerinde önemli etkiler yapabileceğini göstermektedir. Bu bulgular, SARS-CoV-2'nin patogenezini anlamak ve enfeksiyonun hücresel etkilerini daha iyi kavramak için önemli bilgiler sunmaktadır.

Elde edilen bu bulgular, COVID-19 tedavisi ve yönetimi için potansiyel hedefler ve stratejiler geliştirmek amacıyla kullanılabilir. Özellikle enfeksiyonun tetiklediği spesifik biyolojik süreçler ve sinyal yolları üzerine odaklanarak, daha etkili terapötik müdahaleler ve tedavi yaklaşımları geliştirilebilir.

Belirlenen pathway'ler ve genler, COVID-19 tedavisinde hedefe yönelik terapötik stratejilerin geliştirilmesi için potansiyel adaylar olarak değerlendirilebilir.
Anlamlı değişim gösteren genler ve pathway'ler, hastalığın seyrini ve tedaviye yanıtı izlemek için biyobelirteç olarak kullanılabilir.
Gelecek Araştırmalar: Elde edilen sonuçlar, SARS-CoV-2 enfeksiyonunun hücresel etkilerini daha derinlemesine incelemek için ileri araştırmalar için bir temel oluşturabilir.

1. **Herhangi bir disease veya viral enfeksiyon ile ilgili bir terim elde ettiniz mi?**
Evet, analiz sonucunda elde edilen pathway'ler arasında çeşitli hastalıklar ve viral enfeksiyonlarla ilişkili olanlar bulunmaktadır:
    - Influenza A (KEGG:05164)
    - Epstein-Barr virus infection (KEGG:05169)
    - Kaposi sarcoma-associated herpesvirus infection (KEGG:05167)
    - Hepatitis B (KEGG:05161)
    - Measles (KEGG:05162)
    - Bladder cancer (KEGG:05219)

2. **Enfeksiyon sonrası hücrelerin metabolik süreçleri etkilenmiş mi?**
Evet, enfeksiyon sonrası hücrelerin metabolik süreçlerinin etkilendiğini gösteren pathway'ler de bulunmaktadır:
    - Lipid and atherosclerosis (KEGG:05417)
    - Fluid shear stress and atherosclerosis (KEGG:05418)
    - Alcoholic liver disease (KEGG:04936)

3. **P-value sınır değerini arttırmak veya azaltmak sonuçlarınızı nasıl değiştirebilirdi?**
P-value sınır değerini değiştirmek, anlamlı değişim gösteren genlerin ve buna bağlı olarak zenginleştirilmiş pathway'lerin sayısını ve türünü etkileyebilir. Daha düşük bir p-value sınır değeri, daha katı bir anlamlılık kriteri sunarak daha güvenilir sonuçlar elde etmeye yardımcı olabilir, ancak bazı anlamlı değişiklikleri kaçırma riski taşır. Daha yüksek bir p-value sınır değeri ise daha fazla gen ve pathway belirleyerek daha geniş kapsamlı bir analiz sunabilir, ancak yanlış pozitiflerin sayısını arttırabilir.

**Genel Değerlendirme:**
Analiz sonuçları, SARS-CoV-2 enfeksiyonunun hücrelerde geniş kapsamlı biyolojik değişikliklere neden olduğunu göstermektedir. Bu değişiklikler, enfeksiyonun bağışıklık yanıtı, inflamasyon, viral enfeksiyon mekanizmaları, metabolik süreçler ve hücre büyümesi üzerinde önemli etkiler yapabileceğini göstermektedir. Bu bulgular, SARS-CoV-2'nin patogenezini anlamak ve enfeksiyonun hücresel etkilerini daha iyi kavramak için önemli bilgiler sunmaktadır.
