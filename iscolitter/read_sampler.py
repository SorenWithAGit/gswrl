import pandas as pd

def read_txt(txt):
    sampler_df = pd.DataFrame(columns = ["Site", "Date", "Units", "# of Samples",
                                      "Start Volume", "End Volume", "Total Volume"])
    with open(txt) as file:
        lines = file.readlines()

        # iterate through file lines until start of table is found
        for line_count, line in enumerate(lines):
            if "------- ------ ----  -----  ----- -------------" in line:
                begin_line = line_count + 1
                # print("begin line: " + str(begin_line))
                break

        # iterate through file lines until end of table is found
        for line_count, line in enumerate(lines[begin_line:]):
            if "----------------------------------------" in line:
                end_line = begin_line + line_count + 1
                # print("end line: " + str(end_line))
                break

        # iterate through file lines until first sample volume is found
        for line_count, line in enumerate(lines[begin_line:end_line]):
            if "    1     1   " in line:
                start_vol_line = begin_line + line_count
                break

        end_vol_line = lines[end_line - 2]
        if lines[begin_line - 3] == "\n":
            site = lines[begin_line - 9].split("   SITE: ")[1].strip("\n")
        elif lines[begin_line - 5] == "\n":
            site = lines[begin_line - 9].split("   SITE: ")[1].strip("\n")
        else:
            try:
                site = lines[begin_line -8].split("   SITE: ")[1].strip("\n")
            except:
                site = lines[begin_line - 8].strip("   SITE:  ").strip("\n")
        date = lines[begin_line][25:34]
        units = lines[begin_line - 2].split(" ")[-1].strip("\n")
        sample_num = end_vol_line.split(" ")[3].strip("\n")
        start_volume = float(lines[start_vol_line].split(" ")[-1].strip("\n"))
        end_volume = float(end_vol_line.split(" ")[-1].strip("\n"))
        total_volume = end_volume - start_volume
    sampler_df["Site"] = [site]
    sampler_df["Date"] = [date]
    sampler_df["Units"] = [units]
    sampler_df["# of Samples"] = [sample_num]
    sampler_df["Start Volume"] = [start_volume]
    sampler_df["End Volume"] = [end_volume]
    sampler_df["Total Volume"] = [total_volume]
        # print("SITE: " + site)
        # print("DATE: " + date)
        # print("UNITS: " + units)
        # print("NUMBER OF SAMPLES: " + str(sample_num))
        # print("START VOLUME: " + str(start_volume))
        # print("END VOLUME: " + str(end_volume))
        # print("TOTAL VOLUME: " + str(total_volume))
    return sampler_df
