import pandas as pd
import read_data as rd
import calculations as cal
import glob
from pathlib import Path

pd.options.mode.copy_on_write = True


# Create paths to folders and lab data.
root = r"I:\USDA-ARS\Doug Smith\Riesel\Water Quaility\ISCO Raw\2025"
lab_data_path = r"I:\USDA-ARS\Doug Smith\Riesel\Water Quaility\2025\2025 Riesel Water Quality.xlsx"

# Collect subfolders.
isco_path = Path(root)
folder_names = [path.name for path in isco_path.glob("*") if path.is_dir()]

# Create lists to append dataframes to.
sampler_dfs = []
storm_dfs = []
acid_storm_dfs = []

# Read files into pandas DataFrames and append to list.
for folder in folder_names:
    sampler_path = root + "\\" + folder
    sampler_files = glob.glob(str(sampler_path) + "//" + "*.txt", recursive = True)
    sampler_data = pd.DataFrame(columns = ["Site", "Date", "Units", "# of Samples",
                                        "Start Volume", "End Volume"])
    for file in sampler_files:
    # print("File Path: " + file)
        sampler_df = rd.sampler_data.read_txt(file)
        sampler_data = pd.concat([sampler_data, sampler_df]).reset_index(drop = True)
    # print(sampler_data)
    sampler_dfs.append(sampler_data)

# Create dictionary of DataFrames from list.
dataframes = {
    "SW12" : sampler_dfs[0],
    "SW17" : sampler_dfs[1],
    "W1" : sampler_dfs[2],
    "W6" : sampler_dfs[6],
    "W10" : sampler_dfs[3],
    "W12" : sampler_dfs[4],
    "W13" : sampler_dfs[5],
    "Y2" : sampler_dfs[10],
    "Y6" : sampler_dfs[11],
    "Y8" : sampler_dfs[12],
    "Y10" : sampler_dfs[7],
    "Y13" : sampler_dfs[8],
    "Y14" : sampler_dfs[9]
}

# Write each DataFrame to new sheet in excel

with pd.ExcelWriter(r"I:\USDA-ARS\Doug Smith\Riesel\Water Quaility\ISCO Raw\2025\2025_ISCO_Sampler_data.xlsx") as writer:
    for sheet_name, dataframe in dataframes.items():
        dataframe.to_excel(writer, sheet_name = sheet_name, index = False)


# Join Nutrient Data and carry out conversions and calculations
for field, df in dataframes.items():
    
    # calculate total volumes.
    storm_df = rd.lab_data.storm_data(lab_data_path, dataframes[field])
    c = cal.conversions()
    v_ft3 = c.total_vol_ft3(storm_df)
    storm_df["Total Volume (ft3)"] = v_ft3

    # convert from cubic feet to mm.
    v_mm = c.ft3_to_mm(storm_df)
    storm_df["Total Volume (mm)"] = v_mm

    # calculate loads.
    kg_ha = c.kg_per_ha(storm_df)

    # calculate load for NO3 for sample #1 & #2 and average.
    storm_df["NO3-N [kg/ha] Sample #1"] = kg_ha[0]
    storm_df["NO3-N [kg/ha] Sample #2"] = kg_ha[1]
    storm_df["NO3-N [kg/ha] avg"] = kg_ha[2]

    # calculate load for NH3 for sample #1 & #2 and average.
    storm_df["NH3-N [kg/ha] Sample #1"] = kg_ha[3]
    storm_df["NH3-N [kg/ha] Sample #2"] = kg_ha[4]
    storm_df["NH3-N [kg/ha] avg"] = kg_ha[5]

    # calculate load for PO4 for sample #1 & #2 and average.
    storm_df["PO4-P [kg/ha] Sample #1"] = kg_ha[6]
    storm_df["PO4-P [kg/ha] Sample #2"] = kg_ha[7]
    storm_df["PO4-P [kg/ha] avg"] = kg_ha[8]

    # print(storm_df[["Site", "Date", "Units", "# of Samples", "Start Volume", "End Volume", "Total Volume (ft3)", "Total Volume (mm)", \
    #                 "NO3-N [kg/ha] avg", "NH3-N [kg/ha] avg", "PO4-P [kg/ha] avg"]])

    print(storm_df[["Site", "Date", "Units", "# of Samples", "Start Volume", "End Volume", "Total Volume (ft3)", "Total Volume (mm)", \
                    "NO3-N [kg/ha] Sample #1", "NO3-N [kg/ha] Sample #2", "NO3-N [kg/ha] avg"]])

    # organize columns.
    storm_df = storm_df[["Site", "Date", "Units", "# of Samples", "Start Volume", "End Volume", "Total Volume (ft3)", "Total Volume (mm)", \
                        "NO3-N [mg N/liter] smpl 1", "NO3-N [mg N/liter] smpl 2", "NO3-N [mg N/liter] avg", "NH3-N [mg N/liter] smpl 1", \
                            "NH3-N [mg N/liter] smpl 2", "NH3-N [mg N/liter] avg", "PO4-P [mg P/liter] smpl 1", "PO4-P [mg P/liter] smpl 2", \
                                "PO4-P [mg P/liter] avg", "NO3-N [kg/ha] Sample #1", "NO3-N [kg/ha] Sample #2", "NO3-N [kg/ha] avg", \
                                "NH3-N [kg/ha] Sample #1", "NH3-N [kg/ha] Sample #2", "NH3-N [kg/ha] avg", "PO4-P [kg/ha] Sample #1", \
                                "PO4-P [kg/ha] Sample #2", "PO4-P [kg/ha] avg"]]
    storm_dfs.append(storm_df)


# Join Acidified Nutrient Samples and carry out conversions and calculations.
for site, df in dataframes.items():

    # calculate total volumes.
    acid_storm_df = rd.lab_data.acid_data(lab_data_path, dataframes[site])
    c = cal.conversions()
    v_ft3 = c.total_vol_ft3(acid_storm_df)
    acid_storm_df["Total Volume (ft3)"] = v_ft3

    # convert from cubic feet to mm.
    v_mm = c.ft3_to_mm(acid_storm_df)
    acid_storm_df["Total Volume (mm)"] = v_mm

    # calculate loads.
    kg_ha = c.kg_per_ha(acid_storm_df)

    # calculate load for NO3 for sample #1 & #2 and average.
    acid_storm_df["NO3-N [kg/ha] Sample #1"] = kg_ha[0]
    acid_storm_df["NO3-N [kg/ha] Sample #2"] = kg_ha[1]
    acid_storm_df["NO3-N [kg/ha] avg"] = kg_ha[2]

    # calculate load for NH3 for sample #1 & #2 and average.
    acid_storm_df["NH3-N [kg/ha] Sample #1"] = kg_ha[3]
    acid_storm_df["NH3-N [kg/ha] Sample #2"] = kg_ha[4]
    acid_storm_df["NH3-N [kg/ha] avg"] = kg_ha[5]

    # calculate load for PO4 for sample #1 & #2 and average.
    acid_storm_df["PO4-P [kg/ha] Sample #1"] = kg_ha[6]
    acid_storm_df["PO4-P [kg/ha] Sample #2"] = kg_ha[7]
    acid_storm_df["PO4-P [kg/ha] avg"] = kg_ha[8]

    # print(acid_storm_df[["Site", "Date", "Units", "# of Samples", "Start Volume", "End Volume", "Total Volume (ft3)", "Total Volume (mm)", \
    #                 "NO3-N [kg/ha] avg", "NH3-N [kg/ha] avg", "PO4-P [kg/ha] avg"]])
    print(acid_storm_df[["Site", "Date", "Units", "# of Samples", "Start Volume", "End Volume", "Total Volume (ft3)", "Total Volume (mm)", \
                         "NO3-N [kg/ha] Sample #1", "NO3-N [kg/ha] Sample #2", "NO3-N [kg/ha] avg"]])

    # organize columns.
    acid_storm_df = acid_storm_df[["Site", "Date", "Units", "# of Samples", "Start Volume", "End Volume", "Total Volume (ft3)", "Total Volume (mm)", \
                        "NO3-N [mg N/liter] smpl 1", "NO3-N [mg N/liter] smpl 2", "NO3-N [mg N/liter] avg", "NH3-N [mg N/liter] smpl 1", \
                            "NH3-N [mg N/liter] smpl 2", "NH3-N [mg N/liter] avg", "PO4-P [mg P/liter] smpl 1", "PO4-P [mg P/liter] smpl 2", \
                                "PO4-P [mg P/liter] avg", "NO3-N [kg/ha] Sample #1", "NO3-N [kg/ha] Sample #2", "NO3-N [kg/ha] avg", \
                                "NH3-N [kg/ha] Sample #1", "NH3-N [kg/ha] Sample #2", "NH3-N [kg/ha] avg", "PO4-P [kg/ha] Sample #1", \
                                "PO4-P [kg/ha] Sample #2", "PO4-P [kg/ha] avg"]]
    acid_storm_dfs.append(acid_storm_df)

# Create dictionary of storm DataFrames.
storm_dataframes = {
    "SW12" : storm_dfs[0],
    "SW17" : storm_dfs[1],
    "W1" : storm_dfs[2],
    "W6" : storm_dfs[6],
    "W10" : storm_dfs[3],
    "W12" : storm_dfs[4],
    "W13" : storm_dfs[5],
    "Y2" : storm_dfs[10],
    "Y6" : storm_dfs[11],
    "Y8" : storm_dfs[12],
    "Y10" : storm_dfs[7],
    "Y13" : storm_dfs[8],
    "Y14" : storm_dfs[9]
}

# Create dictionary of acid_storm DataFrames.
acid_storm_dataframes = {
    "SW12" : acid_storm_dfs[0],
    "SW17" : acid_storm_dfs[1],
    "W1" : acid_storm_dfs[2],
    "W6" : acid_storm_dfs[6],
    "W10" : acid_storm_dfs[3],
    "W12" : acid_storm_dfs[4],
    "W13" : acid_storm_dfs[5],
    "Y2" : acid_storm_dfs[10],
    "Y6" : acid_storm_dfs[11],
    "Y8" : acid_storm_dfs[12],
    "Y10" : acid_storm_dfs[7],
    "Y13" : acid_storm_dfs[8],
    "Y14" : acid_storm_dfs[9]
}


#Write each storm DataFrame to new sheet in excel

# with pd.ExcelWriter(r"I:\USDA-ARS\Doug Smith\Riesel\Water Quaility\ISCO Raw\2025\2025_ISCO_Calulated_Nutrient_Data.xlsx") as writer:
#     for sheet_name, dataframe in storm_dataframes.items():
#         dataframe.to_excel(writer, sheet_name = sheet_name, index = False)

# # Write each acid_storm DataFrame to new sheet in excel

# with pd.ExcelWriter(r"I:\USDA-ARS\Doug Smith\Riesel\Water Quaility\ISCO Raw\2025\2025_ISCO_Calulated_Acid_Nutrient_Data.xlsx") as writer:
#     for sheet_name, dataframe in acid_storm_dataframes.items():
#         dataframe.to_excel(writer, sheet_name = sheet_name, index = False)

