import arcpy

# To allow overwriting outputs change overwriteOutput option to True.
arcpy.env.overwriteOutput = True
                    
Survey_Start_Stop = "https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_Root_2020/FeatureServer/0"
Sites = "https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_2020_Base/FeatureServer/1"
Other_Species = "https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_Root_2020/FeatureServer/3"
Point_of_Interest = "https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_Root_2020/FeatureServer/4"
WIFL_Detection = "https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_Root_2020/FeatureServer/2"

code_block1 = """
def reclass(a,b):
    if a <= 20:
       return b
    elif a > 20:
      return 'Other-Other-Other'"""



# Process: Select Layer By Attribute (Select Layer By Attribute) 
arcpy.SelectLayerByAttribute_management(in_layer_or_view=Survey_Start_Stop, selection_type="NEW_SELECTION", where_clause="section IS NULL", invert_where_clause="")
# Process: Spatial Join (Spatial Join) 
SurveyStartStop_SpatialJoin = r"N:\Projects\43000\43741-000 LCR SWFL\APRX\SWFL Scripts\SWFL_DF_Scripts\SWFL_DF_Scripts.gdb\SurveyStartStop_SpatialJoin"
arcpy.SpatialJoin_analysis(target_features=Survey_Start_Stop, join_features=Sites, out_feature_class=SurveyStartStop_SpatialJoin, join_operation="JOIN_ONE_TO_ONE", join_type="KEEP_ALL", field_mapping="actv_type \"Activity Type\" true true false 255 Text 0 0,First,#,Survey Start-Stop,actv_type,0,255;sur_pt_type \"Point Type\" true true false 255 Text 0 0,First,#,Survey Start-Stop,sur_pt_type,0,255;pause_time \"Pause Time\" true true false 0 Short 0 0,First,#,Survey Start-Stop,pause_time,-1,-1;livestock_yn \"Livestock?\" true true false 255 Text 0 0,First,#,Survey Start-Stop,livestock_yn,0,255;LivestockInfo \"Livestock Details\" true true false 255 Text 0 0,First,#,Survey Start-Stop,LivestockInfo,0,255;beetles_yn \"Beetles?\" true true false 255 Text 0 0,First,#,Survey Start-Stop,beetles_yn,0,255;BeetlesInfo \"Beetle Details\" true true false 255 Text 0 0,First,#,Survey Start-Stop,BeetlesInfo,0,255;cowbird_yn \"Cowbirds?\" true true false 255 Text 0 0,First,#,Survey Start-Stop,cowbird_yn,0,255;wifl_count \"#fitz-bewing birds\" true true false 0 Short 0 0,First,#,Survey Start-Stop,wifl_count,-1,-1;notes \"Comments\" true true false 4000 Text 0 0,First,#,Survey Start-Stop,notes,0,4000;date_coll \"Date Collected\" true true false 8 Date 0 0,First,#,Survey Start-Stop,date_coll,-1,-1;obs_select \"Observer\" true true false 500 Text 0 0,First,#,Survey Start-Stop,obs_select,0,500;num_obs \"# Other Observers\" true true false 255 Text 0 0,First,#,Survey Start-Stop,num_obs,0,255;obs_text \"Other Observers\" true true false 500 Text 0 0,First,#,Survey Start-Stop,obs_text,0,500;section \"Area-Site\" true true false 255 Text 0 0,First,#,Survey Start-Stop,section,0,255;ofc_editor_1 \"Office Editor 1\" true true false 500 Text 0 0,First,#,Survey Start-Stop,ofc_editor_1,0,500;ofc_editdate_1 \"Office Edit Date 1\" true true false 8 Date 0 0,First,#,Survey Start-Stop,ofc_editdate_1,-1,-1;ofc_edit_1 \"Office Edit 1\" true true false 500 Text 0 0,First,#,Survey Start-Stop,ofc_edit_1,0,500;ofc_editor_2 \"Office Editor 2\" true true false 500 Text 0 0,First,#,Survey Start-Stop,ofc_editor_2,0,500;ofc_editdate_2 \"Office Edit Date 2\" true true false 8 Date 0 0,First,#,Survey Start-Stop,ofc_editdate_2,-1,-1;ofc_edit_2 \"Office Edit 2\" true true false 500 Text 0 0,First,#,Survey Start-Stop,ofc_edit_2,0,500;CreationDate \"CreationDate\" true true false 8 Date 0 0,First,#,Survey Start-Stop,CreationDate,-1,-1;Creator \"Creator\" true true false 128 Text 0 0,First,#,Survey Start-Stop,Creator,0,128;EditDate \"EditDate\" true true false 8 Date 0 0,First,#,Survey Start-Stop,EditDate,-1,-1;Editor \"Editor\" true true false 128 Text 0 0,First,#,Survey Start-Stop,Editor,0,128;GlobalID \"GlobalID\" false false true 38 GlobalID 0 0,First,#,Survey Start-Stop,GlobalID,-1,-1;map \"Map\" true true false 255 Text 0 0,First,#,Survey Start-Stop,map,0,255;key_ \"Key\" true true false 255 Text 0 0,First,#,Survey Start-Stop,key_,0,255;Name \"Name\" true true false 320 Text 0 0,First,#,Sites,Name,0,320;GlobalID_1 \"GlobalID\" false false true 38 GlobalID 0 0,First,#,Sites,GlobalID,-1,-1;CreationDate_1 \"CreationDate\" false true false 8 Date 0 0,First,#,Sites,CreationDate,-1,-1;Creator_1 \"Creator\" false true false 128 Text 0 0,First,#,Sites,Creator,0,128;EditDate_1 \"EditDate\" false true false 8 Date 0 0,First,#,Sites,EditDate,-1,-1;Editor_1 \"Editor\" false true false 128 Text 0 0,First,#,Sites,Editor,0,128;study_area \"Study Area\" true true false 10 Text 0 0,First,#,Sites,study_area,0,10;State \"State\" true true false 5 Text 0 0,First,#,Sites,State,0,5;Land_Mngr \"Land Manager\" true true false 50 Text 0 0,First,#,Sites,Land_Mngr,0,50;area \"Area_ha\" true true false 0 Float 0 0,First,#,Sites,area,-1,-1;mgmt_authority \"mgmt_authority\" true true false 255 Text 0 0,First,#,Sites,mgmt_authority,0,255;veg_spp_1 \"veg_spp_1\" true true false 255 Text 0 0,First,#,Sites,veg_spp_1,0,255;veg_spp_2 \"veg_spp_2\" true true false 255 Text 0 0,First,#,Sites,veg_spp_2,0,255;veg_spp_3 \"veg_spp_3\" true true false 255 Text 0 0,First,#,Sites,veg_spp_3,0,255;veg_spp_4 \"veg_spp_4\" true true false 255 Text 0 0,First,#,Sites,veg_spp_4,0,255;veg_characteristics \"veg_characteristics\" true true false 255 Text 0 0,First,#,Sites,veg_characteristics,0,255;canopy_ht \"Canopy_Height\" true true false 0 Double 0 0,First,#,Sites,canopy_ht,-1,-1;fws_permit_number \"FWS_Permit_Num\" true true false 255 Text 0 0,First,#,Sites,fws_permit_number,0,255;state_permit_number \"State_Permit_Num\" true true false 255 Text 0 0,First,#,Sites,state_permit_number,0,255;type \"Effort_Type\" true true false 255 Text 0 0,First,#,Sites,type,0,255;NameCalc \"Name Calc\" true true false 255 Text 0 0,First,#,Sites,NameCalc,0,255;Shape__Area \"Shape__Area\" true true false 0 Double 0 0,First,#,Sites,Shape__Area,-1,-1;Shape__Length \"Shape__Length\" true true false 0 Double 0 0,First,#,Sites,Shape__Length,-1,-1;Shape__Area_2 \"Shape__Area_2\" false true false 0 Double 0 0,First,#,Sites,Shape__Area_2,-1,-1;Shape__Length_2 \"Shape__Length_2\" false true false 0 Double 0 0,First,#,Sites,Shape__Length_2,-1,-1;Glob_ID \"Glob_ID\" true false false 38 Guid 0 0,First,#,Survey Start-Stop,GlobalID,-1,-1", match_option="CLOSEST", search_radius="", distance_field_name="site_distance")
# Process: Add Field (Add Field) 
arcpy.AddField_management(in_table=SurveyStartStop_SpatialJoin, field_name="sau_field", field_type="TEXT", field_precision=None, field_scale=None, field_length=50, field_alias="", field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")[0]
# Process: Calculate Field (Calculate Field) 
arcpy.CalculateField_management(in_table=SurveyStartStop_SpatialJoin, field="sau_field", expression="reclass(!site_distance!,!Name!)", expression_type="PYTHON3", code_block=code_block1)

cursor1 = arcpy.da.SearchCursor(SurveyStartStop_SpatialJoin, ['Glob_ID', 'sau_field'])

# make a dictionary and store values from watershed table
sectionsUpdateSSS = {}
for row in cursor1:
  sectionsUpdateSSS[row[0]]=row[1]


# Process: Select Layer By Attribute (2) (Select Layer By Attribute) 
arcpy.SelectLayerByAttribute_management(in_layer_or_view=Other_Species, selection_type="NEW_SELECTION", where_clause="section IS NULL", invert_where_clause="")
# Process: Spatial Join (2) (Spatial Join) 
OtherSpecies_SpatialJoin = r"N:\Projects\43000\43741-000 LCR SWFL\APRX\SWFL Scripts\SWFL_DF_Scripts\SWFL_DF_Scripts.gdb\OtherSpecies_SpatialJoin"
arcpy.SpatialJoin_analysis(target_features=Other_Species, join_features=Sites, out_feature_class=OtherSpecies_SpatialJoin, join_operation="JOIN_ONE_TO_ONE", join_type="KEEP_ALL", field_mapping="sp \"Species\" true true false 255 Text 0 0,First,#,Other Species,sp,0,255;det_type \"Detection Type\" true true false 255 Text 0 0,First,#,Other Species,det_type,0,255;indiv_count \"# Individuals\" true true false 0 Short 0 0,First,#,Other Species,indiv_count,-1,-1;bearing \"Offset Bearing\" true true false 0 Double 0 0,First,#,Other Species,bearing,-1,-1;distance \"Offset Distance\" true true false 0 Double 0 0,First,#,Other Species,distance,-1,-1;notes \"Comments\" true true false 3998 Text 0 0,First,#,Other Species,notes,0,3998;date_coll \"Date Collected\" true true false 8 Date 0 0,First,#,Other Species,date_coll,-1,-1;obs_select \"Observer\" true true false 500 Text 0 0,First,#,Other Species,obs_select,0,500;section \"Area-Site\" true true false 255 Text 0 0,First,#,Other Species,section,0,255;ofc_editor_1 \"Office Editor 1\" true true false 255 Text 0 0,First,#,Other Species,ofc_editor_1,0,255;ofc_editdate_1 \"Office Edit Date 1\" true true false 8 Date 0 0,First,#,Other Species,ofc_editdate_1,-1,-1;ofc_edit_1 \"Office Edit 1\" true true false 500 Text 0 0,First,#,Other Species,ofc_edit_1,0,500;ofc_editor_2 \"Office Editor 2\" true true false 255 Text 0 0,First,#,Other Species,ofc_editor_2,0,255;ofc_editdate_2 \"Office Edit Date 2\" true true false 8 Date 0 0,First,#,Other Species,ofc_editdate_2,-1,-1;ofc_edit_2 \"Office Edit 2\" true true false 500 Text 0 0,First,#,Other Species,ofc_edit_2,0,500;CreationDate \"CreationDate\" true true false 8 Date 0 0,First,#,Other Species,CreationDate,-1,-1;Creator \"Creator\" true true false 128 Text 0 0,First,#,Other Species,Creator,0,128;EditDate \"EditDate\" true true false 8 Date 0 0,First,#,Other Species,EditDate,-1,-1;Editor \"Editor\" true true false 128 Text 0 0,First,#,Other Species,Editor,0,128;GlobalID \"GlobalID\" false false true 38 GlobalID 0 0,First,#,Other Species,GlobalID,-1,-1;map \"Map Name\" true true false 255 Text 0 0,First,#,Other Species,map,0,255;key_ \"Key\" true true false 255 Text 0 0,First,#,Other Species,key_,0,255;easting \"UTME\" true true false 0 Long 0 0,First,#,Other Species,easting,-1,-1;northing \"UTMN\" true true false 0 Long 0 0,First,#,Other Species,northing,-1,-1;Name \"Name\" true true false 320 Text 0 0,First,#,Sites,Name,0,320;GlobalID_1 \"GlobalID\" false false true 38 GlobalID 0 0,First,#,Sites,GlobalID,-1,-1;CreationDate_1 \"CreationDate\" false true false 8 Date 0 0,First,#,Sites,CreationDate,-1,-1;Creator_1 \"Creator\" false true false 128 Text 0 0,First,#,Sites,Creator,0,128;EditDate_1 \"EditDate\" false true false 8 Date 0 0,First,#,Sites,EditDate,-1,-1;Editor_1 \"Editor\" false true false 128 Text 0 0,First,#,Sites,Editor,0,128;study_area \"Study Area\" true true false 10 Text 0 0,First,#,Sites,study_area,0,10;State \"State\" true true false 5 Text 0 0,First,#,Sites,State,0,5;Land_Mngr \"Land Manager\" true true false 50 Text 0 0,First,#,Sites,Land_Mngr,0,50;area \"Area_ha\" true true false 0 Float 0 0,First,#,Sites,area,-1,-1;mgmt_authority \"mgmt_authority\" true true false 255 Text 0 0,First,#,Sites,mgmt_authority,0,255;veg_spp_1 \"veg_spp_1\" true true false 255 Text 0 0,First,#,Sites,veg_spp_1,0,255;veg_spp_2 \"veg_spp_2\" true true false 255 Text 0 0,First,#,Sites,veg_spp_2,0,255;veg_spp_3 \"veg_spp_3\" true true false 255 Text 0 0,First,#,Sites,veg_spp_3,0,255;veg_spp_4 \"veg_spp_4\" true true false 255 Text 0 0,First,#,Sites,veg_spp_4,0,255;veg_characteristics \"veg_characteristics\" true true false 255 Text 0 0,First,#,Sites,veg_characteristics,0,255;canopy_ht \"Canopy_Height\" true true false 0 Double 0 0,First,#,Sites,canopy_ht,-1,-1;fws_permit_number \"FWS_Permit_Num\" true true false 255 Text 0 0,First,#,Sites,fws_permit_number,0,255;state_permit_number \"State_Permit_Num\" true true false 255 Text 0 0,First,#,Sites,state_permit_number,0,255;type \"Effort_Type\" true true false 255 Text 0 0,First,#,Sites,type,0,255;NameCalc \"Name Calc\" true true false 255 Text 0 0,First,#,Sites,NameCalc,0,255;Shape__Area \"Shape__Area\" true true false 0 Double 0 0,First,#,Sites,Shape__Area,-1,-1;Shape__Length \"Shape__Length\" true true false 0 Double 0 0,First,#,Sites,Shape__Length,-1,-1;Shape__Area_2 \"Shape__Area_2\" false true false 0 Double 0 0,First,#,Sites,Shape__Area_2,-1,-1;Shape__Length_2 \"Shape__Length_2\" false true false 0 Double 0 0,First,#,Sites,Shape__Length_2,-1,-1;Glob_ID \"Glob_ID\" true false false 38 Guid 0 0,First,#,Other Species,GlobalID,-1,-1", match_option="CLOSEST", search_radius="", distance_field_name="site_distance")
# Process: Add Field (2) (Add Field) 
arcpy.AddField_management(in_table=OtherSpecies_SpatialJoin, field_name="sau_field", field_type="TEXT", field_precision=None, field_scale=None, field_length=50, field_alias="", field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")[0]
# Process: Calculate Field (4) (Calculate Field) 
arcpy.CalculateField_management(in_table=OtherSpecies_SpatialJoin, field="sau_field", expression="reclass(!site_distance!,!Name!)", expression_type="PYTHON3", code_block=code_block1)

cursor2 = arcpy.da.SearchCursor(OtherSpecies_SpatialJoin, ['Glob_ID', 'sau_field'])

# make a dictionary and store values from watershed table
sectionsUpdateOS = {}
for row in cursor2:
  sectionsUpdateOS[row[0]]=row[1]


# Process: Select Layer By Attribute (3) (Select Layer By Attribute) 
arcpy.SelectLayerByAttribute_management(in_layer_or_view=Point_of_Interest, selection_type="NEW_SELECTION", where_clause="section IS NULL", invert_where_clause="")
# Process: Spatial Join (3) (Spatial Join) 
PointofInterest_SpatialJoin = r"N:\Projects\43000\43741-000 LCR SWFL\APRX\SWFL Scripts\SWFL_DF_Scripts\SWFL_DF_Scripts.gdb\PointofInterest_SpatialJoin"
arcpy.SpatialJoin_analysis(target_features=Point_of_Interest, join_features=Sites, out_feature_class=PointofInterest_SpatialJoin, join_operation="JOIN_ONE_TO_ONE", join_type="KEEP_ALL", field_mapping="pnt_type \"Point Type\" true true false 255 Text 0 0,First,#,Point of Interest,pnt_type,0,255;desc_short \"Label / Short Description (20c)\" true true false 20 Text 0 0,First,#,Point of Interest,desc_short,0,20;notes \"Comments\" true true false 4000 Text 0 0,First,#,Point of Interest,notes,0,4000;date_coll \"Date Collected\" true true false 8 Date 0 0,First,#,Point of Interest,date_coll,-1,-1;obs_select \"Observer\" true true false 500 Text 0 0,First,#,Point of Interest,obs_select,0,500;section \"Area-Site\" true true false 255 Text 0 0,First,#,Point of Interest,section,0,255;ofc_editor_1 \"Office Editor 1\" true true false 50 Text 0 0,First,#,Point of Interest,ofc_editor_1,0,50;ofc_editdate_1 \"Office Edit Date 1\" true true false 8 Date 0 0,First,#,Point of Interest,ofc_editdate_1,-1,-1;ofc_edit_1 \"Office Edit 1\" true true false 500 Text 0 0,First,#,Point of Interest,ofc_edit_1,0,500;ofc_editor_2 \"Office Editor 2\" true true false 50 Text 0 0,First,#,Point of Interest,ofc_editor_2,0,50;ofc_editdate_2 \"Office Edit Date 2\" true true false 8 Date 0 0,First,#,Point of Interest,ofc_editdate_2,-1,-1;ofc_edit_2 \"Office Edit 2\" true true false 500 Text 0 0,First,#,Point of Interest,ofc_edit_2,0,500;CreationDate \"CreationDate\" true true false 8 Date 0 0,First,#,Point of Interest,CreationDate,-1,-1;Creator \"Creator\" true true false 128 Text 0 0,First,#,Point of Interest,Creator,0,128;EditDate \"EditDate\" true true false 8 Date 0 0,First,#,Point of Interest,EditDate,-1,-1;Editor \"Editor\" true true false 128 Text 0 0,First,#,Point of Interest,Editor,0,128;GlobalID \"GlobalID\" false false true 38 GlobalID 0 0,First,#,Point of Interest,GlobalID,-1,-1;map \"Map\" true true false 255 Text 0 0,First,#,Point of Interest,map,0,255;key_ \"Key\" true true false 255 Text 0 0,First,#,Point of Interest,key_,0,255;Name \"Name\" true true false 320 Text 0 0,First,#,Sites,Name,0,320;GlobalID_1 \"GlobalID\" false false true 38 GlobalID 0 0,First,#,Sites,GlobalID,-1,-1;CreationDate_1 \"CreationDate\" false true false 8 Date 0 0,First,#,Sites,CreationDate,-1,-1;Creator_1 \"Creator\" false true false 128 Text 0 0,First,#,Sites,Creator,0,128;EditDate_1 \"EditDate\" false true false 8 Date 0 0,First,#,Sites,EditDate,-1,-1;Editor_1 \"Editor\" false true false 128 Text 0 0,First,#,Sites,Editor,0,128;study_area \"Study Area\" true true false 10 Text 0 0,First,#,Sites,study_area,0,10;State \"State\" true true false 5 Text 0 0,First,#,Sites,State,0,5;Land_Mngr \"Land Manager\" true true false 50 Text 0 0,First,#,Sites,Land_Mngr,0,50;area \"Area_ha\" true true false 0 Float 0 0,First,#,Sites,area,-1,-1;mgmt_authority \"mgmt_authority\" true true false 255 Text 0 0,First,#,Sites,mgmt_authority,0,255;veg_spp_1 \"veg_spp_1\" true true false 255 Text 0 0,First,#,Sites,veg_spp_1,0,255;veg_spp_2 \"veg_spp_2\" true true false 255 Text 0 0,First,#,Sites,veg_spp_2,0,255;veg_spp_3 \"veg_spp_3\" true true false 255 Text 0 0,First,#,Sites,veg_spp_3,0,255;veg_spp_4 \"veg_spp_4\" true true false 255 Text 0 0,First,#,Sites,veg_spp_4,0,255;veg_characteristics \"veg_characteristics\" true true false 255 Text 0 0,First,#,Sites,veg_characteristics,0,255;canopy_ht \"Canopy_Height\" true true false 0 Double 0 0,First,#,Sites,canopy_ht,-1,-1;fws_permit_number \"FWS_Permit_Num\" true true false 255 Text 0 0,First,#,Sites,fws_permit_number,0,255;state_permit_number \"State_Permit_Num\" true true false 255 Text 0 0,First,#,Sites,state_permit_number,0,255;type \"Effort_Type\" true true false 255 Text 0 0,First,#,Sites,type,0,255;NameCalc \"Name Calc\" true true false 255 Text 0 0,First,#,Sites,NameCalc,0,255;Shape__Area \"Shape__Area\" true true false 0 Double 0 0,First,#,Sites,Shape__Area,-1,-1;Shape__Length \"Shape__Length\" true true false 0 Double 0 0,First,#,Sites,Shape__Length,-1,-1;Shape__Area_2 \"Shape__Area_2\" false true false 0 Double 0 0,First,#,Sites,Shape__Area_2,-1,-1;Shape__Length_2 \"Shape__Length_2\" false true false 0 Double 0 0,First,#,Sites,Shape__Length_2,-1,-1;Glob_ID \"Glob_ID\" true false false 38 Guid 0 0,First,#,Point of Interest,GlobalID,-1,-1", match_option="CLOSEST", search_radius="", distance_field_name="site_distance")
# Process: Add Field (3) (Add Field) 
arcpy.AddField_management(in_table=PointofInterest_SpatialJoin, field_name="sau_field", field_type="TEXT", field_precision=None, field_scale=None, field_length=50, field_alias="", field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")[0]
# Process: Calculate Field (7) (Calculate Field) 
arcpy.CalculateField_management(in_table=PointofInterest_SpatialJoin, field="sau_field", expression="reclass(!site_distance!,!Name!)", expression_type="PYTHON3", code_block=code_block1)

cursor3 = arcpy.da.SearchCursor(PointofInterest_SpatialJoin, ['Glob_ID', 'sau_field'])

# make a dictionary and store values from watershed table
sectionsUpdatePOI = {}
for row in cursor3:
  sectionsUpdatePOI[row[0]]=row[1]


# Process: Select Layer By Attribute (4) (Select Layer By Attribute) 
arcpy.SelectLayerByAttribute_management(in_layer_or_view=WIFL_Detection, selection_type="NEW_SELECTION", where_clause="map = 'Monitoring' And section IS NULL", invert_where_clause="")
# Process: Spatial Join (4) (Spatial Join) 
WIFLDetection_SpatialJoin = r"N:\Projects\43000\43741-000 LCR SWFL\APRX\SWFL Scripts\SWFL_DF_Scripts\SWFL_DF_Scripts.gdb\WIFLDetection_SpatialJoin"
arcpy.SpatialJoin_analysis(target_features=WIFL_Detection, join_features=Sites, out_feature_class=WIFLDetection_SpatialJoin, join_operation="JOIN_ONE_TO_ONE", join_type="KEEP_ALL", field_mapping="wifl_det_type \"Detection Type\" true true false 50 Text 0 0,First,#,WIFL Detection,wifl_det_type,0,50;det_beh \"Behavior\" true true false 50 Text 0 0,First,#,WIFL Detection,det_beh,0,50;ter_id \"Territory ID\" true true false 10 Text 0 0,First,#,WIFL Detection,ter_id,0,10;bearing \"Offset Bearing\" true true false 0 Double 0 0,First,#,WIFL Detection,bearing,-1,-1;distance \"Offset Distance\" true true false 0 Double 0 0,First,#,WIFL Detection,distance,-1,-1;det_type \"Method of Detection\" true true false 255 Text 0 0,First,#,WIFL Detection,det_type,0,255;timing \"Detected during timed window?\" true true false 50 Text 0 0,First,#,WIFL Detection,timing,0,50;notes \"Comments\" true true false 4000 Text 0 0,First,#,WIFL Detection,notes,0,4000;date_coll \"Date Collected\" true true false 8 Date 0 0,First,#,WIFL Detection,date_coll,-1,-1;obs_select \"Observer\" true true false 500 Text 0 0,First,#,WIFL Detection,obs_select,0,500;section \"Area-Site\" true true false 50 Text 0 0,First,#,WIFL Detection,section,0,50;ofc_editor_1 \"Office Editor 1\" true true false 500 Text 0 0,First,#,WIFL Detection,ofc_editor_1,0,500;ofc_editdate_1 \"Office Edit Date 1\" true true false 8 Date 0 0,First,#,WIFL Detection,ofc_editdate_1,-1,-1;ofc_edit_1 \"Office Edit 1\" true true false 500 Text 0 0,First,#,WIFL Detection,ofc_edit_1,0,500;ofc_editor_2 \"Office Editor 2\" true true false 500 Text 0 0,First,#,WIFL Detection,ofc_editor_2,0,500;ofc_editdate_2 \"Office Edit Date 2\" true true false 8 Date 0 0,First,#,WIFL Detection,ofc_editdate_2,-1,-1;ofc_edit_2 \"Office Edit 2\" true true false 500 Text 0 0,First,#,WIFL Detection,ofc_edit_2,0,500;CreationDate \"CreationDate 1\" true true false 8 Date 0 0,First,#,WIFL Detection,CreationDate,-1,-1;Creator \"Creator_1\" true true false 128 Text 0 0,First,#,WIFL Detection,Creator,0,128;EditDate \"EditDate\" true true false 8 Date 0 0,First,#,WIFL Detection,EditDate,-1,-1;Editor \"Editor\" true true false 128 Text 0 0,First,#,WIFL Detection,Editor,0,128;parentglobalid \"Parent GlobalID\" true true false 38 Guid 0 0,First,#,WIFL Detection,parentglobalid,-1,-1;GlobalID \"GlobalID\" false false true 38 GlobalID 0 0,First,#,WIFL Detection,GlobalID,-1,-1;map \"Map\" true true false 255 Text 0 0,First,#,WIFL Detection,map,0,255;key_ \"Key\" true true false 255 Text 0 0,First,#,WIFL Detection,key_,0,255;Name \"Name\" true true false 320 Text 0 0,First,#,Sites,Name,0,320;GlobalID_1 \"GlobalID\" false false true 38 GlobalID 0 0,First,#,Sites,GlobalID,-1,-1;CreationDate_1 \"CreationDate\" false true false 8 Date 0 0,First,#,Sites,CreationDate,-1,-1;Creator_1 \"Creator\" false true false 128 Text 0 0,First,#,Sites,Creator,0,128;EditDate_1 \"EditDate\" false true false 8 Date 0 0,First,#,Sites,EditDate,-1,-1;Editor_1 \"Editor\" false true false 128 Text 0 0,First,#,Sites,Editor,0,128;study_area \"Study Area\" true true false 10 Text 0 0,First,#,Sites,study_area,0,10;State \"State\" true true false 5 Text 0 0,First,#,Sites,State,0,5;Land_Mngr \"Land Manager\" true true false 50 Text 0 0,First,#,Sites,Land_Mngr,0,50;area \"Area_ha\" true true false 0 Float 0 0,First,#,Sites,area,-1,-1;mgmt_authority \"mgmt_authority\" true true false 255 Text 0 0,First,#,Sites,mgmt_authority,0,255;veg_spp_1 \"veg_spp_1\" true true false 255 Text 0 0,First,#,Sites,veg_spp_1,0,255;veg_spp_2 \"veg_spp_2\" true true false 255 Text 0 0,First,#,Sites,veg_spp_2,0,255;veg_spp_3 \"veg_spp_3\" true true false 255 Text 0 0,First,#,Sites,veg_spp_3,0,255;veg_spp_4 \"veg_spp_4\" true true false 255 Text 0 0,First,#,Sites,veg_spp_4,0,255;veg_characteristics \"veg_characteristics\" true true false 255 Text 0 0,First,#,Sites,veg_characteristics,0,255;canopy_ht \"Canopy_Height\" true true false 0 Double 0 0,First,#,Sites,canopy_ht,-1,-1;fws_permit_number \"FWS_Permit_Num\" true true false 255 Text 0 0,First,#,Sites,fws_permit_number,0,255;state_permit_number \"State_Permit_Num\" true true false 255 Text 0 0,First,#,Sites,state_permit_number,0,255;type \"Effort_Type\" true true false 255 Text 0 0,First,#,Sites,type,0,255;NameCalc \"Name Calc\" true true false 255 Text 0 0,First,#,Sites,NameCalc,0,255;Shape__Area \"Shape__Area\" true true false 0 Double 0 0,First,#,Sites,Shape__Area,-1,-1;Shape__Length \"Shape__Length\" true true false 0 Double 0 0,First,#,Sites,Shape__Length,-1,-1;Shape__Area_2 \"Shape__Area_2\" false true false 0 Double 0 0,First,#,Sites,Shape__Area_2,-1,-1;Shape__Length_2 \"Shape__Length_2\" false true false 0 Double 0 0,First,#,Sites,Shape__Length_2,-1,-1;Glob_ID \"Glob_ID\" true false false 38 Guid 0 0,First,#,WIFL Detection,GlobalID,-1,-1", match_option="CLOSEST", search_radius="", distance_field_name="site_distance")
# Process: Add Field (4) (Add Field) 
arcpy.AddField_management(in_table=WIFLDetection_SpatialJoin, field_name="sau_field", field_type="TEXT", field_precision=None, field_scale=None, field_length=50, field_alias="", field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")[0]
# Process: Calculate Field (10) (Calculate Field) 
arcpy.CalculateField_management(in_table=WIFLDetection_SpatialJoin, field="sau_field", expression="reclass(!site_distance!,!Name!)", expression_type="PYTHON3", code_block=code_block1)

cursor4 = arcpy.da.SearchCursor(WIFLDetection_SpatialJoin, ['Glob_ID', 'sau_field'])

# make a dictionary and store values from watershed table
sectionsUpdateWIFL = {}
for row in cursor4:
  sectionsUpdateWIFL[row[0]]=row[1]
    

fields = ['GlobalID','section']

# Create update cursor for Survey Start Stop feature class to add start and stop times and unique site area IDs 
with arcpy.da.UpdateCursor(Survey_Start_Stop, fields) as cursor:
    for row in cursor:
        for key, value in sectionsUpdateSSS.items():
            if key.lower() == row[0].lower():
                row[1] = value
            else:
                pass
        cursor.updateRow(row)


# Create update cursor for Survey Start Stop feature class to add start and stop times and unique site area IDs 
with arcpy.da.UpdateCursor(Other_Species, fields) as cursor:
    for row in cursor:
        for key, value in sectionsUpdateOS.items():
            if key.lower() == row[0].lower():
                row[1] = value
            else:
                pass
        cursor.updateRow(row)


# Create update cursor for Survey Start Stop feature class to add start and stop times and unique site area IDs 
with arcpy.da.UpdateCursor(WIFL_Detection, fields) as cursor:
    for row in cursor:
        for key, value in sectionsUpdateWIFL.items():
            if key.lower() == row[0].lower():
                row[1] = value
            else:
                pass
        cursor.updateRow(row)


# Create update cursor for Survey Start Stop feature class to add start and stop times and unique site area IDs 
with arcpy.da.UpdateCursor(Point_of_Interest, fields) as cursor:
    for row in cursor:
        for key, value in sectionsUpdatePOI.items():
            if key.lower() == row[0].lower():
                row[1] = value
            else:
                pass
        cursor.updateRow(row)