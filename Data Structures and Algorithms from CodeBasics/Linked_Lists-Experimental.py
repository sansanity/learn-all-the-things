link = str("-->")
compiled = ""

class Nodes():
    # def __init__(self):
    #     self.compiled = ""

    def add_element_to_start(element): 
        # str(element)
        if compiled == "":
            compiled1 = compiled + element + link
            return compiled1
    
        else:   
            ref = compiled[0] + " "
            compiled1 = ref + element + link
            return compiled1

    def add_element_to_end(element):
        # str(element)
        compiled = compiled + " "
        return compiled 

print(Nodes.add_element_to_start("19"))
print(Nodes.add_element_to_start("20"))