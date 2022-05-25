#include <stdio.h>
#include <stdlib.h>

int main()
{   

FILE* file;
    file = fopen("wordlines.txt", "w");

    for (int i = 0; i < 3; ++i)
    {
        char word[255];
        printf("insira as palavras:\n");
        gets(word);
        fprintf(file, "%s\n", word);
    }

    fclose(file);

    file = fopen("wordlines.txt", "r");

    char ch;
    int lineCounter = 0;
    while (!feof(file))
    {
        ch = fgetc(file);
        if (ch == '\n')
            lineCounter++;
    }

    printf("O arquivo tem %d linhas.", lineCounter);

    fclose(file);
}