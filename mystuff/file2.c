#include <stdio.h>

void exibir(int n, int menor, int maior);

int main(void)
{
    int n, menorN, maiorN;
    printf("N: ");
    scanf("%d", n);

    printf("Menor numero: ");
    scanf("%d", menorN);

    printf("Maior numero: ");
    scanf("%d", maiorN);

    void exibir(n, menorN, maiorN);
}

void exibir(int n, int menor, int maior)
{
    int i;
    for(i=menor;i<maior;i++){
        if(i%n!=0){
            printf("%d", i);
        }
    }
}