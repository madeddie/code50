#include <cs50.h>
#include <stdio.h>

void remove_largest(int cents);

int main(void)
{
    // Prompt the user for the required change in cents
    int n;
    do
    {
        cents = get_int("Change owed: ");
    }
    while (n < 1 || n > 8);

    // Print a pyramid of that height
    for (int i = 0; i < n; i++)
    {
        // Print row of bricks
        print_row(i + 1, n);
    }
}
