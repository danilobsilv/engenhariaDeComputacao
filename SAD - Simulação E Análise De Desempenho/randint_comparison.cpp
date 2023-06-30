#include <iostream>
#include <chrono>
#include <random>
#include <vector>
#include <cmath>

class GenerateUsingRand {
public:
    GenerateUsingRand() :
        first_comp(100000),
        second_comp(1000000),
        third_comp(10000000),
        fourth_comp(100000000)
    {}

    int generate(int iterations) {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<int> distribution(0, 9);

        int sum = 0;
        for (int i = 0; i < iterations; ++i) {
            int randomNumber = distribution(gen);
            sum += randomNumber;

            // Atualiza o vetor observed para contagem dos dígitos observados
            observed[randomNumber]++;
        }

        return sum;
    }

    void runTests() {
        std::chrono::high_resolution_clock::time_point start, end;
        double elapsed_seconds;

        std::cout << "Time comparison using GenerateUsingRand:\n";

        start = std::chrono::high_resolution_clock::now();
        firstGen();
        end = std::chrono::high_resolution_clock::now();
        elapsed_seconds = std::chrono::duration<double>(end - start).count();
        std::cout << "1st time: " << elapsed_seconds << " seconds" << std::endl;

        start = std::chrono::high_resolution_clock::now();
        secondGen();
        end = std::chrono::high_resolution_clock::now();
        elapsed_seconds = std::chrono::duration<double>(end - start).count();
        std::cout << "2nd time: " << elapsed_seconds << " seconds" << std::endl;

        start = std::chrono::high_resolution_clock::now();
        thirdGen();
        end = std::chrono::high_resolution_clock::now();
        elapsed_seconds = std::chrono::duration<double>(end - start).count();
        std::cout << "3rd time: " << elapsed_seconds << " seconds" << std::endl;

        start = std::chrono::high_resolution_clock::now();
        fourthGen();
        end = std::chrono::high_resolution_clock::now();
        elapsed_seconds = std::chrono::duration<double>(end - start).count();
        std::cout << "4th time: " << elapsed_seconds << " seconds" << std::endl;
    }

    std::vector<int> getObserved() const {
        return observed;
    }

private:
    int firstGen() {
        return generate(first_comp);
    }

    int secondGen() {
        return generate(second_comp);
    }

    int thirdGen() {
        return generate(third_comp);
    }

    int fourthGen() {
        return generate(fourth_comp);
    }

    int first_comp;
    int second_comp;
    int third_comp;
    int fourth_comp;
    std::vector<int> observed = std::vector<int>(10, 0);  // Vetor para contagem dos dígitos observados
};


// ----------------------------------------------------------------------------------------------------

class LinearCongruentialGenerator {
public:
    LinearCongruentialGenerator(uint64_t a, uint64_t c) : seed(1), multiplier(a), increment(c) {}

    uint64_t generateRandomNumber() {
        const uint64_t modulo = 18446744073709551615ULL;

        seed = (multiplier * seed + increment) % modulo;
        return seed;
    }

private:
    uint64_t seed;
    uint64_t multiplier;
    uint64_t increment;
};

class GenerateUsingLCG {
public:
    GenerateUsingLCG() :
        first_comp(100000),
        second_comp(1000000),
        third_comp(10000000),
        fourth_comp(100000000),
        lcg(3935559000370003845ULL, 2691343689449507681ULL)
    {}

    int generate(int iterations) {
        int sum = 0;
        for (int i = 0; i < iterations; ++i) {
            uint64_t randomNumber = lcg.generateRandomNumber();
            sum += randomNumber % 10;

            // Atualiza o vetor observed para contagem dos dígitos observados
            observed[randomNumber % 10]++;
        }

        return sum;
    }

    void runTests() {
        std::chrono::high_resolution_clock::time_point start, end;
        double elapsed_seconds;

        std::cout << "Time comparison using GenerateUsingLCG:\n";

        start = std::chrono::high_resolution_clock::now();
        firstGen();
        end = std::chrono::high_resolution_clock::now();
        elapsed_seconds = std::chrono::duration<double>(end - start).count();
        std::cout << "1st time: " << elapsed_seconds << " seconds" << std::endl;

        start = std::chrono::high_resolution_clock::now();
        secondGen();
        end = std::chrono::high_resolution_clock::now();
        elapsed_seconds = std::chrono::duration<double>(end - start).count();
        std::cout << "2nd time: " << elapsed_seconds << " seconds" << std::endl;

        start = std::chrono::high_resolution_clock::now();
        thirdGen();
        end = std::chrono::high_resolution_clock::now();
        elapsed_seconds = std::chrono::duration<double>(end - start).count();
        std::cout << "3rd time: " << elapsed_seconds << " seconds" << std::endl;

        start = std::chrono::high_resolution_clock::now();
        fourthGen();
        end = std::chrono::high_resolution_clock::now();
        elapsed_seconds = std::chrono::duration<double>(end - start).count();
        std::cout << "4th time: " << elapsed_seconds << " seconds" << std::endl;
    }

    std::vector<int> getObserved() const {
        return observed;
    }

private:
    int firstGen() {
        return generate(first_comp);
    }

    int secondGen() {
        return generate(second_comp);
    }

    int thirdGen() {
        return generate(third_comp);
    }

    int fourthGen() {
        return generate(fourth_comp);
    }

    int first_comp;
    int second_comp;
    int third_comp;
    int fourth_comp;
    std::vector<int> observed = std::vector<int>(10, 0);  // Vetor para contagem dos dígitos observados
    LinearCongruentialGenerator lcg;
};


// -----------------------------------------------------------------------------------------------------------------

double chi_squared_test(const std::vector<int>& observed, const std::vector<int>& expected) {
    double chi_squared = 0.0;

    for (size_t i = 0; i < observed.size(); ++i) {
        double diff = static_cast<double>(observed[i]) - expected[i];
        chi_squared += (diff * diff) / expected[i];
    }

    return chi_squared;
}

void print_results(double chi_squared, double p_value, bool passed) {
    std::cout << "Chi-Square Statistics: " << chi_squared << std::endl;
    std::cout << "P-Value: " << p_value << std::endl;
    std::cout << "Test " << (passed ? "Approved" : "Disapproved") << std::endl;
}

void run_chi_squared_test(const std::vector<int>& observed, const std::vector<int>& expected) {
    double chi_squared = chi_squared_test(observed, expected);
    double p_value = 1.0 - std::erf(std::sqrt(chi_squared / 2.0));

    bool passed = (p_value >= 0.05);  // Usando um nível de significância de 0.05

    print_results(chi_squared, p_value, passed);
}

int main() {
    GenerateUsingRand gen;
    GenerateUsingLCG gento;

    gen.runTests();
    std::cout << "\n";
    gento.runTests();

    std::vector<int> observedRand = gen.getObserved();  // Vetor observed do GenerateUsingRand
    std::vector<int> expected = { // Vetor expected com contagem esperada de cada dígito (0 a 9)
        10000000, 10000000, 10000000, 10000000, 10000000,
        10000000, 10000000, 10000000, 10000000, 10000000
    };

    run_chi_squared_test(observedRand, expected);

    std::vector<int> observedLCG = gento.getObserved();  // Vetor observed do GenerateUsingLCG

    run_chi_squared_test(observedLCG, expected);

    return 0;
}
