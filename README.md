<img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=header&text=Binggo-Game&fontSize=70" width=100% />

<div align='center'>
	<img src="https://img.shields.io/badge/Python-007396?style=flat&logo=Python&logoColor=white"/>
</div>
<br/>

- 빙고 게임을 위한 프로그램으로써 화면에 빙고를 위한 판을 구성할 수 있는 버튼을 제공하고 1~75까지 Random한 숫자를 뽑아서 List에 추가시켜주는 
기능을 가지고 있습니다.



### 1. 빙고판

<img src="https://user-images.githubusercontent.com/111109411/209888782-9de13839-2f6d-4ec2-9edd-757de6b80b3d.png" width="50%">

- 빙고 보드는 다음과 같이 5줄로 이루어져 있어야 하며 각 줄은 1\~15, 16\~30, 31\~45, 46\~60, 61\~75의 숫자를 가지고 있어야 합니다. 


### 2. 숫자 뽑기

- 전체적인 알고리즘은 크게 프로그램이 실행되면서 1부터 75까지의 숫자를 담고 있는 Array를 생성하고 해당 숫자들을 Random하게 섞어주는 작업을 합니다.
이후 숫자를 뽑는 기능은 해당 Array에서 첫번째 index부터 차례대로 뽑기를 진행하고 index를 분류하기 위해 별도의 Count변수를 선언합니다. 만약 특정
Range에 해당하는 숫자를 뽑을 경우에는 첫번째 index부터 시작해서 해당 Range에 해당하는 번호가 나올 때까지 반복문을 실행시키고 번호가 나오면 
현재 Count되고 있는 부분과 index를 바꾸고 count를 증가시킵니다.

#### 2-1. 전체 Random

- 전체 Random의 경우에는 1\~75까지의 숫자 중에서 Random한 숫자를 뽑아주며  

#### 2-2. 부분 범위 Random

- 부분 범위 Random의 경우에는 빙고 판의 각 Column에 해당하는 범위를 가진 Button이 존재하며 해당 Button을 통해 Random한 숫자를 뽑는게 가능합니다.
