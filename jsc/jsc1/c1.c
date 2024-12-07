#include <stdio.h>
#include <string.h>

typedef struct{
    char nome[50];
    int idade;
    char face[10];
}user;

int main(void)
{
    user users[2];
    user user1={"marco",22,"red"};

    printf("user 1 || name: %s | idade: %d | face: %s", user1.nome, user1.idade, user1.face);
}
