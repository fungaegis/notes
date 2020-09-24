## pytest收集用例的规则：

    1. file name：test_*.py 或者 *test.py
    2. class name：Test* 且类内没有 __init__ 函数
    3. function name: test_* 
   
-- --
## fixtrue方法：
### 设置用例:
```python
@pytest.fixture(scope, params, autouse, ids, name)  # 因为都是关键字参数，所以使用时务必指定传参
"""
param scope: default is function ,other: [class, module, session]  # 有四个作用域（方法、类、模块、会话）默认 方法
parpam params:   可以传入列表参数，进行数据驱动测试
param autouse: default is False  # 是否自动使用该前后置条件
param ids: decorated function name  # 装饰器的引用名字 @pytest.fixture(name='<fixturename>')
"""
@pytest.fixture()
def init_driver():
    driver = webdriver.Chrome(executable_path=DRIVER_DIR + "/chromedriver.exe")
    driver.get(url_conf["web_url"])
    yield driver
    driver.quit()
```
### 支持fixture方法间互相引用：

如果引用的fixtrue在同一个module
直接在函数()中写入要引用的函数名即可
如果不在的话需要pytest.mark.usefixtrue("引用的fixtrue方法名")
```python
@pytest.fixture()
def default_fixture(init_driver):
    print("这是个用例级的前置条件")
    yield init_driver
    print("这是个用例级的后置条件")
```

### 使用fixture方法的返回值:

    fixture用例的返回值要放置在生成器 yield 后
    测试用例要引用时在函数()中填入要引用的用例名即可，如果yield后面没有值即返回为 None
    
```python
@pytest.mark.usefixture("default_fixture")
class TestLogin:

    def test_login_success(self, default_fixture):
        lp(init_driver).login(ld.success_data["account"], ld.success_data["password"])
        title = mp(init_driver).get_my_order_title()
        assert ld.success_data["title"] in title
```
        
### 使用fixtrue方法:

如果fixture用例是在同一个module中可不用@pytest.mark.usefixture()装饰器
直接引用在用例函数中传入fixtrue的func名即可
@pytest.mark.usefixture("需要的fixtrue函数名")  支持多重使用
使用的顺序从上到下
```python
@pytest.mark.usefixture("1")
@pytest.mark.usefixture("2")
def test_demo():
    pass
```
 -- --
### conftest.py 文件作用域：

    conftest.py文件的作用域是文件当前目录层级及当前目录更低的所有层级
    用于存共用的fixtrue方法
-- --
## 参数化数据驱动用例

@pytest.mark.parametrize(argname, argdata)
argname: 引用的参数名 str格式
argdata: 数据源
作用域视装饰器装饰是class还是function
```python
@pytest.mark.parametrize("data", ld.invalid_data)
def func(data):
   print(data)
```
-- --
## 用例执行顺序

安装：
```shell
    pip install pytest-ordering
```

使用：
```python
    @pytest.mark.run(order=1) # 仅支持装饰function
    def func():
       pass
```
-- --
## 用例标记
用例标记
```python
    @pytest.mark.smoke # smoke可以进行替换
    def func():
      pass
```
标记使用
控制台：
```shell
    pytest -m smoke
```
pytest.main()中使用命令：
```python
    pytest.main("-m", "smoke")
```
-- --
## 配置文件pytest.ini

pytest --markers查看配置所有
1.可以在这里做mark的备注
2.指定测试用例路径
3.作用域为当前目录及当前目录的下级
```
[pytest]
mark=
    mark1: remake
    mark2: remake
testpaths=path
```

## 其他
> "-s":允许终端在测试运行时输出某些结果，例如你想输入print的内容，可以加上-s

> "-q"简化输出结果
----
## 原生报告
pytest原生支持三种类型的报告
1. xml文件 2.log 3.html

> 其中xml文件和log及其鸡肋

pytest.main()中使用命令：
```python
    # path 为存放路径
    pytest.main("--junitxml=path", "--resultlog=path", "--html=path")
```
控制台使用命令：
```shell
    pytest --junitxml=path --resultlog=path --html=path
    # path 为存放路径
```
-- --



# plugins 插件系列
-- --
## 失败重跑

失败重跑需要安装插件：
```shell
    pip install pytest-rerunfailures
```
function/class级别标注重跑参数：
```python
    @pytest.mark.flaky(reruns 5, reruns-delay 3)
```
控制台使用命令：作用域是当前会话全部
```shell
    pytest --reruns num --reruns-delay num 
    # num: 重试的次数 num: 间隔时间(s)
```
pytest.main()中使用命令：
```python
    pytest.main(["--reruns", "num", "--reruns-delay", "num"])
    # num: 重试的次数 num: 间隔时间(s)
```
-- --
## 分布式运行

安装：
```shell
    pip install pytest-xdist
```
> 该方法用的是多进程并发
> 支持部署到remote TODO:待研究
> pytest-parallel 该module支持多进程多线程并发 TODO:待研究

使用方法：
pytest.main()中使用命令：
```python
    pytest.main(["-n", "3"]) # 进行三个进程的并发运行
    pytest.main(["-n", "auto"])  # 自动根据CPU确定线程，一般为CPU核心线程数
```
控制台使用命令：
```shell
    pytest -n 3 # 进行三个进程的并发运行
    pytest -n auto # 自动根据CPU确定线程，一般为CPU核心线程数
```
-- --
## allure 测试报告
```shell
  pip install allure-pytest
```
![index](https://upload-images.jianshu.io/upload_images/20499241-eabd309700892d6d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

控制台使用：
```shell
  pytest -alluredir=path # path为输出报告的路径
```
pytest.main()中使用：
```python
  pytest.main(["--alluredir=path"])  # path为输出报告的路径
```
[allure使用详情](https://www.jianshu.com/p/40a5a005ce01)
