import pandas as pd
import read_sampler as rs
import calculations as cal
import glob

sampler_data = pd.DataFrame(columns = ["Site", "Date", "Units", "# of Samples",
                                      "Start Volume", "End Volume", "Total Volume"])

sampler_files = glob.glob(r"I:\programming\python\gswrl\iscolitter\05-08-2019" + "\\" + "*.txt", recursive = True)

for file in sampler_files:
    sampler_df = rs.read_txt(file)
    sampler_data = pd.concat([sampler_data, sampler_df]).reset_index(drop = True)
print(sampler_data)