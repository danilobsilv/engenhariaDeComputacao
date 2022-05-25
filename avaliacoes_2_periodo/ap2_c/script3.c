#include <stdio.h>
#include <stdlib.h>

int main() {
    int N, M;
    printf("Digite N: ");
    scanf("%d", &N);

    printf("Digite M: ");
    scanf("%d", &M);


    M -= 1;

    int* array_ = malloc(sizeof(int) * N);
    for (int i = 0; i < N; ++i) {
        int valor;
        scanf("%d", &valor);
        array_[i] = valor;
    }

    int*copia = malloc(sizeof(int) * N);
    for(int i = 0; i < N; ++i)
    {
        copia[i] = array_[i];
    }

    while (M) {
        int vet = array_[0];
        for (int i = 0; i < N - 1; i++) {
            array_[i] = array_[i + 1];
        }

        array_[N - 1] = vet;

        --M;
    }
    for (int i = 0; i < N; ++i) {
        printf("%d, ", copia[i]);
    }
  printf("\n");
    for (int i = 0; i < N; ++i) {
        printf("%d, ", array_[i]);
    }

    free(array_);
}