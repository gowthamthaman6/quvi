class Mobile:
  def __init__(self):
    self.stack=[]
  def push(self,num):
    self.stack.append(num)
  def pop(self):
    self.stack.pop()
  
x=Mobile()
x.push("Asus")
x.push("Redmi")
x.push("Apple")
x.pop()
x.push("vivo")
print(x.stack)
