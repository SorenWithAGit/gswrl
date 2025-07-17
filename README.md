# readInstruments
## Developed by John A. Sorensen

------------------------------------------------------------------------

A python package that will take the output file from an analytical<br>  
instrument at the USDA-ARS Grassland Soil Water Research Laboratory in<br> 
Temple, TX.

------------------------------------------------------------------------

------------------------------------------------------------------------

## Main.py is utilized by running it with parameters through the command 
## line (i.e. powershell, terminal, etc).

Using if, elif, try, and except statements based on the supplied<br>  
parameters will open all files in a designated folder matching a<br>  
supplied file type and concatenate into a Pandas DataFrame(s),<br>  
which can be exported to Excel if desired.<br>  

The parameters are<br>  
--input_path (required):<br>  
    the folder path containing the exported instrument runs to be<br>
    concatenated.<br>  
--file_type (required):<br>  
    file type of exported runs.<br>  
--module (required):<br>  
    which of the modules contained in gswrlinstruments corresponds to the<br>  
--m_class (required):<br>  
    the class that corresponds to the instrument the exported runs<br>  
    originated from.<br>  
--function (required):<br>  
    the function that corresponds to the exported run format<br>  
    (some classes may only have one function)<br>  
--output_path (optional):<br>  
    file path the concatenated data will save to. (include file name)

------------------------------------------------------------------------

------------------------------------------------------------------------
The cfa.py module is defined by two classes, one for each of two<br>  
instruments at the USDA Grassland Soil and Water Research Laboratory in<br>  
Temple Texas.<br>  

The San class is to be used with output data from an<br>  
Skalar San++ Continious Flow Analyzer (CFA).<br>  
The first of the two functions within this class is used for results<br>  
from a Deionized Water Extraction (DI) and the Haney Three Acid<br>  
Extraction (H3A.<br>  
Both extractions analyze Nitrate/Nitrite (NO3/NO2), Phosphate (PO4),<br>
and Ammonium (NH4).<br>  
The second function is for results of a KCL extraction where only<br>  
NO3/NO2 & NH4 are analyzed.<br>  
Both functions will output a Dataframe of the same format.<br>  

The AA500 class is another CFA at the station an AA500.<br>  
The output of this class's function is a dictionary containing the<br>  
instrument "metadata" and a Dataframe with the analytical data

------------------------------------------------------------------------

------------------------------------------------------------------------

The dry_combusion_cn.py module is defined by three classes, one for each<br>  
of three Dry Combustion Analyzers at the USDA Grassland Soil and Water<br>  
Research Laboratory in Temple Texas.<br>  

The ELIII class is to be used with data from an Elementar VARIO EL III<br>  
for Carbon (C), Nitrogen (N), and Sulfur (S).<br>  
The output of this class's data function is a dataframe containing the<br>  
(C, N, S) data from a single run.<br>  

The MaxCube class is to be used with data from an<br>  
Elementar VARIO Max Cube for (C, N) analysis.<br>  
The output of this class's data function is a dataframe containing the<br>  
(C, N) data from a single run.<br>  

The ThermoFlash class is to be used with data from an Thermo Scientific<br>  
Flash for (C, N) analysis.<br>  
The outputs of this class's data function are three dictionaries:<br>  
Instrumental Metadara, Nitrogen Results, and Carbon Results of a single<br>  
sample within a file.

------------------------------------------------------------------------

------------------------------------------------------------------------

The ghg.py module is defined by a single class to for one instrument at<br>  
the USDA Grassland Soil and Water Research Laboratory in Temple Texas.<br>  

The instrument is an SCION456 Gas Chromatogram (GC) Greenhouse Gas<br>  
Analyzer (GHG).<br>  
The analytes are Carbon Dioxide (CO2), Methane (CH4), and<br>  
Nitrous Oxide (N2O).<br>  
The SCION456 class's function will read a csv file containing the<br>  
analytical and instrumental metadata from a single sample run file.<br>  
The outputs are four dictionaries: Instrumental metadata, CO2 Results,<br>  
CH4 Results, & N2O Results.

------------------------------------------------------------------------

------------------------------------------------------------------------

The icp.py module is defined by two classes, one for each of two<br>  
instruments at the USDA Grassland Soil and Water Research Laboratory in<br>  
Temple Texas.<br>  

The agilent class is to be used with data from an Agilent 5110<br>  
Inductively Coupled Plasma - Optical Emission Spectrometer (ICP_OES).<br>  
The output of this class's data function is a dataframe containing the<br>  
analytical data for the following elements: Aluminium, Calcium, Copper,<br>  
Iron, Potassium, Magnesium, Manganese, Sodium, Phosphorus, Sulfur,<br>  
and Zinc.<br>  

The varian class is to be used with data from a Varian Vista MPX ICP-OES<br>  
that is no longer on station.<br>  
The output of this class's data function is a dataframe containing the<br>  
analytical data for the following elements: Aluminium, Arsenic, Calcium,<br>  
Iron, Potassium, Magnesium, Manganese, Phosphorus, Sulfur, Zinc, and<br>  
Ytrium

------------------------------------------------------------------------

------------------------------------------------------------------------

The liquid_toc.py module is defined by two classes, one for each of two<br>  
instruments at the USDA Grassland Soil and Water Research Laboratory in<br>  
Temple Texas.<br>  

The FormacsTOC class is to be used with data exported from the Skalar<br>  
FORMACS TOC/TN analyzer.<br>  
The Data function will return two items a pandas dataframe containing<br>  
the analytical data and a dictionary containing the instrument<br>  
"metadata" of the run.<br>  

The VarioTOC class like the first is for data from an Elementar Liquid<br>  
TOC/TN Analyzer.<br>  
THe output of this class's data function will match the output of the<br>  
FormacsTOC.data()

------------------------------------------------------------------------

------------------------------------------------------------------------

## Current instruments supported by module:

cfa.py:<br>  
    Skalar San ++ Continious Flow Analyzer<br>  
        Analytes: Nitrate/Nitrite, Phosphate, Ammonium<br>  
    AA500 Continious Flow Analyzer<br>  
        Analytes: Nitrate/Nitrite, Phosphate, Ammonium<br>  

dry_combustion_cn.py:<br>  
    Elementar Vario ELIII Dry Combustion Analyzer<br>  
        Analytes: Carbon, Nitrogen<br>  
    Elementar Vario Max Cube Dry Combustion Analyzer<br>  
        Analytes: Carbon, Nitrogen<br>  
    Thermo Flash Dry Combustion Analyzer<br>  
        Analytes: Carbon, Nitrogen<br>  

ghg.py:<br>  
    SCION456 Greenhouse Gas Gas Chromatograph Analyzer<br>  
        Analytes: Carbon Dioxide, Methane, Nitrious Oxide<br>  

icp.py:<br>  
    Varian Vista MPX Inductively Coupled Plasma - Optical Emission<br>  
    Spetrometer<br>  
        Analytes: Aluminium, Arsenic, Calcium, Iron, Potassium,<br>  
        Magnesium, Manganese, Phosphorus, Sulfur, Zinc, and Ytrium<br>  
    Agilient 5110 Inductively Coupled Plasma - Optical Emission 
    Spectrometer<br>  
        Analytes: Aluminium, Calcium, Copper, Iron, Potassium,<br>  
        Magnesium, Manganese, Sodium, Phosphorus, Sulfur, and Zinc<br>  

liquid_toc.py:<br>  
    Skalar Formacs Total Organic Carbon/Total Nitrogen liquid Analyzer<br>  
        Analytes: Total Carbon, Total Organic Carbon, Inorganic Carbon,<br>  
        Total Nitrogen<br>  
    Elementar Vario Total Organic Carbon/Total Nitrogen Liquid Analyzer<br>  
        Analaytes: Total Organic Carbon, Total Nitrogen<br>  
