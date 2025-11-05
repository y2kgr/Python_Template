# GitHub Copilot 실전 활용 세미나: 생산성과 품질 향상 워크숍

교육 자료 URL : http://bit.ly/GHC-Python

## 채팅기능
- 채팅뷰
- 인라인 채팅
- 스마트 액션
- 퀵 채팅

### 실습환경
- https://github.com/pmj-chosim/Python_Template
- Python 이 없는경우 fork 후 fork된 Project에서 *Code → Codespaces → Create codespaces on main*을 선택
<img width="1202" height="696" alt="image" src="https://github.com/user-attachments/assets/28835052-2bed-495a-a556-5bfeb0010773" /> 

### 채팅 뷰의 3가지 모드
- **Ask** 모드는 채팅창에서 코드나 답을 제시하는 역할을 합니다. 
- **Agent** 모드는 여러 코드들을 이해하고 코드를 직접 수정해줍니다. 더불어, 코드 작성뿐만 아니라 필요한 라이브러리 설치(예: pip install...) 등과 같은 환경 설정까지, 다양한 작업을 처리해주는 실제 대행자처럼 동작합니다. 
- **Edit** 모드는 사용자가 지정한 파일에 대해서 또는 Agent 보다는 좁은 맥락에서 코드를 수정한다는 차이점이 있었습니다.
<img width="486" height="783" alt="image" src="https://github.com/user-attachments/assets/df670aa7-1b88-4481-a3df-bbab2d21a9e7" />  

#### 스마트 액션?? 
- GitHub Copilot을 통해 받고 싶은 도움을 귀찮게 채팅을 치지 않아도 쉽게 받을 수 있게 하는 방법입니다.
- 원하는 코드 블록을 드래그하여 선택한 후, 마우스 우클릭 후 "Explin"을 클릭하면 코드블록의 설명을 한다.
<img width="442" height="308" alt="image" src="https://github.com/user-attachments/assets/dfb3330f-1116-475b-abf8-acffde21e430" />   
<img width="537" height="303" alt="image" src="https://github.com/user-attachments/assets/e5224558-82a0-4484-9810-fc706ed1926f" />  
- 그리고 "코드 생성"에서 Fix, Review, Generate Docs, Generate Tests 등을 자동으로 실행할 수 있다. 
<img width="702" height="407" alt="image" src="https://github.com/user-attachments/assets/27203119-aeff-4130-87d0-f64159bdbb11" />  
- Generate Tests를 사용하는 경우 별도의 파일을 생성하여 테스트 함수를 만들어 줘서 괜찮은거 같다.

### 퀵채팅
- 퀵 채팅(Quick Chat)은 별도의 챗봇 창(사이드바)을 열지 않고, 편집기 화면 위에 바로 작은 채팅창을 띄워 사용한다.(VS Code 기본 단축키: Cmd+Shift+I 또는 Ctrl+Shift+I)
<img width="1256" height="363" alt="image" src="https://github.com/user-attachments/assets/946b3cc5-20db-4bd2-adff-324db89285e2" />
<img width="920" height="298" alt="image" src="https://github.com/user-attachments/assets/44600c38-5d0d-4619-abde-530db34e66b3" />  
- 퀵채팅은 아래와 같은 장점이 있다.
  - 빠른 접근성: 채팅창이 없이, 단축키나 메뉴 클릭 한 번으로 즉시 채팅창을 불러올 수 있어 신속합니다.
  - 작업 흐름 유지: 전체 사이드바를 열어 화면을 가리지 않기 때문에, 현재 작업 중인 코드를 유지한다.
  - 간결한 사용성: 채팅 뷰(사이드바)의 Ask 모드와 유사하게 동작하지만, 인터페이스가 더 간결하고 가볍습니다. 일반적인 질문이나 간단한 코드 스니펫에 대한 질문을 하기에 적합합니다.