import matplotlib.pyplot as plt

def plot_results(observed_rand, observed_lcg):
    digits = list(range(10))
    labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    fig, ax = plt.subplots()
    ax.bar(digits, observed_rand, label='GenerateUsingRand')
    ax.bar(digits, observed_lcg, label='GenerateUsingLCG')

    ax.set_xlabel('Digits')
    ax.set_ylabel('Frequency')
    ax.set_title('Digit Frequency Comparison')
    ax.set_xticks(digits)
    ax.set_xticklabels(labels)

    ax.legend()

    plt.show()

# Dados obtidos do teste
observed_rand = [10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000]
observed_lcg = [10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000]

plot_results(observed_rand, observed_lcg)
