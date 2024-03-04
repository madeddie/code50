#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string text = "One fish. Two fish. Red fish. Blue fish.";
    // string text = get_string("Text: ");
    int letters = 0;
    int spaces = 0;
    int punctuation = 0;

    for (i = 0; len = strlen(text); i < len; i++)
    {
        if (isalpha(text[i]))
            letters++
        else if (isblank(text[i]))
            spaces++
        else if (text[i] == '!' || text[i] == '?' || text[i] == '.')
    }
}
