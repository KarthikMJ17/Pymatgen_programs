
from pymatgen.io.vasp import Vasprun
from pymatgen.electronic_structure.plotter import DosPlotter

v = Vasprun("vasprun.xml")

dos = v.complete_dos

plotter = DosPlotter(sigma=0.05, zero_at_efermi=True)
#plotter.add_dos("Total DOS", dos)

for el in dos.get_element_dos():
    plotter.add_dos(str(el), dos.get_element_dos()[el])

plotter.show()
plotter.save_plot('partial_dos.pdf')