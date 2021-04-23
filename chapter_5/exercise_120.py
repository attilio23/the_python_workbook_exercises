##
#Display a list of items formatted
##Formatting items in a list
# @param l the list
# @return a string containing the formatted elements
def formattingList(l):
    i=0
    n_l=l
    if len(l)==0:
        return "No items have been entered."
    if len(l)==1:
        return str(l[i])
    delimeter=" "
    n_s=""
    while i<len(l)-2:
        n_l.insert(i,(l[i]+","))
        n_l.pop(i+1)
        i=i+1
    n_l.insert(len(l)-1,"and")
    n_s=delimeter.join(n_l)
    return n_s
#Demonstrate the formattingList function           
def main():
    items=[]
    item=input("Enter the first item:\n")
    while item!="":
        items.append(item)
        item=input("Enter the item:\n")
    s_items=formattingList(items)
    print("\n%s"%s_items)
#Call the main function    
main()    
