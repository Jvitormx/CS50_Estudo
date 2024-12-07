#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
  string strings[]={"battleship", "boot", "cannon", "iron", "thimble", "top hat"};
  int i;

  string a = get_string("Enter with what u really want: ");

  for(i=0;i<6;i++){
    if(strcmp(strings[i], a) == 0){
      printf("found\n");
      return 0;
    }

  }
  printf("nothing at all\n");
  return 1;

}