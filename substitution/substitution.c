#import <cs50.h>
#import <stdio.h>
#import <string.h>

void print_usage(string arg);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        print_usage(argv[0]);
        return 1;
    }
    else if (strlen(argv[1]) != 26)
    {
        print_usage(argv[0]);
        return 1;
    }
}

void print_usage(string arg)
{
    printf("Usage: %s key_of_26_chars\n", arg);
}
