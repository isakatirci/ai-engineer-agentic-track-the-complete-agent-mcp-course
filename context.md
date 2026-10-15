Bu sayfa, ders başlıklarını ve bölüm kapsamını doğrulamamı sağlayacak. Mevcut belgeyi müfredatla karşılaştırıp eksikleri tamamlayacağım; junior geliştiriciler için eklediğim hazırlık konularını özgün kurs içeriğinden ayrı tutacağım. Ders listesi eksiksiz doğrulansa bile, her derste anlatılan tüm ayrıntılar için tam altyazıların gerektiğini de belirteceğim.
İçerik sayfası, önceki belgede eksik kalan konuları doğruluyor: Google ADK, A2A, Strands, Pydantic AI, Microsoft Agent Framework, Agno, Mastra ve FastAPI/React bunlar arasında.

Sayfanın kendi içinde de bir fark var: proje tanıtımı AutoGen ile “Agent Creator” diyor; 5. haftanın ders listesi ise çoklu framework kullanan “Agent Loop” projesini gösteriyor. Belgeyi güncellerken ikisini de koruyup bu farkı belirteceğim. Böylece sayfada listelenen kapsamı eksiksiz aktarabiliriz; videoların içindeki bütün ayrıntıları doğruladığımızı ise söylemeyiz.
İçerik sayfası, önceki belgede eksik kalan Google ADK, A2A, Strands, Pydantic AI, Agno ve Mastra gibi konuları da doğruluyor. Ayrıca tanıtımdaki “AutoGen ile Agent Creator” projesiyle güncel 5. hafta ders listesi arasında bir fark var. Belgeyi tüm 132 ders kaydını kapsayacak şekilde güncelleyip bu farkı açıkça belirteceğim; sayfanın doğruladığı içerikle junior’lar için önerdiğim ek çalışmaları ayrı tutacağım.
Bu sayfa sayesinde kapsamı artık yalnızca kapanış altyazısından değil, **kursun gerçek ders envanterinden** oluşturabiliyoruz. Önceki context’te eksik kalan önemli konular var: **Google ADK, A2A, Strands, Pydantic AI, Microsoft Agent Framework, Agno, Mastra, LangSmith, SQLiteSession, Deep Agents Skills, Context7 MCP, Qdrant, FastAPI ve React** bunların arasında.

Ayrıca kaynakların kendi içinde bir fark var: Tanıtım bölümünde **7. proje “AutoGen ile Agent Creator”** olarak anlatılırken, ayrıntılı beşinci hafta müfredatında **birden fazla framework’ün birlikte çalıştığı Agent Loop projesi** bulunuyor. İkisini aynı proje gibi göstermeden korumak gerekiyor.

**Kesinlik sınırı:** Bu sayfayla ilan edilen ders ve konu kapsamını doğrulayabiliriz; videolarda geçen her kod satırını, alt açıklamayı ve ödevi yüzde yüz doğrulayamayız. Aşağıdaki context, **sayfadaki 132 ders kaydının tamamını kapsayacak şekilde**, kaynakta sorunlu görünen başlıkları da işaretleyerek hazırlanmıştır.

---

# Agentic AI Engineering — Junior’dan Bağımsız AI Uygulama Geliştiricisine
## Gerçek kurs müfredatına dayalı kapsamlı kurs context’i

## 1. Belgenin amacı ve kullanım biçimi

Bu belge, **AI Engineer Agentic Track: The Complete Agent & MCP Course** kursunun doğrulanabilen içerik kapsamını, agentic AI konusunda başlangıç seviyesindeki junior geliştiriciler için bir öğrenme bağlamına dönüştürür.

Belge üç farklı bilgi türünü birbirinden ayırır:

| İşaret | Anlam |
|---|---|
| **[Kaynak]** | Yüklenen kurs sayfasında doğrudan bulunan başlık, proje, araç veya açıklama. |
| **[Öğretim tasarımı]** | Konunun junior geliştiriciye nasıl öğretileceğine ilişkin önerilen açıklamalar, uygulamalar ve başarı kriterleri. |
| **[Doğrulama notu]** | Kaynaklar arasındaki farklar veya mevcut belgelerin kesinleştirmediği ayrıntılar. |

**Temel kural:** Öğretim tasarımındaki eklemeler, özgün eğitmenin bütün bu ayrıntıları anlattığı iddiasıyla sunulmaz.

---

## 2. Kursun doğrulanmış kimliği

| Alan | Kurs sayfasındaki bilgi |
|---|---|
| Kurs adı | AI Engineer Agentic Track: The Complete Agent & MCP Course |
| Eğitmenler | Ed Donner, Ligency |
| Görünen son güncelleme | 09/2026 |
| Dil | İngilizce |
| Yapı | 6 bölüm, 132 ders |
| Toplam süre | 20 saat 52 dakika |
| Eğitim yaklaşımı | Uygulamalı, proje tabanlı agentic AI geliştirme |
| Tanıtılan ana proje sayısı | 8 |
| Eğitim rotası | Temeller → framework’ler → MCP → kapsamlı final uygulaması |
| Ek materyal | Temel teknik ve programlama becerileri için self-study lab klasörü; sayfada ayrıca 1 makale belirtiliyor |

**[Kaynak]** Python ve LLM deneyimi faydalı görülüyor; ancak kurs farklı geçmişlerden gelen öğrencileri hedeflediğini söylüyor.

**[Kaynak]** Eğitmen, API harcaması olmadan tamamlamanın mümkün olduğunu; frontier modeller kullanıldığında tipik harcamanın 5 doların altında olabileceğini belirtiyor.

**[Doğrulama notu]** Bu bir maliyet garantisi değildir. Model fiyatları, deneme sayısı, araç kullanımı ve öğrencinin uygulamaları maliyeti değiştirebilir. Video süresi de öğrenme, uygulama ve hata ayıklama süresiyle aynı değildir.

---

## 3. Hedef: “Sıfırdan hero” ne demek?

### Başlangıç profili

**[Öğretim tasarımı]** Öğrenci temel programlama bilgisine sahip bir junior geliştiricidir; fakat aşağıdaki alanlarda başlangıç seviyesindedir:

- LLM API’leri ve model sağlayıcıları.
- Tool calling ve agent loop.
- Çok ajanlı orkestrasyon.
- Context, state ve memory yönetimi.
- MCP ve A2A.
- Ajan uygulamalarında test, tracing ve değerlendirme.
- AI uygulamasını kullanıcıya sunma.

Hiç programlama bilmeyen öğrenci için hazırlık çalışmaları gerekir. “Agentic AI konusunda sıfırdan başlamak” ile “programlamayı da sıfırdan öğrenmek” aynı başlangıç noktası değildir.

### Hedef mezun profili

Öğrenci kurs sonunda yalnızca örnek kodları çalıştıran kişi olmamalıdır. Sınırları belli bir problemi ele alıp şu süreci bağımsız yürütebilmelidir:

**Problemi tanımla → basit çözüm kur → araç ekle → gerektiğinde ajanlaştır → sonucu ölç → hatayı teşhis et → arayüz oluştur → dağıt → sınırlamaları açıkla.**

Buradaki “hero”, senior mühendislik unvanı veya her ölçekte üretim sistemi kurma garantisi değildir. **Yeni bir agentic AI uygulamasını, hazır ders adımlarını birebir izlemeksizin geliştirebilme yeterliliğidir.**

### Mezuniyet yetkinlikleri

| Yetkinlik | Öğrencinin göstereceği davranış |
|---|---|
| Problem çözümleme | LLM, sabit workflow ve otonom ajan arasında gerekçeli seçim yapar. |
| Temel uygulama geliştirme | Model API’sini çağırır, yapılandırmayı ayırır, hataları yönetir. |
| Araç entegrasyonu | Araç tanımlar, girdileri doğrular, sonucu işler. |
| Orkestrasyon | Kodla yönetim, agents-as-tools ve handoff arasındaki farkı uygular. |
| Veri sözleşmeleri | Pydantic ve yapılandırılmış çıktılarla bileşenler arası aktarımı düzenler. |
| Context yönetimi | Geçmiş, memory, görev state’i, araç sonuçları ve retrieval’ı ayırır. |
| Framework seçimi | Araçları popülerliğe değil ihtiyaca göre karşılaştırır. |
| Gözlemlenebilirlik | Model cevabını değil gerçek araç çağrılarını ve akış kayıtlarını inceler. |
| Güvenilirlik | Başarısızlık, tekrar deneme, sonlanma ve onay yollarını tasarlar. |
| Teslim | Çalışan uygulama, test kanıtı ve anlaşılır dokümantasyon sunar. |

---

## 4. Kursun bütününü taşıyan zihinsel model

**[Öğretim tasarımı]** Bütün framework’ler şu temel yapı üzerinden anlatılmalıdır:

> Bir ajan uygulaması; bir hedef, modele verilen context, kullanılabilir araçlar, uygulama state’i, yürütme döngüsü, izin sınırları ve sonlanma koşullarının birlikte tasarlanmasıdır.

Öğrenci özellikle şu ayrımları öğrenmelidir:

| Kavram | Temel anlamı |
|---|---|
| Model | Verilen girdiden çıktı üreten LLM. |
| Tool | Uygulamanın gerçekten yürüttüğü, tanımlı bir işlev. |
| Agent loop | Model çıktısı, araç çalıştırma ve yeni model çağrıları arasındaki döngü. |
| Workflow | Adımları ve geçişleri önemli ölçüde kodla belirlenmiş süreç. |
| Orchestration | Ajanların, araçların ve alt görevlerin koordinasyonu. |
| State | Devam eden görevin mevcut durumu. |
| Memory | Sonraki etkileşimlerde kullanılmak üzere saklanan bilgi. |
| Context | Belirli bir model çağrısına o anda verilen bilgi. |
| Guardrail | Girdi, çıktı veya eylem üzerinde uygulanan sınır ve kontrol. |
| Evaluation | Sistemin görevini ne kadar doğru yaptığının ölçülmesi. |
| Trace | Çalışma sırasında gerçekleşen çağrıların ve adımların iz kaydı. |
| MCP | Uygulamaların araç ve bağlam sağlayan sunucularla standartlaştırılmış iletişimi. |
| A2A | Ajanlar arası iletişim ve birlikte çalışma için ayrı bir protokol yaklaşımı. |
| Agent harness | Ajanın görev yürütmesini destekleyen araç, bağlam ve çalışma ortamı düzeni. |

MCP ile A2A, memory ile context veya framework ile model aynı şeymiş gibi öğretilmemelidir.

---

# 5. Eksiksiz ders envanteri ve haftalık öğrenme context’i

Aşağıdaki İngilizce başlıklar, kaynakla karşılaştırma yapılabilmesi için korunmuştur. Numaralar bu belge için baştan sona verilmiştir.

## Hafta 1 — Temeller, sağlayıcılar ve kendi ajan döngünü kurma

**[Kaynak] 28 ders · yaklaşık 5 saat 28 dakika**

### Öğrenme bağlamı

Öğrenci önce n8n ile bir ajan örneğini görür; ardından Python ortamını kurar, model API’lerini çağırır ve framework kullanmadan tool-calling döngüsü geliştirir.

Bu haftanın amacı yalnızca ilk chatbot’u yapmak değildir. **Ajanın arkasında ne olduğunu göstermek ve sonraki framework’lerin hangi sorumlulukları üstlendiğini anlaşılır kılmaktır.**

### Derslerin tamamı

| No | Kaynaktaki ders başlığı | Süre |
|---:|---|---:|
| 1 | Day 1 - Build Your First Autonomous AI Agent with n8n (No-Code Demo) | 14:30 |
| 2 | Day 1 - Course Roadmap: 6 Weeks, 8 Projects in Agentic AI Engineering | 13:00 |
| 3 | Your Path to Becoming a Proficient AI Engineer | 3:42 |
| 4 | Day 1 - Environment Setup Overview: UV, API Keys, Costs and GitHub Repo | 11:51 |
| 5 | Day 1 - Windows Setup: Install Cursor, Git, Clone the Repo and Run UV | 16:20 |
| 6 | Day 1 - Mac Setup: Install Cursor, Git, Clone the Repo and Run UV | 12:00 |
| 7 | Day 1 - Set Up Your OpenAI API Key and .env File for the First Lab | 18:20 |
| 8 | Day 1 - Your First OpenAI API Call and Chaining LLM Calls in Python | 13:49 |
| 9 | Day 2 - What Is an AI Agent? Definitions, Workflows vs Agents Explained | 11:34 |
| 10 | Day 2 - Agentic AI Design Patterns: Chaining, Routing, Orchestrator | 8:35 |
| 11 | Day 2 - Agentic AI Risks, Guardrails, Evals and Traps to Avoid | 16:39 |
| 12 | Day 3 - LLM Providers Compared: OpenAI, Claude, Gemini, Ollama, Groq | 10:12 |
| 13 | Day 3 - Set Up Multiple LLM API Keys and Generate a Question to Ask | 7:58 |
| 14 | Day 3 - Call 8 LLMs with the OpenAI-Compatible API: GPT, Claude, Gemini | 10:32 |
| 15 | Day 3 - Install Ollama and Run Local LLMs: Llama, GPT-OSS and Gemma | 10:25 |
| 16 | Day 3 - LLM as a Judge: Rank Multiple LLMs with an Orchestration Flow | 9:51 |
| 17 | Day 4 - The Agent Landscape: Frameworks, Runtimes, Tools and Builders | 15:43 |
| 18 | Day 4 - How Tool Calling Works: The Truth Behind AI Agent Autonomy | 8:50 |
| 19 | Day 4 - Start the Digital Twin: Read a PDF and Master System Prompts | 13:42 |
| 20 | Day 4 - Build a Chat UI with Gradio and Define Your First Agent Tool | 16:15 |
| 21 | Day 4 - Build the Agent Loop From Scratch: Tool Calling with a While Loop | 16:07 |
| 22 | Day 5 - Context Engineering for AI Agents: Memory, Tools and RAG | 10:38 |
| 23 | Day 5 - Add Tools to Your Digital Twin Agent with Pushover Notifications | 9:09 |
| 24 | Day 5 - Handle Multiple Tool Calls in Python with the globals Trick | 4:05 |
| 25 | Day 5 - Build the Digital Twin Agent Loop and Test It Live in Gradio | 5:18 |
| 26 | Day 5 - Refactor the Digital Twin Agent into Python Modules and Run It | 9:43 |
| 27 | Day 5 - Deploy Your Digital Twin AI Agent to Hugging Face Spaces | 15:45 |
| 28 | Day 5 - Build a Visible Agent Loop with Checklist Tools Like Claude Code | 13:07 |

### Junior için işlenecek açıklamalar

**[Öğretim tasarımı]**

**Kurulum ve çalışma ortamı:** Cursor’ın editör, Git’in sürüm kontrol aracı, GitHub’ın kod barındırma platformu, `uv`’nin Python ortamı ve paket yönetimi aracı olduğu ayrıştırılır. `.env`, API anahtarı ve bağımlılıkların neden koddan ayrı tutulduğu gösterilir.

**Model sağlayıcıları:** Model, sağlayıcı, barındırma servisi ve yerel çalıştırma birbirine karıştırılmaz. OpenAI-compatible API kullanmanın farklı modellerin bütün özelliklerini aynı hale getirmediği açıklanır.

**Ajan desenleri:** Chaining, routing ve orchestration ayrı örneklerle anlatılır. Deterministik bir görev için gereksiz otonomi eklenmez.

**LLM-as-a-judge:** Bir modelin diğer çıktıları değerlendirmesi gösterilir; ancak bu değerlendirme mutlak gerçek veya tarafsız ölçüm sayılmaz.

**Tool calling:** Modelin araç çağrısı istemesi ile Python fonksiyonunun gerçekten çalışması ayrı olaylar olarak incelenir. Araç sonucunun konuşmaya geri eklenmesi ve döngünün ne zaman duracağı açıkça gösterilir.

**`globals()` yaklaşımı:** Kaynaktaki yöntem öğrenilir; ek mühendislik pratiği olarak yalnızca izin verilen fonksiyonlardan oluşan açık bir araç kayıt tablosuyla karşılaştırılır.

**Digital Twin:** PDF’den gelen profil bilgisi, system prompt, sohbet geçmişi, bildirim araçları ve kullanıcı arayüzü birlikte çalışır. Profilde bulunmayan bilgileri uydurma davranışı özellikle test edilir.

**Görünür görev takibi:** Checklist araçları, kullanıcının işin ilerleyişini görmesini sağlar; gösterilen planın işin gerçekten tamamlandığı anlamına gelmediği vurgulanır.

### Haftalık teslim

Çalışan ve Hugging Face Spaces üzerinde sunulabilen bir Career Digital Twin; yanında örnek sorular, bilinmeyen bilgi testi ve gerçek araç çağrısı kaydı.

---

## Hafta 2 — OpenAI Agents SDK, orkestrasyon ve araştırma

**[Kaynak] 21 ders · yaklaşık 3 saat 49 dakika**

### Öğrenme bağlamı

İlk haftada elle kurulan döngü, bu hafta SDK kavramlarıyla yeniden ele alınır. Öğrenci SDK’yı sihirli bir katman olarak değil, bazı yürütme sorumluluklarını devralan bir geliştirme aracı olarak öğrenir.

### Derslerin tamamı

| No | Kaynaktaki ders başlığı | Süre |
|---:|---|---:|
| 29 | Day 1 - OpenAI Agents SDK Intro and Async Python (asyncio) Explained | 14:00 |
| 30 | Day 1 - OpenAI Agents SDK Core Concepts: Agent, Trace and Runner.run | 13:45 |
| 31 | Day 1 - Build Your First Agent with OpenAI Agents SDK: Runner and Tracing | 13:32 |
| 32 | Day 1 - Add Tools to an Agent with the function_tool Decorator | 10:52 |
| 33 | Day 1 - Adding Memory to Agents with Sessions and SQLiteSession | 10:49 |
| 34 | Day 2 - Build a Multi-Agent Sales Team and Orchestrate Agents Three Ways | 3:17 |
| 35 | Day 2 - Set Up Email Sending Tools for Your AI Sales Agents | 9:06 |
| 36 | Day 2 - Agent Orchestration by Code vs by LLM in the OpenAI Agents SDK | 7:13 |
| 37 | Day 2 - Orchestrate Multiple Sales Agents by Code with asyncio.gather | 12:12 |
| 38 | Day 2 - Orchestrate Agents as Tools with a Sales Manager Agent | 7:33 |
| 39 | Day 2 - Orchestrate Agents with Handoffs in the OpenAI Agents SDK | 10:28 |
| 40 | Day 3 - Use Any LLM with the OpenAI Agents SDK: Gemini, Groq and More | 16:06 |
| 41 | Day 3 - Structured Outputs with Pydantic in the OpenAI Agents SDK | 15:53 |
| 42 | Day 3 - Build Guardrails for AI Agents Plus Sandboxes and MCP | 20:53 |
| 43 | Day 4 - Plan a Deep Research AI Agent with the OpenAI Agents SDK | 5:24 |
| 44 | Day 4 - Build a Web Search Agent with OpenAI Agents SDK Hosted Tools | 8:28 |
| 45 | Day 4 - Build Planner, Writer and Email Agents with Structured Outputs | 8:16 |
| 46 | Day 4 - Run the Full Deep Research Agent Orchestrated by Code | 13:28 |
| 47 | Day 5 - Turn Your Deep Research Agent into Python Modules for Deploy | 9:27 |
| 48 | Day 5 - Build a Gradio UI for Your Deep Research AI Agent | 8:49 |
| 49 | Day 5 - Deploy Your Deep Research Gradio App to Hugging Face Spaces | 9:33 |

### Junior için işlenecek açıklamalar

**[Öğretim tasarımı]**

**Async Python:** `async`, `await` ve `asyncio.gather` önce küçük örneklerle gösterilir. Eşzamanlı API istekleri ile CPU paralelliği aynı kavram olarak anlatılmaz.

**SDK modeli:** `Agent`, `Runner.run`, `Trace`, `function_tool`, session ve çıktı nesnelerinin sorumlulukları ayrılır.

**Memory:** `SQLiteSession` üzerinden konuşma sürekliliği öğrenilir. Saklanan geçmişin her zaman doğru, gerekli veya sınırsız biçimde kullanılabilir olmadığı açıklanır.

**Üç orkestrasyon yaklaşımı:**

| Yaklaşım | Ana kontrol |
|---|---|
| Kodla orkestrasyon | Hangi adımın ne zaman çalışacağı uygulama tarafından belirlenir. |
| Agents-as-tools | Yönetici ajan, başka ajanları araç gibi çağırır. |
| Handoff | İşin yürütülmesi başka bir ajana devredilir. |

**Yapılandırılmış çıktılar:** Pydantic şemalarıyla beklenen veri biçimi tanımlanır. Şemaya uygun bir cevabın içerik olarak doğru olduğu varsayılmaz.

**Guardrails ve sandbox:** Kontrol mekanizmalarının nerede uygulandığı ve hangi hataları kapsamadığı gösterilir.

**SDR:** E-posta yazma ve gönderme ayrı sorumluluklar olarak ele alınır. Öğretim tasarımında gerçek gönderimden önce taslak, test adresi ve onay kullanılır.

**Deep Research:** Araştırma planı, arama, rapor yazımı ve e-posta adımları ayrı bileşenler olarak geliştirilir. Web arama sonucuyla kaynak içeriğinin aynı şey olmadığı açıklanır.

### Haftalık teslim

Bir SDR uygulaması ve kaynakları izlenebilir bir Deep Research uygulaması. Araştırma uygulaması Gradio arayüzüyle Hugging Face Spaces üzerinde sunulur.

---

## Hafta 3 — CrewAI, finansal araştırma ve kod üreten ekipler

**[Kaynak] 19 ders · yaklaşık 3 saat 19 dakika**

### Öğrenme bağlamı

Bu hafta rol, görev, ekip ve çıktı sözleşmeleri üzerinde durulur. Öğrenci birden fazla ajan tanımlamayı değil, **işi gerçekten bölmeyi ve sonuçların birbirine güvenilir biçimde aktarılmasını** öğrenir.

### Derslerin tamamı

| No | Kaynaktaki ders başlığı | Süre |
|---:|---|---:|
| 50 | Day 1 - Intro to CrewAI: Crews, Flows, and the Open Source Framework | 6:04 |
| 51 | Day 1 - CrewAI Core Concepts: Agents, Tasks, Crews, and YAML Files | 10:32 |
| 52 | Day 1 - Installing CrewAI with uv tool and Setting Up Skills | 8:57 |
| 53 | Day 1 - Build Your First Crew: crewai create crew and crewai run | 14:31 |
| 54 | Day 1 - Build a CrewAI Debate Crew: Define Agents and Tasks in YAML | 6:57 |
| 55 | Day 1 - Wire Up crew.py and main.py to Run a CrewAI Debate | 11:15 |
| 56 | Day 2 - The 5 Steps to Build Any CrewAI Project with Tools and Context | 8:41 |
| 57 | Day 2 - Build a Financial Researcher Crew with YAML, Context, and Tools | 12:28 |
| 58 | Day 2 - Add the Serper Tool to a CrewAI Financial Researcher and Run It | 10:20 |
| 59 | Day 3 - Stock Picker Crew: Structured Outputs, Custom Tools, Memory | 7:15 |
| 60 | Day 3 - Define Pydantic Structured Outputs for the Stock Picker Crew | 12:29 |
| 61 | Day 3 - Custom Tools, Memory, and Hierarchical Process in CrewAI | 17:41 |
| 62 | Day 4 - Build a CrewAI Coding Agent: Intro and Installing Docker | 7:22 |
| 63 | Day 4 - Build Custom Sandbox Tools for a CrewAI Coding Agent | 9:20 |
| 64 | Day 4 - Run Python in a Docker Sandbox with a CrewAI Coding Agent | 8:27 |
| 65 | Day 5 - Build a CrewAI Engineering Team: Define the Four AI Agents | 8:39 |
| 66 | Day 5 - Wire Up Engineering Team Tasks and crew.py with Context7 MCP | 9:10 |
| 67 | Day 5 - Build UV Sandbox Tools and Set Requirements for the AI Team | 11:01 |
| 68 | Day 5 - Run the CrewAI Engineering Team with Multiple LLM Models | 17:42 |

### Junior için işlenecek açıklamalar

**[Öğretim tasarımı]**

**CrewAI yapısı:** Agent, task, crew ve flow kavramları birbirinden ayrılır. YAML’daki tanımların `crew.py` ve `main.py` ile nasıl çalıştırıldığı gösterilir.

**Debate Crew:** Aynı soruya farklı rollerden yaklaşma, görev tanımı ve çıktı aktarımı için küçük başlangıç uygulamasıdır. İki ajanın anlaşması doğruluk kanıtı olarak sunulmaz.

**Financial Researcher:** Araştırma hedefi, Serper aracı, kaynak verisi ve rapor çıktısı birbirine bağlanır.

**Stock Picker:** Yapılandırılmış çıktı, özel araç, memory ve hierarchical process birlikte kullanılır. Finansal verinin tarihi ve eksikliği görünür tutulur.

**Coding Agent:** Kod üretmek ve kod çalıştırmak ayrı adımlardır. Docker sandbox’ı içinde çalışma, bağımlılık gereksinimleri ve yürütme sonuçları incelenir.

**Sandbox sınırı:** Docker kullanmak tek başına eksiksiz güvenlik garantisi sayılmaz. Dosya erişimi, ağ erişimi, sırlar ve kaynak limitleri ayrıca düşünülür.

**Engineering Team:** Kaynak dört ajanlı ekip olduğunu doğrular; bu alıntılarda dört rolün tamamı isimleriyle görünmediğinden roller uydurularak özgün içeriğe eklenmez.

**Context7 MCP:** Proje kapsamında kullanılan entegrasyon olarak korunur; genel MCP dersleri başlamadan önce gerçek kullanım örneğiyle karşılaşılır.

**Çoklu model kullanımı:** Farklı görevlerde farklı modellerin çalıştırılması, kalite ve maliyet karşılaştırması için fırsat olarak ele alınır.

### Haftalık teslim

Stock Picker ve dört ajanlı Engineering Team. Ek kanıt olarak üretilen kodun çalıştırma çıktısı, test sonuçları ve sınırlı düzeltme döngüsü sunulur.

---

## Hafta 4 — LangChain ekosistemi, state, kalıcılık ve Sidekick

**[Kaynak] 23 ders · yaklaşık 3 saat 1 dakika**

### Öğrenme bağlamı

Bu hafta dört soyutlama seviyesi birlikte görülür:

**LangChain Core → LangGraph → `create_agent` → Deep Agents**

Öğrenci, “daha üst seviye araç her zaman daha iyidir” yaklaşımı yerine, kontrol ihtiyacıyla geliştirme kolaylığı arasındaki dengeyi öğrenir.

### Derslerin tamamı

| No | Kaynaktaki ders başlığı | Süre |
|---:|---|---:|
| 69 | Day 1 - LangChain Ecosystem Explained: The Four Layers for Building AI Agents | 14:12 |
| 70 | Day 1 - LangChain Core Basics: ChatOpenAI, Invoke, Stream and the Tool Decorator | 9:18 |
| 71 | Day 1 - Bind Tools and Structured Outputs: Your First LangChain AI Agent | 7:17 |
| 72 | Day 2 - LangGraph Explained: Graphs, State, Nodes, Edges and Reducers | 12:59 |
| 73 | Day 2 - Build Your First LangGraph Graph: Nodes, Edges and Tool Calling | 17:23 |
| 74 | Day 2 - LangSmith, Supersteps and Checkpointers for LangGraph Agents | 12:19 |
| 75 | Day 2 - LangGraph Memory and Time Travel: MemorySaver, SQLite and Replay | 12:08 |
| 76 | Day 3 - Intro to LangChain create_agent: The Easy Way to Build AI Agents | 4:14 |
| 77 | Day 3 - Build a Simple Agent with LangChain create_agent and Tools | 5:31 |
| 78 | Day 3 - Agent Memory, Structured Outputs and Middleware in LangChain | 6:07 |
| 79 | Day 3 - Browser Automation with Node and Playwright for AI Agents | 4:48 |
| 80 | Day 3 - Build a Web Research Agent with create_agent and Playwright MCP | 9:06 |
| 81 | Day 4 - Deep Agents Overview: The Agent Harness for Long-Running AI Tasks | 3:30 |
| 82 | Day 4 - Deep Agents Skills Explained: SKILL.md and Progressive Disclosure | 7:29 |
| 83 | Day 4 - Build Your First Deep Agent with a File System and To-Do Tools | 6:35 |
| 84 | Day 4 - Deep Agents Sub-Agents: Delegation and the Task Tool Explained | 7:04 |
| 85 | Day 4 - Add Skills to Deep Agents: Build a PowerPoint with SKILL.md | 6:05 |
| 86 | Day 5 - Intro to the Sidekick: An Autonomous AI Coworker with create_agent | 3:56 |
| 87 | Day 5 - Sidekick Setup: Tools, Middleware and Evaluator with create_agent | 4:37 |
| 88 | Day 5 - Human in the Loop with LangChain create_agent: Approve and Reject | 5:32 |
| 89 | Day 5 - Inside the Sidekick Module: create_agent, Middleware and Evaluator | 7:23 |
| 90 | Day 5 - Run the Sidekick: An Autonomous AI Agent on Real-World Tasks | 6:31 |
| 91 | Day 5 - Build a Gradio UI for the Sidekick AI Agent and Finish the Project | 6:52 |

### Junior için işlenecek açıklamalar

**[Öğretim tasarımı]**

**LangChain Core:** `ChatOpenAI`, `invoke`, `stream`, araç dekoratörü, araç bağlama ve structured output kavramlarının doğrudan API çağrısındaki karşılıkları gösterilir.

**LangGraph:** Graph, state, node, edge ve reducer tanımları küçük bir uygulamada izlenir. Özellikle reducer’ın state güncellemelerini nasıl birleştirdiği açıklanır.

**Çalışma ve kalıcılık:** Supersteps, checkpointer, MemorySaver, SQLite ve replay kavramları birbirinden ayrılır. Bellekte tutulan durum ile kalıcı saklama aynı güvenceyi vermez.

**Time travel:** Geçmiş state’i inceleme veya yeniden yürütme ile dış dünyada yapılmış işlemi geri alma aynı şey değildir. Tekrar yürütmede yan etkiler ayrıca yönetilmelidir.

**LangSmith:** Akışın gözlemlenmesi ve teşhis edilmesi için kullanılır.

**`create_agent`:** Hazır ajan oluşturma arayüzü üzerinden memory, structured output ve middleware’in nereye yerleştiği açıklanır.

**Tarayıcı otomasyonu:** Node, Playwright ve Playwright MCP bağlantısı öğretilir. Tarayıcıdaki dış içerik, uygulamanın temel talimatlarından daha yetkili kabul edilmez.

**Deep Agents:** Uzun görevler, dosya sistemi, yapılacaklar araçları, sub-agent delegasyonu ve task aracı birlikte ele alınır.

**Skills ve progressive disclosure:** Bütün bilgiyi başlangıçta modele yüklemek yerine ilgili beceri açıklamalarının ihtiyaç halinde açılması öğretilir. `SKILL.md` ve PowerPoint üretimi somut uygulamadır.

**Sidekick:** Araçlar, middleware, evaluator, kullanıcı onayı ve Gradio arayüzü birleştirilir. Onay verme kadar reddetme ve işlemi durdurma davranışı da test edilir.

### Haftalık teslim

State’i takip edilebilen, araç kullanımı gözlemlenebilen ve gerekli işlemler için kullanıcı onayı isteyen bir Sidekick.

---

## Hafta 5 — Framework çeşitliliği, A2A ve çok-framework’lü Agent Loop

**[Kaynak] 17 ders · yaklaşık 2 saat 1 dakika**

### Öğrenme bağlamı

Bu hafta önceki context’te en fazla eksik kalan bölümdür. Gerçek müfredat yalnızca AutoGen’e değil, çok sayıda farklı ekosisteme yer veriyor.

Amaç her framework’te uzmanlık iddia etmek değil; aynı temel ajan yapısının farklı araçlarda nasıl ifade edildiğini karşılaştırmaktır.

### Derslerin tamamı

| No | Kaynaktaki ders başlığı | Süre |
|---:|---|---:|
| 92 | Day 1 - Intro to Google ADK and the Agent Development Kit | 6:51 |
| 93 | Day 1 - Build Your First Google ADK Agent and Add Tools | 8:32 |
| 94 | Day 1 - ADK Agent Loop with MCP Tools and the ADK Web Dashboard | 10:47 |
| 95 | Day 1 - The A2A Protocol: Agent Cards and a Live Agent2Agent Demo | 10:33 |
| 96 | Day 2 - Build AI Agents with Strands Agents from AWS and Bedrock | 9:02 |
| 97 | Day 2 - Build AI Agents with Pydantic AI and Structured Outputs | 8:22 |
| 98 | Day 2 - Run a Pydantic AI Agent in Python and Wrap Up Strands | 2:02 |
| 99 | Day 3 - Intro to the Microsoft Agent Framework, AutoGen and Semantic Kernel | 4:35 |
| 100 | Day 3 - Build an AI Agent with the Microsoft Agent Framework Lab | 5:49 |
| 101 | Day 3 - Intro to Agno: The Fast, Lightweight AI Agent Framework | 2:32 |
| 102 | Day 3 - Build an AI Agent with Agno: Tools, MCP and the Agent Loop | 6:39 |
| 103 | Day 4 - Intro to Mastra: The TypeScript-Native AI Agent Framework | 2:36 |
| 104 | Day 4 - Build AI Agents in TypeScript with Mastra: Tools and MCP | 8:47 |
| 105 | Day 4 - Run the Mastra Agent Loop and Explore Mastra Studio | 4:27 |
| 106 | Day 5 - The Agent Loop Project: Multi-Framework Agent Architecture | 11:05 |
| 107 | Day 5 - Inside the Agent Loop: Orchestrator, QA and CSS Agents | 8:05 |
| 108 | Day 5 - Run the Multi-Agent Loop: Six Frameworks Build in Parallel | 10:26 |

### Junior için işlenecek açıklamalar

**[Öğretim tasarımı]**

**Google ADK:** Ajan oluşturma, tool ekleme, MCP bağlantısı ve web dashboard üzerinden çalışma davranışı incelenir.

**A2A:** Agent Cards ve ajanlar arası etkileşim gösterilir. MCP’nin araç/bağlam entegrasyonu ile A2A’nın ajanlar arası iletişim odağı birbirinden ayrılır.

**Strands ve Bedrock:** Framework ile model erişim platformunun farklı sorumluluklar taşıdığı açıklanır.

**Pydantic AI:** Şema odaklı çıktı ve tipli veri aktarımı ele alınır. Önceki haftalardaki Pydantic veri modeli kullanımıyla Pydantic AI framework’ü aynı şey değildir.

**Microsoft ekosistemi:** Microsoft Agent Framework, AutoGen ve Semantic Kernel’in adları ve ilişkileri ders bağlamında incelenir. Tek bir ürünün eşanlamlı isimleri gibi öğretilmez.

**Agno:** Araçlar, MCP ve agent loop üzerinden önceki framework’lerle karşılaştırılır.

**Mastra:** TypeScript tabanlı geliştirme, araçlar, MCP ve Mastra Studio tanıtılır. Python deneyiminin otomatik olarak TypeScript yeterliliği sağlamadığı kabul edilerek gerekli sözdizimi köprüsü kurulur.

**Final Agent Loop:** Orchestrator, QA ve CSS ajanlarıyla çok-framework’lü işbirliği incelenir. Altı framework’ün paralel çalışması; görev paylaşımı, çıktı sözleşmeleri, başarısızlık ve entegrasyon açısından değerlendirilir.

### Haftalık teslim

Bir küçük görevin farklı framework’lerde karşılaştırılması ve çok-framework’lü Agent Loop’un çalıştırılması. Öğrenci her bileşenin neden o framework’te bulunduğunu açıklamalıdır.

### Proje 7 için doğrulama notu

Tanıtım metni **AutoGen ile yeni ajanlar oluşturan Agent Creator** projesini vaat ediyor. Ayrıntılı ders listesi ise **çok-framework’lü Agent Loop** projesini gösteriyor.

Bu nedenle context’te:

- Agent Creator, **tanıtımda belirtilen proje** olarak tutulur.
- Agent Loop, **ayrıntılı müfredatta doğrulanan uygulama** olarak tutulur.

Bunların aynı uygulamanın iki adı olduğu veya birinin diğerini kesin olarak değiştirdiği, mevcut sayfadan tek başına söylenemez.

---

## Hafta 6 — MCP, context engineering ve Trading Floor

**[Kaynak] 24 ders · yaklaşık 3 saat 15 dakika**

### Öğrenme bağlamı

Bu hafta MCP’yi yalnızca sunucu bağlama aracı olarak değil; araç erişimi, bağlam oluşturma, memory, retrieval ve uygulama mimarisiyle birlikte öğretir.

Final uygulaması önceki haftaların model, araç, ajan, orkestrasyon, gözlemlenebilirlik ve arayüz becerilerini birleştirir.

### Derslerin tamamı

| No | Kaynaktaki ders başlığı | Süre |
|---:|---|---:|
| 109 | Day 1 - Welcome to MCP Week: Agent Frameworks and the Agent Harness | 9:29 |
| 110 | Day 1 - What Is MCP? Host, Client and Server Architecture Explained | 12:48 |
| 111 | Day 1 - How MCP Works: Local vs Remote Servers and Calling Tools | 9:29 |
| 112 | Day 1 - Exploring Node-Based MCP Servers & Tool Access | Belirtilmiyor |
| 113 | Day 1 - MCP Transport Mech… | 10:46 |
| 114 | Day 1 - First MCP Lab: Connecting Fetch, Playwright and Filesystem | 10:42 |
| 115 | Day 1 - Build a Web-Browsing AI Agent with MCP Servers and Traces | 12:07 |
| 116 | Day 2 - MCP Recap: Core Concepts Before Building Your Own MCP Server | 7:16 |
| 117 | Day 2 - Why Build Your Own MCP Server (and When You Shouldn't) | 3:49 |
| 118 | Day 2 - MCP Marketplaces and Building an MCP Server with FastMCP | 9:35 |
| 119 | Day 2 - Run and Call Your Own MCP Server from an AI Agent | 4:48 |
| 120 | Day 3 - Context Engineering for AI Agents with MCP Servers | 10:03 |
| 121 | Day 3 - Long-Term Memory and Web Search MCP Servers for AI Agents | 9:22 |
| 122 | Day 3 - Agentic RAG with the Qdrant MCP Server for AI Agents | 6:24 |
| 123 | Day 3 - Market Data MCP Server and Progressive Disclosure of Tools | 10:26 |
| 124 | Day 4 - Capstone Kickoff: Build an Autonomous AI Trading Floor | 4:16 |
| 125 | Day 4 - Trading Floor Architecture: Trader and Researcher AI Agents | 9:26 |
| 126 | Day 4 - Wiring Up MCP Servers and the Researcher-as-Tool Pattern | 10:48 |
| 127 | Day 4 - Orchestrate the Trading Floor and Launch the Gradio Dashboard | 8:29 |
| 128 | Day 5 - Add Observability, Evaluation and Feedback to AI Traders | 6:24 |
| 129 | Day 5 - Ship the Trading App: FastAPI Backend and React Front End | 10:51 |
| 130 | Day 5 - Inspecting Traces and Your Capstone Trading Floor Challenge | 2:25 |
| 131 | Day 5 - Choosing an Agent Framework and 10 Things That Really Matter | 9:08 |
| 132 | Day 5 - Course Wrap-Up: Your Agentic AI Engineering Journey / Bonus Lecture - Your Exclusive Links | Bkz. not |

**Döküm düzeltmesi:** Kaynakta kapanış dersi **3:02**, bonus ders ise **2:42** olarak ayrı görünür. Buna karşılık 112–113 çevresindeki metin, “Exploring Node-Based MCP Servers & Tool AccessDay 1 - MCP Transport Mech10:46” biçiminde birleşmiş/bozulmuş aktarılmıştır. Dolayısıyla bu bölümde **24 ders toplamı doğrulanırken, bu iki başlığın ayrı kayıt mı yoksa tek kaydın bozulmuş başlığı mı olduğu kesinleşmemiştir**. Yukarıdaki son satır, sayıyı sessizce değiştirmemek için iki kapanış kaydını birlikte gösterir; özgün kursta birleşik tek ders olduğu iddiası değildir.

Başka bir ifadeyle: **Görünen bütün içerik adları korunmuştur; ancak 132 dersin kusursuz birebir sıra eşlemesi için bu küçük HTML bölgesinin ayrıca doğrulanması gerekir.**

### Junior için işlenecek açıklamalar

**[Öğretim tasarımı]**

**MCP mimarisi:** Host, client ve server rolleri ayrılır. Yerel sunucu ile uzak sunucu bağlantısının süreç yönetimi, erişim ve yaşam döngüsü bakımından farklı olduğu gösterilir.

**Transport:** İletişim mekanizması ile araçların iş mantığı farklı katmanlardır. Kaynak dökümünde transport dersinin başlığı eksik olduğundan özgün derste hangi mekanizmaların tam olarak anlatıldığı tahminle doldurulmaz.

**Hazır sunucular:** Fetch, Playwright ve Filesystem üzerinden web içeriği, tarayıcı etkileşimi ve dosya işlemleri incelenir.

**Node tabanlı sunucular:** Bir MCP sunucusunun çalıştığı runtime ile ajan uygulamasının yazıldığı dilin aynı olmak zorunda olmadığı gösterilir.

**Kendi sunucunu yazma:** FastMCP ile araç sunma, sunucuyu çalıştırma ve ajandan çağırma ele alınır. Her Python fonksiyonu için ayrı MCP sunucusu kurmanın gerekli olmadığı tartışılır.

**Marketplaces:** Sunucu keşfi ile sunucuya güvenme ayrı kararlar olarak ele alınır.

**Context engineering:** Long-term memory, web search, Qdrant ile agentic RAG ve piyasa verisinin model çağrısına nasıl taşındığı açıklanır.

**Progressive disclosure:** Çok sayıda aracın tamamını sürekli göstermek yerine ilgili araçların ihtiyaç halinde erişilebilir kılınması değerlendirilir.

**Trading Floor:** Trader ve researcher rollerinin ayrımı, researcher-as-tool deseni ve MCP entegrasyonları birlikte çalışır.

**Gözlemlenebilirlik ve değerlendirme:** Kararların, araç sonuçlarının ve geri bildirimin izlenmesi final mimarisinin parçasıdır.

**Ürünleştirme:** Gradio dashboard’dan FastAPI backend ve React frontend yapısına geçiş ele alınır. Tek bir dersin FastAPI veya React’te baştan sona uzmanlık sağladığı varsayılmaz.

### Final teslimi

Trading Floor uygulaması; mimari açıklama, MCP bağlantıları, çalışan arayüz, iz kayıtları, değerlendirme sonuçları ve bir genişletme ile sunulur.

**[Öğretim tasarımı]** Eğitim uygulaması için varsayılan yürütme paper trading/simülasyon olmalıdır. Finansal hesaplama, bakiye ve risk limitleri gibi deterministik kontroller LLM’in serbest yorumuna bırakılmamalıdır.

---

# 6. Ana projelerin tam eşlemesi

| Proje | Kaynaktaki vaat | Müfredattaki karşılığı | Öğrenme amacı |
|---|---|---|---|
| 1. Career Digital Twin | Öğrenciyi potansiyel işverenlere temsil eden ajan | Hafta 1 | Kişisel bağlam, tool calling, Gradio, deploy |
| 2. SDR Agent | Profesyonel satış e-postaları hazırlayan ve gönderen temsilciler | Hafta 2 | Araçlar, çok ajan, orkestrasyon |
| 3. Deep Research | Seçilen konuda kapsamlı araştırma yapan ajan ekibi | Hafta 2 | Planlama, arama, yapılandırılmış aktarım, raporlama |
| 4. Stock Picker | CrewAI ile hisse araştırması ve seçimi | Hafta 3 | Araştırma, custom tools, memory, hierarchical process |
| 5. Engineering Team | Docker içinde uygulama yöneten, geliştiren ve test eden dört ajan | Hafta 3 | Kod üretme, yürütme, ekip koordinasyonu |
| 6. Sidekick | Tarayıcıda kullanıcıyla çalışan yardımcı | Hafta 4 | State, browser tools, evaluator, human-in-the-loop |
| 7. Agent Creator | AutoGen ile yeni ajanlar oluşturup başlatan ajan | Tanıtımda var; ayrıntılı eşleşme belirsiz | Ajan oluşturma ve delegasyon |
| 8. Trading Floor | 4 ajan, 6 MCP sunucusu ve 44 araçla otonom işlemler | Hafta 6 | Bütünleşik final uygulaması |

**Ek olarak ayrıntılı müfredatta doğrulanan proje:** Hafta 5’te altı framework’ün paralel çalıştığı **Multi-Framework Agent Loop**.

**[Doğrulama notu]** Trading Floor’un dört ajan, altı sunucu ve 44 araç sayıları tanıtımda doğrudan bulunuyor. Ancak bütün sunucuların ve 44 aracın tek tek isimleri mevcut ders başlıklarından çıkarılamaz.

---

# 7. Ana projeler dışında kaçırılmaması gereken uygulamalar

Sekiz proje, kursun bütün uygulamalarını temsil etmiyor. Ders listesinde şu ek çalışmalar da var:

| Uygulama | Konumu | Öğrettiği unsur |
|---|---|---|
| n8n no-code ajan demosu | Hafta 1 | İlk zihinsel model |
| Python’da zincirlenen LLM çağrıları | Hafta 1 | Basit workflow |
| Sekiz LLM’i çağırma | Hafta 1 | Sağlayıcılar arası kullanım |
| Ollama ile yerel modeller | Hafta 1 | Yerel yürütme |
| LLM-as-a-judge akışı | Hafta 1 | Model tabanlı değerlendirme |
| Checklist araçlı görünür agent loop | Hafta 1 | Görev ilerlemesini görünür kılma |
| Üç farklı satış orkestrasyonu | Hafta 2 | Kod, tool olarak ajan, handoff |
| CrewAI Debate Crew | Hafta 3 | Roller ve görevler |
| Financial Researcher | Hafta 3 | Arama aracı ve context |
| Docker’da Coding Agent | Hafta 3 | Kod yürütme |
| İlk LangGraph grafiği | Hafta 4 | State ve akış |
| Playwright MCP web araştırmacısı | Hafta 4 | Tarayıcı otomasyonu |
| Dosya sistemi ve to-do araçlı Deep Agent | Hafta 4 | Uzun görev yönetimi |
| `SKILL.md` ile PowerPoint üretimi | Hafta 4 | Skills ve progressive disclosure |
| A2A canlı demo | Hafta 5 | Ajanlar arası etkileşim |
| Framework bazlı ilk ajan laboratuvarları | Hafta 5 | Karşılaştırmalı öğrenme |
| Fetch–Playwright–Filesystem MCP laboratuvarı | Hafta 6 | Birden çok sunucu entegrasyonu |
| FastMCP ile özel sunucu | Hafta 6 | Araç sunma |
| Qdrant MCP ile agentic RAG | Hafta 6 | Retrieval ve context |

---

# 8. Junior geliştirici için hazırlık modülü

**[Öğretim tasarımı — özgün altı haftaya ek hazırlık]**

Kaynak, temel beceriler için self-study lab klasörü bulunduğunu söylüyor; ancak klasörün bütün dosyaları elimizde değil. Aşağıdaki liste, o klasörün doğrulanmış envanteri değil, hedef kitle için önerilen hazırlıktır.

| Alan | Gerekli başlangıç becerileri |
|---|---|
| Python | Fonksiyonlar, döngüler, list/dict, modüller, sınıfları okuyabilme, exception |
| Veri | JSON, dosya okuma, temel şema ve doğrulama |
| API | İstek/yanıt, kimlik doğrulama, durum kodları, timeout |
| Terminal | Dizinler, komut çalıştırma, süreç ve hata çıktısı |
| Git | Clone, değişiklikleri inceleme, commit, sırları dışarıda tutma |
| Ortam | `uv`, bağımlılıklar, `.env`, farklı çalışma ortamları |
| Async | `async`, `await`, eşzamanlı görevlerin temel mantığı |
| Web | Backend, frontend ve API arasındaki ilişki |
| TypeScript köprüsü | Mastra örneklerini okuyacak temel sözdizimi |
| Container | Docker image, container, dosya bağlama ve kaynak sınırı |

### Hazırlık geçiş kriteri

Öğrenci temiz bir ortamda projeyi kurabilmeli, API anahtarını koddan ayırabilmeli, bir JSON girdisini okuyabilmeli ve başarısız bir isteği anlaşılır biçimde yönetebilmelidir.

---

# 9. Her dersin öğretim standardı

**[Öğretim tasarımı]**

Her konu şu sırayla işlenmelidir:

1. **İhtiyaç:** Bu kavram hangi problemi çözüyor?
2. **Zihinsel model:** Sistem içinde nereye yerleşiyor?
3. **Minimum örnek:** En küçük çalışan sürüm.
4. **Genişletme:** Mevcut projeye tek yeni yetenek ekleme.
5. **Başarısızlık örneği:** Yanlış girdi veya bozuk dış servis.
6. **Gözlem:** Trace, çıktı ve state değişimini inceleme.
7. **Bağımsız görev:** Öğrencinin veriyi veya gereksinimi değiştirerek uygulaması.
8. **Gerekçe:** Seçilen yaklaşımın alternatiflerle açıklanması.

Öğrenci yalnızca “bu kod ne yapıyor?” değil, **“bu bileşen olmazsa ne bozulur?”** sorusuna da cevap vermelidir.

---

# 10. Kurs boyunca korunacak mühendislik ilkeleri

Aşağıdaki ilkeler önceki altyazı incelemesinde öne çıkmıştı; ders sayfası da riskler, guardrails, değerlendirme, tracing ve framework seçimi başlıklarını doğruluyor. Ancak bunlar, 131. dersteki “10 Things” listesinin birebir transkripti olarak sunulmamalıdır.

### Basit çözümle başla

Önce tek çağrı veya normal kodla çalışan baseline kur. Ek ajan, framework ve otonomi yalnızca somut bir ihtiyaca cevap versin.

### Promptları deneylerle geliştir

Prompt değişikliklerini sabit örnekler üzerinde karşılaştır. Aynı anda çok sayıda değişkeni değiştirerek neyin işe yaradığını belirsizleştirme.

### Gerçek yürütmeyi doğrula

“Araştırdım”, “gönderdim” veya “test ettim” cümlesi kanıt değildir. Arama, gönderim veya test işleminin gerçekten yapıldığını kontrol et.

### State, memory ve context’i ayır

Bir bilginin saklanması, her model çağrısına gönderilmesi gerektiği anlamına gelmez. İlgili, güncel ve yetkili bilgi seçilmelidir.

### Otonomiyi kademeli artır

Önce güvenilir akış; sonra daha fazla araç seçimi, görev delegasyonu ve bağımsız karar. Her seviyede durdurma ve insan müdahalesi yolu korunsun.

### Model seçimini ölç

Yeterli kapasiteyle çalışan bir başlangıç kur; daha küçük modelleri aynı testlerde karşılaştır. Güçlü model kullanmak doğruluk garantisi değildir.

### Framework’ü gereksinime göre seç

Öğrenme kolaylığı, kontrol, state, tracing, dağıtım ve ekip yetkinliği birlikte değerlendirilsin.

### Deneyci gibi çalış

Her önemli değişiklik için beklenen sonuç, gözlenen davranış ve sonraki adım kaydedilsin.

---

# 11. “Hero” hedefi için ek güvenilirlik ve güvenlik kapsamı

**[Öğretim tasarımı]** Bu ayrıntıların tamamının özgün videolarda işlendiği doğrulanmış değildir. Ancak bağımsız uygulama geliştirme hedefi için öğretime eklenmelidir.

| Alan | Eklenmesi gereken uygulama |
|---|---|
| API güvenilirliği | Timeout, sınırlı retry, rate limit ve açıklayıcı hata |
| Araç güvenliği | İzin verilen araç listesi, parametre doğrulama, en az yetki |
| Yan etkiler | E-posta, dosya yazma ve işlem yürütmede onay ve tekrar işlemeyi önleme |
| Döngü kontrolü | Maksimum adım, süre ve maliyet bütçesi |
| Veri güvenliği | Sırları koruma, kişisel veriyi sınırlama, loglarda maskeleme |
| Prompt injection | Web, PDF ve tool çıktısını güvenilmeyen içerik olarak işleme |
| Kod yürütme | Sandbox, kaynak sınırı, dosya/ağ erişimini sınırlama |
| Çıktı kalitesi | Şema doğruluğu ile bilgi doğruluğunu ayrı test etme |
| Gözlemlenebilirlik | Çağrı, araç, hata, süre ve maliyetin izlenmesi |
| Dağıtım | Yapılandırma, bağımlılık sürümleri, erişim ve operasyon sınırları |

---

# 12. Projeler için zorunlu teslim standardı

**[Öğretim tasarımı]** Her proje yalnızca çalışan demo olarak teslim edilmemelidir.

| Teslim | İçerik |
|---|---|
| Problem tanımı | Hedef kullanıcı, ihtiyaç ve kapsam dışı durumlar |
| Mimari açıklama | Model, araç, state, veri akışı ve orkestrasyon |
| Çalıştırma talimatı | Kurulum, yapılandırma ve komutlar |
| Örnek yapılandırma | Gerçek anahtar içermeyen örnek değişkenler |
| Başarılı senaryo | Beklenen çıktıyı üreten örnek |
| Başarısız senaryo | Araç hatası, eksik bilgi veya reddedilen işlem |
| Test seti | Tekrarlanabilir girdiler ve kontrol edilen davranışlar |
| Trace kanıtı | Gerçek araç çalışmasını gösteren kayıt |
| Maliyet değerlendirmesi | Kullanılan model ve çağrı davranışının etkisi |
| Bilinen sınırlamalar | Sistemin güvenilir olmadığı veya desteklemediği durumlar |

### Proje özelinde başarı kriterleri

| Proje | Tamamlanmış sayılma koşulu |
|---|---|
| Digital Twin | Profil dışındaki bilgiyi uydurmaz; araç kullanımı doğrulanır. |
| SDR | Taslak ve gönderim ayrıdır; yanlışlıkla tekrar gönderim kontrol edilir. |
| Deep Research | İddialar kaynaklarla ilişkilidir; eksik kanıt açıkça belirtilir. |
| Stock Picker | Tarih, veri kaynağı ve riskler görünürdür. |
| Engineering Team | Üretilen kod gerçekten çalıştırılır; test sonucu kaydedilir. |
| Sidekick | Onay, ret, araç hatası ve durdurma senaryoları işler. |
| Agent Loop | Framework’ler arası görev ve çıktı aktarımı açıklanabilir. |
| Trading Floor | Karar, araç çağrısı ve uygulama state’i izlenebilir; simülasyon sınırı açıktır. |

---

# 13. Mezuniyet sınaması

**[Öğretim tasarımı]**

Öğrenciye derste birebir yapılmamış bir alan problemi verilir. Örneğin kaynaklı destek araştırması, belge inceleme veya yazılım bakım planlama.

Öğrenci:

1. Tek çağrılık veya deterministik bir başlangıç kurar.
2. Ajan kullanımına gerçekten ihtiyaç olup olmadığını açıklar.
3. En az bir dış veri veya araç entegrasyonu yapar.
4. Çıktı sözleşmesini tanımlar.
5. State ve context yönetimini açıklar.
6. Başarısızlık ve sonlanma davranışlarını uygular.
7. Tekrarlanabilir değerlendirme yapar.
8. Uygulamayı arayüzle sunar.
9. Mimarisini alternatifleriyle savunur.
10. Sonradan verilen bir gereksinimi bağımsız ekler.

**Başarı ölçütü video bitirmek değil, yeni problemi çözebilmek ve çözümün sınırlarını gösterebilmektir.**

---

# 14. Kapsam doğrulama sonucu

| Kontrol | Sonuç |
|---|---|
| Altı haftanın tamamı | Kapsandı |
| Sayfada görünen bütün ders konuları | Kapsandı |
| Sekiz proje vaadi | Kapsandı |
| Beşinci haftadaki ek/alternatif Agent Loop projesi | Ayrı olarak kapsandı |
| Kurulum ve yerel model çalıştırma | Kapsandı |
| Bütün adı geçen framework’ler | Kapsandı |
| Memory, state, context, RAG ve skills | Kapsandı |
| Guardrails, sandbox, tracing ve evaluation | Kapsandı |
| MCP, A2A ve browser automation | Kapsandı |
| Gradio, Hugging Face Spaces, FastAPI ve React | Kapsandı |
| Kapanış ve bonus bağlantı dersi | Kapsandı |
| MCP başlığındaki bozuk aktarım | Açıkça işaretlendi |
| Proje 7 tanıtım–müfredat farkı | Açıkça işaretlendi |
| Bütün videoların satır satır içeriği | Bu sayfayla doğrulanamaz |
| 44 aracın ve 6 final MCP sunucusunun tam isim listesi | Mevcut başlıklarda yok |
| Özgün ödevler, repo dosyaları ve paket sürümleri | Tam envanterleri doğrulanmadı |

---

## 15. Başka bir AI’a verilebilecek ana kurs context’i

> Bu eğitimin hedefi, temel programlama bilgisi bulunan ancak agentic AI deneyimi olmayan junior geliştiriciyi, sınırları belli gerçek bir problemi bağımsız olarak AI uygulamasına dönüştürebilecek seviyeye taşımaktır. Eğitim; n8n demosu, Cursor–Git–uv ortamı, API anahtarları, doğrudan LLM çağrıları, sağlayıcı karşılaştırmaları, Ollama, LLM-as-a-judge, agent/workflow ayrımı, chaining, routing, orchestration, tool calling, context engineering ve framework kullanmadan agent loop kurmayla başlar. Digital Twin geliştirilir ve Gradio ile Hugging Face Spaces üzerinde sunulur.
>
> OpenAI Agents SDK bölümünde async Python, Agent, Runner, tracing, function tools, sessions, SQLiteSession, kodla orkestrasyon, agents-as-tools, handoffs, farklı modeller, Pydantic structured outputs, guardrails ve sandbox kavramları öğretilir. SDR ve Deep Research uygulamaları geliştirilir.
>
> CrewAI bölümünde agents, tasks, crews, flows, YAML, CLI kullanımı, Debate Crew, Financial Researcher, Serper, Stock Picker, custom tools, memory ve hierarchical process ele alınır. Docker ve UV sandbox araçlarıyla kod çalıştıran ajanlar ve Context7 MCP kullanan dört ajanlı Engineering Team geliştirilir.
>
> LangChain ekosisteminde LangChain Core, LangGraph, create_agent ve Deep Agents ayrıştırılır. Invoke, stream, tools, structured outputs, graphs, state, nodes, edges, reducers, LangSmith, supersteps, checkpointers, MemorySaver, SQLite, replay, middleware, Node, Playwright ve Playwright MCP işlenir. SKILL.md, progressive disclosure, dosya sistemi, to-do tools, sub-agents ve task delegation uygulamaları yapılır. Evaluator ve human-in-the-loop içeren Sidekick geliştirilir.
>
> Framework karşılaştırma bölümünde Google ADK, A2A ve Agent Cards, Strands ve Bedrock, Pydantic AI, Microsoft Agent Framework, AutoGen, Semantic Kernel, Agno ve TypeScript tabanlı Mastra tanıtılır. Orchestrator, QA ve CSS ajanları içeren çok-framework’lü Agent Loop incelenir. Tanıtımda geçen AutoGen Agent Creator projesinin ayrıntılı müfredattaki Agent Loop ile eşleşmesi kesin kabul edilmez.
>
> MCP bölümünde host–client–server mimarisi, yerel ve uzak sunucular, transport konusu, Node tabanlı sunucular, Fetch, Playwright, Filesystem, marketplace’ler, FastMCP ile özel sunucu, long-term memory, web search, Qdrant ile agentic RAG, piyasa verisi ve araçların progressive disclosure yaklaşımı işlenir. Trader ve researcher rolleriyle Trading Floor geliştirilir; researcher-as-tool, MCP entegrasyonları, Gradio dashboard, observability, evaluation, feedback, FastAPI backend ve React frontend bir araya getirilir.
>
> Öğretimde önce küçük ve anlaşılır çözüm kurulur; prompt iterasyonu, gerçek araç yürütmesini doğrulama, context yönetimi ve ölçüme dayalı karar verme sürekli uygulanır. Öğrenciye güvenilirlik, test, izin sınırları, onay, maliyet kontrolü ve dokümantasyon ek mühendislik pratiği olarak öğretilir. Başarı, framework isimlerini bilmekle değil; yeni bir uygulamayı geliştirmek, test etmek, sunmak ve sınırlamalarını açıklamakla değerlendirilir. Kaynakta doğrulanmayan uygulama ayrıntıları özgün kurs içeriğiymiş gibi sunulmaz.