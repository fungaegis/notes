Django基础
一、简介
1.为什么要使用框架来开发?
●站在巨人的肩膀上
●提升开发效率
●只关注业务逻辑的实现，不关心底层建设
2.Django VS Flask
3.Django是什么？
4.特点

●提供创建项目工程自动化工具
●数据库ORM支持
●模板
●表单
●Admin管理站点
●文件管理
●认证权限
●session机制
●缓存

二、创建工程
1.创建虚拟环境

●virtualenv
●virtualenvwrapper
●python-m venv 虚拟环境名

2.安装Django
3.创建项目

● django-admin startproject 项目名

4.运行项目

●python manage.py runserver
●python manage.py runserver ip：端口

5.项目结构

|文件|描述|
|-|-|
|mysite/|项目根目录|
|manage.py|以多种方式与Django项目交互的命令行工具|
|mysite/|与项目根目录同名，项目相关的包|
|mysite/settings.py|项目全局配置文件|
|mysite/urls.py|声明的全局ur1路由表|
|mysite/wsgi.py|兼容WSGI协议的web服务器入口文件|

6.修改默认时区

```py
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True 
USE_L10N = True 
USE_TZ = True
```

三、创建子应用
1.定义

●如果有一些业务功能模块如何做到复用？

    ●将工程项目拆分为不同的子功能模块
    。以子应用的形式存在
    ●各功能模块间可以保持相对的独立
    ●可以将该模块代码整体复制过去（组件化，可插拔）

2.创建

●python manage.py startapp 子应用名

3.注册

●在全局配置文件settings.py中的INSTALLED_APPS列表添加子应用

4.创建视图

●在projects/views.py中添加业务逻辑代码

5.添加路由

●创建subprojects/urls.py 子路由文件
●在全局路由PROJECT/urls.py文件中添加加载子路由信息

6.子应用结构

|文件|描述|
|-|-|
|migrations|用于存放数据库迁移历史记录的目录|
|admin.py|跟网站的后台管理站点配置相关的文件|
|apps.py|用于配置当前子应用相关信息的文件|
|models.py|保存数据库模型类|
|tests.py|用于编写单元测试|
|views.py|用于编写Web应用视图|


五、路由
1.简介

●类似于导航
●类似于路由器

2.主路由

●在项目同名目录下的urls.py文件中定义
●是Django解析路由的入口

3.子路由

4. 路由寻址
    1. 从根路由从上到下查找
    2. 找到子应用/视图函数
    3. 从子路由从上到下查找
    4. 如果找不到返回404

六、视图
1.定义

●类似于MVC模式中的C控制器(mvc mvt区别)
●主要用于业务逻辑的处理

2.分类

●函数视图
。好理解
。代码可读性与复用性都不佳
●类视图
。可读性和复用性更好
。不同的请求方式以不同的方法呈现

七、MVT模式和两种开发模式
1.介绍

前后端不分离才是MVT模式， 

●M全拼为Model, 与MVC中的M功能相同, 负责和数据库交互, 进行数据处理
●V全拼为View, 与MVC中的C功能相同，接收请求，进行业务处理，返回响应
●T全拼为Template，与MVC中的V功能相同，负责构造要返回的html页面

2.两种开发模式
- 前后端不分离
。后端需控制数据的展示
。前后端不分家，耦合严重
。返回的是HTML页面，实应性、拓展性差
■只能用于浏览器，其他终端不适配

- 前后端分离

。当前主流
。后端只对数据进行处理，只提供数据
。前端效率、页面好不好看，全由前端负责，前后端完全独立
。解耦合
。前后端同时开始开发，缩小业务上线周期
。绝大多数情况下，后端发送json格式的参数，后端同样也json格式的数据返回
■适应性、拓展性非常好
■适合多终端运行同一套接口（PC、APP、小程序等）


八、请求与响应

1.请求参数类型

思考：利用HTTP协议向服务器传参有几种途径？

●查询字符串传参
●请求体参数
。form表单传参
。json格式参数
。上传文件
●路径参数
●请求头参数
。url路径中的参数

2.响应

●视图中必须返回HttpResponse对象或子对象
●HttpResponse（content=响应体，content_type=晌应体数据类型，status=状态码）
●JsonResponse


九、ORM框架
1.定义
●把类和数据表进行映射
●通过类和对象就能操作它所对应表格中的数据（CRUD）


2.步骤
●配置数据库连接信息
。创建数据库和用户
CREATE DATABASE my_django charset=utf8mb4；
GRANT ALL PRIVILEGES ON *.* TO 'keyou'@'%' IDENTIFIED BY'123456'；
flush privileges；
。配置数据库
。安装mysqlclient
●在models.py中定义模型类
●迁移
●通过类和对象操作完成数据增删改查操作

3.初探
●在projects/models.py中定 义Model
●迁移
●ORM的作用
![流程图]() TODO
。以后不用再写SQL语句
■生成规范的SQL，可防止SQL注入
。简化数据库迁移操作

4.数据库模型解析
创建interfaces应用

5.admin站点
●创建管理员用户
。python manage.py createsuperuser


十、数据库操作
1.简介
●Django提供了一套抽象的API，让我们来对数据库表进行CRUD（create，retrieve，update delete objects）操作
●简化对数据库的操作

2.演练数据库表相关操作

3.C（create）
●使用模型内构造方法
●使用create

4.r（retrieve）
●获取一个数据表的所有记录
。返回所有记录组成的模型对象集合（queryset查询集）
●获取指定记录
。get
。filter
。exclude

5.u (update)

6.d (delete)

7.其他操作
排序

十一、基础阶段综合演练
1.创建对项目数据进行CRUD操作的接口

