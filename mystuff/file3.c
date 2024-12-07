#include <stdio.h>

int alg(int a);

int main(void)
{
    int n;
    do{
        printf("N: ");
        scanf("%d", &n);
    }while(n<=0);

    printf("%d\n", alg(n));
}

int alg(int a)
{
    int quant=0;
    do {
    a /= 10;
    quant++;
  }while(a!=0);
  return quant;
}
