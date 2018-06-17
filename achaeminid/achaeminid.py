from graphviz import Digraph 

dot = Digraph(comment="Achaeminid")

dot.node("A", "Achaeminid Empire (550 BCE)")
dot.node("B", "Seleucid Empire (312 BCE)")
dot.node("C", "Kingdom of Armenia")
dot.node("D", "Restored to Seleucid Empire (69 BCE)")
dot.node("E", "Annexed by Roman Empire (63 BCE)")
dot.node("F", "Parthian Empire (247 BCE)")
dot.node("G", "Sassanid Empire Establised (224 AD) ")
dot.node("H", "Islamic Conquest (651 AD)")

dot.edges(["AB", "AF", "BC", "CD", "DE", "FG", "GH"])

dot.render('test-output/achaeminid.gv', view=True)  
'test-output/achaeminid.gv.pdf'