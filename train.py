import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
# import numpy as np

class Network(nn.Module):
    def __init__(self):
        super().__init__() # here we don't need to pass the input and output size as we are not using any linear layer
        self.linear1=nn.Linear(1,5)
        self.relu=nn.ReLU()
        self.linear2=nn.Linear(5,5)
        self.linear3=nn.Linear(5,1)# this is the default linear layer which takes input size as 1 and output size as 1
    def forward(self,x):
        x=self.linear1(x)
        x=self.relu(x)  
        x=self.linear2(x)
        x=self.relu(x)
        x=self.linear3(x)
        return x
def main():
    net=Network()
    # print=("par parameter",list(net.parameters()))
    optimizer=optim.SGD(net.parameters(),lr=0.01)# here we are passing the parameters of the network to the optimizer
    # print(net(torch.tensor([2.0])))
    i=0
    # print(list(net.named_parameters()))
    while True:
        optimizer.zero_grad()
        inputs=torch.rand((8192,1))*2*3.1459
        expected=torch.sin(inputs)
        # print(inputs.shape)
        ouput=net(inputs)
        loss=nn.MSELoss()(ouput,expected)
        loss.backward()
        optimizer.step()
        i+=1
        if i%1000==0:
            print(f"Iteration {i}, Loss: {loss.item()}")
        if loss <0.003:
            break
    net.eval()
    test_inputs = torch.linspace(0, 2 * 3.1416, 100).reshape(-1, 1)
    with torch.no_grad():
        predictions = net(test_inputs)

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(test_inputs.numpy(), predictions.numpy(), label='Predicted')
    plt.plot(test_inputs.numpy(), torch.sin(test_inputs).numpy(), label='Actual Sine')
    plt.legend()
    plt.show()
if __name__ == "__main__": 
    main()