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
4.Concrete Generic Views
5.ViewSet
6.action
7.router
8.Exception
六、生成API文档