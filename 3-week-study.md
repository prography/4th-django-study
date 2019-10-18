# Tutorial 5: Relationships & Hyperlinked APIs
> ## 엔티티 간의 관계를 나타 내기 위해 선택할 수있는 여러 가지 방법

'''
* pk값들 사용
* entitiy 간의 하이퍼링크 사용
* related entity에서 유일한 식별 슬러그 필드 사용


### Q1.* 관련 엔터티의 기본 문자열 표현 사용.??
### Q2.* 부모 표현 안에 관련 엔티티를 중첩합니다.??
### Q3.* 다른 사용자 정의 표현.??
'''

### Q.4representation 란?
>어떤 리소스의 특정 시점의 상태를 반영하고 있는 정보이다. 
(https://blog.npcode.com/2017/04/03/rest%EC%9D%98-representation%EC%9D%B4%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80/)

 정방향 또는 역방향 관계에 적용하거나 일반 fk와 같은 커스텀 관리자에 적용 할 수 있음.

> ## ModelSerializer 와 HyperlinkedModelSerializer 차이
'''
*  HyperlinkedModelSerializer는 모델시리얼라이저의 확장형이다
* id기본적으로 필드 는 포함 x
* HyperlinkedModelSerializers는 HyperlinkedIdentityField 사용하면서 url 필드를 포함함
* PrimaryKeyRelatedField 대신에 HyperlinkedRelatedField 사용 
'''
> ## pagination 추가


'''
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,

'''
settings에 추가하고 해당 url에 request를 보내면 페이지와 관련된 정보가 나타난다.







***

# Tutorial 6: ViewSets & Routers

> ## ModelViewSet 

'''
 1. viewSet은 APIView를 상속받음.
 2. CRUD와 리스트 등의 동작들을 액션을 제공함
 3. 권한이나 auth 클래스 사용 가능 

'''

> ## @action 란?
> 뷰셋 클래스를 사용하기 위해서 오버라이딩하고 커스터 마이징할 부분을 정의해줌 




> ## Routers를 사용하면 url이 일정한 규칙에 의해 자동으로 만들어짐



> ## ViewSets의 장점

'''
* 추상화
* 한번의 쿼리셋으로 CRUD의 기능을 정의 할수있음
* 라우터를 사용함으로, url설정을 따로 할 필요 없음.

'''

> ## ViewSets의 단점
'''
* 기존의 방법보다 직관적이지않다.
(처음 봤을 때 코드를 바로 이해 하는것이 어렵다.)
'''