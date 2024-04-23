populacao_A = 80000
taxa_crescimento_A = 3
populacao_B = 200000
taxa_crescimento_B = 1.5

anos = 0
for ano in range(1, 1000):
    populacao_A *= (1 + taxa_crescimento_A / 100)
    populacao_B *= (1 + taxa_crescimento_B / 100)
    if populacao_A >= populacao_B:
        anos = ano
        break

print(f"São necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")