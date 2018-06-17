from graphviz import Digraph 

dot = Digraph(comment="Mesopotamia")

dot.node("A", "Kingdom Of Israel (1050 BCE)")
dot.node("B", "Kingdom Of Israel (930 BCE)")
dot.node("C", "Kingdom Of Judah (930 BCE)")
dot.node("D", "Neo-Assyrian Empire")
dot.node("E", "Neo-Babylonia")
dot.node("F", "Achaeminid Empire")
dot.node("G", "Neo-Assyrian Empire")
dot.node("I", "Neo-Babylonia")
dot.node("J", "Achaeminid Empire")
dot.node("H", "Yehud (586 BCE)")

dot.edges(["AB", "AC", "BD", "DE", "EF", "CG", "GI", "IJ", "JH"])

dot.render('output/israel.gv', view=True)  
'test-output/israel.gv.pdf'