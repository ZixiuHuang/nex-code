# import imageio
# reader = imageio.get_reader('C:\\Users\\HUAWEI\\Desktop\\video_outx4.mp4')
# fps=reader.get_meta_data()['fps']
# imageio.mimsave("C:\\Users\\HUAWEI\\Desktop\\video_outx4.gif", reader, fps=15)

import imageio
import os

def create_gif_and_mp4(img_dir, fps=20.0):
    duration = 1 / fps
    image_list = os.listdir(img_dir + '/')
    frames = []
    for image_name in image_list:
        type = image_name.split('.')
        if(type[-1]=="jpg" or type[-1]=="png"):
            # print("image_name={0} img_dir={1}".format(image_name, img_dir))
            frames.append(imageio.imread(img_dir + '/'+ image_name))
    imageio.mimsave(os.path.join(img_dir,"out.gif"), frames, 'GIF', duration=duration)
    reader = imageio.get_reader(os.path.join(img_dir,"out.gif"))
    imageio.mimsave(os.path.join(img_dir,"out.mp4"), reader, fps=fps)
    return

def main():
    img_dir = './data/images/'
    create_gif_and_mp4(img_dir=img_dir, fps=10.0)

if __name__ == '__main__':
    main()
#
# import cv2
# from PIL import ImageEnhance, Image
# import numpy as np
#
#
# def img_enhance(image):
#     # 亮度增强
#     enh_bri = ImageEnhance.Brightness(image)
#     brightness = 1.5
#     image_brightened = enh_bri.enhance(brightness)
#     # image_brightened.show()
#
#     # 色度增强
#     enh_col = ImageEnhance.Color(image_brightened)
#     color = 1
#     image_colored = enh_col.enhance(color)
#     # image_colored.show()
#
#     # 对比度增强
#     enh_con = ImageEnhance.Contrast(image_colored)
#     contrast = 1.5
#     image_contrasted = enh_con.enhance(contrast)
#     # image_contrasted.show()
#
#     # 锐度增强
#     enh_sha = ImageEnhance.Sharpness(image_contrasted)
#     sharpness = 1.0
#     image_sharped = enh_sha.enhance(sharpness)
#     # image_sharped.show()
#
#     return image_sharped
#
# cap = cv2.VideoCapture('C:\\Users\\HUAWEI\\Desktop\\gif\\video.mp4')
# images = []
# while (cap.isOpened()):
#     ret, frame = cap.read()  # 读出来的frame是ndarray类型
#     image = Image.fromarray(np.uint8(frame))  # 转换成PIL可以处理的格式
#
#     images.append(image)
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break
#
#     # 同步进行增强画质处理，并显示
#     image_enhanced = img_enhance(image)  # 调用编写的画质增强函数
#     cv2.imshow('frame_enhanced', np.asarray(image_enhanced))  # 显示的时候要把格式转换回来
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

# import math
# import numpy as np
#
# import torch.nn.functional as F
# import torch.nn as nn
# import torch
# # torch.autograd.set_detect_anomaly(True)
#
# # SIREN NeRF definitions
#
#
# class Sine(nn.Module):
#     def __init__(self, w0=30.):
#         super().__init__()
#         self.w0 = w0
#
#     def forward(self, x):
#         return torch.sin(self.w0 * x)
#
#
# class SirenLayer(nn.Module):
#     def __init__(self, input_dim, hidden_dim, use_bias=True, w0=1., is_first=False):
#         super().__init__()
#         self.layer = nn.Linear(input_dim, hidden_dim, bias=use_bias)
#         self.activation = Sine(w0)
#         self.is_first = is_first
#         self.input_dim = input_dim
#         self.w0 = w0
#         self.c = 6
#         self.reset_parameters()
#
#     def reset_parameters(self):
#         with torch.no_grad():
#             dim = self.input_dim
#             w_std = (1 / dim) if self.is_first else (math.sqrt(self.c / dim) / self.w0)
#             self.layer.weight.uniform_(-w_std, w_std)
#             if self.layer.bias is not None:
#                 self.layer.bias.uniform_(-w_std, w_std)
#
#     def forward(self, x):
#         out = self.layer(x)
#         out = self.activation(out)
#         return out
#
# if __name__ == "__main__":
#     layer = SirenLayer(128, 111)
#     x = torch.randn([7, 8, 128])
#     y = layer(x)
#     print(x)
#     print(y)
#     print(x.shape)
#     print(y.shape)