import os
import re
import functools
gt_path = './ICPR_text_train_part2_20180313/txt_9000'

gt_out_path = './ICPR_text_train_part2_20180313/txt_9000_'

if not os.path.exists(gt_out_path):
    os.makedirs(gt_out_path)

txt_files = os.listdir(gt_path)

for txt_path in txt_files[:4]:
    # _, basename = os.path.split(file)

    # stem, ext = os.path.splitext(txt_path)
    #
    # print(stem,ext)

    with open(os.path.join(gt_path, txt_path),'r') as f:
        lines = f.readlines()

    with open(os.path.join(gt_out_path, txt_path), 'w') as f:

        for line in lines:
            coordinates = line.split(',')[:-1]
            # print(coordinates)
            f.write(functools.reduce(lambda x, y: x + ',' + y, coordinates[::1]))
            f.write('\n')




