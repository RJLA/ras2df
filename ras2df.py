import pandas as pd
import numpy as np
from osgeo import gdal
from osgeo.gdalconst import *
import os
import matplotlib.pyplot as plt
from skimage import exposure
from datetime import datetime

class Raster_to_dataframe():
             
    def __init__ (
            self, 
            raster_path,
            raster_name,
            raster_extension,
            ):
        
        print('''
        arguments: 
            raster_path,
            raster_name,
            raster_extension,
            working_space
              ''')
            
        self.ws = raster_path  
        
        #create output path
        raster_output_path = os.path.join(
            self.ws, 
            'output_ras2df',
            )

        if not os.path.exists(raster_output_path):
            os.makedirs(raster_output_path)  
        
        self.raster_output_path = os.path.join(
            self.ws, 
            'output_ras2df',
            )
                                     
        self.raster_path = raster_path
        self.file_name = raster_name
        self.file_extension = raster_extension 
        self.raster_file = os.path.join(raster_path,f'{self.file_name}.{self.file_extension}')
        print(f'Opening {self.raster_file} raster')
        print()
        
        while True:
            
            try:
                
                if os.path.exists(self.raster_file) is True:
                    
                    self.data_source = gdal.Open(self.raster_file,
                                              GA_ReadOnly) # read raster file
                    self.gt = self.data_source.GetGeoTransform()  #get affine transformation coefficients
                    self.driver = self.data_source.GetDriver() #get driver of raster
                    self.n_cols = self.data_source.RasterXSize # raster width
                    self.n_rows = self.data_source.RasterYSize # raster height
                    self.pixel = self.gt[1] #pixel size
                    self.n_band = self.data_source.RasterCount #number of bands
                    self.projection = self.data_source.GetProjection() #projection
                    
                    print(f'Rows: {self.n_rows}')
                    print(f'Cols: {self.n_cols}')
                    print(f'Pixel size: {self.pixel}')
                    print(f'Number of bands: {self.n_band}')
                    print(f'Projection: {self.projection}')

                    break
                    
                else:
                    
                    print ("Path does not exists")
                    break     
                    
            except IndexError:
                
                print ("File extension is incorrect")
                break  
        
    def make_df(
            self, 
            round_values = True,
            ):
                        
        def make_flat_array(band_number):

            band = self.data_source.GetRasterBand(band_number)
            no_data = band.GetNoDataValue()
            array = band.ReadAsArray(
                0, 
                0, 
                self.n_cols, 
                self.n_rows
                )  #transform band as array

            array = np.where(
                array == no_data,
                np.nan,
                array,
                ) #change no data values to nan
      
            if round_values is True:
                array = np.round(array, 4) #round to 4 decimals places
            elif round_values is False:
                pass

            del band

            flat_array = array.flatten('F') #make band array to 1D
            del array
            
            return flat_array
                
        array_tupple = () #create empty tupple

        for i in range(self.n_band):
            array_tupple = array_tupple + (make_flat_array(i + 1), ) #append to empty tuple

        array_final = np.vstack(array_tupple).T #stack array vertically 
        
        del array_tupple
        
        #create main data frame
        self.main_df = pd.DataFrame(
            array_final, 
            columns = ['band_%s'%(i + 1) for i in range(self.n_band)],
            )
        
        
        del self.data_source
        del array_final
        
        #make psuedo column where predictions will be insered
        self.main_df['prediction'] = np.nan
        
        df_clean = self.main_df.iloc[:,:-1].dropna(axis = 0, 
                                                 how = 'all') #drop values where "ALL" rows are zero

        df_clean = df_clean.loc[~(df_clean == 0.0).all(axis = 1)] #make clean dataframe
        
        self.df_to_use = df_clean.fillna(0) #fill na with 0
        
        del df_clean
        
        self.df_to_use_idx = self.df_to_use.index
        
        return self.df_to_use
         

    def df_to_raster(
            self, 
            prediction, 
            output_filename,
            analysis_type,
            ):
        
        self.df_to_use = self.df_to_use.set_index(self.df_to_use_idx) #get the index of the original dataframe
        self.df_to_use['prediction'] = prediction * 1 #multiply by 1 to make it int
        self.main_df.update(self.df_to_use) #update the dataframe using the original index
        df_as_array = np.array(self.main_df['prediction']) #make df as array
        df_as_array = df_as_array.reshape(self.n_cols, 
                                      self.n_rows).T #reshape
        
        #get time for filename purposes
        date_time_1 = str(datetime.now()) 

       
        self.raster_output_path_name = os.path.join(
            self.raster_output_path,
            f'{output_filename}_{self.file_name}.tif',
            )

        self.min_value = self.df_to_use['prediction'].min()
        self.max_value = self.df_to_use['prediction'].max()
        
        def create_new_source(data_type):
            
            #create an empty raster that will contain the 'prediction' columns
            new_source = self.driver.Create(
                self.raster_output_path_name, 
                self.n_cols, 
                self.n_rows,
                1, 
                data_type,
                )

            #same as the original raster
            new_source.SetGeoTransform(self.gt) 
            new_source.SetProjection(self.projection)
            
            return new_source
                
        #if method is classification
        if analysis_type == int:
            
            new_source = create_new_source(gdal.GDT_Byte)
            output_raster = new_source.GetRasterBand(1)

            #transform df to array
            output_raster.WriteArray(df_as_array + 1, 
                                 0, 
                                 0)
            output_raster.ComputeStatistics(0)
            
            #visualize
            fig, ax = plt.subplots()
            num_colors = self.max_value + 1
            cmap = plt.cm.get_cmap(
                'Set1', 
                num_colors,
                )
            plt.imshow(df_as_array + 1, cmap=cmap)            

            cbar = plt.colorbar(ticks=np.linspace(
                1, 
                num_colors , 
                num_colors * 2 + 1)[1::2],
                )
            cbar.ax.set_yticklabels(
                range(1, num_colors + 1),
                )
            plt.title(f'{output_filename}', 
                      fontsize = 20)

            plt.axis('off') 
            plt.savefig(os.path.join(self.raster_output_path,
                                    f'{output_filename}.png'),
                        dpi = 300,
                        edgecolor = 'none',
                        bbox_inches='tight',
                        )
                   
            
        #if method is regression    
        elif analysis_type == float:
            try:
                #histogram equalize to improve visualization
                img_eq = exposure.equalize_hist(prediction.to_numpy())
                
                self.main_df['prediction_eq'] = self.main_df['prediction'] = np.nan
                self.df_to_use['prediction_eq'] = img_eq
                self.main_df.update(self.df_to_use) 

                df_as_array_eq = np.array(self.main_df['prediction_eq'])
                
                df_as_array_eq = df_as_array_eq.reshape(self.n_cols, 
                              self.n_rows).T
                
                
                fig, ax = plt.subplots()
    
                cax = ax.imshow(df_as_array_eq, 
                                cmap = 'Spectral_r')
    
                cbar = fig.colorbar(cax)
    
                cbar.set_ticks([img_eq.min(),
                                (img_eq.max() - img_eq.min()) / 2,
                                img_eq.max()])
                
                cbar.set_ticklabels(['Low',
                                     'Medium',
                                    'High'])        


                plt.title(f'{output_filename}', 
                          fontsize = 20)
                plt.axis('off')   
                plt.savefig(os.path.join(self.raster_output_path,
                                        f'{output_filename}.png',),
                            dpi = 300,
                            edgecolor = 'none',
                            bbox_inches='tight',
                            )
                
                 
                del self.df_to_use['prediction_eq']
                del img_eq 
                del df_as_array_eq
                                           
            except:
                ValueError     
                print('Error visualizing results')
                                   
            new_source = create_new_source(GDT_Float32)
            output_raster = new_source.GetRasterBand(1)            
            
            #transform df to array
            output_raster.WriteArray(
                df_as_array, 
                0, 
                0
                )       
            output_raster.ComputeStatistics(0)                         
          
        print()
        print(f'Output raster saved at {self.raster_output_path_name}')
          
        new_source.FlushCache()
        output_raster.FlushCache()      
        
        del output_raster
        del new_source
        del df_as_array
