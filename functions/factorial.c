#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib>

int main(void)
{

    char a='A';
    char b='A';

    if(a==b){
        printf("equal\n");
    }else{
        printf("not equal\n");
    }

    char *s="AAAA";
    printf("%s\n\n", s);




    int n=50;
    int *m=&n;
    printf("%p\n", m);
    printf("%d\n", *m);

    int array[300];
    for(int y=0;y<300;y++){
        printf("\n%d\n", array[y]);
    }
    int *size = malloc()
}