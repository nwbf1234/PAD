
from argparse import ArgumentParser

import torchvision.transforms as transforms
import torch

def parse_args():
    
    parser = ArgumentParser()

    parser.add_argument("--batch_size", type=int,default=64)
    parser.add_argument('--sample_size',type=int,default=256)    

def main(args):
    torch.cuda.set_device(0)
    device = torch.device('cuda',0)
    T = transforms.Compose([transforms.Resize((args.sample_size,args.sample_size)),transforms.ToTensor()]) 
    a =3
    