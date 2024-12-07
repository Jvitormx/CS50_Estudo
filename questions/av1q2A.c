#include <stdio.h>

int main(void)
{
    int i,x,n,pot=1;
/*

    printf("%d ", pot);
    for(i=1;i<n;i++){
        printf("%d ", pot*=x);
    }

        i=1;
    while(i<n){
        printf("%d ", pot*=x);
        i++;
    }

*/
    printf("x: ");
    scanf("%d", &x);

    printf("n: ");
    scanf("%d", &n);

    printf("%d ", pot);

    i=1;
    do{
        printf("%d ", pot*=x);
        i++;
    }while(i<n);
}