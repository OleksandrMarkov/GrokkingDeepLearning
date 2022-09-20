from package.layer import Layer

""" Mean square error loss """
class MSELoss(Layer):
    def __init__(self):
        super().__init__()
    
    def forward(self, pred, target):
        return ((pred - target)*(pred - target)).sum(0)
     