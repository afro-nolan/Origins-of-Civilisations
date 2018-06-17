from graphviz import Digraph 

dot = Digraph(comment="Egypt")

dot.node("A", "Early Dynastic Period (3150 BCE)")
dot.node("B", "Old Kingdom (2686 BCE)")
dot.node("C", "First Intermediate Period (2181 BCE)")
dot.node("D", "Middle Kingdom (2055 BCE)")
dot.node("E", "Second Intermediate Period (1650 BCE)")
dot.node("F", "New Kingdom (1550 BCE)")
dot.node("G", "Third Intermediate Period (1069 BCE)")
dot.node("H", "Achaeminid Empire (672 BCE)")
dot.node("I", "Ptolemaic Egypt (332 BCE)")
dot.node("J", "Roman Empire (30 BCE)")


dot.edges(["AB","BC", "CD", "DE", "EF", "FG", "GH", "HI", "IJ"])








dot.render('test-output/eqypt.gv', view=True)  
'test-output/egypt.gv.pdf'