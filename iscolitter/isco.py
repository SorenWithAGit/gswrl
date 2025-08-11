import pandas as pd
import read_sampler as rs
import calculations as cal
import glob

sampler_data = pd.DataFrame(columns = ["Site", "Date", "Units", "# of Samples",
                                      "Start Volume", "End Volume", "Total Volume"])

path = input("Path to raw Sampler txt files: ")
sampler_files = glob.glob(str(path) + "//" + "*" + ".txt", recursive = True)

for file in sampler_files:
    sampler_df = rs.read_txt(file)
    sampler_data = pd.concat([sampler_data, sampler_df]).reset_index(drop = True)
print(sampler_data)