import numpy as np
from skimage.io import imsave
import torch
from pytorch_gan_myself import Generator
from torch.autograd import Variable
from torchvision.utils import save_image

# ジェネレーターを作ってパラメータをロードする
genera = Generator()
param = 'generator.pth'
genera.load_state_dict(torch.load(param, map_location='cpu'))

for i in range(20):
    z = np.random.uniform(-1,1,[2,100])
    w = np.linspace(0,1,15)[:,None]
    z = z[0]*w+z[1]*(1-w)

    Tensor = torch.FloatTensor

# zをランダムして画像を16枚生成して保存する
    z = Variable(Tensor(z))
    gazou = genera(z)

    save_image(gazou.data[:64], "images/test_%d.png" % i, nrow=8, normalize=True)
