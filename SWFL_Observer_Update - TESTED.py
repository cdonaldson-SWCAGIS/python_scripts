import arcpy

General_Polygon = "https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_Root_2020/FeatureServer/7"
Other_Species = "https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_Root_2020/FeatureServer/3"
Point_Of_Interest = "https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_Root_2020/FeatureServer/4"
Survey_Point = "https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_Root_2020/FeatureServer/1"
Survey_Start_Stop = "https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_Root_2020/FeatureServer/0"
SWFL_Line = "https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_Root_2020/FeatureServer/5"
SWFL_Polygon = "https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_Root_2020/FeatureServer/6"
WIFL_Detection = "https://services1.arcgis.com/ypdMhhEhrtBXLtQv/arcgis/rest/services/SWFL_Root_2020/FeatureServer/2"


fields = ['obs_select', 'Creator']

# Create update cursor for feature class 
with arcpy.da.UpdateCursor(General_Polygon, fields) as cursor:
    for row in cursor:
        if (row[1] == "aLamb_SWCA"):
            row[0] = "Alaina Lamb"
        elif (row[1] == "aPellegrini_SWCA"):
            row[0] = "Anne Pellegrini"
        elif (row[1] == "BRaulston@usbr.gov_USBR"):
            row[0] = "Barbara Raulston"
        elif (row[1] == "lsabin@usbr.gov_USBR"):
            row[0] = "Beth Sabin"
        elif (row[1] == "cronning@usbr.gov_USBR"):
            row[0] = "Carrie Ronning"
        elif (row[1] == "Need C_Dodges_ID"):
            row[0] = "Chris Dodge"
        elif (row[1] == "GCummins_LCR"):
            row[0] = "George Cummins"
        elif (row[1] == "JHill@usbr.gov_USBR"):
            row[0] = "Jeff Hill"
        elif (row[1] == "JenealSmith@usbr.gov_USBR"):
            row[0] = "Jenny Smith"
        elif (row[1] == "jWebber_SWCA"):
            row[0] = "Julie Webber"
        elif (row[1] == "JKahl@usbr.gov_USBR"):
            row[0] = "Joe Kahl"
        elif (row[1] == "jlyon@usbr.gov_USBR"):
            row[0] = "Joe Lyon"
        elif (row[1] == "mMcLeod_SWCA"):
            row[0] = "Mary Anne McLeod"
        elif (row[1] == "qYeates_SWCA"):
            row[0] = "Quick Yeates"        
        elif (row[1] == "sDougill_SWCA"):
            row[0] = "Steve Dougill"
        elif (row[1] == "Needs S_Nichols_ID"):
            row[0] = "Sarah Nichols"
        elif (row[1] == "tHinckley_SWCA"):
            row[0] = "Trevor Hinckley"
        elif (row[1] == "vHaworth_SWCA"):
            row[0] = "Val Haworth"
        elif (row[1] == "zEmery_SWCA"):
            row[0] = "Zach Emery"
        elif (row[1] == "mstandart"):
            row[0] = "Michael Standart"        
        # Update the cursor with the updated list
        cursor.updateRow(row)
# Create update cursor for feature class 
with arcpy.da.UpdateCursor(Other_Species, fields) as cursor:
    for row in cursor:
        if (row[1] == "aLamb_SWCA"):
            row[0] = "Alaina Lamb"
        elif (row[1] == "aPellegrini_SWCA"):
            row[0] = "Anne Pellegrini"
        elif (row[1] == "BRaulston@usbr.gov_USBR"):
            row[0] = "Barbara Raulston"
        elif (row[1] == "lsabin@usbr.gov_USBR"):
            row[0] = "Beth Sabin"
        elif (row[1] == "cronning@usbr.gov_USBR"):
            row[0] = "Carrie Ronning"
        elif (row[1] == "Need C_Dodges_ID"):
            row[0] = "Chris Dodge"
        elif (row[1] == "GCummins_LCR"):
            row[0] = "George Cummins"
        elif (row[1] == "JHill@usbr.gov_USBR"):
            row[0] = "Jeff Hill"
        elif (row[1] == "JenealSmith@usbr.gov_USBR"):
            row[0] = "Jenny Smith"
        elif (row[1] == "jWebber_SWCA"):
            row[0] = "Julie Webber"
        elif (row[1] == "JKahl@usbr.gov_USBR"):
            row[0] = "Joe Kahl"
        elif (row[1] == "jlyon@usbr.gov_USBR"):
            row[0] = "Joe Lyon"
        elif (row[1] == "mMcLeod_SWCA"):
            row[0] = "Mary Anne McLeod"
        elif (row[1] == "qYeates_SWCA"):
            row[0] = "Quick Yeates"        
        elif (row[1] == "sDougill_SWCA"):
            row[0] = "Steve Dougill"
        elif (row[1] == "Needs S_Nichols_ID"):
            row[0] = "Sarah Nichols"
        elif (row[1] == "tHinckley_SWCA"):
            row[0] = "Trevor Hinckley"
        elif (row[1] == "vHaworth_SWCA"):
            row[0] = "Val Haworth"
        elif (row[1] == "zEmery_SWCA"):
            row[0] = "Zach Emery"
        elif (row[1] == "mstandart"):
            row[0] = "Michael Standart"        
        # Update the cursor with the updated list
        cursor.updateRow(row)
# Create update cursor for feature class 
with arcpy.da.UpdateCursor(Point_Of_Interest, fields) as cursor:
    for row in cursor:
        if (row[1] == "aLamb_SWCA"):
            row[0] = "Alaina Lamb"
        elif (row[1] == "aPellegrini_SWCA"):
            row[0] = "Anne Pellegrini"
        elif (row[1] == "BRaulston@usbr.gov_USBR"):
            row[0] = "Barbara Raulston"
        elif (row[1] == "lsabin@usbr.gov_USBR"):
            row[0] = "Beth Sabin"
        elif (row[1] == "cronning@usbr.gov_USBR"):
            row[0] = "Carrie Ronning"
        elif (row[1] == "Need C_Dodges_ID"):
            row[0] = "Chris Dodge"
        elif (row[1] == "GCummins_LCR"):
            row[0] = "George Cummins"
        elif (row[1] == "JHill@usbr.gov_USBR"):
            row[0] = "Jeff Hill"
        elif (row[1] == "JenealSmith@usbr.gov_USBR"):
            row[0] = "Jenny Smith"
        elif (row[1] == "jWebber_SWCA"):
            row[0] = "Julie Webber"
        elif (row[1] == "JKahl@usbr.gov_USBR"):
            row[0] = "Joe Kahl"
        elif (row[1] == "jlyon@usbr.gov_USBR"):
            row[0] = "Joe Lyon"
        elif (row[1] == "mMcLeod_SWCA"):
            row[0] = "Mary Anne McLeod"
        elif (row[1] == "qYeates_SWCA"):
            row[0] = "Quick Yeates"        
        elif (row[1] == "sDougill_SWCA"):
            row[0] = "Steve Dougill"
        elif (row[1] == "Needs S_Nichols_ID"):
            row[0] = "Sarah Nichols"
        elif (row[1] == "tHinckley_SWCA"):
            row[0] = "Trevor Hinckley"
        elif (row[1] == "vHaworth_SWCA"):
            row[0] = "Val Haworth"
        elif (row[1] == "zEmery_SWCA"):
            row[0] = "Zach Emery"
        elif (row[1] == "mstandart"):
            row[0] = "Michael Standart"        
        # Update the cursor with the updated list
        cursor.updateRow(row)
# Create update cursor for feature class 
with arcpy.da.UpdateCursor(Survey_Point, fields) as cursor:
    for row in cursor:
        if (row[1] == "aLamb_SWCA"):
            row[0] = "Alaina Lamb"
        elif (row[1] == "aPellegrini_SWCA"):
            row[0] = "Anne Pellegrini"
        elif (row[1] == "BRaulston@usbr.gov_USBR"):
            row[0] = "Barbara Raulston"
        elif (row[1] == "lsabin@usbr.gov_USBR"):
            row[0] = "Beth Sabin"
        elif (row[1] == "cronning@usbr.gov_USBR"):
            row[0] = "Carrie Ronning"
        elif (row[1] == "Need C_Dodges_ID"):
            row[0] = "Chris Dodge"
        elif (row[1] == "GCummins_LCR"):
            row[0] = "George Cummins"
        elif (row[1] == "JHill@usbr.gov_USBR"):
            row[0] = "Jeff Hill"
        elif (row[1] == "JenealSmith@usbr.gov_USBR"):
            row[0] = "Jenny Smith"
        elif (row[1] == "jWebber_SWCA"):
            row[0] = "Julie Webber"
        elif (row[1] == "JKahl@usbr.gov_USBR"):
            row[0] = "Joe Kahl"
        elif (row[1] == "jlyon@usbr.gov_USBR"):
            row[0] = "Joe Lyon"
        elif (row[1] == "mMcLeod_SWCA"):
            row[0] = "Mary Anne McLeod"
        elif (row[1] == "qYeates_SWCA"):
            row[0] = "Quick Yeates"        
        elif (row[1] == "sDougill_SWCA"):
            row[0] = "Steve Dougill"
        elif (row[1] == "Needs S_Nichols_ID"):
            row[0] = "Sarah Nichols"
        elif (row[1] == "tHinckley_SWCA"):
            row[0] = "Trevor Hinckley"
        elif (row[1] == "vHaworth_SWCA"):
            row[0] = "Val Haworth"
        elif (row[1] == "zEmery_SWCA"):
            row[0] = "Zach Emery"
        elif (row[1] == "mstandart"):
            row[0] = "Michael Standart"        
        # Update the cursor with the updated list
        cursor.updateRow(row)
# Create update cursor for feature class 
with arcpy.da.UpdateCursor(Survey_Start_Stop, fields) as cursor:
    for row in cursor:
        if (row[1] == "aLamb_SWCA"):
            row[0] = "Alaina Lamb"
        elif (row[1] == "aPellegrini_SWCA"):
            row[0] = "Anne Pellegrini"
        elif (row[1] == "BRaulston@usbr.gov_USBR"):
            row[0] = "Barbara Raulston"
        elif (row[1] == "lsabin@usbr.gov_USBR"):
            row[0] = "Beth Sabin"
        elif (row[1] == "cronning@usbr.gov_USBR"):
            row[0] = "Carrie Ronning"
        elif (row[1] == "Need C_Dodges_ID"):
            row[0] = "Chris Dodge"
        elif (row[1] == "GCummins_LCR"):
            row[0] = "George Cummins"
        elif (row[1] == "JHill@usbr.gov_USBR"):
            row[0] = "Jeff Hill"
        elif (row[1] == "JenealSmith@usbr.gov_USBR"):
            row[0] = "Jenny Smith"
        elif (row[1] == "jWebber_SWCA"):
            row[0] = "Julie Webber"
        elif (row[1] == "JKahl@usbr.gov_USBR"):
            row[0] = "Joe Kahl"
        elif (row[1] == "jlyon@usbr.gov_USBR"):
            row[0] = "Joe Lyon"
        elif (row[1] == "mMcLeod_SWCA"):
            row[0] = "Mary Anne McLeod"
        elif (row[1] == "qYeates_SWCA"):
            row[0] = "Quick Yeates"        
        elif (row[1] == "sDougill_SWCA"):
            row[0] = "Steve Dougill"
        elif (row[1] == "Needs S_Nichols_ID"):
            row[0] = "Sarah Nichols"
        elif (row[1] == "tHinckley_SWCA"):
            row[0] = "Trevor Hinckley"
        elif (row[1] == "vHaworth_SWCA"):
            row[0] = "Val Haworth"
        elif (row[1] == "zEmery_SWCA"):
            row[0] = "Zach Emery"
        elif (row[1] == "mstandart"):
            row[0] = "Michael Standart"        
        # Update the cursor with the updated list
        cursor.updateRow(row)
# Create update cursor for feature class 
with arcpy.da.UpdateCursor(SWFL_Line, fields) as cursor:
    for row in cursor:
        if (row[1] == "aLamb_SWCA"):
            row[0] = "Alaina Lamb"
        elif (row[1] == "aPellegrini_SWCA"):
            row[0] = "Anne Pellegrini"
        elif (row[1] == "BRaulston@usbr.gov_USBR"):
            row[0] = "Barbara Raulston"
        elif (row[1] == "lsabin@usbr.gov_USBR"):
            row[0] = "Beth Sabin"
        elif (row[1] == "cronning@usbr.gov_USBR"):
            row[0] = "Carrie Ronning"
        elif (row[1] == "Need C_Dodges_ID"):
            row[0] = "Chris Dodge"
        elif (row[1] == "GCummins_LCR"):
            row[0] = "George Cummins"
        elif (row[1] == "JHill@usbr.gov_USBR"):
            row[0] = "Jeff Hill"
        elif (row[1] == "JenealSmith@usbr.gov_USBR"):
            row[0] = "Jenny Smith"
        elif (row[1] == "jWebber_SWCA"):
            row[0] = "Julie Webber"
        elif (row[1] == "JKahl@usbr.gov_USBR"):
            row[0] = "Joe Kahl"
        elif (row[1] == "jlyon@usbr.gov_USBR"):
            row[0] = "Joe Lyon"
        elif (row[1] == "mMcLeod_SWCA"):
            row[0] = "Mary Anne McLeod"
        elif (row[1] == "qYeates_SWCA"):
            row[0] = "Quick Yeates"        
        elif (row[1] == "sDougill_SWCA"):
            row[0] = "Steve Dougill"
        elif (row[1] == "Needs S_Nichols_ID"):
            row[0] = "Sarah Nichols"
        elif (row[1] == "tHinckley_SWCA"):
            row[0] = "Trevor Hinckley"
        elif (row[1] == "vHaworth_SWCA"):
            row[0] = "Val Haworth"
        elif (row[1] == "zEmery_SWCA"):
            row[0] = "Zach Emery"
        elif (row[1] == "mstandart"):
            row[0] = "Michael Standart"        
        # Update the cursor with the updated list
        cursor.updateRow(row)
# Create update cursor for feature class 
with arcpy.da.UpdateCursor(SWFL_Polygon, fields) as cursor:
    for row in cursor:
        if (row[1] == "aLamb_SWCA"):
            row[0] = "Alaina Lamb"
        elif (row[1] == "aPellegrini_SWCA"):
            row[0] = "Anne Pellegrini"
        elif (row[1] == "BRaulston@usbr.gov_USBR"):
            row[0] = "Barbara Raulston"
        elif (row[1] == "lsabin@usbr.gov_USBR"):
            row[0] = "Beth Sabin"
        elif (row[1] == "cronning@usbr.gov_USBR"):
            row[0] = "Carrie Ronning"
        elif (row[1] == "Need C_Dodges_ID"):
            row[0] = "Chris Dodge"
        elif (row[1] == "GCummins_LCR"):
            row[0] = "George Cummins"
        elif (row[1] == "JHill@usbr.gov_USBR"):
            row[0] = "Jeff Hill"
        elif (row[1] == "JenealSmith@usbr.gov_USBR"):
            row[0] = "Jenny Smith"
        elif (row[1] == "jWebber_SWCA"):
            row[0] = "Julie Webber"
        elif (row[1] == "JKahl@usbr.gov_USBR"):
            row[0] = "Joe Kahl"
        elif (row[1] == "jlyon@usbr.gov_USBR"):
            row[0] = "Joe Lyon"
        elif (row[1] == "mMcLeod_SWCA"):
            row[0] = "Mary Anne McLeod"
        elif (row[1] == "qYeates_SWCA"):
            row[0] = "Quick Yeates"        
        elif (row[1] == "sDougill_SWCA"):
            row[0] = "Steve Dougill"
        elif (row[1] == "Needs S_Nichols_ID"):
            row[0] = "Sarah Nichols"
        elif (row[1] == "tHinckley_SWCA"):
            row[0] = "Trevor Hinckley"
        elif (row[1] == "vHaworth_SWCA"):
            row[0] = "Val Haworth"
        elif (row[1] == "zEmery_SWCA"):
            row[0] = "Zach Emery"
        elif (row[1] == "mstandart"):
            row[0] = "Michael Standart"        
        # Update the cursor with the updated list
        cursor.updateRow(row)
# Create update cursor for feature class 
with arcpy.da.UpdateCursor(WIFL_Detection, fields) as cursor:
    for row in cursor:
        if (row[1] == "aLamb_SWCA"):
            row[0] = "Alaina Lamb"
        elif (row[1] == "aPellegrini_SWCA"):
            row[0] = "Anne Pellegrini"
        elif (row[1] == "BRaulston@usbr.gov_USBR"):
            row[0] = "Barbara Raulston"
        elif (row[1] == "lsabin@usbr.gov_USBR"):
            row[0] = "Beth Sabin"
        elif (row[1] == "cronning@usbr.gov_USBR"):
            row[0] = "Carrie Ronning"
        elif (row[1] == "Need C_Dodges_ID"):
            row[0] = "Chris Dodge"
        elif (row[1] == "GCummins_LCR"):
            row[0] = "George Cummins"
        elif (row[1] == "JHill@usbr.gov_USBR"):
            row[0] = "Jeff Hill"
        elif (row[1] == "JenealSmith@usbr.gov_USBR"):
            row[0] = "Jenny Smith"
        elif (row[1] == "jWebber_SWCA"):
            row[0] = "Julie Webber"
        elif (row[1] == "JKahl@usbr.gov_USBR"):
            row[0] = "Joe Kahl"
        elif (row[1] == "jlyon@usbr.gov_USBR"):
            row[0] = "Joe Lyon"
        elif (row[1] == "mMcLeod_SWCA"):
            row[0] = "Mary Anne McLeod"
        elif (row[1] == "qYeates_SWCA"):
            row[0] = "Quick Yeates"        
        elif (row[1] == "sDougill_SWCA"):
            row[0] = "Steve Dougill"
        elif (row[1] == "Needs S_Nichols_ID"):
            row[0] = "Sarah Nichols"
        elif (row[1] == "tHinckley_SWCA"):
            row[0] = "Trevor Hinckley"
        elif (row[1] == "vHaworth_SWCA"):
            row[0] = "Val Haworth"
        elif (row[1] == "zEmery_SWCA"):
            row[0] = "Zach Emery"
        elif (row[1] == "mstandart"):
            row[0] = "Michael Standart"        
        # Update the cursor with the updated list
        cursor.updateRow(row)