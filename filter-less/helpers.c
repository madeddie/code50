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
        for (int j = 0; j <= (width - 1) / 2; j++)
        {
            RGBTRIPLE tmp = image[i][j];
            image[i][j] = image[i][(width - 1) - j];
            image[i][(width - 1) - j] = tmp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Create a copy of image
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            int pixels = 0;
            int blue = 0;
            int green = 0;
            int red = 0;

            for (int r = -1; r < 2; r++)
            {
                for (int c = -1; c < 2; c++)
                {
                    if (i + r < 0 || i + r > height - 1)
                    {
                        continue;
                    }

                    if (j + c < 0 || j + c > width - 1)
                    {
                        continue;
                    }

                    blue += image[i + r][j + c].rgbtBlue;
                    green += image[i + r][j + c].rgbtGreen;
                    red += image[i + r][j + c].rgbtRed;
                    pixels += 1;
                }
            }
            image[i][j].rgbtBlue = round(blue / pixels);
            image[i][j].rgbtGreen = round(green / pixels);
            image[i][j].rgbtRed = round(red / pixels);
        }
    }
}
