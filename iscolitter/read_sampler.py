def read_txt(txt):
    print(txt)
    with open(txt) as file:
        lines = file.readlines()

        # iterate through file lines until start of table is found
        for line_count, line in enumerate(lines):
            if "------- ------ ----  -----  ----- -------------" in line:
                begin_line = line_count + 1
                print("begin line: " + str(begin_line))
                break

        # iterate through file lines until end of table is found
        for line_count, line in enumerate(lines[begin_line:]):
            if "----------------------------------------" in line:
                end_line = begin_line + line_count + 1
                print("end line: " + str(end_line))
                break

        # iterate through file lines until first sample volume is found
        for line_count, line in enumerate(lines[begin_line:end_line]):
            if "    1     1   " in line:
                start_vol_line = begin_line + line_count
                break

        end_vol_line = lines[end_line - 2]

        site = lines[begin_line - 8].strip("   SITE:  ").strip("\n")
        date = lines[begin_line][25:34]
        units = lines[begin_line - 2].split(" ")[-1].strip("\n")
        start_volume = float(lines[start_vol_line].split(" ")[-1].strip("\n"))
        end_volume = float(end_vol_line.split(" ")[-1].strip("\n"))
        total_volume = end_volume - start_volume
        print("SITE: " + site)
        print("DATE: " + date)
        print("UNITS: " + units)
        print("START VOLUME: " + str(start_volume))
        print("END VOLUME: " + str(end_volume))
        print("TOTAL VOLUME: " + str(total_volume))

y14 = read_txt(r"C:\Users\john.sorensen\Downloads\2019_Y14_138.txt")
w12 = read_txt(r"C:\Users\john.sorensen\Downloads\2019_W12_138.txt")
sw17 = read_txt(r"C:\Users\john.sorensen\Downloads\2019_SW17_138.txt")
w13 = read_txt(r"C:\Users\john.sorensen\Downloads\2019_W13_138.txt")
y6 = read_txt(r"C:\Users\john.sorensen\Downloads\2019_Y6_138.txt")
y13 = read_txt(r"C:\Users\john.sorensen\Downloads\2019_Y13_138.txt")
y2 = read_txt(r"C:\Users\john.sorensen\Downloads\2019_Y2_138.txt")
w10 = read_txt(r"C:\Users\john.sorensen\Downloads\2019_W10_138.txt")
w6 = read_txt(r"C:\Users\john.sorensen\Downloads\2019_W6_138.txt")
w1 = read_txt(r"C:\Users\john.sorensen\Downloads\2019_W1_138.txt")
y10 = read_txt(r"C:\Users\john.sorensen\Downloads\2019_Y10_138.txt")
y8 = read_txt(r"C:\Users\john.sorensen\Downloads\2019_Y8_138.txt")
sw12 = read_txt(r"C:\Users\john.sorensen\Downloads\2019_SW12_138.txt")