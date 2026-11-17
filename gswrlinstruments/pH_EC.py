import io
import pandas as pd

class accument450():

    def __init__(self, data_file):

        self.file_name = data_file

    def data(self):
        pH_col = ["Log_Index", "Measurement_Date", "Measurement_Time", "Measurement_AM/PM",
                                        "Read_Mode", "Meter_Model", "Meter_Serial_#", "Firmware_Version", "Export_Date", "Export_time",
                                        "Export_AM/PM", "Measurement_Mode", "pH_Value", "Primary_Unit", "Raw_Potential_(mV)",
                                        "Potential_Unit", "Temperature_Value", "Temperature_Unit", "Temp_Compensation_&_Channel",
                                        "Electrode_Slope", "Slope_Unit", "Instrument_Sample_Name", "Measurement_Duration", "Probe/Electrode_ID",
                                        "Last_calibration_Date", "Last_Calibration_Time", "Last_Calibration_AM/PM",
                                        "Next_Calibration"]

        EC_col = ["Log_Index", "Measurement_Date", "Measurement_Time", "Measurement_AM/PM",
                                        "Read_Mode", "Meter_Model", "Meter_Serial_#", "Firmware_Version", "Export_Date", "Export_time",
                                        "Export_AM/PM", "Measurement_Mode", "Temp-Compensated_Conductivity", "Conductivity_Unit",
                                         "Temperature_Value", "Temperature_Unit", "Temp_Compensation_&_Channel", "Raw_Conductance",
                                         "Raw_Conductance_Unit", "Nominal_Cell_Constant", "Nominal_Cell_Constant_Unit",
                                         "Actual_Cell_Constant", "Actual_Cell_Constant_Unit", "Instrument_Sample_Name", "Measurement_Duration",
                                         "Probe/Electrode_ID", "Last_Calibration_Date", "Last_Calibration_Time",
                                         "Last_Calibration_AM/PM", "Next_Calibration"]

        pH_EC_col = ["Log_Index", "Measurement_Date", "Measurement_Time", "Measurement_AM/PM",
                                           "Read_Mode", "Meter_Model", "Meter_Serial_#", "Firmware_Version", "Export_Date", "Export_time",
                                           "Export_AM/PM", "Measurement_Mode", "pH_Value", "Primary_Unit", "Raw_Potential_(mV)",
                                           "Potential_Unit", "Temperature_Value", "Temperature_Unit", "Temp_Compensation_&_Channel",
                                           "Electrode_Slope", "Slope_Unit", "Instrument_Sample_Name", "Measurement_Duration", "Probe/Electrode_ID",
                                           "Last_Calibration_Date", "Last_Calibration_Time", "Last_Calibration_AM/PM",
                                           "Next_Calibration", "Measurement_Mode", "Temp-Compensated_Conductivity", "Conductivity_Unit",
                                           "Temperature_Value", "Temperature_Unit", "Temp_Compensation_&_Channel", "Raw_Conductance",
                                           "Raw_Conductance_Unit", "Nominal_Cell_Constant", "Nominal_Cell_Constant_Unit",
                                           "Actual_Cell_Constant", "Actual_Cell_Constant_Unit", "Instrument_Sample_Name", "Measurement_Duration",
                                           "Probe/Electrode_ID", "Last_Calibration_Date", "Last_Calibration_Time",
                                           "Last_Calibration_AM/PM", "Next_Calibration"]
        
        pH_df = pd.DataFrame(columns = pH_col)
        
        EC_df = pd.DataFrame(columns = EC_col)

        pH_EC_df = pd.DataFrame(columns = pH_EC_col)


        with open(self.file_name) as file:
            lines = file.readlines()
            for line in lines:
                values = line.split(",")
                values = values[:-1]
                values = [val for val in values if val != "Remaining"]
                # print(len(values))
                # print(values)

                if len(values) == len(pH_col):
                    new_row = pd.DataFrame([values], columns = pH_col)
                    pH_df = pd.concat([pH_df, new_row], ignore_index = True)

                elif len(values) == len(EC_col):
                    new_row = pd.DataFrame([values], columns = EC_col)
                    EC_df = pd.concat([EC_df, new_row], ignore_index = True)

                elif len(values) == len(pH_EC_col):
                    new_row = pd.DataFrame([values], columns = pH_EC_col)
                    pH_EC_df = pd.concat([pH_EC_df, new_row], ignore_index = True)

            pH_df.insert(loc = 0, column = "data type", value = "pH")
            EC_df.insert(loc = 0, column = "data type", value = "EC")
            pH_EC_df.insert(loc = 0, column = "data type", value = "pH & EC")

            return [df for df in [pH_df, EC_df, pH_EC_df] if not df.empty]

    def excel_export(self, result_dfs, output_path):
            valid_dfs = [df for df in result_dfs if df is not None and not df.empty]
    
            if not valid_dfs:
                print("All DataFrames are empty. No Excel file was created.")
                return

            with pd.ExcelWriter(output_path) as writer:
                for df in valid_dfs:
                    sheet_name = str(df.iloc[:, 0].unique()[0])
                    
                    df.to_excel(writer, sheet_name=sheet_name, index=False)


file_path = r"D:\DATA_LOG\datalog.csv"
output_path = r"I:\programming\pH_EC_example_results.xlsx"

accu = accument450(file_path)

results = accu.data()
print(type(results))
for df in results:
    print(df)

accu.excel_export(results, output_path)