#!/usr/bin/env python3

import shutil
import os

# import additional code to complete our task
os.chdir("/home/student/mycode/")

# move into the working directory
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# copy the fileA to fileB
shutil.copytree("5g_research/", "5g_research_backup/")

# copy the entire directoryA to directoryB
shutil.copytree("5g_research/", "5g_research_backup/")
