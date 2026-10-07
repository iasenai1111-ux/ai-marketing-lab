# Experimento 01: classificador de comentários por palavras-chave

**Pergunta:** antes de usar IA, até onde chega a solução mais simples possível?

## Como testei

- 300 comentários fictícios de clientes, já rotulados como positivo, negativo ou neutro ([`comentarios.csv`](comentarios.csv)).
- Um classificador de 15 linhas: conta palavras positivas e negativas no texto e fica com o lado que tiver mais ([`baseline.py`](baseline.py)).
- Comparei a previsão com o rótulo real.

## Resultado

**Acurácia geral: 74,3%** (223 de 300).

| Sentimento real | Previsto negativo | Previsto neutro | Previsto positivo | Acerto |
|---|---:|---:|---:|---:|
| Negativo (97) | 52 | 35 | 10 | 53,6% |
| Neutro (79) | 0 | 79 | 0 | 100% |
| Positivo (124) | 9 | 23 | 92 | 74,2% |

## Onde ele erra

| Comentário | Real | Previsto | Por quê |
|---|---|---|---|
| "Não gostei do preço." | negativo | positivo | Viu "gostei" e ignorou o "não" |
| "O preço foi horrível, não recomendo." | negativo | neutro | "horrível" e "recomendo" empataram |
| "Não tenho do que reclamar do preço." | positivo | neutro | Elogio sem nenhuma palavra positiva |
| "Esperava mais do site." | negativo | neutro | Crítica sem nenhuma palavra negativa |
| "Achei que ia ser ruim, mas a entrega foi show." | positivo | neutro | "ruim" e "show" empataram |

## O que aprendi

- Palavras-chave resolvem o caso fácil e falham em **negação**, **contraste** ("mas") e **sentido implícito**.
- O erro mais grave é o negativo lido como positivo: 10 clientes insatisfeitos passariam como satisfeitos.
- 100% de acerto em neutro engana: tudo o que o classificador não entende cai em neutro.
- Como os comentários foram gerados a partir de modelos de frase, o texto real de redes sociais (gírias, ironia, erros de digitação) deve ser mais difícil do que este.

## Próximo passo

Experimento 02: classificar os mesmos 300 comentários com um LLM e comparar com estes 74,3%, olhando também custo e tempo.

## Como rodar

```bash
pip install pandas
python baseline.py
```
