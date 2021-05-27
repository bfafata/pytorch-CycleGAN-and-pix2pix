Folder structure:

    new data
    |
    |--SNR003
    |    |
    |    |--1bxn
    |    |   |
    |    |   |--subtomogram_mrc 
    |    |   |--subtomogram_png
    |    |   |--densitymap_mrc
    |    |   |--densitymap_png
    |    |   |--json_label
    |    |   |--json_simulation
    |    |
    |    |
    |    |--1f1b, 1yg6, 2byu, 2h12, 2ldb, 3gl1, 3hhb, 4d4r, 6t3e
    |        |
    |        |...(the same as 1bxn)
    |    
    |
    |--SNR005
    |    |
    |    |...(the same as SNR003)
    |  
    |  
    |--SNR infinity
         |
         |...(the same as SNR003)



#### subtomogram, density map, and lables(.json) with different Signal to Noise Ratio(SNR)
#### Each SNR: 10 types, 500 each, 5000 total
#### ALL data: 3 SNR, 5000 each, 15000 total
#### Macromolecules: 1bxn, 1f1b, 1yg6, 2byu, 2h12, 2ldb, 3gl1, 3hhb, 4d4r, 6t3e.


#### SNR*

SNR003: SNR = 0.03, 

SNR005: SNR = 0.05, 

SNRinfinity: SNR = infinity,


#### 1. subtomogram_mrc 
filenames: tomotarget*.mrc, * = 0,1,2,...,499

This is our input data!
The subtomogram of a single macromolecule and some part of its neighbors. 
The size is 32 * 32 * 32.

.mrc file could be open with python package: mrcfile. 
It could be visualized using software: Chimera (https://www.cgl.ucsf.edu/chimera/). This software is very easy to use.

#### 2. subtomogram_png 
filenames: tomotarget*.png, * = 0,1,2,...,499

the slices of a subtomogram. Sice the size of a subtomogram is 32^3, there are 32 subfigures in each image.

This is to help understand the content in the subtomogram.

#### 3. json_label:
filenames: target*.json, * = 0,1,2,...,499

This is the label for the simulated target data. (you may need to focus on these files)

##### detailed information for target*.json: 

The label of the corresponding subtomogram. The file is in the following format:

{"loc": [5, 4, -2], "rotate": [-2.7956930634210506, 1.1126108053114863, -1.2948702875352103], "name": "1bxn"}

The location parameter is the relative position to the center. The positive direction is the direction in which the array subscript values increase.

The meaning of the rotate parameter is the angle that the protein rotates along the coordinate axis in ZYZ order. For more details, search "Euler angle".

##### 4. json_label:
filenames: packing*.json: ignor these files. 

They are used to guide the simulation, but it's not the label for the simulated data. You can ignore this folder.


#### 5. densitymap_mrc

filenames: packtarget*.mrc, * = 0,1,2,...,499

density map: the Grayscale map, could be regarded as the ground truth of segmentation task


#### 6. densitymap_png

filenames: packtarget*.png, * = 0,1,2,...,499

the slices of a density map. Sice the size of a density map is 32^3, there are 32 subfigures in each image.

This is to help understand the content in the density map.



