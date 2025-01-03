"""
########################################################################
The dry_combusion_cn.py module is defined by three classes, one for each
of three Dry Combustion Analyzers at the USDA Grassland Soil and Water
Research Laboratory in Temple Texas.

The ELIII class is to be used with data from an Elementar VARIO EL III
for Carbon (C), Nitrogen (N), and Sulfur (S).
The output of this class's data function is a dataframe containing the
(C, N, S) data from a single run.

The MaxCube class is to be used with data from an
Elementar VARIO Max Cube for (C, N) analysis.
The output of this class's data function is a dataframe containing the
(C, N) data from a single run.

The ThermoFlash class is to be used with data from an Thermo Scientific
Flash for (C, N) analysis.
The outputs of this class's data function are three dictionaries:
Instrumental Metadara, Nitrogen Results, and Carbon Results of a single
sample within a file.
########################################################################
"""


import pandas as pd

class ELIII():
    """
    This class represents the output data from the Vario ELIII CN 
    Analyzer.
    """

    def __init__(self, file_name):
        """
        Args:
            file_name (.xls): output excel file from instrument, engine
            must be "calamine".
        """
        self.file_name = file_name
        self.run_df = pd.read_excel(self.file_name, engine = "calamine")

    def data(self):
        """
        This function reads and manipulates data from the instrument.

        Returns:
            df: pandas.DataFrame containing analytical results
        """
        drop_lst = ["Blank", "Sulf", "Sulfanilic Acid", "Orchard Leaves"]
        drop_indexes = []
        for ind in range(len(self.run_df)):
            if str(self.run_df.iloc[ind]["Name"]) in drop_lst:
                drop_indexes.append(ind)
        df = self.run_df.iloc[:, [4, 7, 8, 26, 27, 22, 23, 42]]
        df = df.drop(drop_indexes, axis = 0)
        df = df.rename(columns = {
            df.columns[0] : "Sample Name",
            df.columns[1] : "Date/Time",
            df.columns[2] : "Weight (mg)",
            df.columns[3] : "N Area",
            df.columns[4] : "C Area",
            df.columns[5] : "%N",
            df.columns[6] : "%C",
            df.columns[7] : "CN Ratio"})
        return df

class MaxCube():
    """
    This class represents the output files from the Vario Max Cube.
    """
    def __init__(self, file_name):
        """
        Args:
            file_name (.xlsx or .csv): output file from the instrument
            as a excel or csv file
        """
        self.file_name = file_name

    def excel_data(self):
        """
        This function reads and manipulates ouput excel files from the
        instrument.

        Returns:
            df: pandas.DataFrame containing the analytical results of a
            run.
        """
        self.run_df = pd.read_excel(self.file_name)
        drop_lst = ["blank [O2]", "aspartic acid 1"]
        drop_indexes = []
        blank_indexes = self.run_df[self.run_df["Method  "].isna()].index
        for ind in range(len(self.run_df)):
            if str(self.run_df.iloc[ind]["Method  "]) in drop_lst:
                drop_indexes.append(ind)
        df = self.run_df.iloc[:, [3, 14, 2, 5, 6, 7, 8, 11]]
        df = df.drop(drop_indexes, axis = 0)
        df = df.drop(blank_indexes, axis = 0)
        df = df.rename(columns = {
            df.columns[0] : "Sample Name",
            df.columns[1] : "Date/Time",
            df.columns[2] : "Weight (mg)",
            df.columns[3] : "N Area",
            df.columns[4] : "C Area",
            df.columns[5] : "%N",
            df.columns[6] : "$C",
            df.columns[7] : "CN Ration"})
        return df

    def csv_data(self):
        """
        This function reads and manipulates output csv files from the
        instrument.

        Returns:
            df: pandas.DataFrame containing the analytical results of a
            run.
        """
        self.run_df = pd.read_csv(self.file_name, sep = "\t", skiprows = [0])
        drop_lst = ["blank [O2]", "aspartic acid 1"]
        drop_indexes = []
        blank_indexes = self.run_df[self.run_df["Method  "].isna()].index
        for ind in range(len(self.run_df)):
            if str(self.run_df.iloc[ind]["Method  "]) in drop_lst:
                drop_indexes.append(ind)
        df = self.run_df.iloc[:, [3, 14, 2, 5, 6, 7, 8, 11]]
        df = df.drop(drop_indexes, axis = 0)
        df = df.drop(blank_indexes, axis = 0)
        df = df.rename(columns = {
            df.columns[0] : "Sample Name",
            df.columns[1] : "Date/Time",
            df.columns[2] : "Weight (mg)",
            df.columns[3] : "N Area",
            df.columns[4] : "C Area",
            df.columns[5] : "%N",
            df.columns[6] : "%C",
            df.columns[7] : "CN Ratio"})
        return df

class ThermoFlash():
    """
    This class represents the output excel file from the Thermo Flash.
    """
    def __init__(self, file_name):
        """
        Args:
            file_name (.xls, .xlsx): output excel file from the 
            instrument "xlrd" engine is functional.
        """
        self.file_name = file_name
        self.instrument_dict = dict.fromkeys(["Method Name",
                                         "Method File",
                                         "Chromatogram",
                                         "Operator ID",
                                         "Company Name",
                                         "Analysed",
                                         "Printed",
                                         "Sample ID",
                                         "Instrument Number",
                                         "Analysis Type",
                                         "Sample Weight",
                                         "Calibration Method"])
        self.nitrogen_dict = dict.fromkeys(["% Nitrogen",
                                            "Nitrogen Retention Time",
                                            "Nitrogen Area"])
        self.carbon_dict = dict.fromkeys(["% Carbon",
                                          "Carbon Retention Time",
                                          "Carbon Area"])
        self.raw_df = pd.read_excel(self.file_name, engine = "xlrd")

    def data(self):
        """
        This funtion manipulates the self.raw_df and returns three
        dictionaries.

        Returns:
            ins_dict: dictionary containing the instrument/run info
            n_dict: dictionary containing the analytical results for 
                    Nitrogen.
            C_dict: dictionary containing the analytical results for 
                    Carbon.
        """
        method = str(self.raw_df.iloc[1, 0]).strip(" ").split(":")[1][1:]
        method_file = str(self.raw_df.iloc[2,0]).split("   :")[1][1:]
        chromatogram = str(self.raw_df.iloc[3,0]).strip(" ").split(":")[1][1:]
        operator_str = str(self.raw_df.iloc[4,0]).split("   :")[1]
        operator = operator_str.split("          ")[0][1:]
        company = operator_str.split("          ")[1].split(":")[1][1:]
        analysed_str = str(self.raw_df.iloc[5,0]).split("      ")
        analysed = analysed_str[1][2:]
        printed = analysed_str[3][3:]
        sampleid = str(self.raw_df.iloc[6, 0]).split(":")[1][1:]
        instrument = str(self.raw_df.iloc[7,0]).split(":")[1][1:]
        type_lst = str(self.raw_df.iloc[8, 0]).split("         ")
        analy_type = type_lst[0].split(":")[1][1:]
        smpl_wght = type_lst[1].split(":")[1][1:]
        calib = str(self.raw_df.iloc[10, 0]).split(":")[1][1:]
        n_per = self.raw_df.iloc[13, 1]
        n_ret = self.raw_df.iloc[13, 2]
        n_area = self.raw_df.iloc[13, 3]
        c_per = self.raw_df.iloc[14, 1]
        c_ret = self.raw_df.iloc[14, 2]
        c_area = self.raw_df.iloc[14, 3]
        ins_dict = self.instrument_dict
        ins_dict["Method Name"] = method
        ins_dict["Method File"] = method_file
        ins_dict["Chromatogram"] = chromatogram
        ins_dict["Operator ID"] = operator
        ins_dict["Company Name"] = company
        ins_dict["Analysed"] = analysed
        ins_dict["Printed"] = printed
        ins_dict["Sample ID"] = sampleid
        ins_dict["Instrument Number"] = instrument
        ins_dict["Analysis Type"] = analy_type
        ins_dict["Sample Weight"] = smpl_wght
        ins_dict["Calibration Method"] = calib
        n_dict = self.nitrogen_dict
        n_dict["% Nitrogen"] = float(n_per)
        n_dict["Nitrogen Retention Time"] = n_ret
        n_dict["Nitrogen Area"] = n_area
        c_dict = self.carbon_dict
        c_dict["% Carbon"] =float( c_per)
        c_dict["Carbon Retention Time"] = c_ret
        c_dict["Carbon Area"] = c_area
        # for key, value in ins_dict.items():
        #     print((key, value))
        # for key, value in n_dict.items():
        #     print((key, value))
        # for key, value in c_dict.items():
        #     print((key, value))
        return [ins_dict, n_dict, c_dict]


