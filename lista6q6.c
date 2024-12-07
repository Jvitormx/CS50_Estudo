#include <stdio.h>

int main(void)
{
    int num, maiorPar=-1, countPar=0, somaPar=0;
    float mediaPar;

    for(int i=0;i<10;i++)
    {
        scanf("%d", &num);
        if(num%2==0){
            somaPar+=num;
            countPar++;
            if(num>maiorPar){
                maiorPar=num;
            }
        }
    }
    printf("%.1f\n", somaPar/(float)countPar);
    printf("%d", maiorPar);
}