import torch
import torchvision.transforms as transforms

def get_transform(norm):
    return transform = Compose([
    transforms.RandomApply(transforms=[RandomHorizontalFlip(p=0.5)], p=0.75),
    transforms.RandomEqualize(p=0.64),
    transforms.Resize((64,64)),
    transforms.ToTensor(),
    transforms.Normalize(*norm)
])
