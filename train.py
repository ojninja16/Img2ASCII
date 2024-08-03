import torch
import torch.nn as nn
import torch.optim as optim
# import numpy as np

class Network(nn.Module):
    def __init__(self):
        super().__init__() # here we don't need to pass the input and output size as we are not using any linear layer
        self.layer = nn.Linear(1,1)# this is the default linear layer which takes input size as 1 and output size as 1
    def forward(self,x):
        return self.layer(x)
def main():
    net=Network()
    # print=("par parameter",list(net.parameters()))
    optimizer=optim.SGD(net.parameters(),lr=0.00001)# here we are passing the parameters of the network to the optimizer
    # print(net(torch.tensor([2.0])))
    i=0
    # print(list(net.named_parameters()))
    while True:
        optimizer.zero_grad()
        inputs=torch.rand((8192,1))*1000-500
        expected=inputs*4+3
        # print(inputs.shape)
        ouput=net(inputs)
        loss=nn.MSELoss()(ouput,expected)
        loss.backward()
        optimizer.step()
        i+=1
        if i%1000==0:
            print(loss)   
        if loss <0.1:
            break
    net.eval()
    print(net(torch.tensor([1.0,2.0,3.0,4.0,5.0]).reshape(-1,1)))     
    print(list(net.parameters()))
if __name__ == "__main__": 
    main()