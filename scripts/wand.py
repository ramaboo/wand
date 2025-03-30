from wand import Wand

app = None

w = Wand()
w.start(app)

w.print_loop()