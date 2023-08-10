import random

# Valor do dólar hoje
valor_dolar_hoje = 5.50

# Média histórica de variação diária percentual do dólar
media_variacao_percentual = 0.1

# Desvio padrão histórico da variação diária percentual do dólar
desvio_padrao_variacao = 1.5

# Gerando uma variação percentual fictícia com base na distribuição normal
variacao_percentual = random.gauss(media_variacao_percentual, desvio_padrao_variacao)

# Limitando a variação a um máximo de 3 desvios padrão
variacao_percentual = max(min(variacao_percentual, 3 * desvio_padrao_variacao), -3 * desvio_padrao_variacao)

# Cálculo do valor do dólar amanhã
valor_dolar_amanha = valor_dolar_hoje * (1 + variacao_percentual/100)

print(f"Valor do dólar hoje: {valor_dolar_hoje:.2f}")
print(f"Variação percentual fictícia: {variacao_percentual:.2f}%")
print(f"Valor do dólar amanhã: {valor_dolar_amanha:.2f}")
