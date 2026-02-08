from pymatgen.electronic_structure.plotter import DosPlotter
from pymatgen.io.vasp import Vasprun

v = Vasprun("vasprun.xml")
pdos = v.pdos
plotter = DosPlotter()
plotter.add_dos("Partial DOS", pdos)
#plotter.show(xlim=[-5, 5], ylim=[0, 4])
plotter.show()

