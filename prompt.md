Sen deneyimli bir prompt mühendisisin. Aşağıda yazdığım bir prompt var. 
Bunu review etmeni ve geliştirmeni istiyorum.

## Prompt'un amacı
[Bu prompt ile ne elde etmek istiyorsun? Örn: "Müşteri e-postalarını 
kibar ve kısa şekilde yanıtlayan bir asistan"]

## Hedef model / kullanım yeri
[Örn: ChatGPT, Claude, API'de system prompt, otomasyon vb.]

## Şu an yaşadığım sorunlar
[Örn: "Çok uzun cevap veriyor", "formatı tutmuyor", "bazen konudan sapıyor"]
(Bilmiyorsan "Henüz test etmedim" yaz.)

## Mevcut prompt
"""
[PROMPT'UNU BURAYA YAPIŞTIR]
"""

## Senden istediklerim
1. Önce prompt'u değerlendir: belirsiz, çelişkili veya eksik kısımları listele.
2. Modelin yanlış anlayabileceği yerleri belirt.
3. Her önerinin NEDEN önemli olduğunu kısaca açıkla.
4. Ardından geliştirilmiş, kullanıma hazır son halini tek blok olarak ver.
5. Orijinal amacımı ve tonumu değiştirme; gereksiz uzatma.
6. Emin olmadığın bir konu varsa varsayım yapmak yerine bana sor.





------------------------------------------------------------------------------------------------








Sen deneyimli bir prompt mühendisisin. Aşağıda yazdığım bir prompt var. 
Bunu review etmeni ve geliştirmeni istiyorum.

"""

Mevcut Java projemizde; Gherkin Web senaryolarından, projede seçilmiş Java test çalışma modeline uygun Cucumber step definition ve test kodunu otomatik üreten bir "Kod Üretici (Generator)" uygulaması geliştireceğiz. Bu uygulama Cursor IDE içinde bir bütün halinde çalışacaktır. Senden bu uygulamanın tüm mimarisini, core motorunu ve doğrulama katmanını tek seferde oluşturmanı istiyorum.

Lütfen aşağıdaki kurallara, mimari sınırlara ve iş akışına göre tüm sınıfları ve testleri eksiksiz yaz:

1. ÖNCELİKLİ TEKNİK ANALİZ VE KONFİGÜRASYON (Hardcoded Kod Yasağı)
- İlk olarak projedeki bağımlılıkları (pom.xml/build.gradle) ve mevcut runner ayarlarını incele. Hedef runtime'ın "Cucumber Java + Selenium" mu yoksa "Karate" mi olduğunu dinamik olarak tespit et. 
- Bu iki runtime'ın API'leri kesinlikle birbirine karıştırılmamalıdır! Eğer proje her ikisini de istiyorsa, bunları ortak Gherkin girdisi kullanan ayrı üretim adaptörleri şeklinde kurgula.
- Java sürümü, paket yapısı, dosya düzeni ve hedef klasörleri dinamik olarak okuyacak parametrik bir konfigürasyon yapısı (JSON veya YAML) oluştur. Kod içine varsayılanları gizlice sabitleme.

2. GHERKIN PARSER & VALIDATOR (Hata Raporlama)
- Girdi olarak gelen `.feature` dosyalarını doğrulayan bir katman yaz.
- Geçersiz Gherkin yapısı veya desteklenmeyen bir Web adımı tespit edildiğinde süreci sessizce tamamlama; üretimi başarısız say ve hangi adımın neden üretilemediğini açık, anlaşılır bir hata raporu ile sun. Kısmi başarıyı kabul etme.

3. STEP DEFINITION GENERATOR & TEKRARLANAN STEP YÖNETİMİ
- Given/When/Then sorumluluklarını ve hiyerarşisini koruyarak Java test/step kodunu üret.
- Parametre aktarımlarını, regex/cucumber expression eşleşmelerini ve metin kaçışlamalarını (string escaping) Java standartlarına uygun ve güvenli şekilde yap.
- Aynı anlamı taşıyan ve birden fazla senaryoda mükerrer olan adımları (tekrarlanan step) akıllıca yönet. Aynı adım için çakışan veya yinelenen sınıf/metot tanımı üretilmesini kesinlikle engelle, ortak step'e kontrollü biçimde eşle.
- Web etkileşimlerini (tıklama, yazma vb.) doğrudan hardcoded element bularak yapma; projenin mevcut Page Object / Locator mapping sözleşmesi ile uyumlu hale getir. Eğer bu arayüz henüz hazır değilse, kod içinde soyut (Abstract/Interface) bir sözleşme tanımlayarak bağımlılığı oraya bağla.

4. DERLEME, SMOKE TEST VE IDEMPOTENCY (DoD Kriterleri)
- Üretilen Java kaynaklarının proje bağımlılıklarıyla derlenebilir olduğunu doğrulamak için programatik olarak Maven/Gradle derleme kontrolünü (Compilation Checker) tetikle. Derlenemeyen kodu başarılı sayma.
- Derleme sonrası, seçilen runner ile en az bir temsilî Web senaryosunu yürüten bir Smoke Test mekanizması kur.
- Idempotency Güvencesi: Generator aynı Gherkin girdisiyle tekrar çalıştırıldığında gereksiz ve çakışan Java kaynakları oluşturmamalı, mevcut dosyaları bozmamalıdır.
- Kapsam Sınırı: Mobil Appium kod üretiminin bu işin kapsamında OLMADIĞINI, bunun ayrı bir mobil işi olduğunu belirten mimari sınırlar dokümanını (README.md) oluştur.

5. BİRİM TESTLERİ (Unit Tests)
- Yazdığın generator motoru için; Given/When/Then eşlemesi, parametre aktarımı, metin kaçışlama, çakışan step davranışı ve geçersiz girdilerdeki hata fırlatma mekanizmalarını doğrulayan birim testlerini de eksiksiz ekle.

Tüm bu akışı yöneten ana orchestrator sınıfını, konfigürasyon şablonunu ve testlerini tek bir bütün halinde oluşturmaya başla.


"""

## Senden istediklerim
1. Önce prompt'u değerlendir: belirsiz, çelişkili veya eksik kısımları listele.
2. Modelin yanlış anlayabileceği yerleri belirt.
3. Her önerinin NEDEN önemli olduğunu kısaca açıkla.
4. Ardından geliştirilmiş, kullanıma hazır son halini tek blok olarak ver.
5. Orijinal amacımı ve tonumu değiştirme; gereksiz uzatma.
6. Emin olmadığın bir konu varsa varsayım yapmak yerine bana sor.


----------------------------------------------------------------------------------------








Sen bir AI Test Automation Agent Engine'sın (Java dünyası için özelleştirilmiş, UI Element Keşfi ve İngilizce Gherkin Çeviri yeteneğine sahip bütünleşik bir Stagehand altyapısı gibi). Görevin; teknik olmayan ekiplerden (BA/PO/QA) gelen sözlü/doğal dildeki test senaryolarını alan, bunları analiz eden, arayüzdeki UI elementleri için kararlı locator'lar üreten, ardından bunu İngilizce Gherkin senaryolarına ve derlenebilir Java test koduna dönüştüren uçtan uca bir otomasyon hattı inşa etmektir.

Grok 4.7 High Max modelinin çoklu dosya yönetim ve derin akıl yürütme yeteneklerini kullanarak, aşağıdaki 3 bağımsız ama birbiriyle konuşan mimari katmanı tek bir depo (repository) içinde eksiksiz inşa et:

---

### MİMARİ KATMAN 1: DİNAMİK UI LOCATOR GENERATOR & MULTI-BROWSER VALIDATOR (Task 3)
*Gherkin ve Java kodu üretilmeden önce çalışacak ilk katmandır. Sayfa DOM yapısını inceleyerek kararlı locator'lar seçer.*
1. **Locator Stratejileri Arayüzü:** ID, Name, CSS Selector ve XPath stratejilerini tek bir soyut arayüz üzerinden yönetilebilir kıl.
2. **Akıllı Seçim & Fallback (Yedek) Kuralı:** DOM niteliklerini inceleyerek en kararlı olanı (örn: Dinamik ID'ler yerine statik nitelikleri veya kararlı CSS/XPath kombinasyonlarını) seçen bir öncelik sıralaması yap. İlk tercih başarısızsa tanımlı Fallback zincirini işlet. Tüm seçenekler belirsizse tahmin yapma, hata döndür.
3. **Selenium ile Benzersiz Eşleşme Doğrulaması:** Seçilen locator'ı Selenium WebDriver kullanarak hedef sayfada doğrula. Sıfır eşleşme (Bulunamadı) ve birden fazla eşleşme (Belirsizlik) durumlarını sessizce geçiştirmeyip birbirinden ayır. Belirsiz durumda hata/sonuç döndür.
4. **Multi-Browser Desteği:** Chrome, Firefox ve Edge tarayıcıları üzerinde uyumluluğu doğrula. Desteklenmeyen veya ortam nedeniyle çalıştırılamayan tarayıcıyı açıkça raporla.
5. **Page Object Entegrasyonu:** Doğrulanmış locator bilgisini projenin mevcut Page Object Pattern sözleşmesinin (örn: @FindBy anotasyonları veya JSON eşleme) beklediği biçimde dışa aktarılabilir kıl. Mobil (Appium) locator'ları kesinlikle kapsam dışıdır.

---

### MİMARİ KATMAN 2: CORE TRANSLATOR & ENGLISH GHERKIN GENERATOR (Task 1)
*Ekiplerden gelen ham/sözlü test girdilerini standartlaştırılmış test senaryolarına çeviren katmandır.*
1. **Ortak Kurallar & Platform Ayrımı:** Kaynak senaryolardaki ortak iş kurallarını Web ve Mobil platform farklarına göre ayır. Platform bağlamını (`@Web`, `@Mobile`) açıkça koru. Kaynak metinde açıkça belirtilmeyen hiçbir eylemi veya ön koşulu kafana göre varsayıp ekleme!
2. **English Gherkin Çevirisi:** Girdi adımlarını anlamsal olarak analiz edip temiz, standart İngilizce Gherkin (`Given`, `When`, `Then`, `And`) formatında `.feature` dosyalarına dönüştür. Metinlerdeki dinamik verileri yakalayıp parametrik yapılara (`"Ahmet"`, `500`) güvenle eşle.
3. **Prompt Sürümleri & Doğrulama:** AI promptlarını proje içinde sürümlenebilir yapıda tut. Üretilen çıktının Gherkin yapısal ve anlamsal doğrulamasından geçmesini sağlayan kodlanmış bir Validator yaz. Eksik veya çelişkili girdi durumunda süreci durdurup net hata raporu sun.

---

### MİMARİ KATMAN 3: JAVA STEP DEFINITION & RUNTIME GENERATOR (Task 2)
*Katman 1'in ürettiği Locator'ları ve Katman 2'in ürettiği Gherkin senaryolarını birleştirerek nihai Java test kodunu üreten motor.*
1. **Runtime Tespiti & Konfigürasyon:** Projedeki bağımlılıkları (@pom.xml / @build.gradle) dinamik incele. Hedef runtime'ın "Cucumber Java + Selenium" mu yoksa "Karate" mi olduğunu tespit et. İki framework'ün API'lerini KESİNLİKLE birbirine karıştırma! Paket yapısı ve klasör düzenini parametrik bir konfigürasyondan (JSON/YAML) oku.
2. **Çakışma Önleme (Tekrarlanan Step Yönetimi):** Daha önce üretilmiş ortak adımları/metotları tara. Aynı adım için çakışan veya mükerrer sınıf/metot tanımları oluşturulmasını kesinlikle engelle, ortak tanımla eşle.
3. **Compilation Checker & Smoke Test:** Üretim sonrası Maven/Gradle derleme kontrolünü programatik tetikle. Derleme başarılıysa, seçilen runner üzerinden en az bir temsilî Web senaryosunu yürüten bir Smoke Test koştur.
4. **Idempotency Kontrolü:** Aynı girdi seti tekrar işlendiğinde mevcut Java kaynaklarını bozma, mükerrer kod ekleme.

---

### DOĞRULAMA KÜMESİ & TEST YAKLAŞIMI (Definition of Done)
- Katman 1 için: En az 5 temsilî Web test senaryosu içeren fixture/test sayfası oluştur ve tek/sıfır/birden fazla eşleşme ile fallback davranışlarını birim testlerle doğrula.
- Katman 2 için: Ham metin ile ideal İngilizce Gherkin çıktılarını yan yana içeren bir "Doğrulama Kümesi" kur, regression kontrollerini birim testle yap.
- Katman 3 için: Üretilen kodun derlenebilirliğini ve en az bir smoke testin başarıyla koştuğunu doğrula.
- Projede mobil Appium kod üretiminin veya mobil gesture hareketlerinin bu uygulamanın kapsamında olmadığını net belirten mimari sınırlar dokümantasyonunu (`README.md`) oluştur.

Tüm bu mimariyi, gerekli core sınıfları, locator doğrulama motorunu, prompt yönetim sistemini ve unit testleri tek bir bütün halinde oluşturmaya başla.





-------------------------------------------------------------------------------------------



Sen bir AI Web Test Automation Agent Engine'sın (Java dünyası için özelleştirilmiş, UI Element Keşfi ve İngilizce Gherkin Çeviri yeteneğine sahip bütünleşik bir Stagehand altyapısı gibi). Görevin; teknik olmayan ekiplerden (BA/PO/QA) gelen sözlü/doğal dilledeki test senaryolarını alan, bunları analiz eden, arayüzdeki UI elementleri için kararlı locator'lar üreten, ardından bunu İngilizce Gherkin senaryolarına ve derlenebilir Java test koduna dönüştüren uçtan uca bir WEB otomasyon hattı inşa etmektir. Mobil (Appium) süreçleri tamamen kapsam dışıdır.

Grok 4.7 High Max modelinin çoklu dosya yönetim ve derin akıl yürütme yeteneklerini kullanarak, aşağıdaki 3 bağımsız ama birbiriyle konuşan mimari katmanı tek bir depo (repository) içinde eksiksiz inşa et:

---

### MİMARİ KATMAN 1: DİNAMİK UI LOCATOR GENERATOR & MULTI-BROWSER VALIDATOR (Task 3)
*Gherkin ve Java kodu üretilmeden önce çalışacak ilk katmandır. Sayfa DOM yapısını veya UI kodlarını inceleyerek kararlı locator'lar seçer.*

1. **Öncelikli data-testid / data-test-id Stratejisi:** Web uygulamalarındaki arayüz öğelerini kararlı bir şekilde bulmak ve seçmek için HTML etiketlerine eklenen bu özel öznitelikleri (`data-testid` veya `data-test-id`) birincil ve en yüksek öncelikli locator stratejisi olarak belirle. UI kaynak kodlarına veya DOM yapısına bakıp bu niteliklerin tanımlı olduğu elementleri anında tespit etmeli ve XPath/CSS formatında en öncelikli aday olarak üretmelisin.
2. **Locator Stratejileri Arayüzü:** `data-testid`/`data-test-id` önceliğinin ardından sırasıyla standart ID, Name, CSS Selector ve XPath stratejilerini tek bir soyut arayüz üzerinden yönetilebilir kıl.
3. **Akıllı Seçim & Fallback (Yedek) Kuralı:** DOM niteliklerini inceleyerek en kararlı olanı seçen bir öncelik sıralaması yap. (Sıralama: 1. data-testid / data-test-id, 2. Standart Statik ID, 3. Name, 4. Kararlı CSS, 5. Kararlı XPath). Dinamik ID'leri veya kararsız sınıf isimlerini eliyor olmalısın. İlk tercih başarısızsa tanımlı Fallback zincirini işlet. Tüm seçenekler belirsizse tahmin yapma, hata döndür.
4. **Selenium ile Benzersiz Eşleşme Doğrulaması:** Seçilen locator'ı Selenium WebDriver kullanarak hedef sayfada doğrula. Sıfır eşleşme (Bulunamadı) ve birden fazla eşleşme (Belirsizlik) durumlarını sessizce geçiştirmeyip birbirinden ayır. Belirsiz durumda hata/sonuç döndür.
5. **Multi-Browser Desteği:** Chrome, Firefox ve Edge tarayıcıları üzerinde uyumluluğu doğrula. Desteklenmeyen veya ortam nedeniyle çalıştırılamayan tarayıcıyı açıkça raporla.
6. **Page Object Entegrasyonu:** Doğrulanmış locator bilgisini projenin mevcut Page Object Pattern sözleşmesinin (örn: @FindBy anotasyonları veya JSON eşleme) beklediği biçimde dışa aktarılabilir kıl.

---

### MİMARİ KATMAN 2: CORE TRANSLATOR & ENGLISH GHERKIN GENERATOR (Task 1)
*Ekiplerden gelen ham/sözlü test girdilerini standartlaştırılmış test senaryolarına çeviren katmandır.*

1. **İş Kuralları Analizi:** Kaynak senaryolardaki ortak iş kurallarını Web ortamına göre işle. Kaynak metinde açıkça belirtilmeyen hiçbir eylemi veya ön koşulu kafana göre varsayıp ekleme! Kaynakta olmayan adım eklenmeme kuralını kesinlikle katı tut.
2. **English Gherkin Çevirisi:** Girdi adımlarını anlamsal olarak analiz edip temiz, standart İngilizce Gherkin (`Given`, `When`, `Then`, `And`) formatında `.feature` dosyalarına dönüştür. Metinlerdeki dinamik verileri yakalayıp parametrik yapılara (`"Ahmet"`, `500`) güvenle eşle.
3. **Prompt Sürümleri & Doğrulama:** AI promptlarını proje içinde sürümlenebilir yapıda tut. Üretilen çıktının Gherkin yapısal ve anlamsal doğrulamasından geçmesini sağlayan kodlanmış bir Validator yaz. Eksik veya çelişkili girdi durumunda süreci durdurup net hata raporu sun.

---

### MİMARİ KATMAN 3: JAVA STEP DEFINITION & RUNTIME GENERATOR (Task 2)
*Katman 1'in ürettiği Locator'ları ve Katman 2'in ürettiği Gherkin senaryolarını birleştirerek nihai Java test kodunu üreten motor.*

1. **Runtime Tespiti & Konfigürasyon:** Projedeki bağımlılıkları (@pom.xml / @build.gradle) dinamik incele. Hedef runtime'ın "Cucumber Java + Selenium" mu yoksa "Karate" mi olduğunu tespit et. İki framework'ün API'lerini KESİNLİKLE birbirine karıştırma! Paket yapısı ve klasör düzenini parametrik bir konfigürasyondan (JSON/YAML) oku.
2. **Çakışma Önleme (Tekrarlanan Step Yönetimi):** Daha önce üretilmiş ortak adımları/metotları tara. Aynı adım için çakışan veya mükerrer sınıf/metot tanımları oluşturulmasını kesinlikle engelle, ortak tanımla eşle.
3. **Compilation Checker & Smoke Test:** Üretim sonrası Maven/Gradle derleme kontrolünü programatik tetikle. Derleme başarılıysa, seçilen runner üzerinden en az bir temsilî Web senaryosunu yürüten bir Smoke Test koştur.
4. **Idempotency Kontrolü:** Aynı girdi seti tekrar işlendiğinde mevcut Java kaynaklarını bozma, mükerrer kod ekleme.

---

### DOĞRULAMA KÜMESİ & TEST YAKLAŞIMI (Definition of Done)
- Katman 1 için: En az 5 temsilî Web test senaryosu içeren fixture/test sayfası oluştur; bu sayfada mutlaka `data-testid` ve `data-test-id` niteliklerine sahip elementler yer alsın. Tek/sıfır/birden fazla eşleşme ve fallback davranışlarını birim testlerle doğrula.
- Katman 2 için: Ham metin ile ideal İngilizce Gherkin çıktılarını yan yana içeren bir "Doğrulama Kümesi" kur, regression kontrollerini birim testle yap.
- Katman 3 için: Üretilen kodun derlenebilirliğini ve en az bir smoke testin başarıyla koştuğunu doğrula.
- Projenin sadece ve sadece Web UI otomasyonu için tasarlandığını, Mobil platformların tamamen kapsam dışı olduğunu net belirten bir `README.md` dokümantasyonu oluştur.

Tüm bu mimariyi, gerekli core sınıfları, locator doğrulama motorunu, prompt yönetim sistemini ve unit testleri tek bir bütün halinde oluşturmaya başla.
