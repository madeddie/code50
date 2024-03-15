#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define BSIZE 512

int main(int argc, char *argv[])
{
    // Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open the memory card
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Couldn't open file %s, exiting.\n", argv[1]);
        return 1;
    }
    // Create a buffer for a block of data
    uint8_t buffer[BSIZE];

    // While there's still data left to read from the memory card
    while (fread(buffer, 1, sizeof(buffer), card) == 512)
    {
        // Create JPEGs from the data
        FILE *output = fopen("output.jpg", "wb");
        if (output == NULL)
        {
            fclose(card);
            return 1;
        }
        fwrite(buffer, sizeof(buffer), 1, output);
    }
    fclose(card);
    fclose(output);
}
