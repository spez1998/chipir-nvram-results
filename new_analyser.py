from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import numpy as np
import os
import sys

# Process target directory
#targetDir_fullpath = "C:/Users/Sujit/Documents/STFC/Code/Mikroe/nvRAM_experiment/results/live/SRAM3/1/half/"
#targetDir_trunc = targetDir_fullpath.split("/")[-3:]

class Analyser:
    def __init__(self, targetDir_fullpath):
        targetDir_trunc = targetDir_fullpath.split("/")[-3:]
        self.chip    = targetDir_trunc[0]
        self.variant = targetDir_trunc[1]
        self.size    = targetDir_trunc[2]
        log_names = os.listdir(targetDir_fullpath)
        self.log_names = [targetDir_fullpath+i for i in os.listdir(targetDir_fullpath) if ".csv" in i]
        self.log_names.sort(key=os.path.getmtime)

    def getData(self):
        self.data = pd.read_csv(self.log_names[0], error_bad_lines=False)
        for i in range(1, len(self.log_names)):
            print("\n")
            #print(self.log_names[i])
            self.data_next = pd.read_csv(self.log_names[i], error_bad_lines=False)
            self.data_frames = [self.data, self.data_next]
            self.data = pd.concat(self.data_frames, ignore_index=True)

Analyser = Analyser("C:/Users/Sujit/Documents/STFC/Code/Mikroe/nvRAM_experiment/results/live/SRAM3/1/half/")
Analyser.getData()
print(Analyser.data)