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

#compute for ndvi to highlight vegetation areas
df['NDVI'] = (df['NIR'] - df['RED']) / (df['NIR'] + df['RED'])

#compute for dbsi to highlight bare soil areas
df['DBSI'] = (df['SWIR1'] - df['GREEN'])/(df['SWIR1'] + df['GREEN'])

#compute for ndbi to highlight builtup areas
df['NDBI'] = (df['SWIR1'] - df['NIR'])/(df['SWIR1'] + df['NIR'])

#Converts NDVI column to raster
rd.df_to_raster(
     df['NDVI'], #column to rasterize
     'NDVI', #output filename
     float, #data type (float or int)
)

#Converts DBSI column to raster
rd.df_to_raster(
     df['DBSI'], #column to rasterize
     'DBSI', #output filename
     float, #data type (float or int)
)

#Converts NDBI column to raster
rd.df_to_raster(
     df['NDBI'], #column to rasterize
     'NDBI', #output filename
     float, #data type (float or int)
)


```
## Output raster
PNG and tiff format will be stored inside
path_to_file\output_ras2df

![NDVI](https://user-images.githubusercontent.com/18103736/162377341-432bb03e-254c-47de-a34b-f03b2a6e426d.png)
![DBSI](https://user-images.githubusercontent.com/18103736/162377371-d5e76174-1709-463b-911e-f4bdcfdea9b2.png)
![NDBI](https://user-images.githubusercontent.com/18103736/162377422-e3c9493f-8dcb-4f93-8691-5e78b2799930.png)

# Hi, I'm Reginald (Regi for short)! 👋
## 🚀 About Me
I'm a machine learning researcher that specializes on datasets from remote sensing. I was part in a number of government-funded research initiatives carried out by the University of the Philippines' Training Center for Applied Geodesy and Photogrammetry in Diliman. I am excited about using machine learning to remote sensing datasets in order to aid enhance environmental monitoring.

## 🔗 Links
[LinkedIn](https://www.linkedin.com/in/rjla/)

[ResearchGate](https://www.researchgate.net/profile/Reginald-Argamosa)




