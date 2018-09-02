import tkinter as tk
class ConsoleUI :
  
  def show(self) :
    thumb = self._inputToList("Enter thumb position: ")
    index = self._inputToList("Enter index position: ")
    middle = self._inputToList("Enter middle position: ")
    ring = self._inputToList("Enter ring position: ")
    little = self._inputToList("Enter little position: ")
    
    data = [
      thumb,
      index,
      middle,
      ring,
      little
    ]
    return data
  
  def _inputToList(self, prompt) :
    txt = input(prompt)
    data = [float(x) for x in txt.split(" ")]
    return data

class TkinterUI :

  def __init__(self, send_callback) :
    self.root = tk.Tk()
    
    self._init_label()
    self._init_entry()
    self._init_btn()
    self.send_callback = send_callback

  def show(self) :
    self.root.mainloop()

  def _onclickDefault(self, e):
    matrix = [
      [-1.63459, -0.61503, 2.00572],  # thumb
      [-0.55683, -0.50336, 3.52084],  # index
      [0.14531, -0.30629, 3.50997],   # middle
      [0.69138, -0.25835, 3.15876],   # ring
      [1.25930, -0.37258, 2.76084],   # little
      [0.0, -2.41533, 0.0],           # arm
      [-1.57, 0, 0]                   # hand
    ]
    for i in range(len(matrix)) :
      for j in range(3) :
        self.entries[i][j].delete(0, tk.END)
        self.entries[i][j].insert(0, str(matrix[i][j]))

  def _onClickFist(self, e) :
    matrix = [
      [-0.66198, -0.11888, 1.32531],
      [-0.85775, -0.95106, 1.17559],
      [-0.46142, -0.83792, 1.05877],
      [-0.27905, -0.65195, 1.17103],
      [-0.05857, -0.46932, 1.07271],
      [0.0, -2.41533, 0.0],
    ]
    for i in range(len(matrix)) :
      for j in range(3) :
        self.entries[i][j].delete(0, tk.END)
        self.entries[i][j].insert(0, str(matrix[i][j]))
  def _onclikcSend(self, e) :
    matrix = [ [float(e.get()) for e in r] for r in self.entries]
    print(matrix)
    self.send_callback(matrix)

  def _init_label(self) :
    tk.Label(self.root, text="X").grid(row=0, column=1)
    tk.Label(self.root, text="Y").grid(row=0, column=2)
    tk.Label(self.root, text="Z").grid(row=0, column=3)

    row_names = [
      "Thumb",
      "Index",
      "Middle",
      "Ring",
      "Little",
      "Arm",
      "Hand (rotation)"
    ]

    for i in range(len(row_names)) :
      tk.Label(self.root, text=row_names[i]).grid(row=i+1, column=0, sticky=tk.W)

  def _init_entry(self) :
    self.entries = [[0]*3 for i in range(7)]

    for i in range(len(self.entries)) :
      for j in range(3) :
        self.entries[i][j] = tk.Entry(self.root)
        self.entries[i][j].grid(row=i+1, column=j+1)
        self.entries[i][j].insert(0, '0.0')

  def _init_btn(self, start=8) :
    defaultBtn = tk.Button(self.root, text="default")
    defaultBtn.grid(row=start, column=1, sticky=tk.W + tk.E + tk.N + tk.S)
    defaultBtn.bind('<Button-1>', self._onclickDefault)
    
    fistBtn = tk.Button(self.root, text="fist")
    fistBtn.grid(row=start, column=2, sticky=tk.W + tk.E + tk.N + tk.S)
    fistBtn.bind('<Button-1>', self._onClickFist)
    
    sendBtn = tk.Button(self.root, text="send")
    sendBtn.grid(row=start+1, column=2, sticky=tk.W + tk.E + tk.N + tk.S)
    sendBtn.bind('<Button-1>', self._onclikcSend)
  