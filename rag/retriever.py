from models.product import Product


STOP_WORDS = {
    "a","an","the","is","are","was","were","what","which","who","can","i","do",
    "you","have","any","for","me","best","good","with","tell","about","some",
    "give","find","show","want","need","looking","recommend","suggest","help"
}


def retrieve_relevant_products(question: str, top_k: int = 5) -> list:
    """
    Score every product by keyword overlap with the question.
    Apply lightweight price-intent boosting.
    Return top_k as dicts.
    """
    q = question.lower()
    tokens = [t.strip("?,!.") for t in q.split() if t not in STOP_WORDS and len(t) > 2]

    all_products = Product.query.all()
    scored = []

    for p in all_products:
        haystack = f"{p.name} {p.description} {p.tags} {p.category}".lower()
        score = sum(1 for tok in tokens if tok in haystack)

        # price-intent boosts
        if any(w in q for w in ["cheap", "budget", "affordable", "under", "inexpensive"]):
            score += 40.0 / (p.price + 1)
        if any(w in q for w in ["premium", "best", "quality", "top", "high-end"]):
            score += p.price / 400.0

        if score > 0:
            scored.append((score, p))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [p.to_dict() for _, p in scored[:top_k]]


def build_context(products: list) -> str:
    if not products:
        return "No matching products found in the store."
    lines = []
    for p in products:
        lines.append(
            f"• [{p['category']}] {p['name']} — ${p['price']:.2f}\n"
            f"  {p['description']}\n"
            f"  Tags: {p['tags']}"
        )
    return "\n\n".join(lines)
