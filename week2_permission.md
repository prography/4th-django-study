모르는거 개투성이. 

# Q1. 

### 문법??

```
linenos = 'table' if self.linenos else False
```

이거는 if 문 해당하면 앞에꺼 else면 뒤에꺼 하라는거 맞음???? 

그니까 self.linenos가 true면 linenos='table'하고 아니면 linenos= False 하라는건가용????



# Q2.

###Meta 이너 클래스를 찾다보니,,1,2…. 2번에 대한 궁금증?

장고 모델에서 Meta 이너 클래스는 모델로 붙을 몇가지 옵션(metadata)을 가진 클래스 컨테이너다.

1. 퍼미션, 연관된 DB테이블이름~~(ex. 있는 디비랑 연결할때)~~, 모델이 abstract인지 아닌지 등 여기서는 ordering이 있네!

   ```python
   class Snippet(models.Model):
       owner = models.ForiegnKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
       ...
   
       class Meta:
           ordering = ('created',)
   ```

2. 또, internal class는 클래스 인스턴스 간 공유데이터를 위한 편리한 네임스페이스이다…? 진짜 이렇게 쓰는건가? 내가 이해한건,,, Meta이너클래스 내 어떤 변수를 주면 그 변수는 공유데이터변수로 쓰이는것,,, 그리고 configuration stuff 가 read-only라서 바꿀수 없다는데,,??[여기](https://stackoverflow.com/questions/10344197/how-does-djangos-meta-class-work)

   ```py
   In [1]: class Foo(object):
   ...:     class Meta:
   ...:         metaVal = 1
   ...:         
   In [2]: f1 = Foo()
   In [3]: f2 = Foo()
   In [4]: f1.Meta.metaVal
   Out[4]: 1
   In [5]: f2.Meta.metaVal = 2
   In [6]: f1.Meta.metaVal
   Out[6]: 2
   In [7]: Foo.Meta.metaVal
   Out[7]: 2
   ```



# Q3.

###Model에 함수 override하는것. -save()때문에 보다보니 조금 다른 질문일 것 같은데,, 클래스 마다 변수의 개수가 다를수도 있다는 말씀??????

아래와 같이 Model클래스 내부에 함수들이 있고 예를들어 set_image함수 내에 _image_changed변수를 만들었는데 그럼 클래스 마다 저 함수에 들어가지 못한 애들은 저변수가 없고 들어간애들은 변수가 있는 상태???? 클래스 마다 변수의 개수가 다를수도 있다는 말씀??????

```python
class Model(model.Model):
    _image=models.ImageField(upload_to='folder')
    thumb=models.ImageField(upload_to='folder')
    description=models.CharField()

    def set_image(self, val):
        self._image = val
        self._image_changed = True

        # Or put whole logic in here
        small = rescale_image(self.image,width=100,height=100)
        self.image_small=SimpleUploadedFile(name,small_pic)

    def get_image(self):
        return self._image

    image = property(get_image, set_image)

    # this is not needed if small_image is created at set_image
    def save(self, *args, **kwargs):
        if getattr(self, '_image_changed', True):
            small=rescale_image(self.image,width=100,height=100)
            self.image_small=SimpleUploadedFile(name,small_pic)
        super(Model, self).save(*args, **kwargs)
```

# Q4.



# 알게된 것.

1. ForeignKey 속성 중 related_name이란?

   모델간 역관계를 명칭하기 위해 쓰는 속성

   ```python
   class Page(models.Model):
     site = models.ForeignKey(Site, related_name='myapp_pages')
   ```

   ```python
   site = Site.objects.get(sitename='mysite')
   pages = site.myapp_pages.all()
   ```

   이렇게 related_name에 지정한 포린키 이름을 통해 역으로 접근 가능.

2. lexer란? parser와 차이점은?

   [여기](https://stackoverflow.com/questions/2842809/lexers-vs-parsers)