# 디렉토리로 분류된 이미지들을 라벨링화 시킨 npz 파일 생성. 개수는 유동적 변경 가능
from genericpath import exists
import numpy as np 
import random as r
import os 
#image <=> numpy
import PIL.Image as pilimg
from tensorflow.python.keras.backend import resize_images

'''
os.listdir는 운영체제 파일을 순서대로 읽어오질 않는다.
    ========= Label =========
    || natural  |        0 ||
    || art      |        1 ||
    || people   |        2 ||
    || food     |        3 ||
    ========= ===== =========
'''

datapath =    './semiPJ/data/'
defaultPath = '/Users/shift/Desktop/LABs/ML/semiPJ/img/pjForimg/'

def mkdir(size):
    size = str(size)
    try :
        if not os.path.exists(datapath + size) :
            os.mkdir(datapath + size)
    except OSError:
        print('Error~~~~~ mkdir')

# 해상도와 이미지 개수로 npz 파일 만들기
def shortdata(size, howmuch) :
    labels = os.listdir(defaultPath)
    label = 0
    for labelName in labels: # 라벨별 이미지 디렉토리 루프
        if labelName == '.DS_Store' or labelName == 'cartoon': continue # 카툰이 문제되는듯 하니 제외함

        path = defaultPath + labelName + '/'
        nlist = os.listdir(path)         # 이미지 리스트
        files = r.sample(nlist, howmuch) # 이미지 파일 랜덤 n개
        npzData = f'{str(howmuch)}_{labelName}.npz'
        
        data=[]    # 이미지 데이터 list
        targets=[] # 라벨값 들어갈 list
        getout = [] # 예외 데이터 걍 볼려고
        
        for file in files :
            if file == '.DS_Store': continue

            img = pilimg.open(path + file)
            resize_image = img.resize((size, size))
            pixel = np.array(resize_image)
            print(f'================= {labelName} {pixel.shape}=================')
            if len(pixel.shape) != 3 :
                getout.append(file)
                continue
            if pixel.shape[2] != 3 : pixel = pixel[..., :3]
            targets.append(str(label))
            data.append(pixel)
            print(getout)

        # 해상도별 디렉토리 없음 생성하기
        mkdir(size)
        np.savez(f"{datapath + str(size) + '/' + npzData}", data=data, target=targets)
        print(f"{npzData} 파일저장완료.")
        print('label: '+ str(label))
        label += 1
    print(f"labels: {labels}")
    print('END!')

shortdata(100, 1567)