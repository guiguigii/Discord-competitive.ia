import os

CORPUS_DIR = "corpus"

def load_corpus():
    texts = {}
    for fname in os.listdir(CORPUS_DIR):
        if fname.endswith(".md"):
            with open(os.path.join(CORPUS_DIR, fname), "r", encoding="utf-8") as f:
                texts[fname] = f.read()
    return texts

corpus = load_corpus()

def answer_question(question: str) -> str:
    # Simplão: procura palavras-chave nos arquivos
    for name, text in corpus.items():
        if any(word.lower() in text.lower() for word in question.split()):
            return f"📘 **Fonte {name}**\n\n{text[:500]}..."
    return "🤔 Não encontrei nada no corpus ainda. Adicione mais info em /corpus!"
