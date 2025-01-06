from gswrlinstruments import MaxCube
import pandas as pd
import glob

loop_df = pd.DataFrame(columns = [
    "Sample Name",
    "Date/Time",
    "Weight (mg)",
    "N Area",
    "C Area",
    "%N",
    "%C",
    "CN Ratio" ])
dirname = r"C:\Users\john.sorensen\Box\USDA-ARS\Phil Fay\vario MAX CUBE\Exported Runs\Cotton Spacing & K Trials\2018"
files = glob.glob(dirname + '//' + '*.csv', recursive = True)
print("Number of Files: " + str(len(files)))
for file in files:
    run = MaxCube(file)
    data = run.csv_data()
    loop_df = pd.concat([loop_df, data])
print(loop_df)