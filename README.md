# ras2df
A straightforward library for converting raster data to clean pandas data frame. The output dataframe is null data-free, making it ideal for doing column-wise computations and machine learning problems. Additionally, this also converts the updated data frame back to a raster.

## Installation
```cmd
cd ras2df
python setup.py install
```

## Usage
```python
from ras2df import Raster_to_dataframe

#Call class 
rd = Raster_to_dataframe(
     path_to_file, #path to raster data
     raster_name, #raster file name
     raster_file_type, #raster extention (tif, img, etc.)
)

#Converts raster to dataframe 
df = rd.make_df()

#rename columns
df.columns = ['BLUE','GREEN','RED','NIR','SWIR1','SWIR2']

#compute for ndvi
df['NDVI'] = (df['NIR'] - df['RED']) / (df['NIR'] + df['RED'])

#Converts NDVI column to raster
rd.df_to_raster(
     df['NDVI'], #column to rasterize
     'NDVI', #output filename
     float, #data type (float or int)
)
```
## NDVI output
The NDVI in png and tiff format will be stored inside
path_to_file\output_ras2df
![alt text](https://github.com/RJLA/ras2df/blob/main/NDVI.png)
