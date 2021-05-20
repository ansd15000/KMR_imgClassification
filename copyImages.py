# 갯수 지정 해주는게 딱히 없어서.. 나중에 필요하면 추가하자
# 많은 데이터를 필요로 한다면 코드 수정이 필요하거나 따로 로직 만들어 쓰는중
# 디렉토리내 디렉토리가 있는 이미지 디렉토리의 모든 데이터를 끄집어내 복사하는 코드

import os
import shutil

copy_datapath = '/Users/shift/Desktop/LABs/ML/semiPJ/img/artTest/'
savepath = '/Users/shift/Desktop/LABs/ML/semiPJ/img/test/'

copy_datapath2 = '/Users/shift/Desktop/LABs/ML/semiPJ/img/artTest2/'
savepath2 = '/Users/shift/Desktop/LABs/ML/semiPJ/img/test2/'

art = '/Users/shift/Desktop/LABs/ML/semiPJ/img/art/'
artCopy = '/Users/shift/Desktop/LABs/ML/semiPJ/img/art_test/'

food = '/Users/shift/Desktop/LABs/ML/semiPJ/img/food/'
foodCopy = '/Users/shift/Desktop/LABs/ML/semiPJ/img/food_test/'

cartoon = '/Users/shift/Desktop/LABs/ML/semiPJ/img/cartoon/'
cartoonCopy = '/Users/shift/Desktop/LABs/ML/semiPJ/img/cartoon_test/'

natural = '/Users/shift/Desktop/LABs/ML/semiPJ/img/natural/seg_train/'
naturalCopy = '/Users/shift/Desktop/LABs/ML/semiPJ/img/natural_test/'

def __reset(path = '/Users/shift/Desktop/LABs/ML/semiPJ/img/test') :
    if os.path.exists(path) : 
        shutil.rmtree(path)
        os.mkdir(path)
    else : os.mkdir(path)

# 파일 확장자 반환
def __extension(filename) : # ex: sessin2.5.jpg
    # reverse = filename[::-1]  # 뒤집고 ( gpj.5.2nisses  )
    # start = reverse.find('.') # .위치  ( gpj.)
    # return reverse[start::-1] # 뒤집기 (.jpg)
    start = filename.rfind('.')
    return filename[start:]

'''
    path       : 사진이 담긴 디렉토리의 상위 디렉토리
    saveLoc    : 새로저장할 위치 (선택사항)
    delete_dir : 복사하고 이전데이터 삭제할건지... 그냥 move 했으면 됐던겄을.. 자원낭비네
    start      : 중간에 로직 멈췄다면..새로 저장할 데이터 이름 순서 지켜줘야지.
                근데 이건 문제 있을거같다, 함수가 어차피 처음부터 파일 읽어올텐데 아 ;
'''

# for문 없다
def __copyDirImage(path, imageName, saveLoc, sequencal_fileName):
    # 복사위치 지정 안하면 해당 분류 디렉토리의 상위 디렉토리로 위치 설정
    saveLocation = saveLoc if saveLoc is not None else path

    # 분류된 이미지를 지정위치 복사
    print('now file: ' + imageName)
    shutil.copy(path + imageName,  saveLocation)

    os.rename(
        saveLocation + imageName, 
        saveLocation + str(sequencal_fileName) + __extension(imageName) )
    sequencal_fileName += 1
    return sequencal_fileName

# 디렉토리 안에 또 디렉토리가 있어도 가능
def __copyInnerDirImage(path, dirname, saveLoc, sequencal_fileName) :
    print('now location: ' + path + dirname)
    sequencal = sequencal_fileName
    imageDirectory = ''
    for _imageName in os.listdir(path + dirname):  # 디렉토리별로 분류된 내부 파일 이미지
        print('now file: '+ dirname + _imageName)
        if _imageName == '.DS_Store': continue
        imageDirectory = path + dirname + '/' # 이미지가 있는 디렉토리
        if os.path.isdir(imageDirectory + _imageName) :
            print(f'내부 디렉토리 발견: {imageDirectory + _imageName}')
            _dir = dirname + '/' + _imageName + '/'
            # __copyInnerDirImage(path, _dir, saveLoc, sequencal_fileName)
            lo, s = __copyInnerDirImage(path, _dir, saveLoc, sequencal)
            sequencal = s
            continue # 안해주면 카피시 에러남
            
        # 복사위치 지정 안하면 해당 분류 디렉토리의 상위 디렉토리로 위치 설정
        saveLocation = saveLoc if saveLoc is not None else path
        
        # 분류된 이미지를 지정위치 복사.
        original_path = imageDirectory + _imageName
        if '//' in original_path : original_path = original_path.replace("//", "/")
        # print(f'original path: {original_path}')
        shutil.copy( imageDirectory + _imageName,  saveLocation)

        os.rename(
            saveLocation + _imageName, 
            saveLocation + str(sequencal) + __extension(_imageName) )
        print(sequencal)
        sequencal += 1
    return imageDirectory, sequencal

def copyFromDir(path, saveLoc = None, start = 0, delete_file = False) :
    # 주소 문자열은 뒤에 / 없으면 에러
    if path[-1:] != '/' : raise 'not include "/" '
    if saveLoc is not None :
        if saveLoc[-1:] != '/' : raise 'not include "/"' 
            
    sequencal_fileName = start
    
    # 경로 내의 이미지를 다른곳으로 복사
    for imageName in os.listdir(path):
        if imageName == '.DS_Store': continue
        
        # 검색된 데이터가 파일이라면
        if os.path.isfile(path + imageName):
            sequencal = __copyDirImage(path, imageName, saveLoc, sequencal_fileName)
            sequencal_fileName = sequencal
            if delete_file : shutil.remove(path + imageName) # 파일삭제 (선택사항)

        # 검색된 데이터가 디렉토리라면
        elif os.path.isdir(path + imageName) :
            imageDirectory, sequencal = __copyInnerDirImage(path, imageName, saveLoc, sequencal_fileName)
            sequencal_fileName = sequencal
            if delete_file : shutil.rmtree(imageDirectory)
    print('done!')

if __name__ == '__main__' :
    print('=================이미지 카피 테스트 실행=================')
    newpeople = '/Users/shift/Downloads/data/'
    newpeopleCopy = '/Users/shift/Desktop/LABs/ML/semiPJ/img/pjForimg/people/'
    __reset(newpeopleCopy)
    copyFromDir(newpeople, newpeopleCopy)

    
    print('============================================')


