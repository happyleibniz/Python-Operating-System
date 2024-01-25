from PIL import Image, ImageSequence

# 打开图片
img = Image.open('startingup.gif')

# 获取图片的所有帧
frames = [frame.copy() for frame in ImageSequence.Iterator(img)]

# 保存每一帧图片
for i, frame in enumerate(frames):
    frame.save('startupv_{}.png'.format(i))
