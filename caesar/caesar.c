#include <stdio.h>

char ALPHA[] = {'a', 'b', 'c', 'd', 'e', 'f'};

int main(void)
{
    printf("char 2 %c, char -5 %c\n", ALPHA[2], ALPHA[2 - 13]);
}
