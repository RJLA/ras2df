# ras2df
A simple library for converting raster data to clean pandas data frame. The output dataframe is null data-free, making it ideal for doing column-wise computations and machine learning problems. Additionally, this also converts the updated data frame back to a raster.

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
![NDVI](https://user-images.githubusercontent.com/18103736/162381758-4c31d547-9994-4e08-b8da-b7b924c072a2.png)
![DBSI](https://user-images.githubusercontent.com/18103736/162377371-d5e76174-1709-463b-911e-f4bdcfdea9b2.png)
![NDBI](https://user-images.githubusercontent.com/18103736/162377422-e3c9493f-8dcb-4f93-8691-5e78b2799930.png)

## Features

- Converts raster to pandas data frame 
- Converts pandas data frame to raster
## License
[MIT](https://github.com/RJLA/ras2df/files/8449316/LICENSE.txt)
## Authors
- [@RJLA](https://github.com/RJLA)
- regi.argamosa@gmail.com


# Hi, I'm Reginald (Regi for short)! 👋
## 🚀 About Me
I'm a machine learning researcher that specializes on datasets from remote sensing. I was part in a number of government-funded research initiatives carried out by the University of the Philippines' Training Center for Applied Geodesy and Photogrammetry. I am excited about using machine learning to remote sensing datasets in order to aid enhance environmental monitoring.

## 🛠 Skills
-Algorithms: MLR, Random Forest, XGBoost, CatBoost, LightGBM, Lasso, Ridge, Elastic Net, Logistic regression, 
K-Means, Agglomerative Clustering, SVM, PCA, ANN, SHAP

-Technologies: Scikit-learn, Pandas, Keras, NumPy, Scipy,
Matplotlib, Seaborn, GDAL, OGR, ArcPy, ArcGIS, LAStools,
SNAP, Google Earth Engine, Jupyter

-Data: LiDAR point cloud, Optical (Landsat, Sentinel 2,
MODIS, and high resolution multi-spectral data), RADAR (Sentinel 1 and ALOS 2 – PALSAR) 



## 🔗 Links
- [Linkedin](https://www.linkedin.com/in/rjla/)
- [ResearchGate](https://www.researchgate.net/profile/Reginald-Argamosa)




