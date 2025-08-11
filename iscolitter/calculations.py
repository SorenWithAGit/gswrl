import pandas as pd

def constants():
    # attributes of each field that remain constant
    field_constants = {
                        "field" : ["SW12", "SW17", "W1", 
                                "W6", "W10", "W12",
                                "W13", "Y2", "Y6", 
                                "Y8", "Y10", "Y13", 
                                "Y14"],
                        "area (ac)" : [2.97, 2.99, 174.00,
                                    42.30, 19.80, 9.90,
                                    11.30, 132.00, 16.30,
                                    20.80, 18.50, 11.40,
                                    5.60],
                        "landuse" : ["pasture", "pasture", "mixed",
                                    "mixed", "pasture", "cultivated",
                                    "cultivated", "mixed", "cultivated",
                                    "cultivated", "cultivated", "cultivated",
                                    "pasture"],
                        "1-bottle composite flow interval (mm)" : [1.32, 1.32, 1.32,
                                                                1.32, 1.32, 1.32,
                                                                1.32, 1.32, 1.32,
                                                                1.32, 1.32, 1.32,
                                                                1.32],
                        "sampling interval (ft3)" : [565.9, 565.9, 32890.2,
                                                    8000, 3735, 1864,
                                                    2132, 24868.2, 3076,
                                                    3915, 3496, 2132,
                                                    1056]
                        }

    # standard unit conversions
    mm_per_l = 1000
    mg_per_kg = 1000
    l_per_ft3 = 23.3168
    in_per_ft = 12
    mm_per_ft = 25.4
    ft_per_acre = 43560
    acre_per_hectare = 2.47105


    field_df = pd.DataFrame(field_constants)
    field_df["sampling interval (mgal)"] = field_df["sampling interval (ft3)"] * (1/133680.556)
