#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string text = get_string("Text: ");

    int letters = 0;
    int words = 0;
    int sentences = 0;

    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (isalpha(text[i]))
            // Any alphabetical char counts for letters
            letters++;
        else if (isblank(text[i]))
            // Words are delineated by spaces, - 1 word, since there's no space at the end
            // Fixing that after the loop
            words++;
        else if (text[i] == '!' || text[i] == '?' || text[i] == '.')
            // All sentences end with a ., ! or ?
            sentences++;
    }
    // Add one word because the last one doesn't have a space after it.
    words++;

    float L = (float) letters / words * 100.0;
    float S = (float) sentences / words * 100.0;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    if (round(index) < 1)
        printf("Before Grade 1\n");
    else if (round(index) > 16)
        printf("Grade 16+\n");
    else
        printf("Grade %d\n", (int) round(index));
}
