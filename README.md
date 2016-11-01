back_projection.py

This script uses a simple version of the algorithm used by CT scanners, 
the backprojection algorithm, to reconstruct an image.'X-rays' are sent 
through the image at different angles and their attenuation due to the
different 'densities' (greyscale numbers) in the image are recorded.
Projections are created by creating images from the 1D intensity values
the same size as the original image and oriented along the projection
direction and the images are summed together to reconstruct the 
original image. 

Only 4 projections are used so the constructed image is not fantastic but
it demonstrates the concept.

Filtering could be used to make the image clearer.


back_projection_numerical.py

This is the same as the above but the 'image' is a much smaller array of
numbers so the calculations can be followed.