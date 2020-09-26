Django restframework框架
一、REST API
1.简介
二、REST 常用的设计规则
1.URL

命名
●尽量用名词复数形式
●往往与数据库的表名对应

#差的设计
/getProjects
/listUsers
/1ookuser
/retreiveTestcaseById?Id=66

过滤条件
●如果记录数量很多，服务器不可能将所有数据都返回给前端
|命令|描述|
|-|-|
|?limit=10|指定返回记录的数最|
|?offset=10|指定返回记录的开始位置|
|?page=2&size=10|指定第几页和每页的数据条数|
|?sort=name|指定返回结果按照哪个属性排序，以及排序顺序|

2.HTTP请求动词
3.状态码
4.返回结果
5.错误处理

●当请求有误时,服务器需将错误的信息以json格式数据的形式返回
{
    "detail":"身份认证信息未提供.",
    "status_code":401
}

6.Hypermedia API

超链接API
●响应数据中，可以包含下一步操作的URL链接(分页)

三、基础阶段综合演练
1.创建对项目数据进行CRUD操作的接口
2.创建接口的任务

●校验用户数据
●将请求的数据（如json格式）转换为模型类对象
。反序列化
■将其他格式（json、xml等）转换为程序中的数据类型
■将json格式的字符串转换为Django中的模型类对象
●操作数据库
●将模型类对象转换为响应的数据（如json格式）
。序列化
■将程序中的数据类型转换为其他格式（json、xml等）
■例如将Django中的模型类对象装换为json字符串


3.数据增删改查流程

增
●校验请求参数->反序列化->保存数据->将保存的对象序列化并返回
删
●判断要删除的数据是否存在->执行数据库删除
改
●判断要修改的数据是否存在->校验请求参数->反序列化->保存数据->将保存的对象序列化并返回
查
●查询数据库->将数据序列化并返回



4..上述操作有哪些痛点

●代码冗余极其严重，不符合优秀测开的风格
●数据校验非常麻烦，且可复用性差
●编码没有统一的规范，杂乱无章的感觉
●写的代码非常多，不够简洁
●仅支持json格式的传参，不支持form表单传参
●仅能返回json格式的数据，其他类型不支持
●列表页视图没有分页、过滤、排序功能


四、Django REST framework
1.简介

●在Django框架基础之上，进行二次开发
●用于构建Restful API
●简称为DRF框架或REST framework框架

2.特性

●提供了强大的Serializer序列化器，可以高效地进行序列化与反序列化操作；
●提供了极为丰富的类视图、Mixin扩展类、ViewSet视图集；
●提供了直观的Web API界面；
●多种身份认证和权限认证；
●强大的排序、过滤、分页、搜索、限流等功能；
●可扩展性，插件丰富

3.安装&配置

●安装
pip insta11 djangorest framework
pip insta11 markdown #Markdown support for the browsable API.

●配置
INSTALLED_APPS = [
    'rest_framework',
]

4.初探
5.序列化器

●数据校验
。判断用户输入的数据是否异常
●数据转换
。反序列化
■数据格式（json、xml、text）=>程序中的数据类型
。序列化
■程序中的数据类型=>数据格式（前端能处理的数据，如json）

6.序列化
7.反序列化
8.ModelSerializer

●为了简化序列化器类的定义
●功能
。基于模型类自动生成一系列字段
。基于模型类自动为Serializer生成validators，比如unique_together
。包含默认的create()和update()的实现


9.关联字段序列化

●PrimaryKeyRelatedField
●StringRelatedField
●SlugRelatedField
●关联对象的序列化器

10.痛点

●仅支持json格式传参，不支持form表单传参
●仅能返回json格式的数据，其他类型不支持
●对于模型类的获取，仍然有冗余

11.Request

●对Djang0中的HttpRequest进行了拓展
。会根据请求头中的Content-Type，自动进行解析
。无论前端发送的哪种格式的数据，都可以以相同的方式读取
●request.data
。类似于Django中的request.POST和request.FILES
。可以对POST、PUT、PATCH的请求体参数进行解析
。不仅支持form传参，也支持json格式传参
●request.query.params类似于Djang0中的request.GET
。获取查询字符串参数
●支持Django HttpRequest中所有的对象和方法

12.Response

●对Django中的HttpResponse进行了拓展
。会根据请求头中的Accept，自动转化响应数据到对应格式
●如果请求头中未设置Accept，则会采用默认方式处理响应数据（默认返回json格式)
●指定响应默认渲染类


```py

#StudyDjango/settings.py 文件中
#DRF框架所有的全局配置都放在REST_FRAMEWORK这个字典中
REST_FRAMEWORK = {
    #默认响应渲染类
    'DEFAULT_RENDERER_CLASSES':(
        #json渲染器为第优先级
        'rest_framework.renderers.JSONRenderer',
        #可浏览的API渲染器为第二优先级
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
}
```

●Response(data, status=None, template_ name=None, headers=None, content_type=None)

●参数说明
。data
■序列化处理后的数据
■一般为serializer.data（python基本数据类型，字典，嵌套字典的列表）
。status
■状态码，默认为200
。template_name
■模板名称，使用HTMLRenderer渲染时需指明
。headers
■用于存放响应头信息的字典
。content_type
■响应头中的Content-Type
■通常此参数无需设置，会自动根据前端所需类型数据来设置该参数




|||
|-|-|
|||
|||
|||
|||

五、类视图
1.APIView

●继承Django中的View
●APIView与View的不同之处
。传入到视图方法中的是Request对象，而不是Django的HttpRequeset对象
。视图方法可以返回Response对象，会为响应数据处理（render）为符合前端要求的格式
。任何APIException异常都会被捕获到，并且处理成合适的响应信息
。在进行dispatch（）分发前，会对请求进行身份认证、权限检查、流量控制
●常用类属性
。authentication_classes 列表或元祖，身份认证类
。permissoin_classes 列表或元祖，权限检查类
。throttle_classes 列表或元祖，流量控制类


2.GenericAPIView

●继承APIView
●支持的类属性
。必须指定的属性
■queryset
■serializer_Class
。过滤
■filter__backends
■filterset_fields
```py
#使用开源的过滤引擎
#pip install django-filter
from django_filters.rest_framework import DjangoFilterBackend

#a.在视图中指定过滤引擎，也可以在全局指定
filter_backends = [DjangoFilterBackend]
#指定需要过滤的字段
filterset_fields = ['name'，'leader'，'tester']

#b.在settings.py文件中全局指定过滤引擎
INSTALLED_APPS = [
    'django_filters',
]
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}


REST_FRAMEWORK = {
    #指定过滤引擎
    'DEFAULT_FILTER_BACKENDS':[
        'django_filters.rest_framework.DjangoFilterBackend
    ],
}


```

。排序
■filter_backends
■ordering_fields 
```py
from rest_framework import filters

#a.在视图中指定过滤引擎，也可以在全局指定
filter_backends = [filters.orderingFilter]
#指定排序字段
ordering_fields = ['name'，'leader']
#b.在settings.py文件中全局指定过滤引擎
REST_FRAMEWORK ={
    'DEFAULT_FILTER_BACKENDS'：['rest_framework.filters.orderingFilter']
}
```
```py

REST_FRAMEWORK ={
    #指定过滤引擎
    'DEFAULT_FILTER_BACKENDS'：[
        'rest_framework.filters.orderingFilter',
        'django_filters.rest_framework.DjangoFilterBackend'
        ]
}

```

。分页
■pagination_class
```py
#在全局settings.py 文件中指定分页引擎
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS'：'rest_framework.pagination.PageNumberpagination'，
    'PAGE_SIZE': 3
}

```

。详情页视图
■lookup.field查询详情数据时使用的字段名，默认为pk
■lookup.url_kwarg查询详情数据时URL路径参数名称，默认与look_field一样

●支持的类方法
。get.queryset（self）
■返回视图使用的查询集对象
。get.object（self）
■返回详情视图所需的模型类对象
■默认使用lookup_field（pk）参数来过滤
■如果访问的模型类对象不存在，会返回404
。get_serializer（self，*args，**kwargs）
■返回序列化器对象
。get_serializer_class（self）
■返回序列化器类，默认返回serializer_Class
■可以重写


3.Mixin

●RetrieveModelMixin
。提供retrieve（request，*args，**kwargs）方法
。获取已存在的详情数据（一条记录）
。获取成功，则返回200 OK
。如果不存在，则返回404 Not Found
●UpdateModelMixin
。提供update（request，*args，**kwargs）方法，用于全更新
。提供partial_update（request，*args，**kwargs）方法，用于部分更新，
。更新已存在的模型实例（更新一 条记录）
。更新成功，则返回200 OK
●DestroyModelMixin
。提供destroy（request，*args，**kwargs）方法
。删除一条已存在的数据（删除一 条记录）
。删除成功，则返回204 No Content
。如果不存在，则返回404 Not Found
●ListModelMixin
。提供list（request，*args，**kwargs）方法
。获取已存在的列表数据（获取多条记录）
。获取成功，则返回200 OK.
●CreateModelMixin
。提供create（request，*args，**kwargs）方法
。创建新的模型实例（创建新的记录）
。创建成功，则返回201 Created
。如果请求参数有误，则返回400 Bad Request


4.Concrete Generic Views

●RetrieveAPIView
。提供get方法
。继承：RetrieveModelMixin、GenericAPIView
●UpdateAlPIView
。提供put和patch方法
。继承：UpdateModelMixin、GenericAPIView
●DestroyAPIView
。提供delete方法
。继承：DestoryModelMixin、GenericAPIView
●ListAPIView
。提供get方法
。继承：ListModelMixin、GenericAPIView
●CreateAPIView
。提供post方法
。继承：CreateModelMixin、GenericAPIView
●ListCreateAPIView
。提供post、get方法
。继承：ListModelMixin、CreateModelMixin、GenericAPIView
●RetrieveUpdateAPIView
。提供get、put、patch方法
。继承：RetrieveModelMixin、UpdateModelMixin、GenericAPIView
●RetrieveDestroyAPlView
。提供get、delete方法
。继承：RetrieveModelMixin、DestroyModelMixin、GenericAPIView
●RetrieveUpdateDestroyAPIView
。提供get、put、patch、delete方法


●痛点
。两个类视图，不能合并
。有相同的get方法
。两个类视图所对应的url地址不一致


5.ViewSet

请求方法 动作 描述
GET retrieve获取详情数据（单条
GET list获取列表数据（多条
POST create创建数据
PUT update更新数据
PATCH partial_update部分更新
DELETE destroy. 删除数据.

ViewSet类
●继承ViewSetMixin和vieWs.APIView
。ViewSetMixin支 持action动作
●未提供get.object（）、get.serializer（）、queryset.serializer._class等

GenericViewSet类
●继承ViewSetMixin和generics.GenericAPIView
。get.object（）、get_serializer（）、queryset、serializer._class等
●在定义路由时，需要将请求方法与action动作进行绑定


●继承ViewSetMixin和generics.GenericAPIView
。get object（）、get.serializer（）、queryset.serializer._class等
●在定义路由时，需要将请求方法与action动作进行绑定
●使用Mixins类简化程序


ModelViewSet类
●继承ListModelMixin、RetrieveModelMixin、CreateModelMixin、UpdateModelMixin、
DestoryModelMixin、GenericAPIVIew

ReadOnlyModelViewSet类
●继承ListModelMixin、RetrieveModelMixin、GenericAPIVIew

6.action

●使用action装饰器
●methods
。支持的请求方式
。为列表.
●detail
。要处理的是否是详情资源对象（即是否通过url路径获取主键）
。True 表示使用通过URL获取的主键对应的数据对象
。False表示不使用URL获取主键

7.router

●可以使用router来自动生成路由配置
●提供两种路由SimpleRouter和DefaultRouter
。DefaultRouter会 多添加一一个默认的API根视图

8.Exception

DRF能自动处理以下异常：
●APIException类或者子类
●Http404
●PermissionDenied

六、生成API文档

1.简介
●生成API文档平台
●自动生成测试代码
●支持接口测试

2.安装
●coreapi（必须）
●Pygments（可选）
●Markdown（可选）

3.使用coreapi
●最新版的DRF（>3.10）中，需要添加如下配置
```py
REST_FRAMEWORK ={
    #指定用于支持coreapi的Schema
    'DEFALLT._SCHEMA__CLASS'：'rest._framework.schemas.coreapi.Auto'
}


from rest_fr amework.documentation import include_docs_ur1s
from django.urls import path，include 

urlpatterns = [
    path（'docs/'，include_docs_ur1s（tit1e='测试平台接口文档'）），
]
```

●添加注释
。单一方法的视图
■直接给视图类添加注释即可
```py
class ProjectsListView（ListAPIView）：
"""
返回所有项目信息
"""
```

。多个方法的视图
```py
class ProjectsListCreateView（ListCreateAPIView）：
"""
get：返回所有项目信息
post：新建项目
"""
```

。视图集
```py
class ProjectsVi ewset（vi ewsets.Mode 1ViewSet）：
    """
    create：
    创建项目
    partial_update：
    部分更新项目
    destroy：
    删除项目
    1ist：
    获取项日目列表数据
    names：
    获取所有项目名称
    interfaces：
    获取指定项目的所有接口数据

    """
```
4.使用drf-yasg 
●安装
pip insta1l drf-yasg
●添加到INSTALLED_APPS中
```py
INSTALLED_APPS = [
    'drf_yasg'，
]
```

●在全局路由文件urls.py文件中添加配置
```py
#from rest_framework import permi permissions
from drf._yasg.views import get_.schema_view 
from drf_yasg import openapi

schema_.view = get_schema_.view（
    openapi.Info（
    title="Lemon API接11 文档平台",  #必传
    defau1t__version='v1'，#必传
    description="这是一个美轮美奂的接口文档"，terms_of_service="http://api.keyou.site",
    contact=openapi.contact（emai1="keyou100@qq.com"），
    license=openapi.License（name="BSD License"），
    ），
    pub1ic=True，
    #permission_classes=（permissions.A11owAny，），#权限类
）


urlpatterns = [.
    re_path(r ' Aswagger (?P <format>\. json|\. yaml)$',schema_view.without_ui(cache_timeout=0),name='schema-json'), 
    path('swagger/', schema_view.with_ui(' swagger', cache_timeout=0,name='swagger-ui'), 
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='swagger-redoc'),
]
```