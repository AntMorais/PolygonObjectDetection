# import package
import labelme2coco

# set directory that contains labelme annotations and image files
labelme_folder = "tests/data/labelme_annot"

# set path for coco json to be saved
save_json_path = "tests/data/test_coco.json"

# convert labelme annotations to coco
labelme2coco.convert(labelme_folder, save_json_path)

import os


root_dir = "labels"
for dataset in os.listdir(root_dir):
    if not dataset.startswith('.'):
        # images/train
        dataset_path = os.path.join(root_dir, dataset)
        for img_name in os.listdir(dataset_path):
            # images/train/image01.png
            rel_cwd = os.path.join(dataset_path, img_name)
            # final path: ../data_rotation/images/train/image01.png
            img_path = os.path.join(prefix, rel_cwd)
            file_list.append(img_path)
        with open(str(dataset) + '.txt', 'w+') as f:
            for item in file_list:
                f.write("%s\n" % item)
        file_list = []