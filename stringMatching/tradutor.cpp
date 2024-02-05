#include <iostream>
#include <unordered_map>

std::unordered_map<std::string, char> alpha = {{":::", 'A'}, {".::", 'B'}, {":.:", 'C'}, {"::.", 'D'}, {":..", 'E'}, {".:.", 'F'}, {"..:", 'G'}, {"...", 'H'}, {"|::", 'I'}, {":|:", 'J'}, 
{"::|", 'K'}, {"|.:", 'L'}, {".|:", 'M'}, {".:|", 'N'}, {"|:.", 'O'}, {":|.", 'P'}, {":.|", 'Q'}, {"|..", 'R'}, {".|.", 'S'}, {"..|", 'T'}, {".||", 'U'}, {"|.|", 'V'}, {"||.", 'W'}, 
{"-.-", 'X'}, {".--", 'Y'}, {"--.", 'Z'}, {"---", ' '}, {"~~~", '.'}};
std::unordered_map<char, std::string> alpha_inv = {{'A', ":::"}, {'B', ".::"}, {'C', ":.:"}, {'D', "::."}, {'E', ":.."}, {'F', ".:."}, {'G', "..:"}, {'H', "..."}, {'I', "|::"}, {'J', 
":|:"}, {'K', "::|"}, {'L', "|.:"}, {'M', ".|:"}, {'N', ".:|"}, {'O', "|:."}, {'P', ":|."}, {'Q', ":.|"}, {'R', "|.."}, {'S', ".|."}, {'T', "..|"}, {'U', ".||"}, {'V', "|.|"}, {'W', 
"||."}, {'X', "-.-"}, {'Y', ".--"}, {'Z', "--."}, {' ', "---"}, {'.', "~~~"}};

const int TAM_ALFABETO = 26;

std::string cifraDeCesar(const std::string& texto, int chave) {
    std::string resultado = "";
    const std::string alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    for (char caractere : texto) {
        if (isalpha(caractere)) { // Verifica se o caractere é uma letra
            // char maiuscula = isupper(caractere);
            char letra = toupper(caractere);
            // std::cout << letra << ","; 

            int indice = (letra - 'A' + chave) % TAM_ALFABETO;
            // std::cout << indice << ","; 
            if (indice < 0) {
                indice += TAM_ALFABETO; // Para lidar com valores negativos
            }

            char caractereCifrado = alfabeto[indice];
            // std::cout << caractereCifrado << "  ";
            resultado += caractereCifrado;
            // std::cout <<  "  ==>  " << resultado << std::endl;
            // resultado += (maiuscula) ? caractereCifrado : tolower(caractereCifrado);
        } else {
            resultado += caractere; // Mantém caracteres que não são letras inalterados
        }
    }
    // std::cout << std::endl; 
    return resultado;
}

std::string decifraDeCesar(const std::string& texto, int chave) {
    std::string resultado = "";
    const std::string alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    // Inverte o sentido da chave para decifrar
    chave = -chave;
    for (char caractere : texto) {
        if (isalpha(caractere)) { // Verifica se o caractere é uma letra
            // char maiuscula = isupper(caractere);
            char letra = toupper(caractere);
            // std::cout << letra << ","; 

            int indice = (letra - 'A' + chave) % TAM_ALFABETO;
            // std::cout << indice << "  "; 
            if (indice < 0) {
                indice += TAM_ALFABETO; // Para lidar com valores negativos
            }

            char caractereCifrado = alfabeto[indice];
            // std::cout << caractereCifrado << "  ";
            resultado += caractereCifrado;
            // std::cout <<  "  ==>  " << resultado << std::endl;
            // resultado += (maiuscula) ? caractereCifrado : tolower(caractereCifrado);
        } else {
            resultado += caractere; // Mantém caracteres que não são letras inalterados
        }
    }
    // std::cout << std::endl; 
    return resultado;
}

int main() {
    // std::string msg_terra = "UAWBTESTRELAQESSS TPROXIMAOLZ AUSFTOUROMMBMUULARGVQQJXIIAMEACADOVALIQA VAA.";
    // std::string msg_terra = "IANTECO.";
    // std::string msg_terra = "WAABT ESTRELA QESSS TT TOURO LZAUSF CASA WMBMUULASGVQQJX II AMEACA IADFCO IANTECO VAA.";
    // std::string msg_terra = "WAB ESTRELA QESSS TOURO LZAUSF ULASVQQJX II AMEACA IADFCO IANTECO VAA ESTRELA.";
    // std::string msg_terra = "MENSAGEM zibberflux snizzlequop quibblewump glopplejazz DESVIO frabblequack zonkleblip jibberflap SUSPIRAR zazzlewump quonklequop splonkleplunk quibbleflux wobblejinx ESCOLHA BRONZEsnizzleblip zibberwobble jibberdazz frabblequop PODER.";
    std::string msg_terra = "jiaodfjoifdj PREMATURE igjsgj owfkw wkg PTIMIZATION IS efioqjeoiqjoie THE ROOT OF ALL EVIL.";

    int chave = 3;
    std::string msg_terra_cifrada = cifraDeCesar(msg_terra, chave);
    std::cout << "Mensagem cifrada: " << msg_terra_cifrada << std::endl;

    // Cria msg alien
    std::string msg_alien = "";
    for (char simbolo : msg_terra_cifrada) {
        msg_alien += alpha_inv[simbolo];
        // std::cout << "simbolo:" << simbolo << "  alien: " << alpha_inv[simbolo] << std::endl;
    }
    std::cout << "Mensagem alien: " << msg_alien << std::endl;

    std::cout << "Traduzindo..." << std::endl;

    // Traduz msg para latim
    std::string msg_terra_trad_cifrada = "";
    for (int i = 0; i < msg_alien.length(); i += 3) {
        msg_terra_trad_cifrada += alpha[msg_alien.substr(i, 3)];
    }
    std::cout << "Mensagem terra cifrada:   " << msg_terra_trad_cifrada << std::endl;

    std::cout << "Decifrando..." << std::endl;
    chave = 3;
    std::string msg_terra_decifrada = decifraDeCesar(msg_terra_trad_cifrada, chave);
    std::cout << "Mensagem terra decifrada: " << msg_terra_decifrada << std::endl;

    return 0;
}

