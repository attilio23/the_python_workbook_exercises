##
#Express an imperial volume using the largest units possible
#Store the number of teaspoons per tablespoon and the number of tablespoons per cup as constants
TE_PER_TA=3
TA_PER_CU=16
#Convert the measure
# @param n_u the number of units
# @param u_m the unit of measure
# @return the string representing the measure using the largest possible units
def convertMeasure(n_u,u_m):
    s_cu=""
    s_ta=""
    s_te=""
    if u_m=="teaspoons" or u_m=="teaspoon":
        n_cu=n_u//(TE_PER_TA*TA_PER_CU)
        n_ta=(n_u%(TE_PER_TA*TA_PER_CU))//TE_PER_TA
        n_te=(n_u%(TE_PER_TA*TA_PER_CU))%TE_PER_TA
    elif u_m=="tablespoons" or u_m=="tablespoon":
        n_cu=n_u//TA_PER_CU    
        n_ta=n_u%TA_PER_CU
        n_te=0
    else:
        n_cu=n_u
        n_ta=0
        n_te=0
    if n_cu>0:
        s_cu=s_cu+str(n_cu)+" cup"
    if n_cu>1:
        s_cu=s_cu+"s"
    if n_ta>0:
        s_ta=s_ta+str(n_ta)+" tablespoon"
    if n_ta>1:
        s_ta=s_ta+"s"
    if n_te>0:
        s_te=s_te+str(n_te)+" teaspoon"
    if n_te>1:
        s_te=s_te+"s"
    if n_cu>0 and (s_te!="" or s_ta!=""):
        s_cu=s_cu+", "
    if n_ta>0 and s_te!="":
        s_ta=s_ta+", "
    return s_cu+s_ta+s_te
#Demonstrate the convertMeasure function    
def main():
    print("49 teaspoons are equivalent to %s ."%convertMeasure(49,"teaspoons"))
    print("2 teaspoons are equivalent to %s ."%convertMeasure(2,"teaspoons"))
    print("1 teaspoon is equivalent to %s ."%convertMeasure(1,"teaspoon"))
    print("4 teaspoons are equivalent to %s ."%convertMeasure(4,"teaspoons"))
    print("17 tablespoons are equivalent to %s ."%convertMeasure(17,"tablespoons"))
    print("1 tablespoon is equivalent to %s ."%convertMeasure(1,"tablespoon"))
    print("46 tablespoons are equivalent to %s ."%convertMeasure(46,"tablespoons"))
    print("67 teaspoons are equivalent to %s ."%convertMeasure(67,"teaspoons"))
    print("103 teaspoons are equivalent to %s ."%convertMeasure(103,"teaspoons"))
    print("64 tablespoons are equivalent to %s ."%convertMeasure(64,"tablespoons"))
    print("16 tablespoons are equivalent to %s ."%convertMeasure(16,"tablespoons"))
    print("19 teaspoons are equivalent to %s ."%convertMeasure(19,"teaspoons"))
    print("6 teaspoons are equivalent to %s ."%convertMeasure(6,"teaspoons"))
    print("96 teaspoons are equivalent to %s ."%convertMeasure(96,"teaspoons"))
    print("51 teaspoons are equivalent to %s ."%convertMeasure(51,"teaspoons"))
#Call the main function    
main()                