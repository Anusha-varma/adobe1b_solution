
---

```markdown
# 🧠 Adobe India Hackathon 2025 - Round 1B Submission

## 📌 Project Title
**Persona-Based Document Insight Extractor**

---

## 🎯 Objective

The objective of this project is to build a **persona-aware document understanding system** that extracts and ranks the most relevant sections from PDF documents based on a given persona and task. This system helps different stakeholders quickly access the most pertinent information tailored to their roles.

---

## 🔁 Input Understanding

The system accepts:

- A **persona** (e.g., Legal Advisor, Project Manager)
- A **task description** (e.g., "review compliance clauses", "identify budget overrun risks")
- A folder containing **multiple PDF documents**

The input is provided as a structured JSON, and the PDFs are parsed for analysis.

---

## 🧩 Outline Extraction

We use a hybrid pipeline with options for both **mocked outline extraction** and **real text extraction** (for Round 1B, we have a working text extractor). It:
- Extracts headings and subheadings using PDFMiner and regex heuristics
- Cleans and formats the text into a list of outlined chunks

---

## 🧠 Ranking Method

Each chunk of extracted text is ranked based on its relevance to the persona and task using:

- A **sentence-transformer** (`all-MiniLM-L6-v2`) to generate embeddings
- **Cosine similarity** to score each section against the combined persona + task query

The top `k` most relevant chunks are returned in ranked order.

---

## 🧑‍💼 Handling Persona + Task

We construct a unified semantic query:
```

[Persona]: [Task]

```
This combined query ensures contextual relevance. For example:
```

"Legal Advisor: Review compliance clauses related to data usage"

````

This query is then compared with all document sections to find the most semantically relevant ones.

---

## ⚙️ Setup Instructions (Docker)

### 1. Clone this repo:
```bash
git clone https://github.com/your-username/adobe-hackathon-25.git
cd adobe-hackathon-25
````

### 2. Build the Docker image:

```bash
docker build --platform linux/amd64 -t adobe_outline_extractor:anusha .
```

### 3. Run the container:

```bash
docker run -it --rm adobe_outline_extractor:anusha
```

---

## 📦 Folder Structure

```
.
├── main.py                 # Main entry point
├── utils.py                # PDF and text extraction functions
├── approach_explanation.md # Summary of method
├── sample_input.json       # Sample input for testing
├── Dockerfile              # Container config
```

---

## ✅ Assumptions

* PDFs are mostly structured with consistent headings and subheadings
* The persona and task provided are semantically aligned with document content
* Sentence-transformer model is sufficient for relevance scoring

---

## ⚠️ Limitations & Future Improvements

* Headings are detected via regex; may fail for poorly formatted PDFs
* Ranking is purely semantic — no metadata or section type weighting
* No OCR support yet (for scanned/image-based PDFs)
* Can be enhanced with LLMs for abstractive summarization or zero-shot QA

