import pandas as pd
import read_sampler as rs
import calculations as cal
import read_lab_data as rld
import glob

pd.options.mode.copy_on_write = True

sampler_data = pd.DataFrame(columns = ["Site", "Date", "Units", "# of Samples",
                                      "Start Volume", "End Volume"])

sampler_path = r"I:\programming\python\gswrl\iscolitter\05-08-2019"
sampler_files = glob.glob(str(sampler_path) + "//" + "*" + ".txt", recursive = True)

for file in sampler_files:
    sampler_df = rs.read_txt(file)
    sampler_data = pd.concat([sampler_data, sampler_df]).reset_index(drop = True)
# print(sampler_data)

lab_data_path = r"I:\USDA-ARS\Doug Smith\Riesel\Water Quaility\raw_data\2019\wq_nutrients_2019.xlsx"

storm_df = rld.storm_data(lab_data_path, sampler_data)[0]

c = cal.conversions()
v_ft3 = c.total_vol_ft3(storm_df)
storm_df["Total Volume (ft3)"] = v_ft3

v_mm = c.ft3_to_mm(storm_df)
storm_df["Total Volume (mm)"] = v_mm

kg_ha = c.kg_per_ha(storm_df)
storm_df["NO3-N [kg/ha] Sample #1"] = kg_ha[0]
storm_df["NO3-N [kg/ha] Sample #2"] = kg_ha[1]
storm_df["NO3-N [kg/ha] avg"] = kg_ha[2]

storm_df["NH3-N [kg/ha] Sample #1"] = kg_ha[3]
storm_df["NH3-N [kg/ha] Sample #2"] = kg_ha[4]
storm_df["NH3-N [kg/ha] avg"] = kg_ha[5]

storm_df["PO4-P [kg/ha] Sample #1"] = kg_ha[6]
storm_df["PO4-P [kg/ha] Sample #2"] = kg_ha[7]
storm_df["PO4-P [kg/ha] avg"] = kg_ha[8]

print(storm_df[["Site", "Date", "Units", "# of Samples", "Start Volume", "End Volume", "Total Volume (ft3)", "Total Volume (mm)", \
                "NO3-N [kg/ha] avg", "NH3-N [kg/ha] avg", "PO4-P [kg/ha] avg"]])
