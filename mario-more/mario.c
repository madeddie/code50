#include <cs50.h>
#include <stdio.h>

void print_row(int bricks, int height);

int main(void)
{
    // Prompt the user for the pyramid's height
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);

    // Print a pyramid of that height
    for (int i = 0; i < n; i++)
    {
        // Print row of bricks
        print_row(i + 1, n);
    }
}

void print_row(int bricks, int height)
{
    for (int i = 0; i < height - bricks; i++)
    {
        printf(" ");
    }
    for (int j = 0; j < bricks; j++)
    {
        printf("#");
    }
    printf("  ");
    for (int k = 0; k < bricks; k++)
    {
        printf("#");
    }
    for (int l = 0; l < height - bricks; l++)
    {
        printf(" ");
    }
    printf("\n");
}
