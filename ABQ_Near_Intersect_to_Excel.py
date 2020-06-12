#!/usr/bin/env python
# coding: utf-8

# In[1]:


import arcpy


# In[ ]:


near_layer_list = ['ilmnmcrCFOPUBLISH.DBO.Aplomado_Falcon_Grassland_Boundary','LWC_Alternative_C_Final_10_18_2018.shp','ilmnmcrcfopublish.DBO.nlcs_wld_poly','ilmnmcrCFOPUBLISH.DBO.Wilderness_Study_Areas','ilmnmcrcfopublish.DBO.nlcs_wsr_corr_poly','ilmnmcrcfopublish.DBO.nlcs_nsht_corr_poly','ilmnmcrcfopublish.DBO.nlcs_nsht_ln','ilmnmcrcfopublish.DBO.nlcs_wsa_poly','ilmnmcrCFOPUBLISH.DBO.National_Byway','ilmnmcrCFOPUBLISH.DBO.Research_Natural_Areas','ilmnmcrCFOPUBLISH.DBO.BOR_Avalon_Reservior_Stipulations','ilmnmcrcfopublish.DBO.acec_desig_poly','ilmnmcrCFOPUBLISH.DBO.Special_Management_Areas','nps_boundary.shp','same as datasets for "SDA in parcel" above','ilmnmcrCFOPUBLISH.DBO.EXIST_LND_DISP_POLY','need CFO dataset','same as datasets for "ROW Corridor in Parcel" above','ilmnmcrCFOPUBLISH.DBO.ROW_poly','ilmnmcrCFOPUBLISH.DBO.ROW_line']


parcels = 'parcels_layer'

parcels_temp = arcpy.MakeFeatureLayer_management(parcels)

#TODO: Check to see if layers overlap, if no run near.

fields_remove = ['OBJECTID','SHAPE_AREA','SHAPE_LENGTH']

for lyr in near_layer_list:
    lyr_field_list = [f.name for f in arcpy.ListFields(lyr) if f.name not in fields_remove]
    print(lyr)
    print(lyr_field_list)
    #out_near = arcpy.GenerateNearTable_analysis(parcels_temp,lyr)
    #arcpy.JoinField_management(parcels_temp,out_near,'objectid = near_fid',lyr_field_list)
    #output to excel
    #calculate acreage

