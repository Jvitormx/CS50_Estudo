#include <stdio.h>

float convr(float n);

int main(void)
{
    float cel,a,b;

    printf("Celsius: ");
    scanf("%f", &cel);

    printf("%f", convr(cel));
}

float convr(float n)
{
    float fahr;
    fahr = (n*1,8)+32;
    return fahr;
}