from flask import Blueprint, jsonify, request
import requests
import traceback
import os
from dotenv import load_dotenv

from rag.retriever import retrieve_relevant_products, build_context

# Load environment variables
load_dotenv()

assistant_bp = Blueprint("assistant", __name__)

# Groq API setup
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
print(os.getenv("GROQ_API_KEY"))
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

SYSTEM = """You are a warm, knowledgeable shopping assistant for Ragalia — a curated Online store.
Help customers find products, compare options, and make confident purchase decisions.

Rules:
- Be concise and friendly (max ~120 words unless a detailed comparison is asked)
- Only reference products explicitly listed in the context below
- Always mention product names and prices when relevant
- If nothing matches, say so politely and suggest browsing categories
- Never invent products or prices
"""


@assistant_bp.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json(silent=True) or {}
        question = (data.get("question") or "").strip()

        if not question:
            return jsonify({"error": "question is required"}), 400

        # ---------------------------
        # RAG: Retrieve products
        # ---------------------------
        products = retrieve_relevant_products(question, top_k=5)
        context = build_context(products)

        user_message = f"""Customer question: {question}

Available products from our store:
{context}

Answer the customer helpfully based only on the products above.
"""

        # ---------------------------
        # GROQ API CALL
        # ---------------------------
        response = requests.post(
            GROQ_URL,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {GROQ_API_KEY}"
            },
            json={
                "model": "llama-3.1-8b-instant",
                "messages": [
                    {"role": "system", "content": SYSTEM},
                    {"role": "user", "content": user_message},
                ],
                "temperature": 0.7
            },
            timeout=60
        )

        if response.status_code != 200:
            print(f"❌ Groq error {response.status_code}: {response.text}")
            return jsonify({
                "error": "Groq API error",
                "details": response.text
            }), 500

        answer = response.json()["choices"][0]["message"]["content"]

        return jsonify({
            "answer": answer,
            "products_used": products
        })

    except requests.exceptions.RequestException as e:
        print("❌ Network error:", str(e))
        return jsonify({"error": "Network error while calling Groq API"}), 500

    except Exception as e:
        print("❌ ERROR in /ask:", str(e))
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500