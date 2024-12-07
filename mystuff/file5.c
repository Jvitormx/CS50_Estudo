#include <stdio.h>

void alg(int first, int last);

int main(void)
{
    int a, b;

    printf("A: ");
    scanf("%d", &a);

    printf("B: ");
    scanf("%d", &b);

   alg(a, b);
}

void alg(int first, int last)
{
    int i,quant=0,x=1;
    for(i=first;i<last;i*=2){
        x=x*2;
        printf("%d ", x);
        if(i==x){
            quant++;code
        }
    }
    printf("\n %d\n", quant);
}
