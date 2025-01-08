from nilearn import plotting
import numpy as np

# MNI152 2mm standard brain
brain_img = 'MNI152_T1_2mm_brain.nii.gz'

# Define the coordinates (x, y, z)
coordinates = [(30, -22, -16), (-28, -20, -15)]  # Example coordinates

# Plot points on the brain
plotting.plot_glass_brain(brain_img, display_mode='ortho',
                          annotate=True, colorbar=True)
plotting.plot_markers(np.array(coordinates), color='r', alpha=0.7)
plotting.show()
