#!/c/Users/karth/anaconda3/python

"""
Use cif files to generate powder xrd patters
by default it plots 2Theta vs intensity using bar chart of matplotlib

-d                In command line argument outputs data insted of plot
-cut 50           Outputs data with a intsity cutoff .. 50 is given here 
-plotwithcut 50   Plots peks corresponding to intesities above cutoff

"""

from pymatgen.analysis.diffraction.xrd import XRDCalculator
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.core.structure import Structure
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import numpy as np
import sys
import os
import argparse
import warnings
warnings.simplefilter("ignore")
#
root = tk.Tk()
root.withdraw()
#file name choosing dialog box
#filename = filedialog.askopenfilename(title="select a file",filetypes=(("cif files","*.cif"),("all files","*.*")))
if len(sys.argv)  > 1:
        folder=os.getcwd()
        file_name=sys.argv[1]
        filename = os.path.join(folder, file_name)
else:
        filename = filedialog.askopenfilename(title="select a file",filetypes=(("cif files","*.cif"),("all files","*.*")))



def get_xrd(file):
  structure = Structure.from_file(file)
  sga = SpacegroupAnalyzer(structure)
  conventional_structure = sga.get_conventional_standard_structure()
  calculator = XRDCalculator(wavelength="CuKa")
  pattern = calculator.get_pattern(conventional_structure)
  return pattern


pattern = get_xrd(filename)

compound_name = os.path.splitext(os.path.basename(filename))[0]


parser = argparse.ArgumentParser(description="To choose output type.")
parser.add_argument("cif_file", type=str, help="Input CIF file")
parser.add_argument("-d","-data",'--d','--data', action="store_true", help="Avoid plot and print 2Theta and Intensity")
parser.add_argument("-cut", "--cut", type=int, help="Print 2Theta and Intensity with the given cut-off value")
parser.add_argument("-plotwithcut", "-PlotWithCut", "--plotwithcut", "--PlotWithCut", type=int, help="Print 2Theta and Intensity with the given cut-off value")

args = parser.parse_args()

if any(arg.startswith("-d") for arg in sys.argv):
    print("2Th   | I \n-----    ------")
    for x_val, y_val in zip(pattern.x, pattern.y):
        print(f"{x_val:.2f} | {y_val:.0f}")
elif any(arg.startswith("-cut") or arg.startswith("--cut") for arg in sys.argv):
    if args.cut is not None:
        cutoff = int(args.cut)  # Convert cut-off value to integer
        print("2Th   | I \n-----    ------")
        for x_val, y_val in zip(pattern.x, pattern.y):
            if y_val >= cutoff:
                print(f"{x_val:.2f} | {y_val:.0f}")
elif any(arg.startswith("-plotwithcut") or arg.startswith("--plotwithcut") for arg in sys.argv):
    if args.plotwithcut is not None:
        cutoff = int(args.plotwithcut)
        # Position=[]; Intensity=[];
        # for x_val, y_val in zip(pattern.x, pattern.y):
        #     if y_val >= cutoff:
        #         Position.append(x_val)
        #         Intensity.append(y_val)
        beyond_cutoff = pattern.y >= cutoff
        plt.clf()
        plt.bar(pattern.x[beyond_cutoff], pattern.y[beyond_cutoff], label=compound_name, width=0.25)
        plt.legend()
        plt.show()
else:
    plt.clf()
    plt.bar(pattern.x, pattern.y, label=compound_name, width=0.25)
    plt.legend()
    plt.show()
