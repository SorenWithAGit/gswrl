import pandas as pd
import read_data as rd
import calculations as cal
import glob
from pathlib import Path

class date_range:
    # function to create DataFrame of dates within range
    def generate_dates(start_date: str, end_date: str):
        date_range = pd.date_range(start = start_date, end = end_date)
        date_df = pd.DataFrame({"Date" : date_range})
        return date_df

# test_isco = rd.sampler_data.read_raw_volumes(r"I:\USDA-ARS\Doug Smith\Riesel\Water Quaility\ISCO Raw\2025\Y8\2025_Y8_325.txt")
# print(test_isco)

# # Create paths to folders and lab data.
root = r"I:\USDA-ARS\Doug Smith\Riesel\Water Quaility\ISCO Raw\2025"
# lab_data_path = r"I:\USDA-ARS\Doug Smith\Riesel\Water Quaility\raw_data\wq_raw_data_2025.xlsx"

# # Collect subfolders.
isco_path = Path(root)
folder_names = [path.name for path in isco_path.glob("*") if path.is_dir()]

cols = ["Site", "Date", "Units", "Sample", "bottle",
                "Time", "Level (ft)", "Flow Rate (cfs)", 
                "Total Flow (cf)"]
isco_dfs = []

# # Get Individual Folders
for folder in folder_names:
    sampler_path = root + "\\" + folder
    sampler_files = glob.glob(str(sampler_path) + "//" + "*.txt", recursive = True)
    isco_df = pd.DataFrame(columns = cols)

#     # Read each file in folder and concat dataframes
    for file in sampler_files:
        print("File Path: " + file)
        run_isco = rd.sampler_data.read_raw_volumes(file)
        if not run_isco.empty:
            isco_df = pd.concat([isco_df, run_isco]).reset_index(drop = True)
            isco_dfs.append(isco_df)
        print(isco_df)

# for df in isco_dfs:
#     print(df)

# # Create dictionary of DataFrames from list.
isco_dataframes = {
    "SW12" : isco_dfs[0],
    "SW17" : isco_dfs[1],
    "W1" : isco_dfs[2],
    "W6" : isco_dfs[6],
    "W10" : isco_dfs[3],
    "W12" : isco_dfs[4],
    "W13" : isco_dfs[5],
    "Y2" : isco_dfs[10],
    "Y6" : isco_dfs[11],
    "Y8" : isco_dfs[12],
    "Y10" : isco_dfs[7],
    "Y13" : isco_dfs[8],
    "Y14" : isco_dfs[9]
}

for field, df in isco_dataframes.items():
    print(df)

############################################################

# Create lists to append dataframes to.
# sampler_dfs = []
# storm_dfs = []

# # Read files into pandas DataFrames and append to list.
# for folder in folder_names:
#     sampler_path = root + "\\" + folder
#     sampler_files = glob.glob(str(sampler_path) + "//" + "*.txt", recursive = True)
#     sampler_data = pd.DataFrame(columns = ["Site", "Date", "Units", "# of Samples",
#                                         "Start Volume", "End Volume"]).astype({"Site" : "str", "Date" : "str", "Units" : "str", 
#                                           "# of Samples" : "int", "Start Volume" : "float", 
#                                           "End Volume" : "float"})
#     for file in sampler_files:
#         print("File Path: " + file)
#         sampler_df = rd.sampler_data.read_total_vol(file)
#         sampler_data = pd.concat([sampler_data, sampler_df]).reset_index(drop = True)
        
#     sampler_data["Date"] = pd.to_datetime(sampler_data["Date"])
#     sampler_data["Date"] = sampler_data["Date"].dt.strftime("%m-%d-%Y")
#     # print(sampler_data)
#     sampler_dfs.append(sampler_data)

# # Create dictionary of DataFrames from list.
# dataframes = {
#     "SW12" : sampler_dfs[0],
#     "SW17" : sampler_dfs[1],
#     "W1" : sampler_dfs[2],
#     "W6" : sampler_dfs[6],
#     "W10" : sampler_dfs[3],
#     "W12" : sampler_dfs[4],
#     "W13" : sampler_dfs[5],
#     "Y2" : sampler_dfs[10],
#     "Y6" : sampler_dfs[11],
#     "Y8" : sampler_dfs[12],
#     "Y10" : sampler_dfs[7],
#     "Y13" : sampler_dfs[8],
#     "Y14" : sampler_dfs[9]
# }


# for field, df in dataframes.items():
#     # calculate total volumes.
#     storm_df = dataframes[field]
#     c = cal.conversions()
#     v_ft3 = c.total_vol_ft3(storm_df)
#     storm_df["Total Volume (ft3)"] = v_ft3

#     # convert from cubic feet to mm.
#     v_mm = c.ft3_to_mm(storm_df)
#     storm_df["Total Volume (mm)"] = v_mm
#     storm_df["Date"] = pd.to_datetime(storm_df["Date"])

#     # storm_df.set_index("Date").asfreq("D").reset_index()
#     # storm_df = storm_df.set_index("Date").resample("D").sum().reset_index()
#     storm_dfs.append(storm_df)

# fields = [
#      "SW12", "SW17", "W1",
#      "W6", "W10", "W12",
#      "W13", "Y2", "Y6",
#      "Y8", "Y10", "Y13",
#      "Y14"
# ]

# runoff_dfs = []

# for f, fld in enumerate(fields):
#     date_df = pd.DataFrame()
#     date_df = date_range.generate_dates("2025-01-01", "2025-12-31")
#     runoff = pd.merge(storm_dfs[f], date_df, on = ["Date"], how = "outer").sort_values("Date")
#     runoff_dfs.append(runoff)

# with pd.ExcelWriter(r"I:\USDA-ARS\Merillyn Schantz\Riesel\Riesel Runoff\2025_isco_(Runoff).xlsx") as writer:
#     for i, field in enumerate(fields):
#         dataframe = runoff_dfs[i]
#         dataframe["Date"] = dataframe["Date"].dt.strftime("%Y-%m-%d")
#         print(dataframe)
#         dataframe.to_excel(writer, sheet_name = field, index = False)

