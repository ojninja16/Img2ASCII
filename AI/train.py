import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import torchvision.transforms as transforms
import os
from torch.utils.data import Dataset,DataLoader
import cv2
from directory_tree import display_tree
char_lookup = [" ", ".", ",", ":", ";", "i", "1", "t", "f", "L", "C", "G", "0", "8", "#", "@"][::-1]
char_to_index={char:key for key,char in enumerate(char_lookup)}
# import numpy as np

class DataloaderS:
    def __init__(self):
        self.orignal_images_path='../data/original_images'
        self.ascii_images_path='../data/ascii_art_images'
        self.images=os.listdir(self.orignal_images_path)
        self.ascii_images=os.listdir(self.ascii_images_path)
    def __len__(self):
        return len(self.images)
    def __getitem__(self,idx):
        img_path=os.path.join(self.orignal_images_path,self.images[idx])
        ascii_path=os.path.join(self.ascii_images_path,self.ascii_images[idx])
        img=cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
        ascii_img=cv2.imread(ascii_path)
        img = cv2.resize(img, (360, 360))
        ascii_img = cv2.resize(ascii_img, (360, 360))
        chunks=[]
        asciich=[]
        ## normalize the image so that the pixel values are between 0 and 1 which results in faster convergence when training the model
        # img=transforms(img)
        ## what we will do now is to basically sample the image  we will take a chunk of 30*30 pixels and then we will convert that chunk to tensor and pas it  hrough the model itervatively
        for y in range(0, img.shape[0], 30):
            for x in range(0, img.shape[1], 30):
                y_end = min(y + 30, img.shape[0])
                x_end = min(x + 30, img.shape[1])
                chunk = img[y:y_end, x:x_end]
                ascii_chunk=ascii_img[y:y_end, x:x_end]
                chunk=cv2.resize(chunk,(30,30))
                chunk=transform(chunk)
                ascii_char=int(ascii_chunk.mean()//16)
                # label=char_lookup[ascii_char] 
                chunks.append(chunk)
                asciich.append(ascii_char)
        return torch.stack(chunks),torch.tensor(asciich)
        
    
transform=transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5],std=[0.5])
])
data=DataloaderS()
dataloader=DataLoader(data,batch_size=32,shuffle=True)

class Network(nn.Module):
    def __init__(self):
        super().__init__() # here we don't need to pass the input and output size as we are not using any linear layer
        self.flatten = nn.Flatten()
        self.linear1=nn.Linear(129600,900)
        self.relu=nn.ReLU()
        self.linear2=nn.Linear(900,64)
        self.linear3=nn.Linear(64,len(char_lookup))
    def forward(self,x):
        x=self.flatten(x)
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
    criterion=nn.CrossEntropyLoss()
    for epoch in range(10):
        for i,(chunks,asciich) in enumerate(dataloader):
            optimizer.zero_grad()
            output=net(chunks)
            loss=criterion(output,asciich)
            loss.backward()
            optimizer.step()
            print(f"Epoch {epoch}, Batch {i}, Loss {loss.item()}")
    print('Finished Training')
if __name__ == "__main__": 
    main()
    # display_tree('./',ignore_list=['../data/ascii_art_images','../data/original_images','../data/VOCdevkit'])
    
    