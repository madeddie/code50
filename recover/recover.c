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
    while (fread(buffer, 1, 512, card) == 512)
    {
        // Create JPEGs from the data
        printf("%s", buffer);
    }
}
