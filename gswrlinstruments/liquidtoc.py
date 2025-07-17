"""
########################################################################
The liquid_toc.py module is defined by two classes, one for each of two
instruments at the USDA Grassland Soil and Water Research Laboratory in
Temple Texas.

The FormacsTOC class is to be used with data exported from the Skalar
FORMACS TOC/TN analyzer.
The Data function will return two items a pandas dataframe containing
the analytical data and a dictionary containing the instrument
"metadata" of the run.

The ---- class like the first is for data from an Elementar Liquid
TOC/TN Analyzer.
THe output of this class's data function will match the output of the
FormacsTOC.data()
########################################################################
"""

import pandas as pd

class FormacsTOC():
    """
    This class represents the output file from the Formacs TOC.
    """
    def __init__(self, file_name):
        """
        Defines dataframe self.analytical data and dictionary 
        self.instrument_info

        Args:
            file_name (.csv): output csv file from instrument
        """
        self.analytical_data = pd.DataFrame(columns = [
            "Sample ID",
            "TC Area",
            "IC Area",
            "TN Area",
            "TOC (ppm)",
            "TC (ppm)",
            "TC (ppm)",
            "IC (ppm)",
            "TN (ppm)"])
        self.instrument_info = dict.fromkeys(["Analysis Name",
                                              "Template Name",
                                              "Operator",
                                              "Run Date",
                                              "Time Started",
                                              "Version"])
        self.file_name = file_name

    def data(self):
        """
        Reads the output csv file and iterates through the fiel to add
        data to the instrument info dictionary and sanaly_df dataframe.

        Returns:
            ins: dictionary containing instrument/run info
            analy_df: pandas.DataFrame containing analytical results of
            samples from the run.
        """
        ins = self.instrument_info
        analy_df = self.analytical_data
        with open(self.file_name, "r") as file:
            lines = file.readlines()
            file.close()
        sample_ids =[]
        TC_area = []
        IC_area = []
        TN_area = []
        TOC_ppm = []
        TC_ppm = []
        IC_ppm = []
        TN_ppm = []
        for count in range(len(lines)):
            if str(lines[count].split(",")[0]) == str("Sample Info") or str(lines[count].split(",")[0].replace('"', '')) == str("Sample Info"):
                smpl_TOC = count + 2
                smpl_TC = count + 3
                smpl_IC = count + 4
                smpl_TN = count + 5
                break
        while smpl_TOC <= (len(lines) - 5):
            sample_ids.append(lines[smpl_TOC].split(",")[4])
            TOC_ppm.append(lines[smpl_TOC].split(",")[7].replace('"', ''))
            smpl_TOC += 5
        while smpl_TC <= len(lines):
            if str(lines[smpl_TC].split(",")[0]) == str('" "'):
                TC_area.append(lines[smpl_TC].split('"')[17])
            else:
                TC_area.append(lines[smpl_TC].split('"')[1])
            TC_ppm.append(lines[smpl_TC].split(",")[7].replace('"', ''))
            smpl_TC += 5
        while smpl_IC <= len(lines):
            if str(lines[smpl_IC].split(",")[0]) == str('" "'):
                IC_area.append(lines[smpl_IC].split('"')[17])
            else:
                IC_area.append(lines[smpl_IC].split('"')[1])
            IC_ppm.append(lines[smpl_IC].split(",")[7].replace('"', ''))
            smpl_IC += 5
        while smpl_TN <= len(lines):
            if str(lines[smpl_TN].split(",")[0]) == str('" "'):
                TN_area.append(lines[smpl_TN].split('"')[17])
            else:
                TN_area.append(lines[smpl_TN].split('"')[1])
            TN_ppm.append(lines[smpl_TN].split(",")[7].replace('"', ''))
            smpl_TN += 5
        analy_df['Sample ID'] = sample_ids
        analy_df["TC Area"] = TC_area
        analy_df["IC Area"] = IC_area
        analy_df["TN Area"] = TN_area
        analy_df["TOC (ppm)"] = TOC_ppm
        analy_df["TC (ppm)"] = TC_ppm
        analy_df["IC (ppm)"] = IC_ppm
        analy_df["TN (ppm)"] = TN_ppm
        #print(analy_df)
        analysis_line = 1
        template_line = 2
        operator_line = 3
        run_date_line = 4
        time_started_line = 5
        version_line = 7
        ins["Analysis Name"] = lines[analysis_line].split(",")[1]
        ins["Template Name"] = lines[template_line].split(",")[1]
        ins["Operator"] = lines[operator_line].split(",")[1]
        ins["Run Date"] = lines[run_date_line].split(",")[1]
        ins["Time Started"] = lines[time_started_line].split(",")[1]
        ins["Version"] = lines[version_line].split(",")[1]
        # print("Analysis Name: " + str(analysis_name) + "\n" + \
        #     "Template Name: " + str(template_name) + "\n" + \
        #     "Operator: " + str(operator) + "\n" + \
        #     "Run Date: " + str(run_date) + "\n" + \
        #     "Time Started: " + str(time_started) + "\n" + \
        #     "Version: " + str(version))
        return [analy_df, ins]


class VarioTOC():

    def __init__(self, file_name):
        self.file_name = file_name
    
    def data(self):
        run_df = pd.read_csv(self.file_name)
        return run_df