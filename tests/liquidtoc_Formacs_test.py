from gswrlinstruments import FormacsTOC
import pandas as pd
import glob

loop_df = pd.DataFrame(columns = [
        "Sample ID",
        "TC Area",
        "IC Area",
        "TN Area",
        "TOC (ppm)",
        "TC (ppm)",
        "TC (ppm)",
        "IC (ppm)",
        "TN (ppm)"])
dirname = r"C:\Users\john.sorensen\Box\programming\python\formacs_toc\Riesel Grazing Soils\Formacs TOC-TN"
files = glob.glob(dirname + '//' + '*', recursive = True)
print("Number of Files: " + str(len(files)))
for filename in files:
    print(filename)
for file in files:
    run = FormacsTOC(file)
    data = run.data()
    loop_df = pd.concat([loop_df, data[0]])
print(loop_df)