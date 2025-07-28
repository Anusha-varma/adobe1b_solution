from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_outline_from_pdf(pdf_path):
    # Placeholder outline for demo purposes
    return [
        {"level": "H1", "text": "Introduction to Graph Neural Networks", "page": 1},
        {"level": "H2", "text": "Datasets for Drug Discovery", "page": 2},
        {"level": "H2", "text": "Performance Benchmarks", "page": 3},
    ]

def rank_relevant_sections(outline, persona, job):
    query = f"{persona}. Task: {job}"
    query_embedding = model.encode(query, convert_to_tensor=True)
    results = []

    for section in outline:
        section_embedding = model.encode(section["text"], convert_to_tensor=True)
        similarity = util.pytorch_cos_sim(query_embedding, section_embedding).item()
        section["score"] = similarity
        results.append(section)

    return sorted(results, key=lambda x: x["score"], reverse=True)