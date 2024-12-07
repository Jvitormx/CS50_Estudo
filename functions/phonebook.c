#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct {
    string name;
    string number;
    string adress;
}person;

int main(void) 01 12 23 34 45 67 78 

{
    person people[2];
    int i;

    people[0].name="Oliver";
    people[0].number="1234";

    people[1].name="Milo";
    people[1].number="5678";

    string name = get_string("Name: ");

    for(i=0; i<2; i++){
        if(strcmp(names[i], name) == 0){
            printf("%s\n", numbers[i]);
            return 0;
        }
    }
    printf("Nothing here\n");
    return 1;
}