#include <stdio.h>

int dois(int num, int *maisum);

int main(void)
{
    int num, *maisum;
    printf("num: ");
    scanf("%d", &num);

    printf("%d\n",dois(num, *maisum));
    printf("%d\n", maisum);

}

int dois(int num, int *maisum)
{
    *maisum=(num*2)+1;
    return num*2;
}
