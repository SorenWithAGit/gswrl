from gswrlinstruments import SCION456
import pandas as pd
import glob



dirname = r"C:\Users\john.sorensen\Box\programming\python\tillage\Dorothy Long Term Tillage\Summer 2021 200s\4-8-2021 200's"
files = glob.glob(dirname + '//' + '*.csv', recursive = True)
print("Number of Files: " + str(len(files)))
for file in files:
    run = SCION456(file)
    data = run.data()
    print(data[0])
    print(data[1])
    print(data[2])
    print(data[3])
