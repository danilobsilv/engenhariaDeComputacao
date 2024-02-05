#include <iostream>
#include <unordered_map>

std::unordered_map<std::string, char> alpha = {{":::", 'A'}, {".::", 'B'}, {":.:", 'C'}, {"::.", 'D'}, {":..", 'E'}, {".:.", 'F'}, {"..:", 'G'}, {"...", 'H'}, {"|::", 'I'}, {":|:", 'J'}, 
{"::|", 'K'}, {"|.:", 'L'}, {".|:", 'M'}, {".:|", 'N'}, {"|:.", 'O'}, {":|.", 'P'}, {":.|", 'Q'}, {"|..", 'R'}, {".|.", 'S'}, {"..|", 'T'}, {".||", 'U'}, {"|.|", 'V'}, {"||.", 'W'}, 
{"-.-", 'X'}, {".--", 'Y'}, {"--.", 'Z'}, {"---", ' '}, {"~~~", '.'}};
std::unordered_map<char, std::string> alpha_inv = {{'A', ":::"}, {'B', ".::"}, {'C', ":.:"}, {'D', "::."}, {'E', ":.."}, {'F', ".:."}, {'G', "..:"}, {'H', "..."}, {'I', "|::"}, {'J', 
":|:"}, {'K', "::|"}, {'L', "|.:"}, {'M', ".|:"}, {'N', ".:|"}, {'O', "|:."}, {'P', ":|."}, {'Q', ":.|"}, {'R', "|.."}, {'S', ".|."}, {'T', "..|"}, {'U', ".||"}, {'V', "|.|"}, {'W', 
"||."}, {'X', "-.-"}, {'Y', ".--"}, {'Z', "--."}, {' ', "---"}, {'.', "~~~"}};

const int TAM_ALFABETO = 26;

std::string decifraDeCesar(const std::string& texto, int chave) {
    std::string resultado = "";
    const std::string alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    // Inverte o sentido da chave para decifrar
    chave = -chave;
    for (char caractere : texto) {
        if (isalpha(caractere)) {
            char letra = toupper(caractere);
            int indice = (letra - 'A' + chave) % TAM_ALFABETO;
            if (indice < 0) {
                indice += TAM_ALFABETO;
            }
            resultado += alfabeto[indice];
        } else {
            resultado += caractere;
        }
    }
    return resultado;
}

int main() {
    std::string msg_alien = ":|....:.||.|::.:|:...:|.---:.:|.::..:......|||::|:.-.-:::---|.|:.||.::.::.:|:......|-.-|...|.---..|-.-|.::..:..|:....--.-.-:|..|.---:|:|:.|...|..|.|:.....|:::.:.::.:---..:...|.|.--|.:|..---|::.||::.:..:..|:......|-.-::..:..:|---:.:|..:.|.:||:....:..|:.|.:.|.---.|:|.::..:......|||::|:.::..|.---|.|-.-|.|.|.|.:.||::..||---:.:::.:.::.:|:....--.-.-:|..|.---..|-.-|..:.|.:||:......|-.-|...|.---|.|.|.|:.|..:.|.:||:.....|.|:.-.-:.|.:|---..|-.-|.::..:..|:....|::|:.-.-:::-----.|..:..:..|:.....|:|.::.|:::---...|.|.:.|..|:.::|::.---:...|||..:.|:.:...|.|:.||.::.::.:|:....:..|:.|.:.|.---:.:|.::..:......||--.|..:..:..|:....---.|:|.::..:......||..:::.:.::.:---|::.||::.:..:..|:......|-.-|...|.---.|.|....:....||~~~";

    // Traduz mensagem alienígena para latim
    std::string msg_cifrada_latim = "";
    for (int i = 0; i < msg_alien.length(); i += 3) {
        msg_cifrada_latim += alpha[msg_alien.substr(i, 3)];
    }

    // Decifra mensagem cifrada em latim
    int chave = 3;  // Utilize a mesma chave usada na cifração de César
    std::string msg_original = decifraDeCesar(msg_cifrada_latim, chave);

    std::cout << "Mensagem Original: " << msg_original << std::endl;

    return 0;
}
