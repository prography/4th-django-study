의문점들..

- 왜 `Installed_app`에 Config경로를 명시하는가?

  ```python
  INSTALLED_APPS = (
      ...
      'rest_framework',
      'snippets.apps.SnippetsConfig',
  )
  ```

  - 내가 원래 알던 바로는 app의 name을 명시해서 사용했었음

  - 찾은 답변: [stack overflow](https://stackoverflow.com/questions/34377237/confused-a-bit-about-django-installed-apps-naming-convention)

    - 장고 1.7이후 피쳐

    - 앱이 더 쉽게 구성될 수 있고 커스터마이징 가능해짐

    - 하나의 모듈에 여러개의 앱을 가질 수 있음

    - 내가 이해해본 바로는

      - `apps.py`

        ```python
        from django.apps import AppConfig
        
        
        class UserConfig(AppConfig):
            name = 'user'
            ...
        
        class UserProdConfig(AppConfig):
            name = 'user'
            ...
        ```

        이런식으로 config를 여러개 정의하고 `__init__`에서 필요할때 default config를 바꿔쓸 수 있지 않을까?