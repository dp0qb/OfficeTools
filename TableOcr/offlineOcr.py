import os
import subprocess



def main():
    data_folder = "./data"
    # output_folder = "./output"
    img_fnames = os.listdir(data_folder)
    for img_fname in img_fnames:
        img_path = os.path.join(data_folder, img_fname)
        result = subprocess.run(['paddleocr', f'--image_dir={img_path}', "--type=structure", "--layout=False"])


if __name__ == '__main__':
    main()
