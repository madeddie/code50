#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long ccnum_orig = get_long("Number: ");
    bool valid = false;
    int counteven = 0;
    int countodd = 0;
    int i = 1;

    long ccnum_count = ccnum_orig;
    while (ccnum_count > 0)
    {
        if (i % 2 == 0)
        {
            int res = (ccnum_count % 10) * 2;
            counteven += res / 10;
            counteven += res % 10;
        }
        else
        {
            countodd += ccnum_count % 10;
        }
        ccnum_count /= 10;
        i++;
    }
    int count = counteven + countodd;
    if (count % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }
    
}
