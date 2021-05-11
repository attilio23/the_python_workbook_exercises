##
#Show the chemical elements whose name can only be written using the element symbols
#The following list contains the name of the chemical elements
name_chemical_elements = ["Actinium", "Aluminium", "Americium", "Antimony", "Argon", \
"Arsenic", "Astatine", "Barium", "Berkelium", "Beryllium", "Bismuth", "Bohrium", "Boron", \
"Bromine", "Cadmium", "Caesium", "Calcium", "Californium", "Carbon", "Cerium", "Chlorine", \
"Chromium", "Cobalt", "Copernicium", "Copper", "Curium", "Darmstadtium", "Dubnium", \
"Dysprosium", "Einsteinium", "Erbium", "Europium", "Fermium", "Flerovium", "Fluorine", \
"Francium", "Gadolinium", "Gallium", "Germanium", "Gold", "Hafnium", "Hassium", "Helium", "Holmium", \
"Hydrogen", "indium", "Iodine", "Iridium", "Iron", "Krypton", "Lanthanum", "Lawrencium", \
"Lead", "Lithium", "Livermorium", "Lutetium", "Magnesium", "Manganese", "Meitnerium", \
"Mendelevium", "Mercury", "Molybdenum", "Moscovium", "Neodymium", "Neon", "Neptunium", \
"Nickel", "Nihonium", "Niobium", "Nitrogen", "Nobelium", "Oganesson", "Osmium", "Oxygen", \
"Palladium", "Phosphorus", "Platinum", "Plutonium", "Polonium", "Potassium", "Praseodymium", \
"Promethium", "Protactinium", "Radium", "Radon", "Rhenium", "Rhodium", "Roentgenium", \
"Rubidium", "Ruthenium", "Rutherfordium", "Samarium", "Scandium", "Seaborgium", "Selenium", \
"Silicon", "Silver", "Sodium", "Strontium", "Sulfur", "Tantalum", "Technetium", "Tellurium", \
"Tennessine", "Terbium", "Thallium", "Thorium", "Thulium", "Tin", "Titanium", "Tungsten", \
"Uranium", "Vanadium", "Xenon", "Ytterbium", "Yttrium", "Zinc", "Zirconium"]
#The following list contains the element symbols
symbols_chemical_elements = ["Ac", "Al", "Am", "Sb", "Ar", "As", "At", "Ba", "Bk", \
"Be", "Bi", "Bh", "B", "Br", "Cd", "Cs", "Ca", "Cf", "C", "Ce", "Cl", "Cr", "Co", "Cn", \
"Cu", "Cm", "Ds", "Db", "Dy", "Es", "Er", "Eu", "Fm", "Fl", "F", "Fr", "Gd", "Ga", "Ge", \
"Au", "Hf", "Hs", "He", "Ho", "H", "In", "I", "Ir", "Fe", "Kr", "La", "Lr", "Pb", "Li", "Lv", \
"Lu", "Be", "Mn", "Mt", "Md", "Hg", "Mo", "Mc", "Nd", "Ne", "Np", "Ni", "Nh", "Nb", "N", \
"No", "Og", "Os", "O", "Pd", "P", "Pt", "Pu", "Po", "K", "Pr", "Pm", "Pa", "Ra", "Rn", "Re", "Rh", "Rg", \
"Rb", "Ru", "Rf", "Sm", "Sc", "Sg", "Se", "Si", "Ag", "Na", "Sr", "S", "Ta", "Tc", "Te", "Ts", \
"Tb", "Tl", "Th", "Tm", "Sn", "Ti", "W", "U", "V", "Xe", "Yb", "Y", "Zn", "Zr"]
## Determine chemical element name using only elements symbols
# @param n_e_c the name of the chimical element
# @param s_c_e the list contanining the elements symbols
# @return the name of the chimical element using only elements symbols
def spellingElementSymbols(n_e_c, s_c_e):
    if n_e_c in s_c_e:
        return n_e_c
    else:
        try:
            if n_e_c[0:2] in s_c_e:
                return n_e_c[0:2] + spellingElementSymbols(n_e_c[2:].capitalize(), s_c_e)
            if n_e_c[0] in s_c_e:
                return n_e_c[0] + spellingElementSymbols(n_e_c[1:].capitalize(), s_c_e) 
            return False                                   
        except TypeError:
            return False 
# Demonstrate the spellingElementSymbols function                           
def main():
    n_pn = {}
    for name in name_chemical_elements:
        t_s = spellingElementSymbols(name, symbols_chemical_elements)
        if t_s:
            n_pn[name] = t_s
    for k in n_pn:
        print("%s can be spelled as %s"%(k, n_pn[k]))
# Call the main function                     
main()
