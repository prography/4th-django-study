하 다썻는데 실수로 날렸다...
-1Serialization
시리얼라이저- 원시데이터->제이슨
디시리얼라이저- 제이슨 ->원시데이터
모델시리얼라이저 - 필드에다 제이슨으로바꿔주고싶은거 넣으면 바뀜

메소드 방식에 의해 crud기능을 수행함

-2Requests and Responses
기존 장고의 http리퀘스트보다 DRF 리퀘스트가 더유연함
DRF의 리스폰스는 올바른 내용을 선택해서 리턴해줌 

요약: DRF가 더 쌔다

상태코드도 DRF꺼 써라. 덜 모호하다

래핑
함수형 쓸려면 @api_view
클래스형 쓸려면 APIView

urlpatterns = format_suffix_patterns(urlpatterns) 
이거쓰면 데이터 어떤형식으로 해줄지 접미사를 이용해 보다 쉽게 사용 할수있음

-3Class-based Views
제네릭 클래스 기반 뷰 가 매우 편하드아 

-4 Authentication & Permissions
인증된 사용자만 API를 이용 할 수 있게한다.
permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
기본적으로 SessionAuthentication및 BasicAuthentication. API 인증 
