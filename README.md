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
#The output (PNG and TIFF) of this function will be
#stored inside path_to_file\output_ras2df
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
## Output
RGB
![image](https://user-images.githubusercontent.com/18103736/162382989-e88d70ba-8cf4-423d-a7d6-7dd50704b726.png)
![NDVI](https://user-images.githubusercontent.com/18103736/162382840-e41205e8-364e-4912-8ce1-12f8ea0bb45d.png)
![DBSI](https://user-images.githubusercontent.com/18103736/162382887-0560ee4d-cd53-407c-85c2-f9eceb308b66.png)
![NDBI](https://user-images.githubusercontent.com/18103736/162382907-f2055c47-91ef-4a96-844e-dedc0c190e92.png)

## Features

- Converts raster to pandas data frame 
- Converts pandas data frame to raster
## License
[MIT](https://github.com/RJLA/ras2df/files/8449316/LICENSE.txt)
## Author
- [@RJLA](https://github.com/RJLA)
- regi.argamosa@gmail.com


# Hi, I'm Reginald (Regi for short)! 👋
## 🚀 About Me
I'm a machine learning researcher that specializes on datasets from remote sensing. I was part in a number of government-funded research initiatives carried out by the University of the Philippines' Training Center for Applied Geodesy and Photogrammetry. I am excited about using machine learning to remote sensing datasets in order to aid enhance environmental monitoring.

## 🛠 Skills
- Algorithms: MLR, Random Forest, XGBoost, CatBoost, LightGBM, Lasso, Ridge, Elastic Net, Logistic regression, 
K-Means, Agglomerative Clustering, SVM, PCA, ANN, SHAP

- Technologies: Scikit-learn, Pandas, Keras, NumPy, Scipy,
Matplotlib, Seaborn, GDAL, OGR, ArcPy, ArcGIS, LAStools,
SNAP, Google Earth Engine, Jupyter

- Data: LiDAR point cloud, Optical (Landsat, Sentinel 2,
MODIS, and high resolution multi-spectral data), RADAR (Sentinel 1 and ALOS 2 – PALSAR) 



## 🔗 Links
- [Linkedin](https://www.linkedin.com/in/rjla/)
- [ResearchGate](https://www.researchgate.net/profile/Reginald-Argamosa)
