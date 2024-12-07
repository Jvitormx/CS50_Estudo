#include <stdio.h>
#define TAM 4

int buscar(int vet[], int tamanho, int numero, int *place);

int main(void)
{
    int num, retorno, placeMain, vetor[]={3,5,7,8};
    printf("Num: ");
    scanf("%d", &num);

    if(buscar(vetor,TAM,num,&placeMain)==1){
        printf("Nada aqui, parceiro");
    }else{
        printf("Here it is: %d. And this is they position: %d", buscar(vetor,TAM,num, &placeMain), placeMain);
    }
}

int buscar(int vet[], int tamanho, int numero, int *place)
{
    int i,tal=-1,quant=0;
    for(i=0;i<tamanho;i++){
        if(numero==vet[i]){
            tal=vet[i];
        }
        quant++;
    }
    if(tal==-1){
        return 1;
    }else{
        *place=quant;
        return tal;
    }
}