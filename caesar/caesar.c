#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

void print_usage(string command);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        print_usage(argv[0]);
        return 1;
    }
    
}

void print_usage(string command)
{
    printf("Usage: %s key\n", command);
}
