/**
 * Agentic AI Engineering: Sıfırdan Hero Seviyesine Kurs Kitabı Etkileşimleri
 * Sayfalar arası hızlı geçiş, ders filtreleme, kod kopyalama ve A4 PDF yazdırma
 */

const COURSE_PAGES = [
  { file: "index.html", title: "00. Ana Portal: Zihinsel Model, Sözlük & 132 Ders Haritası" },
  { file: "mod00-hazirlik.html", title: "Modül 0: Junior Geliştirici İçin Hazırlık Modülü" },
  { file: "hafta01-gun01.html", title: "Hafta 1 - Gün 1: n8n, Ortam Kurulumu ve İlk OpenAI API (Ders 1-8)" },
  { file: "hafta01-gun02.html", title: "Hafta 1 - Gün 2: Workflows vs Agents, Desenler & Guardrails (Ders 9-11)" },
  { file: "hafta01-gun03.html", title: "Hafta 1 - Gün 3: 8 LLM Çağırma, Ollama & LLM-as-a-Judge (Ders 12-16)" },
  { file: "hafta01-gun04.html", title: "Hafta 1 - Gün 4: Tool Calling, Gradio & Sıfırdan Agent Loop (Ders 17-21)" },
  { file: "hafta01-gun05.html", title: "Hafta 1 - Gün 5: Context, Pushover, Checklist & Proje 1 Digital Twin (Ders 22-28)" },
  { file: "hafta02-gun01.html", title: "Hafta 2 - Gün 1: OpenAI Agents SDK, Async, Trace & SQLiteSession (Ders 29-33)" },
  { file: "hafta02-gun02.html", title: "Hafta 2 - Gün 2: 3 Orkestrasyon, Handoffs & Proje 2 SDR Agent (Ders 34-39)" },
  { file: "hafta02-gun03.html", title: "Hafta 2 - Gün 3: Çoklu Model, Pydantic Çıktılar & Guardrails (Ders 40-42)" },
  { file: "hafta02-gun04.html", title: "Hafta 2 - Gün 4: Deep Research Planlama, Arama & Yazar Ajanlar (Ders 43-46)" },
  { file: "hafta02-gun05.html", title: "Hafta 2 - Gün 5: Modülerleştirme, Gradio & Proje 3 Deep Research (Ders 47-49)" },
  { file: "hafta03-gun01.html", title: "Hafta 3 - Gün 1: CrewAI Temelleri, YAML, CLI & Debate Crew (Ders 50-55)" },
  { file: "hafta03-gun02.html", title: "Hafta 3 - Gün 2: 5 Adımda CrewAI, Financial Researcher & Serper (Ders 56-58)" },
  { file: "hafta03-gun03.html", title: "Hafta 3 - Gün 3: Pydantic, Custom Tools, Memory & Proje 4 Stock Picker (Ders 59-61)" },
  { file: "hafta03-gun04.html", title: "Hafta 3 - Gün 4: Coding Agent, Docker Kurulumu & Sandbox (Ders 62-64)" },
  { file: "hafta03-gun05.html", title: "Hafta 3 - Gün 5: Context7 MCP, UV Sandbox & Proje 5 Engineering Team (Ders 65-68)" },
  { file: "hafta04-gun01.html", title: "Hafta 4 - Gün 1: 4 Katmanlı LangChain Ekosistemi & Core (Ders 69-71)" },
  { file: "hafta04-gun02.html", title: "Hafta 4 - Gün 2: LangGraph State, Reducers, Checkpointers & Replay (Ders 72-75)" },
  { file: "hafta04-gun03.html", title: "Hafta 4 - Gün 3: create_agent, Middleware & Playwright MCP (Ders 76-80)" },
  { file: "hafta04-gun04.html", title: "Hafta 4 - Gün 4: Deep Agents, SKILL.md, Progressive Disclosure & Sub-Agents (Ders 81-85)" },
  { file: "hafta04-gun05.html", title: "Hafta 4 - Gün 5: Human-in-the-Loop, Evaluator & Proje 6 Sidekick (Ders 86-91)" },
  { file: "hafta05-gun01.html", title: "Hafta 5 - Gün 1: Google ADK, MCP Dashboard & A2A Protokolü (Ders 92-95)" },
  { file: "hafta05-gun02.html", title: "Hafta 5 - Gün 2: AWS Strands Agents, Bedrock & Pydantic AI (Ders 96-98)" },
  { file: "hafta05-gun03.html", title: "Hafta 5 - Gün 3: Microsoft Agent Framework, AutoGen, SK & Agno (Ders 99-102)" },
  { file: "hafta05-gun04.html", title: "Hafta 5 - Gün 4: TypeScript-Native Mastra, MCP & Mastra Studio (Ders 103-105)" },
  { file: "hafta05-gun05.html", title: "Hafta 5 - Gün 5: Proje 7 Doğrulama Notu & 6-Framework Agent Loop (Ders 106-108)" },
  { file: "hafta06-gun01.html", title: "Hafta 6 - Gün 1: MCP Mimarisi, Transport & Fetch/Playwright/FS Lab (Ders 109-115)" },
  { file: "hafta06-gun02.html", title: "Hafta 6 - Gün 2: Marketplaces & FastMCP ile Özel Sunucu Yazma (Ders 116-119)" },
  { file: "hafta06-gun03.html", title: "Hafta 6 - Gün 3: MCP Context Engineering, Qdrant RAG & Market Data (Ders 120-123)" },
  { file: "hafta06-gun04.html", title: "Hafta 6 - Gün 4: Trading Floor Mimarisi, Researcher-as-Tool & Dashboard (Ders 124-127)" },
  { file: "hafta06-gun05.html", title: "Hafta 6 - Gün 5: Observability, FastAPI/React & Proje 8 Trading Floor (Ders 128-132)" },
  { file: "mod07-guvenilirlik-ve-mezuniyet.html", title: "Modül 7: Hero Güvenlik, Zorunlu Teslim Standardı & Mezuniyet Sınaması" },
  { file: "tam-kitap-baski.html", title: "Tam Kitap (Tüm Kurs Tek PDF Baskı Görünümü - 132 Ders)" }
];

document.addEventListener("DOMContentLoaded", () => {
  const selectEl = document.getElementById("page-jump-select");
  const currentFile = window.location.pathname.split("/").pop() || "index.html";

  if (selectEl) {
    COURSE_PAGES.forEach((p) => {
      const opt = document.createElement("option");
      opt.value = p.file;
      opt.textContent = p.title;
      if (p.file === currentFile) {
        opt.selected = true;
      }
      selectEl.appendChild(opt);
    });

    selectEl.addEventListener("change", (e) => {
      if (e.target.value) {
        window.location.href = e.target.value;
      }
    });
  }

  // Kod kopyalama butonları
  document.querySelectorAll(".code-block-wrapper").forEach((wrapper) => {
    const header = wrapper.querySelector(".code-header");
    const pre = wrapper.querySelector("pre");
    if (header && pre && !header.querySelector(".copy-btn")) {
      const btn = document.createElement("button");
      btn.className = "copy-btn no-print";
      btn.type = "button";
      btn.textContent = "Kodu Kopyala";
      btn.addEventListener("click", () => {
        navigator.clipboard.writeText(pre.innerText).then(() => {
          btn.textContent = "Kopyalandı!";
          setTimeout(() => {
            btn.textContent = "Kodu Kopyala";
          }, 1500);
        });
      });
      header.appendChild(btn);
    }
  });

  // Ana sayfa ders arama filtresi
  const searchInput = document.getElementById("lesson-search-input");
  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      const q = e.target.value.toLowerCase().trim();
      document.querySelectorAll(".curriculum-row").forEach((row) => {
        const text = row.innerText.toLowerCase();
        row.style.display = text.includes(q) ? "" : "none";
      });
    });
  }
});

function printCurrentPage() {
  window.print();
}
