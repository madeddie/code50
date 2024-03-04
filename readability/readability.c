#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string text = get_string("Text: ");
    int letters = 0;
    int spaces = 0;
    int punctuation = 0;

    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (isalpha(text[i]))
            letters++;
        else if (isblank(text[i]))
            spaces++;
        else if (text[i] == '!' || text[i] == '?' || text[i] == '.')
            punctuation++;
    }
    float L = (letters * 100) / ((spaces + 1) * 100);
    float index = 0.0588 * L - 0.296 * S - 15.8
    printf("letters %d, spaces %d, punct %d\n", letters, spaces, punctuation);
}
