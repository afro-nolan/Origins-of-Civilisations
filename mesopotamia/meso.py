from graphviz import Digraph 

dot = Digraph(comment="Mesopotamia")

dot.node("A", "Sumer (4500BCE)")
dot.node("B", "Akkadian Empire (2334BCE)")
dot.node("C", "Assyria")
dot.node("D", "Babylonia")
dot.node("E", "Neo-Assyria")
dot.node("F", "Neo-Babylonia")
dot.node("G", "Median Empire")
dot.node("H", "Achaeminid Empire")
dot.node("I", "Macedonian Empire")
dot.node("J", "Seleucid Empire")
dot.node("K", "Parthian Empire")
dot.node("L", "Roman Empire")
dot.node("N", "Achaeminid Empire")
dot.node("M", "Elam (2700 BCE)")

dot.edges(["AB", "BC", "BD", "CE", "DF", "EG", "GH", "HI","IJ", "JK", "KL", "FH", "MN"])

dot.render('test-output/meso.gv', view=True)  
'test-output/mesopotamia.gv.pdf'