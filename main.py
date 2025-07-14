import gswrlinstruments as gs
import argparse
import glob
import pandas as pd
from pathlib import Path

def main(input_path, file_type, module_name, class_name, class_func) -> None:
    
    files = glob.glob(str(input_path) + "//" + "*." + str(file_type), recursive = True)
    
    ####################################################################
    #Logic to differentiate arguments passed for CFA Data.
    if module_name == "cfa" and class_name == "San" and class_func == "DI_H3A_Data":
        DI_H3A_df = pd.DataFrame(columns = [
            "SampleIdentity",
            "Nitrate Nitrite- Results[mg N/liter]",
            "Phosphate- Results[mg P/liter]",
            "Ammonia- Results[mg N/liter]" ])
        
        for file in files:
            run = gs.cfa.San(file)
            data = run.DI_H3A_data()
            DI_H3A_df = pd.concat([DI_H3A_df, data])
    
    elif module_name == "cfa" and class_name == "San" and class_func == "KCL_data":
        KCl_df = pd.DataFrame(columns = [
            "SampleIdentity",
            "Nitrate Nitrite- Results[mg N/liter]",
            "Phosphate- Results[mg P/liter]",
            "Ammonia- Results[mg N/liter]" ])
        
        for file in files:
            run = gs.cfa.San(file)
            data = run.KCL_data()
            KCl_df  = pd.concat(KCl_df, data)

    elif module_name == "cfa" and class_name == "AA500" and class_func == "data":
        AA500_df = pd.DataFrame(columns = [
             "Sample ID",
             "Nitrate/Nitrite",
             "Phosphate",
             "Ammonium"])
        
        for file in files:
            run = gs.cfa.AA500(file)
            data = run.data()
            AA500_df = pd.concat([AA500_df, data[1]])
    ####################################################################

    ####################################################################
    # Logic to differentiate arguments passed for Dry Combustion Data
    if module_name == "drycombustion" and class_name == "ELIII" and class_func == "data":
        eliii_df = pd.DataFrame(columns = [
            "Sample Name",
            "Date/Time",
            "Weight (mg)",
            "N Area",
            "C Area",
            "%N",
            "%C",
            "CN Ratio" ])
        for file in files:
            run = gs.drycombustion.ELIII(file)
            data = run.data()
            eliii_df = pd.concat([eliii_df, data])

    elif module_name == "drycombustion" and class_name == "MaxCube" and class_func == "excel_data":
        max_excel_df = pd.DataFrame(columns = [
            "Sample Name",
            "Date/Time",
            "Weight (mg)",
            "N Area",
            "C Area",
            "%N",
            "%C",
            "CN Ratio" ])
        for file in files:
            run = gs.drycombustion.MaxCube(file)
            data = run.excel_data()
            max_excel_df = pd.concat([max_excel_df, data])

    elif module_name == "drycombustion" and class_name == "MaxCube" and class_func == "csv_data":
        max_csv_df = pd.DataFrame(columns = [
            "Sample Name",
            "Date/Time",
            "Weight (mg)",
            "N Area",
            "C Area",
            "%N",
            "%C",
            "CN Ratio" ])       
        for file in files:
            run = gs.drycombustion.MaxCube(file)
            data = run.csv_data()
            max_csv_df = pd.concat([max_csv_df, data])

    #Save for Thermo Data

    ####################################################################

    ####################################################################
    
    #Save for GHG Data

    ####################################################################

    ####################################################################
    # Logic to differentiate arguments passed for liquid TOC Data.
    if module_name == "liquidtoc" and class_name == "FormacsTOC" and class_func == "data":
        toc_df = pd.DataFrame(columns = [
            "Sample ID",
            "TC Area",
            "IC Area",
            "TN Area",
            "TOC (ppm)",
            "TC (ppm)",
            "TC (ppm)",
            "IC (ppm)",
            "TN (ppm)"])
        for file in files:
            run = gs.liquidtoc.FormacsTOC(file)
            data = run.data()
            toc_df = pd.concat([toc_df, data[0]])
    ####################################################################

    ####################################################################
    # Logic to differentiate arguments passed for ICP Data.
    if module_name == "icp" and class_name == "agilent" and class_func == "data":
        agilent_df = pd.DataFrame(columns = [
            "Solution Label",
            "Aluminium (ppm)",
            "Calcium (ppm)",
            "Copper (ppm)",
            "Iron (ppm)",
            "Potassium (ppm)"
            "Magnesium (ppm)"
            "Manganese (ppm)"
            "Sodium (ppm)", 
            "Phosphorus (ppm)",
            "Sulfur (ppm)",
            "Zinc (ppm)" ])
    
        for file in files:
            icp_agilent = gs.icp.agilent(file)
            data = icp_agilent.data()
            agilent_df = pd.concat([agilent_df, data])
        print(agilent_df)

    elif module_name == "icp" and class_name == "varian" and class_func == "data":
        varian_df = pd.DataFrame(columns = [
            "Sample Labels",    
            "Aluminium (ppm)",
            "Arsenic (ppm)",
            "Calcium (ppm)",
            "Iron (ppm)",
            "Potassium (ppm)"
            "Magnesium (ppm)"
            "Manganese (ppm)"
            "Phosphorus (ppm)",
            "Sulfur (ppm)",
            "Zinc (ppm)",
            "Ytrium (ppm)" ])
        
        for file in files:
            icp_varian = gs.icp.varian(file)
            data = icp_varian.data()
            varian_df = pd.concat([varian_df, data])
        print(varian_df)
    ####################################################################


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path",
                        type = Path,
                        required = True,
                        help = "Path to read data from folder")
    parser.add_argument("--file_type",
                        type = str,
                        required = True)
    parser.add_argument("--module_name",
                        type = str,
                        required = True)
    parser.add_argument("--class_name",
                        type = str,
                        required = True)
    parser.add_argument("--class_func",
                        type = str,
                        required = True)
    args = parser.parse_args()
    main(args.input_path, args.file_type, args.module_name, args.class_name, args.class_func)