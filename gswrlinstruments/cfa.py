"""
########################################################################
The cfa.py module is defined by two classes, one for each of two
instruments at the USDA Grassland Soil and Water Research Laboratory in
Temple Texas.

The San class is to be used with output data from an
Skalar San++ Continious Flow Analyzer (CFA).
The first of the two functions within this class is used for results
from a Deionized Water Extraction (DI) and the Haney Three Acid
Extraction (H3A.
Both extractions analyze Nitrate/Nitrite (NO3/NO2), Phosphate (PO4),
and Ammonium (NH4).
The second function is for results of a KCL extraction where only
NO3/NO2 & NH4 are analyzed.
Both functions will output a Dataframe of the same format.

The AA500 class is another CFA at the station an AA500.
The output of this class's function is a dictionary containing the
instrument "metadata" and a Dataframe with the analytical data
########################################################################
"""


import pandas as pd
import csv
from sylk_parser import SylkParser
from io import StringIO

class San():
    """
    This class represents the output data of the Skalar San++ CFA.
    """
    def __init__(self, file_name):
        """
        Reads excel file into a pandas.DataFrame.
        Args:
            file_name (.xls, .xlsx): output excel file from instrument
        """
        self.file_name = file_name
        self.data = pd.read_excel(self.file_name)

    def DI_H3A_data(self):
        """
        Function to anipulate data from self.data from
        instrument for two extractions DI & H3A.

        Returns:
            df: pandas.DataFrame containing analytical results.
        """
        Data = self.data
        drop_lst = []
        for ind in range(len(Data)):
            if str(self.data.iloc[ind]["SampleType"].replace(" ", "")) != str("U"):
                drop_lst.append(ind)
        df = Data.drop(drop_lst, axis = 0)
        df = df.drop(["NeedleNumber",
                      "ResultID", "Position ",
                      "SampleType",
                      "PDCupsHistory"], axis = 1)
        return df

    def KCL_data(self):
        """
        Function to manipulate data from self.data from the
        instrument for one extraction KCl.

        Returns:
            df: pandas.DataFrame containing analytical results.
        """
        Data = self.data
        drop_lst = []
        for ind in range(len(Data)):
            if str(Data.iloc[ind]["SampleType"].replace(" ", "")) != str("U"):
                drop_lst.append(ind)
        df =Data.drop(drop_lst, axis = 0)
        df = df.drop(["NeedleNumber",
                      "ResultID",
                      "Position ",
                      "SampleType",
                      "PDCupsHistory"], axis = 1)
        df["Phosphate- Results[mg P/liter]"] = "NaN"
        df = df.iloc[:, [0, 1, 3, 2]]
        return df


class AA500():
    """
    This class represents the output SLK file from the AA500 CFA.
    """

    def __init__(self, file_name):
        """
        Args:
            file_name (.SLK): Output file from analyzer
        """
        self.file_name = file_name
        parser = SylkParser(self.file_name)
        fbuf = StringIO()
        parser.to_csv(fbuf)
        self.test_results = fbuf.getvalue()
        self.instrument_info = dict.fromkeys([
             "Analysis",
             "Run Name",
             "Run Date",
             "Run Started"])
        self.analytical_data = pd.DataFrame(columns = [
             "Sample ID",
             "Nitrate/Nitrite",
             "Phosphate",
             "Ammonium"])

    def data(self):
        """
        Function to read and manipulate data from the output SLK file.

        Returns:
            ins: dictionary containing instrument/run info.
            analy_df: pandas.DataFrame containing analytical results.

        """
        split_str = self.test_results.split("\n")
        ins = self.instrument_info
        analy_df = self.analytical_data
        sampleids = []
        NitrateNitrite = []
        Phosphate = []
        Ammonium = []
        for count in range(len(split_str) - 1):
            if count == 1:
                ins["Analysis"] = split_str[count].split(",")[1]
            if count == 2:
                ins["Run Name"] = split_str[count].split(",")[1]
            if count == 3:
                ins["Run Date"] = split_str[count].split(",")[1]
            if count == 4:
                ins["Run Started"] = split_str[count].split(",")[1]
            if count > 5 and count <= len(split_str):
                if str(split_str[count].split(",")[0]) == '" "':
                    sampleids.append("NaN")
                else:
                    sampleids.append(str(split_str[count].split(",")[0]))
                NitrateNitrite.append(split_str[count].split(",")[4])
                if str(split_str[count].split(",")[5]) == '" "':
                    Phosphate.append("NaN")
                else:
                    Phosphate.append(split_str[count].split(",")[5])
                Ammonium.append(split_str[count].split(",")[6])
        analy_df["Sample ID"] = sampleids
        analy_df["Nitrate/Nitrite"] = NitrateNitrite
        analy_df["Phosphate"] = Phosphate
        analy_df["Ammonium"] = Ammonium
        print(ins)
        print(analy_df)
        return [ins, analy_df]
