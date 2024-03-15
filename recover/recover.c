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

    FILE *output = fopen("output.jpg", "wb");
    if (output == NULL)
    {
        fclose(card);
        return 1;
    }
    int image_start = 0;
    // While there's still data left to read from the memory card
    while (fread(buffer, 1, sizeof(buffer), card) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff)
        {
            printf("Found image!\n");
            fclose(output);
            image_start += 1;
            char image_name[8];
            sprintf(image_name, "%i.jpg\n", image_start);
            printf("%s\n", image_name);
            output = fopen(image_name, "wb");
            if (output == NULL)
            {
                fclose(card);
                return 1;
            }
        }
        // Create JPEGs from the data
        if (image_start)
        {
            fwrite(buffer, sizeof(buffer), 1, output);
        }
    }
    fclose(card);
    fclose(output);
}
