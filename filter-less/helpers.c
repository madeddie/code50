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
            image[i][j].rgbtRed = round(.393 * pxl.rgbtRed) + round(.769 * pxl.rgbtGreen) + round(.189 * pxl.rgbtBlue);
            image[i][j].rgbtGreen = round(.349 * pxl.rgbtRed) + round(.686 * pxl.rgbtGreen) + round(.168 * pxl.rgbtBlue);
            image[i][j].rgbtBlue = round(.272 * pxl.rgbtRed) + round(.534 * pxl.rgbtGreen) + round(.131 * pxl.rgbtBlue);

            image[i][j].rgbtRed = (image[i][j].rgbtRed > 255) ? 255 : image[i][j].rgbtRed;
            image[i][j].rgbtGreen = (image[i][j].rgbtGreen > 255) ? 255 : image[i][j].rgbtGreen;
            image[i][j].rgbtBlue = (image[i][j].rgbtBlue > 255) ? 255 : image[i][j].rgbtBlue;
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
