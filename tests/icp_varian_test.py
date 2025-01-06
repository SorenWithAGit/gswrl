from gswrlinstruments import varian
import pandas as pd
import glob

loop_df = pd.DataFrame(columns = [
    "Sample Labels",    
    "Aluminium (ppm)",
    "Arsenic (ppm)",
    "Calcium (ppm)",
    "Iron (ppm)",
    "Potassium (ppm)"
    "Magnesium (ppm)"
    "Manganese (ppm)"
    "Phosphorus (ppm)",
    "Sulfur (ppm)",
    "Zinc (ppm)",
    "Ytrium (ppm)" ])

dirname = r"C:\Users\john.sorensen\Box\USDA-ARS\Doug Smith\Old ICP Computer Backup\ICP Files\Hal Collins\2018 Cotton"
files = glob.glob(dirname + '//' + '*.xls', recursive = True)
for file in files:
    run = varian(file)
    data = run.data()
    loop_df = pd.concat([loop_df, data])
print(loop_df)