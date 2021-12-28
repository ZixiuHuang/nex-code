import imageio
reader = imageio.get_reader('C:\\Users\\HUAWEI\\Desktop\\video_outx4.mp4')
fps=reader.get_meta_data()['fps']
imageio.mimsave("C:\\Users\\HUAWEI\\Desktop\\video_outx4.gif", reader, fps=15)

# import imageio
# import os
#
# def create_gif(img_dir, image_list, gif_name, duration=0.05):
#     frames = []
#     for image_name in image_list:
#         print("image_name={0} img_dir={1}".format(image_name, img_dir))
#         frames.append(imageio.imread(img_dir + '/'+ image_name))
#     imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
#     return
#
# def main():
#     img_dir = './image_dir'
#     duration = 0.05 # 每秒20帧
#     image_list = os.listdir(img_dir + '/')
#     gif_name = img_dir+'.gif'
#     create_gif(img_dir, image_list, gif_name, duration)
#
# if __name__ == '__main__':
#     main()
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