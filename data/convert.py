import os
import glob

if __name__ == '__main__':
    classes = ['Lumpy', 'Giggles', 'Cuddles']
    path = './'
    for name in classes:
        images = glob.glob(path + 'origin_'+ name + '/*')

        for i, img in enumerate(images):
            new_name = path + name + '/{0:03d}'.format(i) + '.jpg'
            os.rename(img, new_name)

