#include <stdio.h>
#include <stdlib.h>
 
int main(int argc, char *argv[])
{
  char letters [26] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
  int choose;
  int length;
  int logic = 0;
  printf("How many letters should your word consist of?\n");
  scanf("%i",&length);
  if(length>0)
  {
    while(logic == 0, logic <=length) //loop that displays the text
    {
      ++logic;
      choose = rand()%25;
      printf("%c", letters[choose]);
    }
  }
  else
  { 
    printf("A word must contain at least one letter!\n\n");
  }
  printf("\n"); //seperate
  system("PAUSE");  
  return 0;
}
