#include <stdio.h>

int main(void)
{
    int a=28;
    int b=50;
    int *c=&a;

    printf("%d", *c);

    *c=14;
     c=&b;
    *c=25;

    printf("Adress of A: %p", &a);
    printf("Value of A: %d", a);

    printf("Adress of B: %p", &b);
    printf("Value of B: %d", b);

    printf("Adress of C: %p", &c);
    printf("Value of C: %p", c);
}