
---

```markdown
# 🧠 Adobe India Hackathon 2025 – Round 1B Solution

## 👩‍💻 Problem Statement: Persona-Driven Document Intelligence

This solution extracts relevant sections from a set of PDFs based on a given *persona* and *task*. It uses an LLM-based pipeline to:
- Segment the documents into headings
- Score them using persona-task relevance
- Return the top-ranked sections per document in structured JSON format.

---

## 🗂️ Directory Structure

```

adobe1b\_solution/
├── input/                  # Folder containing input PDF documents
│   └── doc1.pdf
├── output/                 # Folder to store output JSON results
├── sample\_input/           # Contains input JSON describing persona, task, etc.
│   └── input.json
├── main.py                 # Entry-point script
├── utils.py                # Core pipeline utilities
├── Dockerfile              # For containerized execution
└── requirements.txt        # Python dependencies

````

---

## 🚀 Run Using Docker

Make sure Docker is installed and running.

### 1. Build the Docker Image
```bash
docker build --platform linux/amd64 -t outline_extractor:latest .
````

### 2. Run the Container

```bash
docker run -v $(pwd)/input:/app/input \
           -v $(pwd)/output:/app/output \
           -v $(pwd)/sample_input:/app/sample_input \
           outline_extractor:latest
```

---

## 🔧 Run Locally (Without Docker)

Make sure you have **Python 3.9+** installed.

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Pipeline

```bash
python main.py --input_json sample_input/input.json --input_dir input --output_dir output
```

---

## 📥 Sample Input Format

```json
{
  "persona": "Environmental Researcher",
  "task": "Investigate the environmental impacts of mining",
  "documents": ["doc1.pdf"]
}
```

---

## 📤 Output Format

```json
{
  "doc1.pdf": [
    {
      "heading": "Mining Effects on Biodiversity",
      "text": "The environmental impact of mining includes erosion, loss of biodiversity...",
      "score": 0.84
    }
  ]
}
```

---

## 🧪 Testing Tips

* Ensure all PDFs are placed in the `input/` folder.
* Modify `sample_input/input.json` to include the document names you're using.
* Output will be saved in `output/output.json`.



---

```

Let me know if you also want me to auto-generate a clean `.gitignore` or a downloadable version of this `README.md`.
```
