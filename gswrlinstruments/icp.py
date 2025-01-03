"""
########################################################################
The icp.py module is defined by two classes, one for each of two
instruments at the USDA Grassland Soil and Water Research Laboratory in
Temple Texas.

The agilent class is to be used with data from an Agilent 5110
Inductively Coupled Plasma - Optical Emission Spectrometer (ICP_OES).
The output of this class's data function is a dataframe containing the
analytical data for the following elements: Aluminium, Calcium, Copper,
Iron, Potassium, Magnesium, Manganese, Sodium, Phosphorus, Sulfur,
and Zinc.

The varian class is to be used with data from a Varian Vista MPX ICP-OES
that is no longer on station.
The output of this class's data function is a dataframe containing the
analytical data for the following elements: Aluminium, Arsenic, Calcium,
Iron, Potassium, Magnesium, Manganese, Phosphorus, Sulfur, Zinc, and
Ytrium
########################################################################
"""


import pandas as pd

class agilent():
    """
    This class represents the output file from the Agilent 5110.
    """
    def __init__(self, file_name):
        """
        reads the excel data as a pandas.DataFrame

        Args:
            file_name (.xlsx): output excel file from instrument
        """
        self.file_name = file_name
        self.run_df = pd.read_excel(self.file_name)

    def data(self):
        """
        This function manipulates the self.run_df DataFrame.

        Returns:
            df: pandas.DataFrame containing the analytical results from
            the run.
        """
        drop_lst = ["S1:1", "S1:2", "S1:3", "S1:4", "S1:5"]
        drop_indexes = []
        for ind in range(len(self.run_df)):
            if str(self.run_df.iloc[ind]["Rack:Tube"]) in drop_lst:
                drop_indexes.append(ind)
        df = self.run_df.drop(drop_indexes, axis = 0)
        df = df.drop(["Rack:Tube"], axis = 1)
        df = df.rename(columns = {
            df.columns[1] : "Aluminium (ppm)",
            df.columns[2] : "Calcium (ppm)",
            df.columns[3] : "Copper (ppm)",
            df.columns[4] : "Iron (ppm)",
            df.columns[5] : "Potassium (ppm)",
            df.columns[6] : "Magnesium (ppm)",
            df.columns[7] : "Manganese (ppm)",
            df.columns[8] : "Sodium (ppm)",
            df.columns[9] : "Phosphorus (ppm)",
            df.columns[10] : "Sulfur (ppm)",
            df.columns[11] : "Zinc (ppm)"})
        return df

class varian():
    """
    This class represents the output file from the Varian Vista MPX.
    """
    def __init__(self, file_name):
        """
        Reads the output file as a pandas.DataFrame

        Args:
            file_name (.xls, .xlsx): output excel file from instrument.
        """
        self.file_name = file_name
        self.run_df = pd.read_excel(self.file_name)

    def data(self):
        """
        Manipulates the self.run_df so only analytical data for samples
        is displayed.

        Returns:
            df: pandas.DataFrame containing analytical data from run.
        """
        drop_lst = [
            "Blank",
            "0.1ppmCation",
            "0.1ppmAnion",
            "1.0ppmCation",
            "1.0ppmAnion",
            "10ppmCation",
            "10ppmAnion",
            "100ppmCation",
            "100ppmAnion",
            "CHECKCATION",
            "CHECKANION"]
        drop_indexes = []
        for ind in range(len(self.run_df)):
            if str(str(self.run_df.iloc[ind]["Sample Labels"]).replace(" ", "")) in drop_lst:
                drop_indexes.append(ind)
        blank_indexes = self.run_df[self.run_df["Sample Labels"].isna()].index
        df = self.run_df.drop(drop_indexes, axis = 0)
        df = df.drop(blank_indexes, axis = 0)
        df = df.drop(["Tube"], axis = 1)
        df = df.rename(columns = {
            df.columns[1] : "Aluminium (ppm)",
            df.columns[2] : "Arsenic (ppm)",
            df.columns[3] : "Calcium (ppm)",
            df.columns[4] : "Iron (ppm)",
            df.columns[5] : "Potassium (ppm)",
            df.columns[6] : "Magnesium (ppm)",
            df.columns[7] : "Manganese (ppm)",
            df.columns[8] : "Phosphorus (ppm)",
            df.columns[9] : "Sulfur (ppm)",
            df.columns[10] : "Zinc (ppm)",
            df.columns[11] : "Ytrium (ppm)"})
        return df
