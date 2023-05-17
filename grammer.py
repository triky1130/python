#하나만 출력합니다
print("# 하나만 출력합니다.")
print() #한 줄 띄우기 설정

#여러 개를 출력합니다.
print(10, 20, 30, 40, 50)
print("안녕", "나는", "이원호야")

#문자열은 큰따옴표, 작은따옴표 모두 가능
print('안녕하세요')
print("안녕하세요")
print("\"Hi\"라고 말했습니다") #내부에 큰따옴표 넣는 법 
print("'Hi'라고 말했습니다") #내부에 작은따옴표 넣는 법

#문자열 반복연산자
print("안녕하세요" *3)

#문자열 선택연산자
print("안녕하세요"[0])
print("안녕하세요"[1])
print("안녕하세요"[2])
print("안녕하세요"[3])
print("안녕하세요"[4])


#이스케이프 문자
print("안녕하세요 \n 안녕하세요") #줄바꿈
print("안녕하세요 \t 안녕하세요") #탭

#딕셔너리 = 키와 값을 한 쌍으로 저장
me = {'height':180} #딕셔너리 생성
me['height'] #원소에 접근
>>180

#if문
if hungry:
  print("I'm hungry")
else
  print("I'm not hungry")
  
#for문
for i in [1, 2, 3]:
  print(i)
>>1
>>2
>>3

#함수
def hello():
  print("Hello world!")
 hello()
>>Hello world!

#넘파이 = 딥러닝을 구현할 때 배열이나 행렬 계산을 위한 메서드 사용
import numpy as np

#넘파이 배열 생성하기
x = np.array([1.0, 2.0, 3.0])
print(x)
>>[1. 2. 3.]

#넘파이의 N차원 배열
A = np.array([1, 2], [3, 4])
print(A)
>>[[1 2]
   [3 4]]
A.shape
>>(2, 2)
B = np.array([3, 0], [0, 6])
A + B
>>array([[4, 2],
         [3, 10]])
A * B
>>array([[3, 0],
         [0, 24]])

#브로드캐스트=형상이 다른 배열끼리 계산할 때 행렬 사이즈를 맞춰서 계산되는 기능
A = np.array([1, 2], [3, 4])
B = np.array([10, 20]) #2x2 행렬 사이즈로 맞춰서 계산됨
A * B
>>array([[10, 40],
         [30, 80]])

#matplotlib = 딥러닝에서 그래프를 그려주는 라이브러리
import numpy as np
import matplotlib.pyplot as plt #pyplot이라는 모듈을 이용
x = np.arange(0, 6, 0.1) #0에서 6까지 0.1간격으로 생성
y = np.sin(x) #x값을 넣은 sin을 y에 할당

plt.plot(x,y) #그래프를 그리는 코드
plt.show()

#pyplot의 기능
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label = "sin")
plt.plot(x, y2, linestyle = "--", label = "cos") #cos 함수는 점선으로 그리기
plt.xlabel("x") #x축 이름
plt.ylabel("y") #y축 이름
plt.title('sin&cos') #제목
plt.legend() #그래프의 범례를 나타냄
plt.show()

#이미지 표시하기
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('lena.png') #이미지 읽어오기

plt.imshow(img) #이미지 표시해주는 메서드
plt.show()
