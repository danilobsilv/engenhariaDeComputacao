#include <iostream>
#include <string>
#include <vector>
#include <cstring> // c_str, strcpy

// Definindo o tamanho do alfabeto
const int TAM_ALFABETO = 256;

// Função para computar a tabela de saltos
void computaTabelaSaltos(const char P[], const int M, char R[]) {
    for (int i = 0; i < TAM_ALFABETO; ++i) {
        R[i] = -1;
    }
    for (int j = 0; j < M; ++j) {
        R[(int)P[j]] = j;
    }
}

// Função Boyer-Moore para encontrar padrões em um texto
std::vector<std::string> boyerMoore(const char T[], const int N, const char P[], const int M, const char R[]) {
    int salto = 0;
    std::vector<std::string> saida;

    for (int i = 0; i <= N - M; i += salto) {
        salto = 0;
        for (int j = M - 1; j >= 0; --j) {
            if (P[j] != T[i + j]) {
                salto = j - R[(int)T[i + j]];
                if (salto < 1) salto = 1;
                // std::cout << salto << " ";
                saida.push_back(std::to_string(salto));
                break;
            }
        }
        if (salto == 0) {
            // std::cout << salto << " ";
            // std::cout << "(" << i << ") ";
            saida.push_back(std::to_string(salto));
            saida.push_back("(" + std::to_string(i) + ")");
            salto = 1;
        }
    }
    return saida;
}

int main() {
    //                            1         2         3         4         5         6         7       
    //                  012345678901234567890123456789012345678901234567890123456789012345678901234
    // std::string TStr = "ABCDABCABBCCDDABCDCDACAABBAAC";
    // std::string PStr = "ABCD";
    // std::string TStr = "OROBONAOROUBAROBE";
    // std::string PStr = "ROBE";
    // std::string TStr = "UAWBTESTRELAQESSS TPROXIMAOLZ AUSFTOUROMMBMUULARGVQQJXIIAMEACADOVALIQA VAA.";
    // std::string PStr = "TOURO";
    // std::string PStr = "TOLRO";
    // std::string TStr = "ASDASBBDASDAASDASAD";
    // std::string PStr = "ASDA";
    // std::string TStr = "WAABT ESTRELA QESSS TT TOURO LZAUSF CASA WMBMUULASGVQQJX II AMEACA IADFCO IANTECO VAA.";
    // std::string TStr = "WAB ESTRELA QESSS TOURO LZAUSF ULASVQQJX II AMEACA IADFCO IANTECO VAA ESTRELA.";
    std::string TStr = "MENSAGEM flibberjib zorptangle quizzlump Barril snazzlebock  wobbleplix SILVA gloptiddly scrunglewump ziggledorf frizzleplunk quibberfuzz snozzwangle EVIL.";
    std::vector<std::string> PStr_list = {"MENSAGEM", "Barril", "SILVA", "EVIL"};
    const int N = TStr.size(); 

    for(auto PStr: PStr_list) {
        const int M = PStr.size();
        char T[N + 1];
        char P[M + 1];
        
        strcpy(T, TStr.c_str());
        strcpy(P, PStr.c_str());
        char R[TAM_ALFABETO];
        
        // Computa a tabela de saltos
        computaTabelaSaltos(P, M, R);
    
        // Encontra as posições usando Boyer-Moore
        std::vector<std::string> saida = boyerMoore(T, N, P, M, R);
    
        // Imprime as posições encontradas
        std::cout << PStr << ": ";        
        for (std::string s : saida) {
            std::cout << s << " ";
        }
        std::cout << std::endl;
    }
    return 0;
}

