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
    printf("letters %d, spaces %d, punct %d\n", letters, spaces, punctuation);
}
