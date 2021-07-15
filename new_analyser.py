from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import numpy as np
import os
import sys
 
print(sys.version)

# Process target directory
target_directory = "../../SRAM3/1/half/"
options     = target_directory.split("/")
options     = [i for i in options if i.isalnum()]
chip        = options[0]
exp_variant = options[1]
exp_size    = options[2]

log_names = [i for i in os.listdir(target_directory) if ".csv" in i]
print("git test")