import os
import json
from utils import extract_outline_from_pdf, rank_relevant_sections

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def main():
    input_path = os.path.join(INPUT_DIR, "input.json")
    with open(input_path, "r") as f:
        query_data = json.load(f)

    persona = query_data["persona"]
    job = query_data["job_to_be_done"]
    documents = query_data["documents"]

    response = {
        "metadata": {
            "input_documents": documents,
            "persona": persona,
            "job_to_be_done": job,
        },
        "timestamp": __import__("datetime").datetime.now().isoformat(),
        "extracted_sections": [],
        "subsection_analysis": []
    }

    for doc in documents:
        doc_path = os.path.join(INPUT_DIR, doc)
        outline = extract_outline_from_pdf(doc_path)
        ranked = rank_relevant_sections(outline, persona, job)

        for rank, item in enumerate(ranked, start=1):
            response["extracted_sections"].append({
                "document": doc,
                "page_number": item.get("page"),
                "section_title": item.get("text"),
                "importance_rank": rank
            })
            response["subsection_analysis"].append({
                "document": doc,
                "page_number": item.get("page"),
                "refined_text": item.get("text"),
            })

    output_path = os.path.join(OUTPUT_DIR, "output.json")
    with open(output_path, "w") as out:
        json.dump(response, out, indent=4)

if __name__ == "__main__":
    main()