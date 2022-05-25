#include <stdio.h>
#include <stdlib.h>

int main(){

    int vet[10];
    for (int i = 0; i < 10; ++i)
    {
        int a;
        scanf(" %d", &a);
        vet[i] = a;
    }

    int vetcopy[10];
    for(int i = 0; i < 10; i++)
      {
         vetcopy[i] = vet[i]; 
      }

    int values[11] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

    int repeat = 0;
    for (int i = 0; i < 10; ++i)
    {
        if (values[i] == 0)
            repeat++;

        values[vet[i]] += 1;
    }

    int position = 0;
    int* vet2 = (int*)malloc(sizeof(int) * repeat);
    for (int i = 0; i < repeat; ++i)
    {
        if (values[i] == 0)
            continue;

        vet2[position] = values[i];
        ++position;
    }

    for (int i = 0; i < repeat; ++i)
    {
        for (int j = i + 1; j < repeat; ++j)
        {
            if (vet2[i] < vet2[j])
            {
                int temp = vet2[i];
                vet2[i] = vet2[j];
                vet2[j] = temp;
            }
        }
    }

    for (int i = 0; i < 10; i++)
    {
        printf("%d ", vetcopy[i]);
    }
  printf("\n");
  
    for (int i = 0; i < repeat; i++)
    {
        if (values[i] == 0)
        {
            continue;
        }
          

        printf("%d ", values[i]);
    }
  }