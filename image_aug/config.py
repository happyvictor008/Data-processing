class DefaultConfigs(object):
    #raw_images = "/home/victor/dataset/augmen/testaug/"
    raw_images = "/home/victor/dataset/segmentation-airplane/" # 原始图片路径
    #raw_csv_files = "/home/victor/dataset/augmen/testaug/0_dataset.csv"   
    raw_csv_files = "/home/victor/dataset/segmentation-airplane/0_dataset.csv"# 原始csv格式标签
    #augmented_images = "/home/victor/dataset/augmen/testaug/newimage/new_wheelchairuser/"
    augmented_images = "/home/victor/dataset/augmen/newimage/new_airplane/" # 增强后的图片保存路径
    #augmented_csv_file = "/home/victor/dataset/augmen/testaug/newimage/new_wheelchairuser/augmented_label.csv"
    augmented_csv_file = "/home/victor/dataset/augmen/newimage/new_airplane/augmented_label.csv"# 增强后的csv格式的标注文件
    image_format = "jpg"                                                    # 默认图片格式
config = DefaultConfigs()