#import <cs50.h>
#import <ctype.h>
#import <stdio.h>
#import <string.h>

void print_usage(string arg);
bool all_alpha(string s);
char substitute(char c, string k);
bool all_letters_once(string s);

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
    else if (!all_alpha(argv[1]))
    {
        print_usage(argv[0]);
        return 1;
    }
    else if (!all_letters_once(argv[1]))
    {
        print_usage(argv[0]);
        return 1;
    }

    string key = argv[1];
    string plaintext = get_string("plaintext:  ");
    printf("ciphertext: ");
    for (int i = 0, len = strlen(plaintext); i < len; i++)
    {
        printf("%c", substitute(plaintext[i], key));
    }
    printf("\n");
}

void print_usage(string arg)
{
    printf("Usage: %s KEY       # key needs to be 26 alphabetic characters, upper and lower case allowed, all letters once and only once\n", arg);
}

// return false is any character in string s is not alphabetic
bool all_alpha(string s)
{
    for (int i = 0, len = strlen(s); i < len; i++)
    {
        if (!isalpha(s[i]))
        {
            return false;
        }
    }
    return true;
}

// Replace char with char at same index of string key `k`)
char substitute(char c, string k)
{
    if (!isalpha(c))
    {
        return c;
    }
    else if (isupper(c))
    {
        return toupper(k[c - 'A']);
    }
    else
    {
        return tolower(k[c - 'a']);
    }
}

// uppercase all letters, add them together, if they add up to the wrong value, letters
// are double and/or missing. A-Z ascii values add up to 2015
bool all_letters_once(string s)
{
    int sumval = 0;
    for (int i = 0, len = strlen(s); i < len; i++)
    {
        sumval += toupper(s[i]);
    }
    if (sumval != 2015)
        return false;
    else
        return true;
}
