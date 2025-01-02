from readInstruments import *


sci = SCION456(r"C:\Users\john.sorensen\Box\programming\python\tillage\Dorothy Long Term Tillage\Summer 2020 Growing Season\3-7-2020 100's\CT 2 - 60.CSV")
data = sci.GHG_Data()
print(data)