# readInstruments
# Developed by John A. Sorensen

------------------------------------------------------------------------

A python package that will take the output file from an analytical 
instrument at the USDA-ARS Grassland Soil Water Research Laboratory in 
Temple, TX.

------------------------------------------------------------------------

## Main.py is utilized by running it with parameters through the command 
## line (i.e. powershell, terminal, etc).

Using if, elif, try, and except statements based on the supplied
parameters will open all files in a designated folder matching a 
supplied file type and concatenate into a Pandas DataFrame(s), 
which can be exported to Excel if desired.

The parameters are
--input_path (required): 
    the folder path containing the exported instrument runs to be 
    concatenated.
--file_type (required): 
    file type of exported runs.
--module (required): 
    which of the modules contained in gswrlinstruments corresponds to the
--m_class (required):
    the class that corresponds to the instrument the exported runs 
    originated from.
--function (required):
    the function that corresponds to the exported run format
    (some classes may only have one function)
--output_path (optional):
    file path the concatenated data will save to. (include file name)

------------------------------------------------------------------------

------------------------------------------------------------------------
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

------------------------------------------------------------------------

------------------------------------------------------------------------

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

------------------------------------------------------------------------

------------------------------------------------------------------------

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

------------------------------------------------------------------------

------------------------------------------------------------------------

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

------------------------------------------------------------------------

------------------------------------------------------------------------

The liquid_toc.py module is defined by two classes, one for each of two
instruments at the USDA Grassland Soil and Water Research Laboratory in
Temple Texas.

The FormacsTOC class is to be used with data exported from the Skalar
FORMACS TOC/TN analyzer.
The Data function will return two items a pandas dataframe containing
the analytical data and a dictionary containing the instrument
"metadata" of the run.

The VarioTOC class like the first is for data from an Elementar Liquid
TOC/TN Analyzer.
THe output of this class's data function will match the output of the
FormacsTOC.data()

------------------------------------------------------------------------

------------------------------------------------------------------------

## Current instruments supported by module:

cfa.py:
    Skalar San ++ Continious Flow Analyzer
        Analytes: Nitrate/Nitrite, Phosphate, Ammonium
    AA500 Continious Flow Analyzer
        Analytes: Nitrate/Nitrite, Phosphate, Ammonium

dry_combustion_cn.py:
    Elementar Vario ELIII Dry Combustion Analyzer
        Analytes: Carbon, Nitrogen
    Elementar Vario Max Cube Dry Combustion Analyzer
        Analytes: Carbon, Nitrogen
    Thermo Flash Dry Combustion Analyzer
        Analytes: Carbon, Nitrogen

ghg.py:
    SCION456 Greenhouse Gas Gas Chromatograph Analyzer
        Analytes: Carbon Dioxide, Methane, Nitrious Oxide

icp.py:
    Varian Vista MPX Inductively Coupled Plasma - Optical Emission Spetrometer
        Analytes: Aluminium, Arsenic, Calcium, Iron, Potassium, Magnesium, Manganese, Phosphorus, Sulfur, Zinc, and Ytrium
    Agilient 5110 Inductively Coupled Plasma - Optical Emission Spectrometer
        Analytes: Aluminium, Calcium, Copper, Iron, Potassium, Magnesium, Manganese, Sodium, Phosphorus, Sulfur, and Zinc

liquid_toc.py:
    Skalar Formacs Total Organic Carbon/Total Nitrogen liquid Analyzer
        Analytes: Total Carbon, Total Organic Carbon, Inorganic Carbon, Total Nitrogen
    Elementar Vario Total Organic Carbon/Total Nitrogen Liquid Analyzer
        Analaytes: Total Organic Carbon, Total Nitrogen
