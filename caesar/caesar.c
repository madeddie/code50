#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{

}

string rotate(int key, string text)
{
    string new_string = "";
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (isalpha(text[i]))
        {
            char new_char = text[i] - key;
            if (new_char < 65)
            {
                new_char = 'Z' - (64 - new_char);
            }
        }
        else
        {
            char new_char = text[i];
        }
        new_string += new_char;
    }
}
