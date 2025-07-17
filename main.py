import gswrlinstruments as gs
import argparse
import glob
import pandas as pd
from pathlib import Path

def main(input_path, file_type, module, m_class, function, output_path):
    
    files = glob.glob(str(input_path) + "//" + "*." + str(file_type), recursive = True)
    
    ####################################################################
    # Logic to differentiate arguments passed for CFA Data.
    if module == "cfa" and m_class == "San" and function == "DI_H3A_Data":
        DI_H3A_df = pd.DataFrame(columns = [
            "SampleIdentity",
            "Nitrate Nitrite- Results[mg N/liter]",
            "Phosphate- Results[mg P/liter]",
            "Ammonia- Results[mg N/liter]" ])
        
        for file in files:
            run = gs.cfa.San(file)
            data = run.DI_H3A_data()
            DI_H3A_df = pd.concat([DI_H3A_df, data])
        if args.output_path is not None:
                with pd.ExcelWriter(output_path) as writer:
                    DI_H3A_df.to_excel(writer, index = False)
        return DI_H3A_df
    
    elif module == "cfa" and m_class == "San" and function == "KCL_data":
        KCl_df = pd.DataFrame(columns = [
            "SampleIdentity",
            "Nitrate Nitrite- Results[mg N/liter]",
            "Phosphate- Results[mg P/liter]",
            "Ammonia- Results[mg N/liter]" ])
        
        for file in files:
            run = gs.cfa.San(file)
            data = run.KCL_data()
            KCl_df  = pd.concat([KCl_df, data])
        if args.output_path is not None:
                with pd.ExcelWriter(output_path) as writer:
                    KCl_df.to_excel(writer, index = False)
        return KCl_df

    elif module == "cfa" and m_class == "AA500" and function == "data":
        AA500_df = pd.DataFrame(columns = [
             "Sample ID",
             "Nitrate/Nitrite",
             "Phosphate",
             "Ammonium"])
        
        for file in files:
            run = gs.cfa.AA500(file)
            data = run.data()
            AA500_df = pd.concat([AA500_df, data[1]])
        if args.output_path is not None:
            with pd.ExcelWriter(output_path) as writer:
                AA500_df.to_excel(writer, index = False)
        return AA500_df
    ####################################################################

    ####################################################################
    # Logic to differentiate arguments passed for Dry Combustion Data
    if module == "drycombustion" and m_class == "ELIII" and function == "data":
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
        if args.output_path is not None:
                with pd.ExcelWriter(output_path) as writer:
                    eliii_df.to_excel(writer, index = False)
        return eliii_df

    elif module == "drycombustion" and m_class == "MaxCube" and function == "excel_data":
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
        if args.output_path is not None:
                with pd.ExcelWriter(output_path) as writer:
                    max_excel_df.to_excel(writer, index = False)
        return max_excel_df

    elif module == "drycombustion" and m_class == "MaxCube" and function == "csv_data":
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
        if args.output_path is not None:
                with pd.ExcelWriter(output_path) as writer:
                    max_csv_df.to_excel(writer, index = False)
        return max_csv_df

    elif module == "drycombustion" and m_class == "ThermoFlash" and function == "data":
        instrument_df = pd.DataFrame(columns = ["Method Name",
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
        nitrogen_df = pd.DataFrame(columns = ["Sample ID",
                                            "% Nitrogen",
                                            "Nitrogen Retention Time",
                                            "Nitrogen Area"])
        carbon_df = pd.DataFrame(columns = ["Sample ID",
                                          "% Carbon",
                                          "Carbon Retention Time",
                                          "Carbon Area"])
        for file in files:
            try:
                run = gs.drycombustion.ThermoFlash(file)
                ins_data = run.data()[0]
                n_data = run.data()[1]
                c_data = run.data()[2]
                instrument_df = pd.concat([instrument_df, ins_data]).reset_index(drop = True)
                nitrogen_df = pd.concat([nitrogen_df, n_data]).reset_index(drop = True)
                carbon_df = pd.concat([carbon_df, c_data]).reset_index(drop = True)
            except:
                 print("Unable to read file: " + file)
        if args.output_path is not None:
                with pd.ExcelWriter(output_path) as writer:
                    instrument_df.to_excel(writer, sheet_name = "Instrument Info", index = True)
                    nitrogen_df.to_excel(writer, sheet_name = "Nitrogen Data", index = True)
                    carbon_df.to_excel(writer, sheet_name = "Carbon Data", index = True)
        return [instrument_df, nitrogen_df, carbon_df]
    ####################################################################

    ####################################################################
    # Logic for Greenhouse Gas Data
    if module == "ghg" and m_class == "SCION456" and function == "data":
        instrument_info = pd.DataFrame(columns = [
                         "Run File",
                         "Method",
                         "Sample ID",
                         "Inject Date",
                         "Recalc Date",
                         "Operator",
                         "Workstation",
                         "Instrument",
                         "Run Mode",
                         "Peak Measurement",
                         "Calculation Type",
                         "Normalized?"])
        co2_data = pd.DataFrame(columns = [
                        "Analyte Number",
                        "Peak Name",
                        "Channel",
                        "Retention Time",
                        "Results",
                        "Area"])
        ch4_data = pd.DataFrame(columns = ["Analyte Number",
                        "Peak Name",
                        "Channel",
                        "Retention Time",
                        "Results",
                        "Area"])
        n2o_data = pd.DataFrame(columns = ["Analyte Number",
                        "Peak Name",
                        "Channel",
                        "Retention Time",
                        "Results",
                        "Area"])
        for file in files:
            run = gs.ghg.SCION456(file)
            instrument_run_data = run.data()[0]
            co2_run_data = run.data()[1]
            ch4_run_data = run.data()[2]
            n2o_run_data = run.data()[3]
            instrument_info = pd.concat([instrument_info, instrument_run_data]).reset_index(drop = True)
            co2_data = pd.concat([co2_data, co2_run_data]).reset_index(drop = True)
            ch4_data = pd.concat([ch4_data, ch4_run_data]).reset_index(drop = True)
            n2o_data = pd.concat([n2o_data, n2o_run_data]).reset_index(drop = True)
        if args.output_path is not None:
            with pd.ExcelWriter(output_path) as writer:
                    instrument_info.to_excel(writer, sheet_name = "Instrument Info", index = True)
                    co2_data.to_excel(writer, sheet_name = "CO2 Data", index = True)
                    ch4_data.to_excel(writer, sheet_name = "CH4 Data", index = True)
                    n2o_data.to_excel(writer, sheet_name = "N2O Data", index = True)
        return [instrument_info, co2_data, ch4_data, n2o_data]
    ####################################################################

    ####################################################################
    # Logic to differentiate arguments passed for ICP Data.
    if module == "icp" and m_class == "agilent" and function == "data":
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
        if args.output_path is not None:
                with pd.ExcelWriter(output_path) as writer:
                    agilent_df.to_excel(writer, index = False)
        return agilent_df

    elif module == "icp" and m_class == "varian" and function == "data":
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
        if args.output_path is not None:
                with pd.ExcelWriter(output_path) as writer:
                    varian_df.to_excel(writer, index = False)
        return varian_df
    ####################################################################

    ####################################################################
    # Logic to differentiate arguments passed for liquid TOC Data.
    if module == "liquidtoc" and m_class == "FormacsTOC" and function == "data":
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
            data = run.data()[0]
            toc_df = pd.concat([toc_df, data])
        if args.output_path is not None:
                with pd.ExcelWriter(output_path) as writer:
                    toc_df.to_excel(writer, index = False)
        return toc_df
    
    elif module == "liquidtoc" and m_class == "VarioTOC" and function == "data":
        analytical_data = pd.DataFrame(columns = [
                                                "No. ",
                                                "Hole  Pos.",
                                                "Name  ",
                                                "Method  ",
                                                "Coefficients  ",
                                                "NPOC vol. [ml]",
                                                "NPOC  Area"
                                                "TNb  Area",
                                                "NPOC [mg/l]",
                                                "TNb [mg/l]"
                                                ])
        for file in files:
            run = gs.liquidtoc.VarioTOC(file)
            data = run.data()
            analytical_data = pd.concat([analytical_data, data])
        analytical_data = analytical_data.reset_index(drop = True)
        if args.output_path is not None:
             with pd.ExcelWriter(output_path) as writer:
                  analytical_data.to_excel(writer, index = False)
        return analytical_data
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
    parser.add_argument("--module",
                        type = str,
                        required = True)
    parser.add_argument("--m_class",
                        type = str,
                        required = True)
    parser.add_argument("--function",
                        type = str,
                        required = True)
    parser.add_argument("--output_path",
                        type = str,
                        required = False)
    args = parser.parse_args()
    main(args.input_path, args.file_type, args.module, args.m_class, args.function, args.output_path)