"""
########################################################################
The ghg.py module is defined by a single class to for one instrument at
the USDA Grassland Soil and Water Research Laboratory in Temple Texas.

The instrument is an SCION456 Gas Chromatogram (GC) Greenhouse Gas
Analyzer (GHG).
The analytes are Carbon Dioxide (CO2), Methane (CH4), and
Nitrous Oxide (N2O).
The SCION456 class's function will read a csv file containing the
analytical and instrumental metadata from a single sample run file.
The outputs are four dictionaries: Instrumental metadata, CO2 Results,
CH4 Results, & N2O Results.
########################################################################
"""

import pandas as pd

class SCION456():
    """
    This class represents the output file from the SCION456 GC.
    """
    def __init__(self, file_name):
        """
        generates dictionaries with keys for instrument info, CO2 data,
        CH4 data, N2O data, and totals.
        Args:
            file_name (.csv): Output csv file from instrument
        """
        self.file_name = file_name
        self.instrument_info = dict.fromkeys([
                         "Run File",
                         "Method",
                         "Sample ID ",
                         "Inject Date",
                         "Recalc Date",
                         "Operator",
                         "Workstation",
                         "Instrument",
                         "Run Mode",
                         "Peak Measurement",
                         "Calculation Type",
                         "Normalized?"])
        self.co2_data = dict.fromkeys(["Analyte Number",
                        "Peak Name",
                        "Channel",
                        "Retention Time",
                        "Results",
                        "Area"])
        self.ch4_data = dict.fromkeys(["Analyte Number",
                        "Peak Name",
                        "Channel",
                        "Retention Time",
                        "Results",
                        "Area"])
        self.n2o_data = dict.fromkeys(["Analyte Number",
                        "Peak Name",
                        "Channel",
                        "Retention Time",
                        "Results",
                        "Area"])
        self.totals = dict.fromkeys(["Result",
                                     "Area"])

    def data(self):
        """
        Opens csv file and appends data to appropriate dictionaries

        Returns:
            self.instrument_info: dictionary containing the instrument
            and run info
            self.co2_data: dictionary containing the analytical results
            for CO2
            self.ch4_data: dictionary contianing the analytical results
            for CH4
            self.n2o_data: dictionary containg the analytical totals for
            the run
        """
        with open(self.file_name) as file:
            lines = file.readlines()
            file.close()
        for line in lines:
            sline = line.rstrip("\n").split(",")
            for key in self.instrument_info.keys():
                if str(key) in sline:
                    self.instrument_info[key] = sline[1]
            if "1" in str(sline[0]):
                for key, value in zip(self.co2_data.keys(), sline):
                    self.co2_data[key] = value
            if "2" in str(sline[0]):
                for key, value in zip(self.ch4_data.keys(), sline):
                    self.ch4_data[key] = value
            if "3" in str(sline[0]):
                for key, value in zip(self.n2o_data.keys(), sline):
                    self.n2o_data[key] = value
            if "Totals" in str(sline[0]):
                self.totals["Result"] = sline[4]
                self.totals["Area"] = sline[5]
        # for key, value in self.instrument_info.items():
        #     print((key, value))
        # for key, value in self.co2_data.items():
        #     print((key, value))
        # for key, value in self.ch4_data.items():
        #     print((key, value))
        # for key, value in self.n2o_data.items():
        #     print((key, value))
        # for key, value in self.totals.items():
        #     print((key, value))
        return [self.instrument_info, self.co2_data, self.ch4_data, self.n2o_data, self.totals]
