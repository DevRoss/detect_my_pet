import sys
import glob
import os
from multiprocessing import Pool
import logging

logging.basicConfig(
    level=logging.INFO
)

extensions = ['jpg', 'JPG', 'jpeg', 'JPEG', 'png', 'PNG']


def get_files(directory):
    if os.path.isabs(directory):
        abs_dir = directory
    else:
        abs_dir = os.path.join(os.path.abspath(os.curdir), directory)
    files = glob.glob(abs_dir + '/' + '*.JPG')
    return files


def get_path(target_path=None):
    if target_path is None:
        abs_dir = os.path.join(os.path.abspath(os.curdir), 'tmp')
    else:
        if os.path.isabs(target_path):
            abs_dir = target_path
        else:
            abs_dir = os.path.join(os.path.abspath(os.curdir), target_path)

    if not os.path.exists(abs_dir):
        os.makedirs(abs_dir)
    return abs_dir


def perform(size, origin, target):
    logging.info('Converting {origin} to {target}'.format(origin=origin, target=target))
    cmd = 'convert -resize {size}% {origin} {target}'.format(size=size, origin=origin, target=target)
    os.system(cmd)


def pipeline(size, directory, target_path=None):
    file_list = get_files(directory)
    target_dir = get_path(target_path)
    pool = Pool(4)
    image_label = len(os.listdir(target_dir))
    logging.info('Converting start....')
    for file in file_list:
        target_file = os.path.join(target_dir, str(image_label) + '.jpg')
        pool.apply_async(perform, args=(size, file, target_file))
        image_label += 1
    pool.close()
    pool.join()
    logging.info('Converting completed !!!!')


# directory = 'images'
# print get_files(directory)
if __name__ == '__main__':
    pipeline(10, 'remove')
