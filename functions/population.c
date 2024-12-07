#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int nInicial, nFinal, years = 0;

    printf("n inicial de llamas: ");
    scanf("%d", &nInicial);

    printf("n final de llamas: ");
    scanf("%d", &nFinal);

    while(nInicial < nFinal)
    {
        nInicial += nInicial /3;
        nInicial += nInicial /4;
        years++;
    }

    printf("Years: %d\n", years);
}