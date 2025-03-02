from pymatgen.analysis.phase_diagram import PhaseDiagram, PDPlotter, PDPlotter3D
from pymatgen.entries.computed_entries import ComputedEntry
from pymatgen.core.composition import Composition

# Define your own entries (example energies)
data = [
    (Composition("Nb"), 0),         
    (Composition("Al"), 0),         
    (Composition("C"), 0),         
    #(Composition("AlC3"), 0.5204),
    #(Composition("Al3C"), 0.95876),
    #(Composition("AlC"), 0.37991),
    #(Composition("AlC2"), 0.4352),
    #(Composition("Al2C"), -0.00047),
    (Composition("Al4C3"), -0.24388),
    #(Composition("Nb4C3"), -0.49094),
    (Composition("Nb2C"), -0.48502),
    (Composition("NbC"), -0.52754),
    #(Composition("Nb6C5"), -0.59103),
    #(Composition("Nb10C7"), -0.51065),
    (Composition("NbAl3"), -0.42786),
    (Composition("Nb2Al"), -0.27951),
    (Composition("Nb3Al"), -0.16807),
    #(Composition("NbAl"), -0.02857),
    #(Composition("Nb4Al"), -0.1001),
    (Composition("Nb3Al2C"), -0.46626),
    (Composition("Nb3AlC2"), -0.55387),
    (Composition("Nb2AlC"), -0.52188),
    (Composition("Nb4AlC3"), -0.56075),
]

# Create ComputedEntry objects for each entry
entries = [ComputedEntry(comp, energy, parameters ={"method": "DFT-PBE SCAN", "code": "VASP"}) for comp, energy in data]

# Create a PhaseDiagram object
pd = PhaseDiagram(entries)

# Plot the phase diagram
#plotter = PDPlotter(pd, show_unstable=True, Literal = "3d")
#plotter.show()

plotter = PDPlotter3D(pd, show_unstable=True)
plotter.show()