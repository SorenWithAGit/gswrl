from gswrlinstruments import agilent
import pandas as pd
import glob

loop_df = pd.DataFrame(columns = [
    "Solution Label",
    "Aluminium (ppm)",
    "Calcium (ppm)",
    "Copper (ppm)",
    "Iron (ppm)",
    "Potassium (ppm)"
    "Magnesium (ppm)"
    "Manganese (ppm)"
    "Sodium (ppm)", 
    "Phosphorus (ppm)",
    "Sulfur (ppm)",
    "Zinc (ppm)" ])

dirname = r"C:\Users\john.sorensen\Box\USDA-ARS\Doug Smith\Riesel\Water Quaility\Total Nutrients (P)\Raw Data"
files = glob.glob(dirname + '//' + '*.xlsx', recursive = True)
for file in files:
    run = agilent(file)
    data = run.data()
    loop_df = pd.concat([loop_df, data])
print(loop_df)



