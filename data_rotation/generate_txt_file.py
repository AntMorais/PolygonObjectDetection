import os

file_list = []
prefix = "../data_rotation"
root_dir = "images"
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