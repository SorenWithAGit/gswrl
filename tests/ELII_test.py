from gswrlinstruments import ELIII
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
dirname = r"C:\Users\john.sorensen\Box\USDA-ARS\Hal Collins\N Corn"
files = glob.glob(dirname + '//' + '*.xls', recursive = True)
print("Number of Files: " + str(len(files)))
for file in files:
    run = ELIII(file)
    data = run.data()
    loop_df = pd.concat([loop_df, data])
print(loop_df)