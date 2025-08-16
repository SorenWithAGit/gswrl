import pandas as pd

pd.options.mode.copy_on_write = True

def storm_data(file_path, sampler_data):
    lab_data = pd.read_excel(file_path)
    lab_data["Sample Date"] = lab_data["Sample Date"].dt.strftime("%m-%d-%Y")
    for entry in lab_data.index:
        if lab_data["Nitrate Nitrite- Results[mg N/liter]"][entry] < 0:
            lab_data.at[entry, "Nitrate Nitrite- Results[mg N/liter]"] = 0.05
        if lab_data["Ammonia- Results[mg N/liter]"][entry] < 0:
             lab_data.at[entry, "Ammonia- Results[mg N/liter]"] = 0.05
        if lab_data["Phosphate- Results[mg P/liter]"][entry] < 0:
             lab_data.at[entry, "Phosphate- Results[mg P/liter]"] = 0.05
              
    nutrient_data = lab_data[lab_data["Sample Type"] == "N"]
    rep_lst = []
    for ind in nutrient_data.index:
        rep = nutrient_data["Sample Name"][ind].split(" ")[1]
        rep_lst.append(rep)
    nutrient_data["Replicate"] = rep_lst

    no3_lst_1 = []
    nh3_lst_1 = []
    po4_lst_1 = []
    no3_lst_2 = []
    nh3_lst_2 = []
    po4_lst_2 = []
    storm_df = sampler_data

    for i in sampler_data.index:
        for iter in nutrient_data.index:
            if sampler_data["Site"][i] == nutrient_data["Sample Name"][iter].split(" ")[0] \
                and sampler_data["Date"][i] == nutrient_data["Sample Date"][iter] and nutrient_data["Replicate"][iter] == "#1":
                # print(str(sampler_data["Site"][i]) + " Found! " + str(nutrient_data["Sample Name"][iter]) + " " + \
                #       str(nutrient_data["Sample Date"][iter]))
                no3_lst_1.append(nutrient_data["Nitrate Nitrite- Results[mg N/liter]"][iter])
                nh3_lst_1.append(nutrient_data["Ammonia- Results[mg N/liter]"][iter])
                po4_lst_1.append(nutrient_data["Phosphate- Results[mg P/liter]"][iter])
                no3_lst_2.append("NaN")
                nh3_lst_2.append("NaN")
                po4_lst_2.append("NaN")
    storm_df["NO3-N [mg N/liter] smpl 1"] = no3_lst_1
    storm_df["NH3-N [mg N/liter] smpl 1"] = nh3_lst_1
    storm_df["PO4-P [mg P/liter] smpl 1"] = po4_lst_1
    storm_df["NO3-N [mg N/liter] smpl 2"] = no3_lst_2
    storm_df["NH3-N [mg N/liter] smpl 2"] = nh3_lst_2
    storm_df["PO4-P [mg P/liter] smpl 2"] = po4_lst_2


    for i in storm_df.index:
        for iter in nutrient_data.index:
                        if storm_df["Site"][i] == nutrient_data["Sample Name"][iter].split(" ")[0] \
                            and storm_df["Date"][i] == nutrient_data["Sample Date"][iter] and nutrient_data["Replicate"][iter] == "#2":
                            # print(str(sampler_data["Site"][i]) + " Found! " + str(nutrient_data["Sample Name"][iter]) + " " + \
                            #       str(nutrient_data["Sample Date"][iter]))
                            storm_df.at[i, "NO3-N [mg N/liter] smpl 2"] = nutrient_data["Nitrate Nitrite- Results[mg N/liter]"][iter]
                            storm_df.at[i, "NH3-N [mg N/liter] smpl 2"] = nutrient_data["Ammonia- Results[mg N/liter]"][iter]
                            storm_df.at[i, "PO4-P [mg P/liter] smpl 2"] = nutrient_data["Phosphate- Results[mg P/liter]"][iter]

    storm_df["NO3-N [mg N/liter] avg"] = "NaN"
    storm_df["NH3-N [mg N/liter] avg"] = "NaN"
    storm_df["PO4-P [mg P/liter] avg"] = "NaN"

    for i in storm_df.index:
        if storm_df["NO3-N [mg N/liter] smpl 2"][i] != "NaN":
            storm_df.at[i, "NO3-N [mg N/liter] avg"] = (storm_df["NO3-N [mg N/liter] smpl 1"][i] + storm_df["NO3-N [mg N/liter] smpl 2"][i]) / 2 

        if storm_df["NH3-N [mg N/liter] smpl 2"][i] != "NaN":
            storm_df.at[i, "NH3-N [mg N/liter] avg"] = (storm_df["NH3-N [mg N/liter] smpl 1"][i] + storm_df["NH3-N [mg N/liter] smpl 2"][i]) / 2

        if storm_df["PO4-P [mg P/liter] smpl 2"][i] != "NaN":
            storm_df.at[i, "PO4-P [mg P/liter] avg"] = (storm_df["PO4-P [mg P/liter] smpl 1"][i] + storm_df["PO4-P [mg P/liter] smpl 2"][i]) / 2
    return storm_df


def acid_data(file_path, sampler_data):
    lab_data = pd.read_excel(file_path)
    lab_data["Sample Date"] = lab_data["Sample Date"].dt.strftime("%m-%d-%Y")

    nutrient_acid_data = lab_data[lab_data["Sample Type"] == "NutAcid"]
    na_rep_lst = []
    for index in nutrient_acid_data.index:
        na_rep = nutrient_acid_data["Sample Name"][index].split(" ")[1]
        na_rep_lst.append(na_rep)
    nutrient_acid_data["Replicate"] = na_rep_lst
    
    acid_no3_lst_1 = []
    acid_nh3_lst_1 = []
    acid_po4_lst_1 = []
    acid_no3_lst_2 = []
    acid_nh3_lst_2 = []
    acid_po4_lst_2 = []
    
    for id in sampler_data.index:
        for count in nutrient_acid_data.index:
            if sampler_data["Site"][id] == nutrient_acid_data["Sample Name"][count].split(" ")[0] \
                and sampler_data["Date"][id] == nutrient_acid_data["Sample Date"][count] and nutrient_acid_data["Replicate"][count] == "#1":
                # print(str(sampler_data["Site"][id]) + " Found! " + str(nutrient_acid_data["Sample Name"][count]) + " " + \
                #       str(nutrient_acid_data["Sample Date"][count]))
                acid_no3_lst_1.append(nutrient_acid_data["Nitrate Nitrite- Results[mg N/liter]"][count])
                acid_nh3_lst_1.append(nutrient_acid_data["Ammonia- Results[mg N/liter]"][count])
                acid_po4_lst_1.append(nutrient_acid_data["Phosphate- Results[mg P/liter]"][count])
                acid_no3_lst_2.append("NaN")
                acid_nh3_lst_2.append("NaN")
                acid_po4_lst_2.append("NaN")

    acid_storm_df = sampler_data
    acid_storm_df["NO3-N [mg N/liter] smpl 1"] = acid_no3_lst_1
    acid_storm_df["NH3-N [mg N/liter] smpl 1"] = acid_nh3_lst_1
    acid_storm_df["PO4-P [mg P/liter] smpl 1"] = acid_po4_lst_1
    acid_storm_df["NO3-N [mg N/liter] smpl 2"] = acid_no3_lst_2
    acid_storm_df["NH3-N [mg N/liter] smpl 2"] = acid_nh3_lst_2
    acid_storm_df["PO4-P [mg P/liter] smpl 2"] = acid_po4_lst_2

    for i in acid_storm_df.index:
        for iter in nutrient_acid_data.index:
                if acid_storm_df["Site"][i] == nutrient_acid_data["Sample Name"][iter].split(" ")[0] \
                    and acid_storm_df["Date"][i] == nutrient_acid_data["Sample Date"][iter] and nutrient_acid_data["Replicate"][iter] == "#2":
                    # print(str(sampler_data["Site"][i]) + " Found! " + str(nutrient_acid_data["Sample Name"][iter]) + " " + \
                    #       str(nutrient_acid_data["Sample Date"][iter]))
                    acid_storm_df.at[i, "NO3-N [mg N/liter] smpl 2"] = nutrient_acid_data["Nitrate Nitrite- Results[mg N/liter]"][iter]
                    acid_storm_df.at[i, "NH3-N [mg N/liter] smpl 2"] = nutrient_acid_data["Ammonia- Results[mg N/liter]"][iter]
                    acid_storm_df.at[i, "PO4-P [mg P/liter] smpl 2"] = nutrient_acid_data["Phosphate- Results[mg P/liter]"][iter]

    acid_storm_df["NO3-N [mg N/liter] avg"] = "NaN"
    acid_storm_df["NH3-N [mg N/liter] avg"] = "NaN"
    acid_storm_df["PO4-P [mg P/liter] avg"] = "NaN"

    for i in acid_storm_df.index:
        if acid_storm_df["NO3-N [mg N/liter] smpl 2"][i] != "NaN":
            acid_storm_df.at[i, "NO3-N [mg N/liter] avg"] = (acid_storm_df["NO3-N [mg N/liter] smpl 1"][i] + acid_storm_df["NO3-N [mg N/liter] smpl 2"][i]) / 2 

        if acid_storm_df["NH3-N [mg N/liter] smpl 2"][i] != "NaN":
            acid_storm_df.at[i, "NH3-N [mg N/liter] avg"] = (acid_storm_df["NH3-N [mg N/liter] smpl 1"][i] + acid_storm_df["NH3-N [mg N/liter] smpl 2"][i]) / 2

        if acid_storm_df["PO4-P [mg P/liter] smpl 2"][i] != "NaN":
            acid_storm_df.at[i, "PO4-P [mg P/liter] avg"] = (acid_storm_df["PO4-P [mg P/liter] smpl 1"][i] + acid_storm_df["PO4-P [mg P/liter] smpl 2"][i]) / 2

    return acid_storm_df