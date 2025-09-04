import spacy
import pandas as pd

# ========================== InovaTech ==========================
# Responsável: carregar dicionário cultural no código (primeiro em memória)
# e implementar função simples de busca
# ----------------------------------------------------------

# Carregar modelo do spaCy em português
nlp = spacy.load("pt_core_news_sm")

# Carregar glossário CSV
df = pd.read_csv("datasets/dicionario_cultural2.csv")

# Criar dicionário a partir do CSV
glossario = {}
for _, row in df.iterrows():
    termo = str(row["termo"]).lower().strip()
    glossario[termo] = {
        "significado": row["significado"],
        "explicacao": row["explicacao"],
        "exemplo": row["exemplo"],
        "contextualizacao": row["contextualizacao"],
    }

# ======================== FIM InovaTech ========================

# ========================= MANUEL =========================
# Responsável: implementar motor NLP (tokenização + detecção de gírias)
# e integrar tradução/explicação final
# ----------------------------------------------------------
def traduzir_frase(frase):
    doc = nlp(frase)
    explicacoes = []

    for token in doc:
        termo = token.text.lower()
        if termo in glossario:
            g = glossario[termo]
            explicacoes.append(
                f"'{termo}' → {g['significado']}\n"
                f"Explicação: {g['explicacao']}\n"
                f"Exemplo: {g['exemplo']}\n"
                f"Contextualização: {g['contextualizacao']}\n"
            )

    return explicacoes if explicacoes else ["Nenhuma gíria encontrada."]

# ======================= FIM MANUEL =======================

# ======================== JOEL ==========================
# Responsável: interface de uso (CLI → Web)
# Criar CLI interativa e evoluir para API REST
# ----------------------------------------------------------
# contador global de traduções
contador_traducoes = 0

def main():
    global contador_traducoes
    print("=== Tradutor Cultural com IA ===")
    while True:
        frase = input("Digite uma frase (ou 'sair' para encerrar): ")
        if frase.lower() == "sair":
            print(f"Total de traduções realizadas: {contador_traducoes}" + "," + " Isso reflete o quanto os turistas usam nosso app para aprender gírias locais")
            break

        resultado = traduzir_frase(frase)
        for explicacao in resultado:
            print(explicacao)
        contador_traducoes += 1
        print("-" * 40)

if __name__ == "__main__":
    main()
# ======================= FIM JOEL =======================
