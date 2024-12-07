#include <stdio.h>

#define QUANT 5

/*
Foi feita uma pesquisa entre os habitantes
de uma região e coletados os dados de
altura e gênero das pessoas. Faça um
programa que leia as informações de 50
pessoas e informe:
− a maior e a menor alturas
encontradas;
− a média de altura das mulheres;
− a média de altura da população;
− o percentual de homens na
população.
*/


int main(void)
{
    int i;
    float altura;
    char gen;

    for(i=1;i<=QUANT;i++){
        printf("Altura: ");
        scanf("%d",&altura);

        printf("Genere: ");
        scanf("%c", &gen);
    }
}