#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

char rotate(int key, string text);
int main(void)
{
    string text = get_string("Text ");
    printf("%s\n", rotate(13, text));
}

char rotate(int key, string text)
{
    char new_string[strlen(text)];
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        char new_char;
        if (isalpha(text[i]))
        {
            new_char = text[i] - key;
            if (new_char < 65)
            {
                new_char = 'Z' - (64 - new_char);
            }
        }
        else
        {
            new_char = text[i];
        }
        new_string[i] = new_char;
    }
    return new_string;
}
