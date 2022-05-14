# ras2df
A simple library for converting raster data to clean pandas data frame. The output dataframe is null data-free, making it ideal for doing column-wise computations and machine learning problems. Additionally, this also converts the updated data frame back to a raster. This is built on top of Pandas, Numpy, GDAL, and Matplotlib



## Installation
```cmd
cd Drive:\path\ras2df
python setup.py install
```


```python
##google colab
!pip install git+https://github.com/RJLA/ras2df.git
```


## Usage
In this example we will use the included l8_data.tif as sample data
- RGB
![image](https://user-images.githubusercontent.com/18103736/162382989-e88d70ba-8cf4-423d-a7d6-7dd50704b726.png)

```python
from ras2df import Raster_to_dataframe

#Call class 
rd = Raster_to_dataframe(
     r'path\to\file', #path to raster data
     'l8_data', #raster file name
     'tif', #raster extention (tif, img, etc.)
)

#Converts raster to dataframe 
df = rd.make_df()
print(df)
```
![image](https://user-images.githubusercontent.com/18103736/162557283-fc16cf76-0465-4a05-b82f-8c7949673841.png)


```python
#since this is now a pandas dataframe, we can just use pandas methods like renaming columns
df.columns = ['BLUE','GREEN','RED','NIR','SWIR1','SWIR2']
print(df)
```
![image](https://user-images.githubusercontent.com/18103736/162557315-374e404c-8b63-4253-86bf-f38e038b5a60.png)

```python
#make scatter plot using pandas' scatter method
df.plot.scatter(
    x='GREEN',
    y='NDVI',
    c='DarkBlue' #color)
```
![image](https://user-images.githubusercontent.com/18103736/168415856-e7b56b99-c93f-486b-a894-f2eafff49337.png)


```python
#compute for ndvi to highlight vegetation areas
#using the pandas way
df['NDVI'] = (df['NIR'] - df['RED']) / (df['NIR'] + df['RED'])
print(df) # the NDVI column was created
```
![image](https://user-images.githubusercontent.com/18103736/162557391-a7eaf766-53d2-42ab-8d75-510b621da935.png)

```python
#Converts NDVI column to raster
#The output (PNG and TIFF) of this function will be
#stored inside path_to_file\output_ras2df
rd.df_to_raster(
     df['NDVI'], #column to rasterize
     'NDVI', #output filename
     float, #data type (float or int)
)
```
![image](https://user-images.githubusercontent.com/18103736/162557437-c5b57202-342a-40ea-b5fe-06af2c057c0f.png)
![NDVI](https://user-images.githubusercontent.com/18103736/162382840-e41205e8-364e-4912-8ce1-12f8ea0bb45d.png)

```python
#compute for dbsi to highlight bare soil areas
df['DBSI'] = (df['SWIR1'] - df['GREEN'])/(df['SWIR1'] + df['GREEN'])

#compute for ndbi to highlight builtup areas
df['NDBI'] = (df['SWIR1'] - df['NIR'])/(df['SWIR1'] + df['NIR'])

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
![DBSI](https://user-images.githubusercontent.com/18103736/162382887-0560ee4d-cd53-407c-85c2-f9eceb308b66.png)
![NDBI](https://user-images.githubusercontent.com/18103736/162382907-f2055c47-91ef-4a96-844e-dedc0c190e92.png)

```python
#Do classification problem like kmeans
from sklearn.cluster import KMeans

kmeans = KMeans(3) # 3 classes
kmeans.fit(df)
identified_clusters = kmeans.fit_predict(df)
df['Clusters'] = identified_clusters

#Converts Clusters column to raster
rd.df_to_raster(
     df['Clusters'], #column to rasterize
     'Clusters', #output filename
     int, #data type (float or int)
)
```
![Clusters](https://user-images.githubusercontent.com/18103736/162556069-3b351745-cbb2-4060-b596-39366d3a2110.png)



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
