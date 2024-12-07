#include <stdio.h>

void alg(int num, int first, int last);

int main(void)
{
    int n, a, b;
    printf("N: ");
    scanf("%d", &n);

    printf("A: ");
    scanf("%d", &a);

    printf("B: ");
    scanf("%d", &b);

    alg(n, a, b);
}

void alg(int num, int first, int last)
{
    int i;
   for(i=first+1;i<last;i++){
    if(i%num!=0){
        printf("%d ", i);
    }
   }
}
