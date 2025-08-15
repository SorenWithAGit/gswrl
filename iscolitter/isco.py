import pandas as pd
import read_sampler as rs
import calculations as cal
import read_lab_data as rld
import glob

pd.options.mode.copy_on_write = True

sampler_data = pd.DataFrame(columns = ["Site", "Date", "Units", "# of Samples",
                                      "Start Volume", "End Volume"])

sampler_path = r"I:\USDA-ARS\Doug Smith\Riesel\Water Quaility\ISCO Raw\2018\W1"
sampler_files = glob.glob(str(sampler_path) + "//" + "*" + ".txt", recursive = True)

for file in sampler_files:
    sampler_df = rs.read_txt(file)
    sampler_data = pd.concat([sampler_data, sampler_df]).reset_index(drop = True)
print(sampler_data)

lab_data_path = r"I:\USDA-ARS\Doug Smith\Riesel\Water Quaility\raw_data\2018\wq_raw_data_2018.xlsx"

storm_df = rld.storm_data(lab_data_path, sampler_data)

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

storm_df = storm_df[["Site", "Date", "Units", "# of Samples", "Start Volume", "End Volume", "Total Volume (ft3)", "Total Volume (mm)", \
                     "NO3-N [mg N/liter] smpl 1", "NO3-N [mg N/liter] smpl 2", "NO3-N [mg N/liter] avg", "NH3-N [mg N/liter] smpl 1", \
                        "NH3-N [mg N/liter] smpl 2", "NH3-N [mg N/liter] avg", "PO4-P [mg P/liter] smpl 1", "PO4-P [mg P/liter] smpl 2", \
                            "PO4-P [mg P/liter] avg", "NO3-N [kg/ha] Sample #1", "NO3-N [kg/ha] Sample #2", "NO3-N [kg/ha] avg", \
                            "NH3-N [kg/ha] Sample #1", "NH3-N [kg/ha] Sample #2", "NH3-N [kg/ha] avg", "PO4-P [kg/ha] Sample #1", \
                            "PO4-P [kg/ha] Sample #2", "PO4-P [kg/ha] avg"]]

with pd.ExcelWriter(r"I:\USDA-ARS\Doug Smith\Riesel\Water Quaility\2018\2018_isco_calculations.xlsx") as writer:
    storm_df.to_excel(writer, sheet_name = "W1", index = False)

acid_df = rld.acid_data(lab_data_path, sampler_data)

ca = cal.conversions()
acid_v_ft3 = ca.total_vol_ft3(acid_df)
acid_df["Total Volume (ft3)"] = acid_v_ft3

acid_v_mm = ca.ft3_to_mm(acid_df)
acid_df["Total Volume (mm)"] = acid_v_mm

acid_kg_ha = ca.kg_per_ha(acid_df)
acid_df["NO3-N [kg/ha] Sample #1"] = acid_kg_ha[0]
acid_df["NO3-N [kg/ha] Sample #2"] = acid_kg_ha[1]
acid_df["NO3-N [kg/ha] avg"] = acid_kg_ha[2]

acid_df["NH3-N [kg/ha] Sample #1"] = acid_kg_ha[3]
acid_df["NH3-N [kg/ha] Sample #2"] = acid_kg_ha[4]
acid_df["NH3-N [kg/ha] avg"] = acid_kg_ha[5]

acid_df["PO4-P [kg/ha] Sample #1"] = acid_kg_ha[6]
acid_df["PO4-P [kg/ha] Sample #2"] = acid_kg_ha[7]
acid_df["PO4-P [kg/ha] avg"] = acid_kg_ha[8]

print(acid_df[["Site", "Date", "Units", "# of Samples", "Start Volume", "End Volume", "Total Volume (ft3)", "Total Volume (mm)", \
                "NO3-N [kg/ha] avg", "NH3-N [kg/ha] avg", "PO4-P [kg/ha] avg"]])

acid_df = storm_df[["Site", "Date", "Units", "# of Samples", "Start Volume", "End Volume", "Total Volume (ft3)", "Total Volume (mm)", \
                     "NO3-N [mg N/liter] smpl 1", "NO3-N [mg N/liter] smpl 2", "NO3-N [mg N/liter] avg", "NH3-N [mg N/liter] smpl 1", \
                        "NH3-N [mg N/liter] smpl 2", "NH3-N [mg N/liter] avg", "PO4-P [mg P/liter] smpl 1", "PO4-P [mg P/liter] smpl 2", \
                            "PO4-P [mg P/liter] avg", "NO3-N [kg/ha] Sample #1", "NO3-N [kg/ha] Sample #2", "NO3-N [kg/ha] avg", \
                            "NH3-N [kg/ha] Sample #1", "NH3-N [kg/ha] Sample #2", "NH3-N [kg/ha] avg", "PO4-P [kg/ha] Sample #1", \
                            "PO4-P [kg/ha] Sample #2", "PO4-P [kg/ha] avg"]]

# with pd.ExcelWriter(r"I:\USDA-ARS\Doug Smith\Riesel\Water Quaility\2018\2018_isco_calculations.xlsx") as writer:
#     storm_df.to_excel(writer, sheet_name = "SW12", index = False)
#     row_start_acid_storm = len(storm_df) + 3
#     acid_df.to_excel(writer, sheet_name = "SW12", startrow = row_start_acid_storm, index = False)

with pd.ExcelWriter(r"I:\USDA-ARS\Doug Smith\Riesel\Water Quaility\2018\2018_isco_acid_calculations.xlsx") as writer:
    acid_df.to_excel(writer, sheet_name = "W1", index = False)