import pandas as pd

pd.options.mode.copy_on_write = True

class conversions():

        def __init__(self):
                # standard unit conversions
                self.mm_per_l = 1000
                self.mg_per_kg = 1000
                self.l_per_ft3 = 28.3168
                self.in_per_ft = 12
                self.mm_per_ft = 25.4
                self.ft_per_acre = 43560
                self.acre_per_hectare = 2.47105
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
                                        vol = storm_df["End Volume"][i] - storm_df["Start Volume"][i] + self.field_df["sampling interval"][id]
                                        t_vol.append(vol)
                                        continue

                                elif self.field_df["field"][id] == storm_df["Site"][i] and \
                                storm_df["Units"][i] == "Mgal":
                                        # print(str(storm_df["Site"][i]) + " has units: " + str(storm_df["Units"][i]) + " and sampling interval: " + \
                                        #       str(self.field_df["sampling interval"][id]))
                                        # print("Start Volume: " + str(storm_df["Start Volume"][i]) +  " End Volume: " + str(storm_df["End Volume"][i]) \
                                        #       + " difference: " + str((storm_df["End Volume"][i] - storm_df["Start Volume"][i])) + " Total Mgal: " + \
                                        #         str((storm_df["End Volume"][i] - storm_df["Start Volume"][i]) + self.field_df["sampling interval"][id]) + \
                                        #         " Total (ft3): " + str(((storm_df["End Volume"][i] - storm_df["Start Volume"][i]) + self.field_df["sampling interval"][id])*133700))
                                        vol = ((storm_df["End Volume"][i] - storm_df["Start Volume"][i]) + self.field_df["sampling interval"][id])*133700
                                        t_vol.append(vol)
                                        continue
                return t_vol



        def ft3_to_mm(self, storm_df):
                mm_lst = [] 
                for i in storm_df.index:
                        for id in self.field_df.index:
                                if self.field_df["field"][id] == storm_df["Site"][i]:
                                        mm_vol = (storm_df["Total Volume (ft3)"][i] * self.in_per_ft * self.mm_per_ft) \
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
                                        no3_s1_val = (((storm_df["NO3-N [mg N/liter] smpl 1"][i] * self.l_per_ft3 * storm_df["Total Volume (ft3)"][i] * self.acre_per_hectare))/((self.mm_per_l * self.mg_per_kg * self.field_df["area (ac)"][id])))
                                        no3_s1_lst.append(no3_s1_val)
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

                                        nh3_s1_val = (((storm_df["NH3-N [mg N/liter] smpl 1"][i] * self.l_per_ft3 * storm_df["Total Volume (ft3)"][i] * self.acre_per_hectare))/((self.mm_per_l * self.mg_per_kg * self.field_df["area (ac)"][id])))
                                        nh3_s1_lst.append(nh3_s1_val)
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

                                        po4_s1_val = (((storm_df["PO4-P [mg P/liter] smpl 1"][i] * self.l_per_ft3 * storm_df["Total Volume (ft3)"][i] * self.acre_per_hectare))/((self.mm_per_l * self.mg_per_kg * self.field_df["area (ac)"][id])))
                                        po4_s1_lst.append(po4_s1_val)
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
