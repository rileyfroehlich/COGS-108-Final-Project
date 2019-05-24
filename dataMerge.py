import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.options.display.max_rows = 7
pd.options.display.max_columns = 8

#parse data
df_index = pd.read_csv("oci_2015_datasd.csv")
df_collisions = pd.read_csv("pd_collisions_datasd.csv")
df_traffic = pd.read_csv("traffic_counts_datasd.csv")
df_meters = pd.read_csv("treas_parking_meters_loc_datasd.csv")

#drop OCI columns
df_index.drop( columns = "seg_id", inplace = True )
df_index.drop( columns = "oci_wt", inplace = True )
df_index.drop( columns = "pvm_class", inplace = True )
df_index.drop( columns = "func_class", inplace = True )
df_index.drop( columns = "oci_desc", inplace = True )
df_index.dropna( inplace = True )

#drop collision columns
df_collisions.drop( columns = "report_id", inplace = True )
df_collisions.drop( columns = "date_time", inplace = True )
df_collisions.drop( columns = "street_no", inplace = True )
df_collisions.drop( columns = "street_dir", inplace = True )
df_collisions.drop( columns = "cross_st_dir", inplace = True )
df_collisions.drop( columns = "violation_section", inplace = True )
df_collisions.drop( columns = "violation_type", inplace = True )
df_collisions.drop( columns = "charge_desc", inplace = True )
df_collisions.drop( columns = "injured", inplace = True )
df_collisions.drop( columns = "killed", inplace = True )
df_collisions.drop( columns = "hit_run_lvl", inplace = True )
df_collisions.drop( columns = "police_beat", inplace = True )
df_collisions[ 'street' ] = df_collisions[ 'street_name' ].map( str ) + ' ' + df_collisions[ 'street_type' ]
df_collisions.drop( columns = "street_name", inplace = True )
df_collisions.drop( columns = "street_type", inplace = True )
df_collisions.dropna( inplace = True )

#drop traffic columns
df_traffic.drop( columns = "id", inplace = True )
df_traffic.drop( columns = "all_count", inplace = True )
df_traffic.drop( columns = "northbound_count", inplace = True )
df_traffic.drop( columns = "southbound_count", inplace = True )
df_traffic.drop( columns = "eastbound_count", inplace = True )
df_traffic.drop( columns = "westbound_count", inplace = True )
df_traffic.drop( columns = "file_no", inplace = True )
df_traffic.drop( columns = "count_date", inplace = True )
new = df_traffic[ 'limits' ].str.split( ' - ', n = 1, expand = True) 
df_traffic[ 'limit_1' ] = new[ 0 ]
df_traffic[ 'limit_2' ] = new[ 1 ]
df_traffic.drop( columns = "limits", inplace = True )
#df2 can be used to find lat and long coordinates
df2 = df_traffic.groupby( [ 'street_name', 'limit_1', 'limit_2' ]).agg({ 'total_count' : 'sum' })
df_traffic.dropna( inplace = True )

df_meters.drop( columns = "area", inplace = True )
df_meters.drop( columns = "sub_area", inplace = True )
df_meters.drop( columns = "pole", inplace = True )
df_meters.drop( columns = "config_id", inplace = True )
df_meters.drop( columns = "config_name", inplace = True )
df_meters.dropna( inplace = True )


