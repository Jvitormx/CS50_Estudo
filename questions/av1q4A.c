#include <stdio.h>

int main(void)
{
    int valor, temp, cont=1;

    printf("Valor: ");
    scanf("%d", &valor);

    do{
        temp=valor;
        printf("Valor: ");
        scanf("%d", &valor);
        if(valor!=temp){
            printf("%d-%d vezes\n", temp, cont);
            cont=1;
        }else{
            cont++;
        }
    }while(valor!=0);
}