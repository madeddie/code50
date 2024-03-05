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
    printf("Usage: %s KEY       # KEY is 26 alphabetic chars, upper and lower case, "
           "all letters once and only once\n",
           arg);
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

// Loop through all chars if key then loop through again and see if
// any char _not_ at the same index of the current char is equal to the
// current char. If doubles are found return false
bool all_letters_once(string s)
{
    for (int i = 0, len = strlen(s); i < len; i++)
    {
        for (int j = 0; j < len; j++)
        {
            if (j != i && toupper(s[i]) == toupper(s[j]))
            {
                return false;
            }
        }
    }
    return true;
}
