#include <stdio.h>
#define TAM 4

void swap(int vet[], int tamanho);

int main(void)
{
    int i, vetor[]={30,40,50,60};

    for(i=0;i<TAM;i++)
    {
        printf("%d ", vetor[i]);
    }
    printf("\n ");

    swap(vetor,TAM);
}

void swap(int vet[], int tamanho)
{
    int i, aux;
    for(i=0;i<tamanho;i++)
    {
        vet[i+1]=vet[i];
        vet[i]=aux;
    }

    for(i=0;i<tamanho;i++)
    {
        printf("%d ", vet[i]);
    }
}