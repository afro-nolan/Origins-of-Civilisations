from graphviz import Digraph 

dot = Digraph(comment="China")

dot.node("A", "Xia Dynasty (2070 BCE)")
dot.node("B", "Shang Dynasty (1600 BCE)")
dot.node("C", "Zhou Dynasty (1046 BCE)")
dot.node("D", "Spring and Autumn Period: States Divided (722 BCE)")
dot.node("E", "Warring States Period (476 BCE)")
dot.node("F", "Imperial China: Qin Dynasty (221 BCE)")


dot.edges(["AB", "BC", "CD", "DE", "EF"])



dot.render('test-output/china.gv', view=True)  
'test-output/china.gv.pdf'