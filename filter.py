import numpy as np
from osgeo import gdal
import matplotlib.pyplot as plt

# read the img
data = gdal.Open("E:\考研\复试\Lenna.png")
arr = data.ReadAsArray()
band1 = arr[0].astype(float)
# Fill
pad_band1 = np.pad(array=band1, pad_width=((1, 1), (1, 1)), mode='edge')
# 3*3filter
out_img = np.empty((arr.shape[1], arr.shape[2]), dtype=float)
for i in range(1, pad_band1.shape[0] - 1):
    for j in range(1, pad_band1.shape[1] - 1):
        a = np.array([pad_band1[i - 1][j - 1], pad_band1[i - 1][j], pad_band1[i - 1][j + 1],
                      pad_band1[i][j - 1],
                      pad_band1[i][j], pad_band1[i][j + 1], pad_band1[i + 1][j - 1],
                      pad_band1[i + 1][j],
                      pad_band1[i + 1][j + 1]])
        out_img[i - 1][j - 1] = np.median(a)

plt.imshow(out_img)
plt.show()
# output
outfile = "E:\考研\复试\Lenna_median.tif"
driver = gdal.GetDriverByName('GTIFF')
output = driver.Create(outfile, xsize=arr.shape[0], ysize=arr.shape[1], bands=1)
output.WriteArray(out_img, interleave='band')
