import pandas as pd
import numpy as np

pd.options.mode.copy_on_write = True

class conversions():

        def __init__(self):
                # standard unit conversions
                self.mm_per_l = 1000
                self.mg_per_kg = 1000
                self.l_per_ft3 = 28.3168
                self.in_per_ft = 12
                self.mm_per_in = 25.4
                self.ft_per_acre = 43560
                self.acre_per_hectare = 2.47105
                self.ton_per_kg = 0.00110231
                # attributes of each field that remain constant
                self.field_constants = {
                                        "field" : ["SW12", "SW17", "W1", 
                                                "W6", "W10", "W12",
                                                "W13", "Y2", "Y6", 
                                                "Y8", "Y10", "Y13", 
                                                "Y14"],
                                        "area (ac)" : [2.97, 2.99, 174.00,
                                                42.30, 19.80, 9.90,
                                                11.30, 132.00, 16.30,
                                                20.80, 18.50, 11.40,
                                                5.60],
                                        "landuse" : ["pasture", "pasture", "mixed",
                                                "mixed", "pasture", "cultivated",
                                                "cultivated", "mixed", "cultivated",
                                                "cultivated", "cultivated", "cultivated",
                                                "pasture"],
                                        "1-bottle composite flow interval (mm)" : [1.32, 1.32, 1.32,
                                                                                1.32, 1.32, 1.32,
                                                                                1.32, 1.32, 1.32,
                                                                                1.32, 1.32, 1.32,
                                                                                1.32],
                                        "measurement unit" : ["cf", "cf", "Mgal",
                                                        "cf", "cf", "cf",
                                                        "cf", "Mgal", "cf",
                                                        "cf", "cf", "cf",
                                                        "cf"],
                                        "sampling interval" : [565.9, 565.9, 0.246,
                                                                8000, 3735, 1864,
                                                                2132, 0.186, 3076,
                                                                3915, 3496, 2132,
                                                                1056]
                                        }

                self.field_df = pd.DataFrame(self.field_constants)
                self.field_df = self.field_df.sort_values(by = "field").reset_index(drop = True)
                # print(self.field_df)

        def total_vol_ft3(self, storm_df):
                t_vol = []
                for i in storm_df.index:
                        for id in self.field_df.index:
                                if self.field_df["field"][id] == storm_df["Site"][i] and storm_df["Units"][i] == "cf":
                                        # print(str(storm_df["Site"][i]) + " has units: " + str(storm_df["Units"][i]) + " and sampling interval: " + \
                                        #       str(self.field_df["sampling interval"][id]))
                                        try:
                                                vol = storm_df["End Volume"][i] - storm_df["Start Volume"][i] + self.field_df["sampling interval"][id]
                                                t_vol.append(vol)
                                                continue
                                        except:
                                                vol = storm_df["Total Flow (cf)"][i] + self.field_df["sampling interval"][id]
                                                t_vol.append(vol)

                                elif self.field_df["field"][id] == storm_df["Site"][i] and \
                                storm_df["Units"][i] == "Mgal":
                                        # print(str(storm_df["Site"][i]) + " has units: " + str(storm_df["Units"][i]) + " and sampling interval: " + \
                                        #       str(self.field_df["sampling interval"][id]))
                                        # print("Start Volume: " + str(storm_df["Start Volume"][i]) +  " End Volume: " + str(storm_df["End Volume"][i]) \
                                        #       + " difference: " + str((storm_df["End Volume"][i] - storm_df["Start Volume"][i])) + " Total Mgal: " + \
                                        #         str((storm_df["End Volume"][i] - storm_df["Start Volume"][i]) + self.field_df["sampling interval"][id]) + \
                                        #         " Total (ft3): " + str(((storm_df["End Volume"][i] - storm_df["Start Volume"][i]) + self.field_df["sampling interval"][id])*133700))
                                        try:
                                                vol = ((storm_df["End Volume"][i] - storm_df["Start Volume"][i]) + self.field_df["sampling interval"][id])*133700
                                                t_vol.append(vol)
                                                continue
                                        except:
                                                vol = storm_df["Total Flow (cf)"][i] + self.field_df["sampling interval"][id]*133700
                                                t_vol.append(vol)
                                                continue 
                return t_vol



        def ft3_to_mm(self, storm_df):
                mm_lst = [] 
                for i in storm_df.index:
                        for id in self.field_df.index:
                                if self.field_df["field"][id] == storm_df["Site"][i]:
                                        mm_vol = (storm_df["Total Volume (ft3)"][i] * self.in_per_ft * self.mm_per_in) \
                                        / (self.field_df["area (ac)"][id] * self.ft_per_acre)
                                        mm_lst
                                        mm_lst.append(mm_vol)
                return mm_lst
        
        def kg_per_ha(self, storm_df):
                no3_s1_lst = []
                no3_s2_lst = []
                no3_avg_lst = []
                nh3_s1_lst = []
                nh3_s2_lst = []
                nh3_avg_lst = []
                po4_s1_lst = []
                po4_s2_lst = []
                po4_avg_lst = []
                for i in storm_df.index:
                        for id in self.field_df.index:
                                if self.field_df["field"][id] == storm_df["Site"][i]:
                                        try:
                                                no3_s1_val = (((storm_df["NO3-N [mg N/liter] smpl 1"][i] * self.l_per_ft3 * storm_df["Total Volume (ft3)"][i] * self.acre_per_hectare))/((self.mm_per_l * self.mg_per_kg * self.field_df["area (ac)"][id])))
                                                no3_s1_lst.append(no3_s1_val)
                                        except:
                                                no3_s1_lst.append("NaN")
                                        try:
                                                no3_s2_val = (((storm_df["NO3-N [mg N/liter] smpl 2"][i] * self.l_per_ft3 * storm_df["Total Volume (ft3)"][i] * self.acre_per_hectare))/((self.mm_per_l * self.mg_per_kg * self.field_df["area (ac)"][id])))
                                                no3_s2_lst.append(no3_s2_val)
                                        except:
                                                no3_s2_lst.append("NaN")
                                        try:
                                                no3_avg_val = (((storm_df["NO3-N [mg N/liter] avg"][i] * self.l_per_ft3 * storm_df["Total Volume (ft3)"][i] * self.acre_per_hectare))/((self.mm_per_l * self.mg_per_kg * self.field_df["area (ac)"][id])))
                                                no3_avg_lst.append(no3_avg_val)
                                        except:
                                                no3_avg_lst.append(no3_s1_val)
                                        try:
                                                nh3_s1_val = (((storm_df["NH3-N [mg N/liter] smpl 1"][i] * self.l_per_ft3 * storm_df["Total Volume (ft3)"][i] * self.acre_per_hectare))/((self.mm_per_l * self.mg_per_kg * self.field_df["area (ac)"][id])))
                                                nh3_s1_lst.append(nh3_s1_val)
                                        except:
                                                nh3_s1_lst.append("NaN")
                                        try:
                                                nh3_s2_val = (((storm_df["NH3-N [mg N/liter] smpl 2"][i] * self.l_per_ft3 * storm_df["Total Volume (ft3)"][i] * self.acre_per_hectare))/((self.mm_per_l * self.mg_per_kg * self.field_df["area (ac)"][id])))
                                                nh3_s2_lst.append(nh3_s2_val)
                                        except:
                                                nh3_s2_lst.append("NaN")
                                        try:
                                                nh3_avg_val = (((storm_df["NH3-N [mg N/liter] avg"][i] * self.l_per_ft3 * storm_df["Total Volume (ft3)"][i] * self.acre_per_hectare))/((self.mm_per_l * self.mg_per_kg * self.field_df["area (ac)"][id])))
                                                nh3_avg_lst.append(nh3_avg_val)
                                        except:
                                                nh3_avg_lst.append(nh3_s1_val)

                                        try:
                                                po4_s1_val = (((storm_df["PO4-P [mg P/liter] smpl 1"][i] * self.l_per_ft3 * storm_df["Total Volume (ft3)"][i] * self.acre_per_hectare))/((self.mm_per_l * self.mg_per_kg * self.field_df["area (ac)"][id])))
                                                po4_s1_lst.append(po4_s1_val)
                                        except:
                                                po4_s1_lst.append("NaN")
                                        try:
                                                po4_s2_val = (((storm_df["PO4-P [mg P/liter] smpl 2"][i] * self.l_per_ft3 * storm_df["Total Volume (ft3)"][i] * self.acre_per_hectare))/((self.mm_per_l * self.mg_per_kg * self.field_df["area (ac)"][id])))
                                                po4_s2_lst.append(po4_s2_val)
                                        except:
                                                po4_s2_lst.append("NaN")
                                        try:
                                                po4_avg_val = (((storm_df["PO4-P [mg P/liter] avg"][i] * self.l_per_ft3 * storm_df["Total Volume (ft3)"][i] * self.acre_per_hectare))/((self.mm_per_l * self.mg_per_kg * self.field_df["area (ac)"][id])))
                                                po4_avg_lst.append(po4_avg_val)
                                        except:
                                                po4_avg_lst.append(po4_s1_val)
                return no3_s1_lst, no3_s2_lst, no3_avg_lst, nh3_s1_lst, nh3_s2_lst, nh3_avg_lst, po4_s1_lst, po4_s2_lst, po4_avg_lst
        
        def sediment_kg_per_ha(self, field, sediment_conc, total_storm):
                area = self.field_df.loc[self.field_df["field"] == field, "area (ac)"]
                sed_kg_per_ha = (sediment_conc*28.32*total_storm*2.471) / (1000*1000*area)
                return sed_kg_per_ha
        
        def sediment_t_per_ac(self, sed_kg_per_ha):
                sed_t_per_ac = (sed_kg_per_ha * 0.00110231) / 2.471
                return sed_t_per_ac
        
        def raw_sampler_to_daily(self, df):
                daily_df = df.groupby(df["Datetime"].dt.date).agg(
                                                                Site = ("Site", "last"),
                                                                Units = ("Units", "last"),
                                                                Samples = ("Sample", "last"),
                                                                Total_Vol = ("Total Flow (cf)", lambda x: float(x.iloc[-1]) - float(x.iloc[0]))
                                                                ).reset_index()
                daily_df = daily_df.rename(columns = {"Total_Vol" : "Total Flow (cf)"})
                return daily_df
        
class runoff_calculator():

        def __init__(self):
                self.field_constants = {
                                        "area (ac)" :{
                                                "SW12" : 2.97,
                                                "SW17" : 2.99,
                                                "W1" : 174.00,
                                                "W6" : 42.30,
                                                "W10" : 19.80,
                                                "W12" : 9.90,
                                                "W13" : 11.30,
                                                "Y2" : 132.00,
                                                "Y6" : 16.30,
                                                "Y8" : 20.80,
                                                "Y10" : 18.50,
                                                "Y13" : 11.40,
                                                "Y14" : 5.60
                                        },
                                        "flow constants" : {
                                                "SW12" : [[1.93, 1.755], [2.371, 1.93], [2.574, 2.088], [2.488, 2.577]],
                                                "SW17" : [[1.838, 1.723], [2.364, 1.929], [2.593, 2.124], [2.532, 2.239]],
                                                "W1" : [[1.657, 2.72], [2.58, 3.138], [3.455, 4.047]],
                                                "W6" : [[11.67, 2.508], [21.92, 2.914]],
                                                "W10" : [[11.67, 2.508], [21.92, 2.914]],
                                                "W12" : [[14.16, 2.58], [12.59, 2.53], [13.79, 2.66]],
                                                "W13" : [[15.68, 2.6], [13.07, 2.52], [14.17, 2.64]],
                                                "Y2" : [[12.6, 2.55], [15.03, 2.9992], [15.809, 3.11567]],
                                                "Y6" : [[10.24, 2.476], [15.18, 2.751], [18.65, 3.039]],
                                                "Y8" : [[11.67, 2.508], [21.92, 2.914]],
                                                "Y10" : [[11.67, 2.508], [21.92, 2.914]],
                                                "Y13" : [[14.0, 2.56], [12.94, 2.51], [13.84, 2.64]],
                                                "Y14" : [[13.15, 2.55], [14.15, 2.64]]
                                        },
                                        "flow checks" : {
                                                "SW12" : [0.3, 0.6, 1.1, 1.1],
                                                "SW17" : [0.3, 0.6, 1.5, 1.5],
                                                "W1" : [0.399, 0.699, 0.699],
                                                "W6" : [0.219, 0.219],
                                                "W10" : [0.219, 0.219],
                                                "W12" : [0.1, 0.5, 0.5],
                                                "W13" : [0.1, 0.5, 0.5],
                                                "Y2" : [0.65, 0.9, 0.9],
                                                "Y6" : [0.249, 0.499, 0.499],
                                                "Y8" : [0.219, 0.219],
                                                "Y10" : [0.219, 0.219],
                                                "Y13" : [0.2, 0.6, 0.6],
                                                "Y14" : [0.6, 0.6]
                                        }
                }

        def flow_calculator(self, site, t_interval, level_df):
                site = site
                multiplier_list = self.field_constants["flow constants"][site]
                check_list = self.field_constants["flow checks"][site]
                active_checks = check_list[:-1]
                # print(multiplier_list)
                # print(check_list)

                sublist_arr = np.array(multiplier_list, dtype=float)
                multipliers_arr = sublist_arr[:, 0]  # First column: Multipliers
                exponents_arr = sublist_arr[:, 1]  # Second column: Exponents

                last_index = len(multiplier_list) - 1

                clean_series = level_df["level (ft)"].to_numpy()
                indices = np.searchsorted(active_checks, clean_series, side="right")

                indices = np.where(indices >= len(active_checks), last_index, indices)

                matched_multipliers = multipliers_arr[indices]
                matched_exponents = exponents_arr[indices]

                level_df["new cfs"] = (clean_series**matched_exponents) * matched_multipliers

                level_df["new in/hr"] = ((level_df["new cfs"]*12*3600)/(self.field_constants["area (ac)"][site]*43560))

                level_df["JSKT runoff (mm)"] = ((level_df["new cfs"]*12*t_interval*60)/(self.field_constants["area (ac)"][site]*435600))

                return level_df
        
        def calculate_delta_t(self, runoff_df, flow_sum_df):
                merged_df = pd.merge(flow_sum_df, runoff_df, on = "date")
                merged_df["delta_t"] = merged_df["in"] / merged_df["flow (in/hr)"]
                return merged_df

        
# c = conversions()
# kgc = c.sediment_kg_per_ha("SW12", 858.5, 6266)
# print(kgc)
# tac = c.sediment_t_per_ac(kgc)
# print(tac)


# w13 = {"Site" : "Y14",
#        "Date" : "05-26-2025",
#        "Units" : "cf",
#        "# of Samples" : 1,
#        "Start Volume" : 1300,
#        "End Volume" : 1300}
# w13_df = pd.DataFrame(w13, index = [0])
# c = conversions()
# tvol = c.total_vol_ft3(w13_df)
# w13_df["Total Volume (ft3)"] = tvol
# mmvol = c.ft3_to_mm(w13_df)
# w13_df["Total Volume (mm)"] = mmvol
# print(w13_df)

# no3 = 0.6
# nh3 = 0.29
# po4 = 0.85

# w13_df["NO3-N [mg N/liter] smpl 1"] = no3
# w13_df["NH3-N [mg N/liter] smpl 1"] = nh3
# w13_df["PO4-P [mg P/liter] smpl 1"] = po4
# w13_df["NO3-N [mg N/liter] smpl 2"] = "NaN"
# w13_df["NH3-N [mg N/liter] smpl 2"] = "NaN"
# w13_df["PO4-P [mg P/liter] smpl 2"] = "NaN"
# w13_df["NO3-N [mg N/liter] avg"] = no3
# w13_df["NH3-N [mg N/liter] avg"] = nh3
# w13_df["PO4-P [mg P/liter] avg"] = po4
# # print(w13_df)

# kg_ha = c.kg_per_ha(w13_df)

# # calculate load for NO3 for sample #1 & #2 and average.
# w13_df["NO3-N [kg/ha] Sample #1"] = kg_ha[0]
# w13_df["NO3-N [kg/ha] Sample #2"] = kg_ha[1]
# w13_df["NO3-N [kg/ha] avg"] = kg_ha[2]

# # calculate load for NH3 for sample #1 & #2 and average.
# w13_df["NH3-N [kg/ha] Sample #1"] = kg_ha[3]
# w13_df["NH3-N [kg/ha] Sample #2"] = kg_ha[4]
# w13_df["NH3-N [kg/ha] avg"] = kg_ha[5]

# # calculate load for PO4 for sample #1 & #2 and average.
# w13_df["PO4-P [kg/ha] Sample #1"] = kg_ha[6]
# w13_df["PO4-P [kg/ha] Sample #2"] = kg_ha[7]
# w13_df["PO4-P [kg/ha] avg"] = kg_ha[8]

# w13_df["Sample Type"] = "Acid Nutrients"

# w13_df = w13_df[["Site", "Date", "Units", "# of Samples", "Start Volume", "End Volume", "Total Volume (ft3)", \
#                                    "Total Volume (mm)", "Sample Type", \
#                         "NO3-N [mg N/liter] smpl 1", "NO3-N [mg N/liter] smpl 2", "NO3-N [mg N/liter] avg", "NH3-N [mg N/liter] smpl 1", \
#                             "NH3-N [mg N/liter] smpl 2", "NH3-N [mg N/liter] avg", "PO4-P [mg P/liter] smpl 1", "PO4-P [mg P/liter] smpl 2", \
#                                 "PO4-P [mg P/liter] avg", "NO3-N [kg/ha] Sample #1", "NO3-N [kg/ha] Sample #2", "NO3-N [kg/ha] avg", \
#                                 "NH3-N [kg/ha] Sample #1", "NH3-N [kg/ha] Sample #2", "NH3-N [kg/ha] avg", "PO4-P [kg/ha] Sample #1", \
#                                 "PO4-P [kg/ha] Sample #2", "PO4-P [kg/ha] avg"]]

# print(w13_df)

# w13_df.to_excel(r"I:\USDA-ARS\Doug Smith\Riesel\Water Quaility\ISCO Raw\2025\w13_point.xlsx")

