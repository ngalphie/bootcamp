import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')

# We'll use scipy.optimize.curve_fit to do the nonlinear regression
import scipy.optimize

#for image processing
import skimage.io as io
import skimage.exposure as exposure
import skimage.morphology as morphology
import skimage.filters as filters
import skimage.measure as measure
import skimage.segmentation as segmentation

#load image series
bs = io.imread_collection('data/bacterial_growth/bacillus_*.tif')

# Get the histogram data
#hist_phase, bins_phase = exposure.histogram(bs[0])

# # Use matplotlib to make a pretty plot of histogram data
# plt.close()
# plt.clf()
# plt.fill_between(bins_phase, hist_phase, alpha=0.5)

# Label axes
# plt.xlabel('pixel value')
# plt.ylabel('count')

'''manual method of thresholding
# Threshold value, as obtained by eye
thresh_fluor = 250
'''
thresh_fluor = []

# Compute Otsu thresholds
for i in range(len(bs)):
    thresh_fluor.append(filters.threshold_otsu(bs[i]))

image_list = []
# Generate thresholded image
for i in range(len(bs)):
    image_list.append(morphology.closing(bs[i] > thresh_fluor[i], morphology.square(3)))

image_list_rgb = []

for i in range(len(bs)):
    # Build RGB image by stacking grayscale images
    image_list_rgb.append(np.dstack(3 * [bs[i] / bs[i].max()]))

    # Saturate red channel wherever there are white pixels in thresh image
    image_list_rgb[i][image_list[i], 1] = 1.0

# plt.close()
# plt.clf()
# for i in range(len(bs)):
#     image_list_rgb[i][850:860, 400:400+156] = 1
#     %plt.figure(i)
#     %plt.imshow(image_list_rgb[i], cmap=plt.cm.gray)
#     %plt.savefig('img{:d}.pdf'.format(i), bbox_inches='tight')

image_list_labeled = []
# Label binary image; background kwarg says value in im_bw to be background
for i in range(len(bs)):
    image_list_labeled.append(measure.label(image_list[i], background=0))

image_list_prop = []
# Extract region props
for i in range(len(bs)):
    image_list_prop.append(measure.regionprops(image_list_labeled[i]))

areas = []
#Extract area
for i in range(len(bs)):
    areas.append([prop.area for prop in image_list_prop[i]])

#Flatten
areas = np.array(areas)
y_area_px = np.ndarray.flatten(areas)

y_area  = y_area_px*0.00416025

#Create time array x_time [The time between frames is 15 minutes.]
x_time = np.arange(0,15*(len(bs)),15)

# Plot
plt.close()
plt.clf()
plt.plot(x_time, y_area, marker='.', linestyle='none')
# Label axes (no units on x because it's dimensionless)
plt.xlabel('time (min)')
plt.ylabel('area of bacteria (um$^2$)')

#Nonlinear regression

def exponential_area(x, A_0, r):
    """Exponential model"""
    assert np.any(np.array(x) > 0), 'All values of x must be >= 0.'
    assert np.any(np.array([A_0, r]) > 0), 'All parameters must be >= 0.'

    return A_0 * np.exp(x * r)

def exponential_area_log(x, log_A_0, log_r):
    """
    Model with log parameters.
    """

    # Exponentiate parameters
    A_0, r = np.exp(np.array([log_A_0, log_r]))

    return exponential_area(x, A_0, r)


# Specify initial guess
A_0_guess = 6
r_guess = 0.02

# Construct initial guess array
p0 = np.array([A_0_guess, r_guess])

log_p0 = np.log(p0)

# Do curve fit, but dump covariance into dummy variable
log_p, _ = scipy.optimize.curve_fit(exponential_area_log, x_time, y_area, p0=log_p0)

p = np.exp(log_p)
# Print the results
print("""
  A_0 = {0:.2f}
  r = {1:.2f}
""".format(*tuple(p)))






# Show the result
# plt.imshow(image_list_rgb[0], cmap=plt.cm.gray)

#
# # Saturate green channel wherever there are white pixels in thresh image
# im_phase_rgb[im_phase_bw, 1] = 1.0
#
# # Show the result
# with sns.axes_style('dark'):
#     plt.imshow(im_phase_rgb)
#
# plt.figure(1)
# for i in range(len(bs)):
#     plt.subplot(,1,1)
#     plt.imshow(image_list[i], cmap=plt.cm.gray)
#
#
#     with sns.axes_style('dark'):
#     fig, ax = plt.subplots(1, 2, figsize=(10, 5))
#     ax[0].imshow(im_cfp_filt, cmap=plt.cm.gray)
#     ax[1].imshow(im_cfp_bw, cmap=plt.cm.gray)
