#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

void print_usage(string command);
bool all_digits(string value);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        print_usage(argv[0]);
        return 1;
    }
    else if (!all_digits(argv[1]))
    {
        print_usage(argv[0]);
        return 1;
    }
    int k = (int) argv[1];
}

void print_usage(string command)
{
    printf("Usage: %s key\n", command);
}

bool all_digits(string value)
{
    for (int i = 0, len = strlen(value); i < len; i++)
    {
        if (!isdigit(value[i]))
        {
            return 0;
        }
    }
    return 1;
}
