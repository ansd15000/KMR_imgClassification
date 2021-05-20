# KMR_imgClassification
## copyImages.py
이미지가 저장된 디렉토리 내에 하위 디렉토리가 여럿 있어도 간편히 복제하여 활용할 수 있도록 작성한 로직

## makeNPZ_label.py
디렉토리별로 분류한 이미지를 라벨링하며 npz 파일로 변환하는 로직.  
이렇게 변환한 npz 파일들은 이미지 분류 모델을 만들때 활용한다.

## 이미지 대분류 모델링.ipynb
npz 파일들을 불러와 모델을 만드는 로직.  
CNN 기법을 활용하며 여러 레이어 옵션 등을 확인할 수 있다.  
Colab 에서 Google Drive와 마운트하여 작업했다.

## 만든 모델로 디렉토리별 분류.ipynb
Colab 에서 Google Drive와 마운트된 경로에 저장된 모델을 로드하여 이미지 분류하는 로직  
Colab 기본 경로에 test 디렉토리를 생성한 뒤 진행하도록 한다.  
reset() 함수는 여러 모델들을 테스트하며 분류된 이미지 데이터들을 제거하기 위해 작성됐다.
