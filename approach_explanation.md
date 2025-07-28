
---

# 🧠 Approach Explanation

## 🎯 Objective

Our goal is to build a **persona-driven document intelligence system**. Given a user-defined persona and a specific task, the system must intelligently extract and rank the most relevant sections from a set of PDF documents. This enables faster, tailored information retrieval for decision-making.

---

## 📥 Input Understanding

The input to the system is a structured JSON file containing:

* A list of PDF document file paths (uploaded to the `/input` directory).
* A `persona` representing the stakeholder (e.g., Government Officer, Data Scientist).
* A `task` that describes the user’s goal (e.g., "Analyze funding trends", "Review environmental impact").

Example:

```json
{
  "persona": "Environmental Analyst",
  "task": "Assess the impact of mining projects on local biodiversity",
  "documents": ["doc1.pdf", "doc2.pdf"]
}
```

---

## 📄 Outline Extraction

Each PDF is parsed to extract its content. Our system supports both **mock** (stubbed outlines for testing) and **real** extraction using `pdfplumber`, which preserves document structure like paragraphs and headings. The text is chunked into meaningful sections for further analysis.

This phase builds a structured representation:

```json
{
  "doc1.pdf": [
    {"heading": "Biodiversity Impact", "text": "..."},
    {"heading": "Mining Overview", "text": "..."}
  ]
}
```

---

## 🧠 Ranking Method

We use the `sentence-transformers` library (`all-MiniLM-L6-v2`) to semantically embed:

* Each text section from the documents
* The combined persona + task string

For each document section:

1. Compute its embedding.
2. Compute cosine similarity with the persona+task embedding.
3. Assign a relevance score.

Top-k relevant sections are selected based on highest similarity values and returned as output.

---

## 🧑‍💼 Handling Persona + Task

The persona and task are combined into a single input prompt:

> `"As a [persona], your task is to [task]"`

This formulation helps contextualize the semantic intent of the user when encoding via the sentence transformer, resulting in better alignment with relevant document chunks.

---

## 🧩 Assumptions

* PDF content is mostly extractable as text (not image-based).
* Persona and task are sufficiently descriptive to guide semantic ranking.
* Sections are independent; cross-section relevance is not calculated.

---

## ⚠️ Limitations & Future Improvements

**Current limitations:**

* OCR not implemented (text in scanned/image-based PDFs will be ignored).
* Equal weight is given to all sections regardless of document metadata.
* Only cosine similarity is used for ranking — no advanced reranking.

**Future improvements:**

* Integrate layout-aware models (e.g., LayoutLM).
* Implement OCR fallback for image-based PDFs.
* Add multi-modal reasoning using vision-language models.
* Cache embeddings to optimize for large-scale PDFs.

