#include "helpers.h"
#include <math.h>

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
            BYTE rgbtRed = round(.393 * pxl.rgbtRed) + round(.769 * pxl.rgbtGreen) + round(.189 * pxl.rgbtBlue);
            BYTE rgbtGreen = round(.349 * pxl.rgbtRed) + round(.686 * pxl.rgbtGreen) + round(.168 * pxl.rgbtBlue);
            BYTE rgbtBlue = round(.272 * pxl.rgbtRed) + round(.534 * pxl.rgbtGreen) + round(.131 * pxl.rgbtBlue);

            image[i][j].rgbtRed = (rgbtRed > 255) ? 255 : rgbtRed;
            image[i][j].rgbtGreen = (rgbtGreen > 255) ? 255 : rgbtGreen;
            image[i][j].rgbtBlue = (rgbtBlue > 255) ? 255 : rgbtBlue;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
