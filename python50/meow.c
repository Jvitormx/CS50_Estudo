#include <stdio.h>

void meow(int x);

int main(void)
{
    meow(4);
}

void meow(int x)
{
    int i;
    for(i=0;i<x;i++){
        printf("meow\n");
    }
}