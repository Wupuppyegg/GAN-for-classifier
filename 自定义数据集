import torch
import torchvision.transforms as transforms
import numpy as np
import torch.utils.data as data
import os
from PIL import Image



#####自定义数据集#############
class CustomDataset(torch.utils.data.Dataset):
  def _init_(self, root1, root2)###root1为数据集，root2为标签集
    imgs =os.listdir(root1)
    labels = np.loadtxt(root2)
    self.imgs = [os.path.join(root1, k) for k in imgs] ###定义图片集
    self.labels = torch.from_numpy(labels)
    self.transforms = transforms ###定义数据的转化
  def _getitem_(self, index):
    img_path = self.imgs[index]##索引图片所在位置，并将其打开
    pil_img = Image.open(img_path)
    data = self.transforms(pil_img)
    labels = self.labels[index]###索引表签所在的位置，并加载
    return data, labels
   def _len_(self):
    return len(self.imgs)
    
transforms=transforms.Compose(
            [transforms.Resize(32), transforms.ToTensor(), transforms.Normalize([0.5], [0.5])]
        )###将图片reshape,转化为Tensor的格式，并将其归一化
        
        
dataset = CustomDataset('D:/武泽煦-tju/tran_baidu_image/', 'D:/武泽煦-tju/labels.txt')###定义数据集

dataset = data.DataLoader(dataset = dataset, batch_size = 3, shuffle = True)

for i, (data, labels) in enumerate(dataset):
  print("data is :", data)
  print("labels is :", lables)
