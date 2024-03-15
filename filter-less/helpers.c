#include "helpers.h"
#include <math.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int avg = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            image[i][j].rgbtBlue = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtRed = avg;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE pxl = image[i][j];
            int rgbtRed = round(.393 * pxl.rgbtRed + .769 * pxl.rgbtGreen + .189 * pxl.rgbtBlue);
            int rgbtGreen = round(.349 * pxl.rgbtRed + .686 * pxl.rgbtGreen + .168 * pxl.rgbtBlue);
            int rgbtBlue = round(.272 * pxl.rgbtRed + .534 * pxl.rgbtGreen + .131 * pxl.rgbtBlue);

            image[i][j].rgbtRed = (rgbtRed > 255) ? 255 : rgbtRed;
            image[i][j].rgbtGreen = (rgbtGreen > 255) ? 255 : rgbtGreen;
            image[i][j].rgbtBlue = (rgbtBlue > 255) ? 255 : rgbtBlue;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            printf("%i, %i\n", j, (width - 1) - j);
            RGBTRIPLE tmp = image[i][j];
            image[i][j] = image[i][(width - 1) - j];
            image[i][width - j] = tmp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
