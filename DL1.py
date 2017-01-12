class Layer:

  def fprop(self, x):
      inp = dot(x, self.W) + self.b
      return self.func(inp)
      
  def bprop(self, x, grad_above):
      inp = dot(x, self.W) + self.b
      return grad_above * self.grad_func(inp) * self.W
      
  def update(self, x, grad_above):
      inp = dot(x, self.W) + self.b
      grad_w = grad_above * self.grad_func(inp) * x
      grad_b = grad_above * self.grad_func(inp) * b
      self.W - self.W + self.lr * grad_w
      self.b = self.b + self.lr * grad_b
