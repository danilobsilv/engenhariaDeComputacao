import matplotlib.pyplot as plt

# Resultados obtidos pelo código em C++
observed_rand = [10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000]
observed_lcg = [9998469, 10004823, 9997611, 10000871, 10000843, 10004635, 10000342, 9999516, 10000813, 10000667]

digits = list(range(10))

plt.figure(figsize=(8, 6))
plt.bar(digits, observed_rand, label='GenerateUsingRand', alpha=0.7)
plt.bar(digits, observed_lcg, label='GenerateUsingLCG', alpha=0.7)
plt.xlabel('Dígitos')
plt.ylabel('Contagem')
plt.title('Contagem de dígitos observados')
plt.legend()

plt.show()
