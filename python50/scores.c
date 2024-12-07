#include <stdio.h>
#define TAM 3

int score(int scores[], int tamanho);

int main(void)
{
    int scores[]={72,73,33};
    printf("%d", score(scores, TAM));
}


int score(int scores[], int tamanho)
{
    int i, quant=0, soma=0;

    for(i=0;i<tamanho;i++){
        soma+=scores[i];
        quant++;
    }
    return soma/quant;
}