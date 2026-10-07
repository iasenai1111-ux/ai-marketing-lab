"""Experimento 01: até onde um classificador de palavras-chave chega?
Uso: python baseline.py"""
import pandas as pd

POSITIVAS = ["adorei", "excelente", "recomendo", "muito bom", "ótimo", "gostei", "parabéns", "nota 10", "show", "valeu a pena"]
NEGATIVAS = ["péssimo", "horrível", "decepç", "decepcion", "ruim", "problema", "nunca mais", "a desejar", "bagunça"]

def classificar(texto: str) -> str:
    t = texto.lower()
    pos = sum(p in t for p in POSITIVAS)
    neg = sum(p in t for p in NEGATIVAS)
    if pos > neg: return "positivo"
    if neg > pos: return "negativo"
    return "neutro"

df = pd.read_csv("comentarios.csv")
df["previsto"] = df.comentario.apply(classificar)
df["acertou"] = df.previsto == df.sentimento

print(f"Acurácia geral: {df.acertou.mean():.1%}  ({df.acertou.sum()} de {len(df)})\n")
print("Acurácia por sentimento real:")
print((df.groupby("sentimento").acertou.mean() * 100).round(1).to_string(), "\n")
print("Matriz de confusão (linha = real, coluna = previsto):")
print(pd.crosstab(df.sentimento, df.previsto).to_string(), "\n")
print("Exemplos de erro:")
for _, r in df[~df.acertou].drop_duplicates("comentario").head(6).iterrows():
    print(f"  [{r.sentimento} -> {r.previsto}] {r.comentario}")
df[~df.acertou].to_csv("erros.csv", index=False)
