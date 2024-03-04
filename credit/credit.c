#include <cs50.h>
#include <stdio.h>

int get_first2(int cardnum);

int main(void)
{
    long ccnum_orig = get_long("Number: ");
    bool valid = false;
    int counteven = 0;
    int countodd = 0;
    int cardlen = 0;

    long ccnum_count = ccnum_orig;
    while (ccnum_count > 0)
    {
        if (cardlen % 2 == 1)
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
        cardlen++;
    }
    int count = counteven + countodd;
    if (count % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }
    switch(get_first2(ccnum_orig))
    {
        case 51:
        case 52:
        case 53:
        case 54:
        case 55:
            if (cardlen == 16)
                printf("MASTERCARD");
            break;
    }
}

int get_first2(int cardnum)
{
    while (cardnum > 100)
    {
        cardnum /= 10;
    }
    return cardnum;
}
