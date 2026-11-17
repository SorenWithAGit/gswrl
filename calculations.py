import pandas as pd
import numpy as np

class soil_calculations():

    def __init__(self):
        self.mL_per_L = 1000
        self.g_per_kg = 1000
        self.extract_to_soil = 10

    def soil_extracts(self, result):
        mg_per_kg = result / self.mL_per_L * self.extract_to_soil *self.g_per_kg
        return mg_per_kg
    

# input_path = r"I:\USDA-ARS\Kabindra Adhikari\Riesel\PbyYSi_24\ICP_Results\DI\KA_PbyYSi24_ICP_data.xlsx"
# output_path = r"I:\USDA-ARS\Kabindra Adhikari\Riesel\PbyYSi_24\ICP_Results\DI\KA_PbyYSi24_ICP_data_final.xlsx"

# c = soil_calculations()
# df = pd.read_excel(input_path)
# print(df.dtypes)
# df.iloc[:, 1:-1] = df.iloc[:, 1:-1].mask(df.iloc[:, 1:-1] < 0, 0.05)
# new_df = pd.DataFrame()
# new_df["lab_id"] = df.iloc[:, 0]
# new_df["Aluminium (mg Al/kg soil)"] = c.soil_extracts(df.iloc[:, 1])
# new_df["Arsenic (mg As/kg soil)"] = "NaN"
# new_df["Calcium (mg Ca/kg soil)"] = c.soil_extracts(df.iloc[:, 3])
# new_df["Copper (mg Cu/kg soil)"] = c.soil_extracts(df.iloc[:, 4])
# new_df["Iron (mg Fe/kg soil)"] = c.soil_extracts(df.iloc[:, 5])
# new_df["Potassium (mg K/kg soil)"] = c.soil_extracts(df.iloc[:, 6])
# new_df["Magnesium (mg Mg/kg soil)"] = c.soil_extracts(df.iloc[:, 7])
# new_df["Manganese (mg Mn/kg soil)"] = c.soil_extracts(df.iloc[:, 8])
# new_df["Sodium (mg Na/kg soil)"] = c.soil_extracts(df.iloc[:, 9])
# new_df["Phosphorus (mg P/kg soil)"] = c.soil_extracts(df.iloc[:, 10])
# new_df["Sulfur (mg S/kg soil)"] = c.soil_extracts(df.iloc[:, 11])
# new_df["Zinc (mg Zn/kg soil)"] = c.soil_extracts(df.iloc[:, 12])
# new_df["Ytrium (mg Y/kg soil)"] = "NaN"

# print(df)
# print(new_df)
# # new_df.to_excel(output_path, index = False)


input_path = r"I:\USDA-ARS\Kabindra Adhikari\Riesel\PbyYSi_24\Skalar_Results\DI\KA_PbyYSi_24_DI_CFA.xlsx"
output_path = r"I:\USDA-ARS\Kabindra Adhikari\Riesel\PbyYSi_24\Skalar_Results\DI\KA_PbyYSi_24_DI_CFA_final.xlsx"

c = soil_calculations()
df = pd.read_excel(input_path)
new_df = pd.DataFrame()
new_df["lab_id"] = df["SampleIdentity"]
new_df["Nitrate Nitrite [mg N/kg soil]"] = c.soil_extracts(df.iloc[:, 1])
new_df["Ammonia [mg N/kg soil]"] = c.soil_extracts(df.iloc[:, 2])
new_df["Phosphate [mg P/kg soil]"] = c.soil_extracts(df.iloc[:, 3])
new_df.iloc[:, [1, 2, 3]] = new_df.iloc[:, [1, 2, 3]].mask(new_df.iloc[:, [1, 2, 3]] < 0, 0.05)
print(new_df)
new_df.to_excel(output_path, index = False)