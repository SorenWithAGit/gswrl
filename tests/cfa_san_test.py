from gswrlinstruments import San
import pandas as pd
import glob

loop_df = pd.DataFrame(columns = [
    "SampleIdentity",
    "Nitrate Nitrite- Results[mg N/liter]",
    "Phosphate- Results[mg P/liter]",
    "Ammonia- Results[mg N/liter]" ])
dirname = r"C:\Users\john.sorensen\Box\USDA-ARS\Doug Smith\Riesel\Water Quaility\Riesel Storm Skalar"
files = glob.glob(dirname + '//' + '*', recursive = True)
print("Number of Files: " + str(len(files)))
for filename in files:
    print(filename)
for file in files:
    run = San(file)
    data = run.DI_H3A_data()
    loop_df = pd.concat([loop_df, data])
loop_df = loop_df.iloc[:, [0, 1, 2, 3]]
print(loop_df)
