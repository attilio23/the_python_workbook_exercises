##
# Find the longest sequence of elements starting with the chemical element entered from the user, so that each
# element follows an element whose last letter coincides with its first letter; the sequence cannot contain duplicates
# The following list contains the name of the chemical elements
c_e_l = ["Actinium", "Aluminium", "Americium", "Antimony", "Argon", \
"Arsenic", "Astatine", "Barium", "Berkelium", "Beryllium", "Bismuth", "Bohrium", "Boron", \
"Bromine", "Cadmium", "Caesium", "Calcium", "Californium", "Carbon", "Cerium", "Chlorine" , \
"Chromium", "Cobalt", "Copernicium", "Copper", "Curium", "Darmstadtium", "Dubnium", \
"Dysprosium", "Einsteinium", "Erbium", "Europium", "Fermium", "Flerovium", "Fluorine", \
"Francium", "Gadolinium", "Gallium", "Germanium", "Gold", "Hafnium", "Hassium", "Helium", "Holmium", \
"Hydrogen", "Indium", "Iodine", "Iridium", "Iron", "Krypton", "Lanthanum", "Lawrencium", \
"Lead", "Lithium", "Livermorium", "Lutetium", "Magnesium", "Manganese", "Meitnerium", \
"Mendelevium", "Mercury", "Molybdenum", "Moscovium", "Neodymium", "Neon", "Neptunium", \
"Nickel", "Nihonium", "Niobium" , "Nitrogen", "Nobelium", "Oganesson", "Osmium", "Oxygen", \
"Palladium", "Phosphorus", "Platinum", "Plutonium", "Polonium", "Potassium", "Praseodymium", \
"Promethium", "Protactinium", "Radium", "Radon", "Rhenium", "Rhodium", "Roentgenium", \
"Rubidium", "Ruthenium", "Rutherfordium", "Samarium", "Scandium", "Seaborgium", "Selenium", \
"Silicon", "Silver", "Sodium", "Strontium", "Sulfur", "Tantalum", "Technetium", "Tellurium", \
"Tennessine", "Terbium", "Thallium", "Thorium", "Thulium", "Tin", "Titanium", "Tungsten", \
"Uranium", "Vanadium", "Xenon", "Ytterbium", "Yttrium", "Zinc", "Zirconium"]
## Find the longest sequence of elements
# @param c_e the chemical element
# @param c_es the list of the chemical elements
# @return the longest sequence
def theLongestSequence(c_e, c_es):
    if not(c_e):
        return []    
    t_l_s = []
    for i in range(0, len(c_es)):
        if c_e[-1] == c_es[i][0].lower():
            p_t_l_s = theLongestSequence(c_es[i], c_es[0:i] + c_es[i + 1 : len(c_es)])
            if len(p_t_l_s) > len(t_l_s):
                t_l_s = p_t_l_s
    return [c_e] + t_l_s                                                
# Demonstrate the theLongestSequence function
def main():
    delimeter = " "
    name_chemical_element = input("Enter the name of a chemical element:\n")
    if name_chemical_element in c_e_l:
        c_e_l.remove(name_chemical_element)
        sequence = theLongestSequence(name_chemical_element, c_e_l)
        print("The longest sequence for",name_chemical_element,"is:",delimeter.join(sequence))
    else:
        print("The name entered isn't valid.")
# Call the main function           
main()
