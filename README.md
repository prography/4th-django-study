# 4th-django-study
장고 스터디 내용 올리는 레포입니다! :)

# 1주차

[핵심내용]

1. serializers.ModelSerializer 는 models.py에 정의 되어있는 field attribute를 알아서 가져와준다.
2. function view에서는 정의된 serializer를 이용하여 request method에 따라 어떻게 대응하고 답변할지를 정한다.
3. api_view wrapper를 사용하면 보다 간결하게 api 코드를 작성할 수 있다.
4. url 접미사를 활용하면 웹브라우저로도 api서버에 접속할 수 있다.

[추가로 알아볼 것]
1. api_view에서 csrf_token은 어떻게 처리하는지
2. models.py에 정의된 field로 가공된 정보를 보여주기 위해선 어떻게 해야하는지
3. 매뉴얼하게 error code를 return 하기 위해선 어떻게

# 2주차

[핵심내용]

1. APIView class 를 통해 class view로 api를 구현할 수 있다.
2. generic class view를 사용하면 일반적인 기능을 매우 쉽게 구현할 수 있다.
3. class view 에 permission_classes를 정의함으로서 user authentication 또는 object authentication을 할 수 있다.

#3주차

[핵심내용]

1. 하이퍼링크 필드 이용가능