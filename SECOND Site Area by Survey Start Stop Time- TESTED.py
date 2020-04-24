import arcpy
from datetime import datetime

General_Polygon = "https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_Root_2020/FeatureServer/7"
Other_Species = "https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_Root_2020/FeatureServer/3"
Point_Of_Interest = "https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_Root_2020/FeatureServer/4"
Survey_Point = "https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_Root_2020/FeatureServer/1"
Survey_Start_Stop = "https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_Root_2020/FeatureServer/0"
SWFL_Line = "https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_Root_2020/FeatureServer/5"
SWFL_Polygon = "https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_Root_2020/FeatureServer/6"
WIFL_Detection = "https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_Root_2020/FeatureServer/2"

SurveyStartStop_Combined = "N:\\Projects\\43000\\43741-000 LCR SWFL\\APRX\\SWFL Scripts\\SWFL_DF_Scripts\\SWFL_DF_Scripts.gdb\\SSS_SA_Combined"

ID = 0
Survey_Start_Stop_calcs = "N:\\Projects\\43000\\43741-000 LCR SWFL\\APRX\\SWFL Scripts\\SWFL_DF_Scripts\\SWFL_DF_Scripts.gdb\\SSS_SA"
fields = ['sur_pt_type', 'SSS_ID', 'date_coll', 'StartTime', 'StopTime']
#######
###copy the Survey Start Stop times to a scrap FC that clears unwated fields
arcpy.conversion.FeatureClassToFeatureClass("https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_Root_2020/FeatureServer/0", r"N:\Projects\43000\43741-000 LCR SWFL\APRX\SWFL Scripts\SWFL_DF_Scripts\SWFL_DF_Scripts.gdb", "SSS_SA", '', 'sur_pt_type "Point Type" true true false 255 Text 0 0,First,#,https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_Root_2020/FeatureServer/0,sur_pt_type,0,255;date_coll "Date Collected" true true false 8 Date 0 0,First,#,https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_Root_2020/FeatureServer/0,date_coll,-1,-1;section "Area-Site" true true false 255 Text 0 0,First,#,https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_Root_2020/FeatureServer/0,section,0,255', '')
###add fields needed to combine start and stop points info into 1 feature per start and stop.
arcpy.management.AddFields("SSS_SA", "SSS_ID LONG # # # #;StartTime DATE # # # #;StopTime DATE # # # #")


# Create update cursor for Survey Start Stop feature class to add start and stop times and unique site area IDs 
with arcpy.da.UpdateCursor(Survey_Start_Stop_calcs, fields) as cursor:
    for row in cursor:
        if (row[0] == "start"):
            start_time = row[2]
            row[3] = start_time
            ID += 1
            row[1] = ID
        if (row[0] == "stop"):
            stop_time = row[2]
            row[3] = start_time
            row[4] = stop_time
            row[1] = ID            
        cursor.updateRow(row)

Survey_Start_Stop_selection, count = arcpy.management.SelectLayerByAttribute(Survey_Start_Stop_calcs, "NEW_SELECTION", "sur_pt_type = 'stop'", None)
arcpy.conversion.FeatureClassToFeatureClass(Survey_Start_Stop_selection, r"N:\Projects\43000\43741-000 LCR SWFL\APRX\SWFL Scripts\SWFL_DF_Scripts\SWFL_DF_Scripts.gdb", "SSS_SA_Combined", '', 'sur_pt_type "Point Type" true true false 255 Text 0 0,First,#,SSS_SA,sur_pt_type,0,255;date_coll "Date Collected" true true false 8 Date 0 0,First,#,SSS_SA,date_coll,-1,-1;section "Area-Site" true true false 255 Text 0 0,First,#,SSS_SA,section,0,255;SSS_ID "SSS_ID" true true false 4 Long 0 0,First,#,SSS_SA,SSS_ID,-1,-1;StartTime "StartTime" true true false 8 Date 0 0,First,#,SSS_SA,StartTime,-1,-1;StopTime "StopTime" true true false 8 Date 0 0,First,#,SSS_SA,StopTime,-1,-1', '')



############# GETTING SITE AREA AND START AND STOP TIMES INTO LISTS
fc = SurveyStartStop_Combined
field1 = 'section'
field2 = 'StartTime'
field3 = 'StopTime'
listSA = []
listST = []
listSTT = []
listSTFormat = []
listSTTFormat = []


rows = arcpy.SearchCursor(fc)
for row in rows:  
    listSA.append(row.getValue(field1)) 
    listST.append(row.getValue(field2))
    listSTT.append(row.getValue(field3))
for dates in listST:
    listSTFormat.append(dates.strftime('%Y-%m-%d %H:%M:%S'))
for dates in listSTT:
    listSTTFormat.append(dates.strftime('%Y-%m-%d %H:%M:%S'))


###Loop through the start stop times and select the attributes that match
for a1,b1,c1 in zip(listSA,listSTFormat,listSTTFormat):
    arcpy.management.SelectLayerByAttribute(SWFL_Line, "NEW_SELECTION","CreationDate > timestamp '" + b1 + "' And CreationDate < timestamp '" + c1 + "'", None)
    arcpy.management.CalculateField(SWFL_Line, "section",  "'" +a1.rsplit(' ', 1)[0] +"'" , "PYTHON3", '', "TEXT")

###Loop through the start stop times and select the attributes that match
for a1,b1,c1 in zip(listSA,listSTFormat,listSTTFormat):
    arcpy.management.SelectLayerByAttribute(WIFL_Detection, "NEW_SELECTION","CreationDate > timestamp '" + b1 + "' And CreationDate < timestamp '" + c1 + "'", None)
    arcpy.management.CalculateField(WIFL_Detection, "section", "'" +a1.rsplit(' ', 1)[0]+ "'" , "PYTHON3", '', "TEXT")

###Loop through the start stop times and select the attributes that match
for a1,b1,c1 in zip(listSA,listSTFormat,listSTTFormat):
    arcpy.management.SelectLayerByAttribute(Survey_Point, "NEW_SELECTION","CreationDate > timestamp '" + b1 + "' And CreationDate < timestamp '" + c1 + "'", None)
    arcpy.management.CalculateField(Survey_Point, "section", "'" +a1.rsplit(' ', 1)[0] +"'" , "PYTHON3", '', "TEXT")

###Loop through the start stop times and select the attributes that match
for a1,b1,c1 in zip(listSA,listSTFormat,listSTTFormat):
    arcpy.management.SelectLayerByAttribute(General_Polygon, "NEW_SELECTION","CreationDate > timestamp '" + b1 + "' And CreationDate < timestamp '" + c1 + "'", None)
    arcpy.management.CalculateField(General_Polygon, "section", "'" +a1.rsplit(' ', 1)[0] +"'" , "PYTHON3", '', "TEXT")



