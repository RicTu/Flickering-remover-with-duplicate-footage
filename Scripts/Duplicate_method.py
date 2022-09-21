import os
import cv2
import tqdm

def remove_flicker(file_path):
    filenames = os.listdir(file_path)
    filenames.sort()
    folder_path = file_path+"_deflicker/"
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)
    for i in tqdm.trange(1,len(filenames)):
        img=cv2.imread(file_path+'/'+filenames[i-1])
        img2=cv2.imread(file_path+'/'+filenames[i])
        result = cv2.addWeighted(img,0.5,img2,0.5,0)
        cv2.imwrite(folder_path+str(filenames[i-1]), result)
    return folder_path


if __name__ == "__main__":
    path = "D:/Thesis_data/KMU/25661226/"
    remove_flicker(path)