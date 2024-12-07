#include <cs50.h>
#include <stdio.h>

typedef struct
{
    string name;
    string votes;
}
candidate;

candidate get_candidate(string prompt);

int main(void)
{
    candidate president = get_president("Enter a candidate: ");
    printf("name: %s", president.name);
    printf("votes: %d", president.votes);
}

candidate get_candidate(string prompt)
{
    printf("%s\n", prompt);
    candidate c;
    c.name = get_string("Enter a name: ")
    c.votes = get_int("Enter number os votes: ")
    return c;
}