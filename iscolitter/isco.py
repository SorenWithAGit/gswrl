import pandas as pd
import read_sampler as rs
import calculations as cal
import glob

sampler_data = pd.DataFrame(columns = ["Site", "Date", "Units", "# of Samples",
                                      "Start Volume", "End Volume", "Total Volume"])

sampler_path = r"I:\programming\python\gswrl\iscolitter\05-08-2019"
sampler_files = glob.glob(str(sampler_path) + "//" + "*" + ".txt", recursive = True)

for file in sampler_files:
    sampler_df = rs.read_txt(file)
    sampler_data = pd.concat([sampler_data, sampler_df]).reset_index(drop = True)
print(sampler_data)

lab_data = pd.read_excel(r"I:\USDA-ARS\Doug Smith\Riesel\Water Quaility\raw_data\2019\wq_nutrients_2019.xlsx")
lab_data["Sample Date"] = lab_data["Sample Date"].dt.strftime("%m-%d-%Y")

nutrient_data = lab_data[lab_data["Sample Type"] == "N"]
rep_lst = []
for ind in nutrient_data.index:
    rep = nutrient_data["Sample Name"][ind].split(" ")[1]
    rep_lst.append(rep)
nutrient_data["Replicate"] = rep_lst

nutrient_acid_data = lab_data[lab_data["Sample Type"] == "NutAcid"]
na_rep_lst = []
for index in nutrient_acid_data.index:
    na_rep = nutrient_acid_data["Sample Name"][index].split(" ")[1]
    na_rep_lst.append(na_rep)
nutrient_acid_data["Replicate"] = na_rep_lst

no3_lst_1 = []
nh3_lst_1 = []
po4_lst_1 = []

for i in sampler_data.index:
    for iter in nutrient_data.index:
        if sampler_data["Site"][i] == nutrient_data["Sample Name"][iter].split(" ")[0] \
            and sampler_data["Date"][i] == nutrient_data["Sample Date"][iter] and nutrient_data["Replicate"][iter] == "#1":
            # print(str(sampler_data["Site"][i]) + " Found! " + str(nutrient_data["Sample Name"][iter]) + " " + \
            #       str(nutrient_data["Sample Date"][iter]))
            no3_lst_1.append(nutrient_data["Nitrate Nitrite- Results[mg N/liter]"][iter])
            nh3_lst_1.append(nutrient_data["Ammonia- Results[mg N/liter]"][iter])
            po4_lst_1.append(nutrient_data["Phosphate- Results[mg P/liter]"][iter])

no3_lst_2 = []
nh3_lst_2 = []
po4_lst_2 = []

for i in sampler_data.index:
    for iter in nutrient_data.index:
        if sampler_data["Site"][i] == nutrient_data["Sample Name"][iter].split(" ")[0] \
            and sampler_data["Date"][i] == nutrient_data["Sample Date"][iter] and nutrient_data["Replicate"][iter] == "#2":
            # print(str(sampler_data["Site"][i]) + " Found! " + str(nutrient_data["Sample Name"][iter]) + " " + \
            #       str(nutrient_data["Sample Date"][iter]))
            no3_lst_2.append(nutrient_data["Nitrate Nitrite- Results[mg N/liter]"][iter])
            nh3_lst_2.append(nutrient_data["Ammonia- Results[mg N/liter]"][iter])
            po4_lst_2.append(nutrient_data["Phosphate- Results[mg P/liter]"][iter])

storm_df = sampler_data
storm_df["NO3-N [mg N/liter] smpl 1"] = no3_lst_1
storm_df["NH3-N [mg N/liter] smpl 1"] = nh3_lst_1
storm_df["PO4-P [mg P/liter] smpl 1"] = po4_lst_1
storm_df["NO3-N [mg N/liter] smpl 2"] = no3_lst_2
storm_df["NH3-N [mg N/liter] smpl 2"] = nh3_lst_2
storm_df["PO4-P [mg P/liter] smpl 2"] = po4_lst_2
storm_df["NO3-N [mg N/liter] avg"] = (storm_df["NO3-N [mg N/liter] smpl 1"] + storm_df["NO3-N [mg N/liter] smpl 2"]) / 2
storm_df["NH3-N [mg N/liter] avg"] = (storm_df["NH3-N [mg N/liter] smpl 1"] + storm_df["NH3-N [mg N/liter] smpl 2"]) / 2
storm_df["PO4-P [mg P/liter] avg"] = (storm_df["PO4-P [mg P/liter] smpl 1"] + storm_df["PO4-P [mg P/liter] smpl 2"]) / 2

acid_no3_lst_1 = []
acid_nh3_lst_1 = []
acid_po4_lst_1 = []

for id in sampler_data.index:
    for count in nutrient_acid_data.index:
        if sampler_data["Site"][id] == nutrient_acid_data["Sample Name"][count].split(" ")[0] \
            and sampler_data["Date"][id] == nutrient_acid_data["Sample Date"][count] and nutrient_acid_data["Replicate"][count] == "#1":
            # print(str(sampler_data["Site"][id]) + " Found! " + str(nutrient_acid_data["Sample Name"][count]) + " " + \
            #       str(nutrient_acid_data["Sample Date"][count]))
            acid_no3_lst_1.append(nutrient_acid_data["Nitrate Nitrite- Results[mg N/liter]"][count])
            acid_nh3_lst_1.append(nutrient_acid_data["Ammonia- Results[mg N/liter]"][count])
            acid_po4_lst_1.append(nutrient_acid_data["Phosphate- Results[mg P/liter]"][count])

acid_no3_lst_2 = []
acid_nh3_lst_2 = []
acid_po4_lst_2 = []

for id in sampler_data.index:
    for count in nutrient_acid_data.index:
        if sampler_data["Site"][id] == nutrient_acid_data["Sample Name"][count].split(" ")[0] \
            and sampler_data["Date"][id] == nutrient_acid_data["Sample Date"][count] and nutrient_acid_data["Replicate"][count] == "#2":
            # print(str(sampler_data["Site"][id]) + " Found! " + str(nutrient_data["Sample Name"][count]) + " " + \
            #       str(nutrient_data["Sample Date"][count]))
            acid_no3_lst_2.append(nutrient_acid_data["Nitrate Nitrite- Results[mg N/liter]"][count])
            acid_nh3_lst_2.append(nutrient_acid_data["Ammonia- Results[mg N/liter]"][count])
            acid_po4_lst_2.append(nutrient_acid_data["Phosphate- Results[mg P/liter]"][count])

acid_storm_df = sampler_data
acid_storm_df["NO3-N [mg N/liter] smpl 1"] = acid_no3_lst_1
acid_storm_df["NH3-N [mg N/liter] smpl 1"] = acid_nh3_lst_1
acid_storm_df["PO4-P [mg P/liter] smpl 1"] = acid_po4_lst_1
acid_storm_df["NO3-N [mg N/liter] smpl 2"] = acid_no3_lst_2
acid_storm_df["NH3-N [mg N/liter] smpl 2"] = acid_nh3_lst_2
acid_storm_df["PO4-P [mg P/liter] smpl 2"] = acid_po4_lst_2
acid_storm_df["NO3-N [mg N/liter] avg"] = (acid_storm_df["NO3-N [mg N/liter] smpl 1"] + acid_storm_df["NO3-N [mg N/liter] smpl 2"]) / 2
acid_storm_df["NH3-N [mg N/liter] avg"] = (acid_storm_df["NH3-N [mg N/liter] smpl 1"] + acid_storm_df["NH3-N [mg N/liter] smpl 2"]) / 2
acid_storm_df["PO4-P [mg P/liter] avg"] = (acid_storm_df["PO4-P [mg P/liter] smpl 1"] + acid_storm_df["PO4-P [mg P/liter] smpl 2"]) / 2

print(acid_storm_df)
