#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long ccnum = get_long("Number: ");
    int counteven = 0;
    int countodd = 0;
    int i = 1;

    while (ccnum > 0)
    {
        if (i % 2 == 0)
        {
            int res = (ccnum % 10) * 2;
            counteven += res / 10;
            counteven += res % 10;
        }
        else
        {
            countodd += ccnum % 10;
        }
        ccnum /= 10;
        i++;
    }
    int count = counteven + countodd;
    if (count % 10 == 0)
    {
        printf("VALID\n");
    }
    else
    {
        printf("INVALID\n");
    }
}

bool is_mastercard()
