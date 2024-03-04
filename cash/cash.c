#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt the user for the required change in cents as positive integer
    int cents = -1;
    while (cents < 0)
    {
        cents = get_int("Change owed: ");
    }

    int changecoins = 0;
    // delete 25, 10, 5 or 1 cents
    while (cents > 0)
    {
        if (cents >= 25)
        {
            cents -= 25;
            changecoins++;
        }
        else if (cents >= 10)
        {
            cents -= 10;
            changecoins++;
        }
        else if (cents >= 5)
        {
            cents -= 5;
            changecoins++;
        }
        else
        {
            cents -= 1;
            changecoins++;
        }
    }
    printf("%d\n", changecoins);
}
