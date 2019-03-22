나의 생각도 함께 적었으니 틀린것은 말해줘용용용


# Q1.
### viewset이라는 것을 알게 되었는데,,,`GenericAPIView`와 mixin 둘다 받아 쓰는것 vs `GeneriaViewSet` 의 차이점이 무엇인가????

GeneriaViewSet은 GenericAPIView를 상속받고 mixin을 오버라이드 하거나 action implementaion 정의한 것 이라고 한다!!

그렇다면 현재 우리가 쓰고있는 GenericAPIView와 mixin 둘다 받아서 쓰는것과는 무엇이 다른점일까????

[viewset 설명 여기](https://brownbears.tistory.com/82)
(viewset에서도 queryset이랑 serializer_class이 내부적으로 쓰이기 위해 꼭 필요하다고 함 - 이름도 그대로)

~~mixin클래스와 GenericAPIView혼합하는것 / 이미 혼합된 뷰 쓰는것(ex.ListCreatAPIView)의 차이점은 
queryset과 serializer_class만 설정해주면 알아서 def해준다는 점이 될 것 같다!!!~~

>ViewSet이란

>Django REST framework는 단일 클래스에서 관련있는 view들의 집합을 위해 logic의 결합을 허용합니다. 이를 ViewSet이라 합니다. 
>또한 다른 framework에서 resource 또는 controller같이 이름이 개념적으로 유사한 implementation을 찾을 수 있습니다.
>클래스는 단순하게 class 기반 view 타입이며  이는 .get() 또는 .post()와 같은 모든 method 핸들러를 제공하지 못하지만 대신 .list()와 .create()같은 액션을 제공합니다.
>ViewSet을 위한 method 핸들러들은 as_view()함수를 사용해 view가 끝나는 시점에 해당하는 행동이 취할 때, 바인딩 합니다.
>일반적으로 url설정의 viewset안에서 view들을 명시적으로 등록하는 것 보다 router 클래스를 가지고 있는 viewset을 등록할 것이고, 이 것은 자동으로 사용자를 위해 url 설정을 결정합니다.


# Q2.
### serializer_class이 필요한 이유는???

queryset과 serializer_class는 둘 다 꼭 필요하고 변수이름도 꼭 그대로여야 한다. --> 그렇다면 serializer_class이 필요한 이유는???
각 def 함수 내에서는 queryset이나 serializer_class가 명시적으로 써있지 않은데 내부적으로 어떻게 쓰이는 지 모르겠오요.

~~queryset이 필요한 이유는 모델을 가져오려고 생각했음...all()가져와서 그거를 바탕으로 list()나 retrieve()같은 것을 뿌려주려고...??? 
그니까 `queryset = Snippet.objects.all()`같은 경우 Snippet 모델을 가져와서 그거를 기준으로 액션한다고 생각했음~~


# Q3.
### args는 언제 쓰이는거지???
url 파라미터 —> *args, **kwargs 로 받음
- 따라서 url에 url파라미터 없으면 *args, **kwargs의미없음.
그런데 url파라미터는 무조건 변수로 받는건데 kwargs로 다 들어감. 그럼 args는 언제쓰이는?
- args는 들어오는 대로 name, like 들어가면 차례로 들어감. kwargs에는 키워드패키징 name=“상은”, like=“7”으로 들어오면 상은, 7가 들어간다고 알고 있음. 


# 알게된 것.
1. 함수이름 get post… 등은 제공되는 함수이므로 이름 바꾸면 안됨.

   바꾸려면 @action[detail=“True”, method=POST] 이런 데코레이터 써줘야함.
- detail 트루면 url파라미터 받겠다. 아니면 안받겠다. 
- 메소드 액션 정해줌. 
—> 이러면 함수이름 다른걸로 쓸수있음.

---
2. 파이썬에서 *는 패키징. **는 키워드패키징
