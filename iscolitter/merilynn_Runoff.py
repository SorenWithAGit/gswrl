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

# # # Create paths to folders and lab data.
# root = r"I:\USDA-ARS\Doug Smith\Riesel\Water Quaility\ISCO Raw\2019"


# # # Collect subfolders.
# isco_path = Path(root)
# folder_names = [path.name for path in isco_path.glob("*") if path.is_dir()]

# cols = ["Site", "Date", "Units", "Sample", "bottle",
#                 "Time", "Level (ft)", "Flow Rate (cfs)", 
#                 "Total Flow (cf)"]
# isco_dfs = []

# # # Get Individual Folders
# for folder in folder_names:
#     sampler_path = root + "\\" + folder
#     sampler_files = glob.glob(str(sampler_path) + "//" + "*.txt", recursive = True)
#     isco_df = pd.DataFrame(columns = cols)

# #     # Read each file in folder and concat dataframes
#     for file in sampler_files:
#         # print("File Path: " + file)
#         run_isco = rd.sampler_data.read_raw_volumes(file)
#         if not run_isco.empty:
#             isco_df = pd.concat([isco_df, run_isco]).reset_index(drop = True)
#     isco_dfs.append(isco_df)
#     # print(isco_df)

# # for df in isco_dfs:
# #     print(df)

# # print(len(isco_dfs))

# # # Create dictionary of DataFrames from list.
# isco_dataframes = {
#     "SW12" : isco_dfs[0],
#     "SW17" : isco_dfs[1],
#     "W1" : isco_dfs[2],
#     "W6" : isco_dfs[6],
#     "W10" : isco_dfs[3],
#     "W12" : isco_dfs[4],
#     "W13" : isco_dfs[5],
#     "Y2" : isco_dfs[10],
#     "Y6" : isco_dfs[11],
#     "Y8" : isco_dfs[12],
#     "Y10" : isco_dfs[7],
#     "Y13" : isco_dfs[8],
#     "Y14" : isco_dfs[9]
# }

# # for field, df in isco_dataframes.items():
# #     print(df)

# fields = [
#     "SW12", "SW17", "W1",
#     "W6", "W10", "W12",
#     "W13", "Y2", "Y6",
#     "Y8", "Y10", "Y13",
#     "Y14"
# ]
# c = cal.conversions()
# dly_rnoff = []

# for i, field in enumerate(fields):
#     df = isco_dataframes[field]
#     df["Datetime"] = pd.to_datetime(df["Date"] + " " + df["Time"])
#     df = df.iloc[:, [0, 9, 2, 3, 4, 6, 7, 8]]
#     daily_raw = c.raw_sampler_to_daily(df)
#     # print(daily_raw)
#     daily_t_vol = c.total_vol_ft3(daily_raw)
#     # print(daily_t_vol)
#     daily_raw["Total Volume (ft3)"] = daily_t_vol
#     mm = c.ft3_to_mm(daily_raw)
#     daily_raw["Total Volume (mm)"] = mm
#     daily_raw = daily_raw.iloc[:, [1, 0, 4, 5, 6]]
#     daily_raw.set_index("Datetime", inplace = True)
#     all_dates = pd.date_range(start = "2019-01-01", end = "2019-12-31", freq = "D").normalize()
#     daily_raw = daily_raw.reindex(all_dates)
#     daily_raw["Site"] = field
#     daily_raw = daily_raw.fillna(0)
#     dly_rnoff.append(daily_raw)
#     print(daily_raw)

# daily_runoffs = {
#     "SW12" : dly_rnoff[0],
#     "SW17" : dly_rnoff[1],
#     "W1" : dly_rnoff[2],
#     "W6" : dly_rnoff[6],
#     "W10" : dly_rnoff[3],
#     "W12" : dly_rnoff[4],
#     "W13" : dly_rnoff[5],
#     "Y2" : dly_rnoff[10],
#     "Y6" : dly_rnoff[11],
#     "Y8" : dly_rnoff[12],
#     "Y10" : dly_rnoff[7],
#     "Y13" : dly_rnoff[8],
#     "Y14" : dly_rnoff[9]
# }

# with pd.ExcelWriter(r"I:\USDA-ARS\Merillyn Schantz\Riesel\Riesel Runoff\calculated_runoff\2019_calculated_isco_(Runoff).xlsx") as writer:
#     for i, field in enumerate(fields):
#         dataframe = daily_runoffs[field]
#         dataframe.to_excel(writer, sheet_name = field, index = True)

############################################################



runoff_path = r"I:\USDA-ARS\Georgie\runoff\2019\y2_2019.xls"
web_runoff = r"I:\USDA-ARS\Georgie\runoff\2019\daily_inches\y2\roy219.dly"
calcd = rd.calculated_data
df = calcd.read_subdly_runoff(runoff_path)
webro = calcd.read_txt_runoff(web_runoff)
webro["in"] = webro["in"].astype(float)
# print(webro)
# print(df["level (ft)"].shape)

rc = cal.runoff_calculator()
time = 10
new_df = rc.flow_calculator("Y2", time,  df)
# new_df["runoff (in)"] = new_df["new in/hr"] * .817
new_df["date"] = pd.to_datetime(new_df[["year", "month", "day"]])
# print(new_df)
daily_df = new_df.iloc[:, [0, 11, 4, 5, 6, 8, 7, 9, 10]]
# print(daily_df)

flow_sum = daily_df.set_index("date").resample("D")[["flow (in/hr)"]].sum()
# print(flow_sum)

t = rc.calculate_delta_t(webro, flow_sum)
# print(t)
t["daily (in)"] = t["flow (in/hr)"] * t["delta_t"]
average_t = t[t["delta_t"] != 0]["delta_t"].mean()
# print(average_t)

daily_df["runoff (in)"] = daily_df["new in/hr"] * (time/60)
daily_df = daily_df.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 9, 8]]
print(daily_df)

runoff_sum = daily_df.set_index("date").resample("D")["runoff (in)"].sum()
jskt_runoff = daily_df.set_index("date").resample("D")["JSKT runoff (mm)"].sum()
# print(jskt_runoff)

comparison_runoff = pd.merge(webro, runoff_sum, on = "date")
comparison_runoff = pd.merge(comparison_runoff, t, on = "date")
# print(comparison_runoff)

comparison_runoff["georgie runoff (mm)"] = comparison_runoff["in_x"] * 25.4

comparison_runoff = pd.merge(comparison_runoff, jskt_runoff, on = "date")

comparison_runoff = comparison_runoff.iloc[:, [0, 1, 7, 4, 2, 8, 9, 10]]
comparison_runoff = comparison_runoff.rename(columns = {"site_x" : "site",
                                                        "delta_t": "calculated time (hr)",
                                                        "in_x" : "georgie runoff (in)", 
                                                        "daily (in)" : "recalculated georgie (in)"})
comparison_runoff["georgie:john"] = comparison_runoff["georgie runoff (mm)"] / comparison_runoff["JSKT runoff (mm)"]
print(comparison_runoff)



with pd.ExcelWriter(r"I:\USDA-ARS\Merillyn Schantz\Riesel\Riesel Runoff\calculated_runoff\daily\y2_2019.xlsx") as writer:
    daily_df.to_excel(writer, sheet_name = "y2 2017 subdaily", index = True)
    comparison_runoff.to_excel(writer, sheet_name = "y2 2017 daily", index = True)