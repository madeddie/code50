#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_usage(string command);
bool not_digits(string value);
char rotate(int k, char c);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        print_usage(argv[0]);
        return 1;
    }
    else if (not_digits(argv[1]))
    {
        print_usage(argv[0]);
        return 1;
    }
    int key = atoi(argv[1]);
    string plaintext = get_string("plaintext:  ");

    // Print the ciphertext: label and rotate and print alls chars 1by1
    printf("ciphertext: ");
    for (int i = 0, len = strlen(plaintext); i < len; i++)
    {
        printf("%c", rotate(key, plaintext[i]));
    }
    printf("\n");
}

void print_usage(string command)
{
    printf("Usage: %s key\n", command);
}

bool not_digits(string value)
{
    for (int i = 0, len = strlen(value); i < len; i++)
    {
        if (!isdigit(value[i]))
        {
            return 1;
        }
    }
    return 0;
}

// Take a char, delete value of A or a to 0 index, add key
// calculate remainder to loop back over 26 to 0 and add
// A or a respectively back
char rotate(int k, char c)
{
    if (!isalpha(c))
        return c;
    else if (isupper(c))
    {
        return (((c - 'A') + k) % 26) + 'A';
    }
    else
    {
        return (((c - 'a') + k) % 26) + 'a';
    }
}
