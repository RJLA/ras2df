##Usage
'''python
from ras2df import Raster_to_dataframe

##Call class
rd = Raster_to_dataframe(path_to_file,raster_name, raster_file_type)


#Convert raster to dataframe
df = rd.make_df()

#Convert dataframe to raster

rd.df_to_raster(column_to_rasterize,output_filename,data_type)
note that the 3rd arguement:
data type: float or int
'''