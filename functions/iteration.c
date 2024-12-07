#include <cs50.h>
#include <stdio.h>

void draw(int n);

void draw(int n)
{
    int i;
    for(i=0;i<n;i++){
        printf("#");
    }
}

int main(void)
{
    int altura=get_int("Altura: ");
    draw(altura);
}