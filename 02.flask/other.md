## 模板(jinja2)
### 变量
Jinja2 能识别所有类型的变量, 甚至是一些复杂的类型, 例如列表. 字典和对象；
在视图函数返回响应处可以传参
```html
<p>A value from a dictionary: {{ mydict['key'] }}.</p>
<p>A value from a list: {{ mylist[3] }}.</p>
<p>A value from a list, with a variable index: {{ mylist[myintvar] }}.</p>
<p>A value from an object's method: {{ myobj.somemethod() }}.</p>
```

### 过滤器
|函数|说明|
|-|-|
|safe|渲染值时不转义|
|capitalize|把值的首字母改为大写, 其他为小写|
|lower|把值改为小写|
|upper|把值改为大写|
|title|把值中每个单词的首字母改为大写|
|trim|把值的首尾空格去除|
|striptags|渲染前将值中的html标签去除|
```html
Hello, {{ name|capitalize }}

<!-- {#当变量未定义时, 显示默认字符串, 可以缩写为d#} -->
<p>{{name | default('No name', true)}}</p>
<!-- {#单词首字母大写#} -->
<p>{{'hel1o' | capitalize}}</p>
<!-- {#单词全小写#} -->
<p>{{'XML'| lower}}</p>
<!-- {#去除字符串前后的空白字符#} -->
<p>{{' he1lo ' | trim}}</p>
<!-- {#字符串反转, 返回“o11eh”#} -->
<p>{{'hello' | reverse}}</p>
<!-- {#格式化输出, 返回"Numberis 2”#} -->
<p>{{%s is %d' | format("Number", 2)}}</p>

<!-- {#关闭HTML自动转义#} -->
<p>{{'<em>name</em>'I safe}}</p>
{%autoescape false%}
<!-- {#HTML转义, 即使autoescape关了也转义, 可以缩写为e#} -->
<p>{{'<em>name</em>' |  escape}}</p>
{%endautoescape%}
```
#### 数字
```html
<!-- {#四舍五入取整, 返回13.0#} -->
<p>{{12.8888 | round}}</p>
<!-- {#向下截取到小数点后2位, 返回12.88#} -->
<p>{{12.8888 | round(2, 'floor')}}</p>
<!-- {#绝对值, 返回12#}| -->
<p>{{-12 | abs}}</p>
```

#### 列表
```html
<!-- {#取第一个元素#} -->
<p>{{[1, 2, 3, 4, 5] | first }}</p>
<!-- {#取最后一个元素#} -->
<p>{{[1, 2, 3, 4, 5] | last }}</p>
<!-- {#返回列表长度, 可以写为count#} -->
<p>{{[1, 2, 3, 4, 5]|1ength }}</p>
<!-- {#列表求和#} -->
<p>{{[1, 2, 3, 4, 5] | sum }}</p>
<!-- {#列表排序, 默认为升序#} -->
<p>{{[3, 2, 1, 5, 4] | sort }}</p>
<!-- {#合并为字符串, 返回“1|2|3|4|5"#} -->
<p>{{[1, 2, 3, 4, 5] | join('|')}}</p>
<!-- {#列表中所有元素都全大写. 这里可以用upper, lower, 但capitalize无效#} -->
<p>{{['tom', 'bob', 'ada'] | upper }}</p>
```

#### 判断
除了过滤器, 所谓的“测试”也是可用的. 测试可以用于对照普通表达式测试一个变量. 要测试一个变量或表达式, 你要在变量后加上一个is以及测试的名称. 例如, 要得出一个值是否定义过, 你可以用name is defined, 这会根据name是否定义返回true或false. 

测试也可以接受参数. 如果测试只接受一个参数, 你可以省去括号来分组它们. 例如, 下面的两个表达式做同样的事情: 
- `{%if 1oop.index is divisibleby3%}`
- `{%if loop.index is divisibleby(3)%}`

```html
<!-- {#检查变量是否被定义, 也可以用undefined检查是否未被定义#} -->
{% if name is defined %}
<p>Name is:{{ name }}</p>
{%endif%}
<!-- {#检查是否所有字符都是大写#} -->
{%if name is upper%}
<h2>"{{ name}}"are all upper case.</h2>
{%endif%}
<!-- {#检查变量是否为空#} -->
{% if name is none %}
<h2>variable is none.</h2>
{%endif%}
<!-- {#检查变量是否为字符串, 也可以用number检查是否为数值#} -->
{% if name is string %}
<h2>{{ name}}is a string.</h2>
{%endif%}
<!-- {#检查数值是否是偶数, 也可以用odd检查是否为奇数#} -->
{% if 2 is even%}
<h2>variable is an even number.</h2>
{%endif%}
<!-- {#检查变量是否可被迭代循环, 也可以用sequence检查是否是序列#} -->
{%if[1, 2, 3]is iterable%}
<h2>variable is iterable.</h2>
{%endif%}
<!-- {#检查变量是否是字典#} -->
{%if{'name': 'test'}is mapping%}
<h2>variable is dict.</h2>
{%endif%}
```
### 控制结构
```html
<!-- f循环-->
{% if user %}
    Hello ,{{user}}!
{% else %}
    Error
{% endif %}

<!-- for循环 -->
{% for x in args %}
    <li>{{x}}</li>
{% endfor %}

<!-- 默认每个for元素之间会有空白, 如果要去除, 使用- -->
{% for p in projects - %}
项目: {{p.name}}: {{p.interfaces}}
{%-endfor%}
```
- loop.index当前循环迭代的次数(从1开始)
- loop.index0当前循环迭代的次数(从0开始)
- loop.revindex到循环结束需要迭代的次数(从1开始)
- loop.revindex0到循环结束需要迭代的次数(从0开始)
- loop.first如果是第一次迭代, 为True. 
- loop.last如果是最后一次迭代, 为True.  
- loop.length序列中的项目数. 

### 宏(函数)
```html
<!-- 宏基类文件 -->
<!-- 定义宏 -->
{% macro func(args)  %}
    <li>{{args}}</li>
{% endmacro %}

<!-- 同文件下使用宏 -->
{% for i in comments %}
    {{ func(i) }}
{% endfor %}
```
```html
<!-- 另一个引用宏基类的文件 -->
{% import "宏模板.html" as macros %}

<ul>
    {% for i in comments %}
        {{ macros.func(i) }}
    {% endfor %}
</ul>
```
### 包含模板
`include` 子模板完全拥有父类内容.
```html
<!-- common.html -->
<div>
    <ul>
        <li>贴吧</li>
        <li>音乐</li>
    </ul>
</div>
```
```html
<body>
{% include 'common.html' %}
</body>
```
### 继承模板
`extends` 继承模板, 共性抽取, 代码复用,子类可以扩充独有内容
```html
<!-- base.html -->
<html>
<head>
    {% block head %}
    <title>Baidu - {% block title %}{% endblock %}</title>
    {% endblock %}
</head>
<body>
    {% block body %}
    {% endblock %}
</body>
</html>
```
```html
<!-- 衍生模板 -->
{% extends "base.html" %}
{% block title %}Index{% endblock %}
{% block head %}
{{super()}}
<style src="xx.css"></style>
{% endblock %}
{% block body %}
<div>content text!</div>
{% endblock %}
```
### include & extends 区别
> include基类一般为公用组件, 子类引用全部代码  
> extends基类一般为整个html的骨架, 由子类去填充空白

### Flask-Bootstrap
`pip install flask-bootstrap`  bootstrap库里面有现成模板骨架
https://getbootstrap.com/docs/4.1/getting-started/introduction/

|块名|说明|
|-|-|
|doc|整个html页面|
|html_attribs|`<html>`页面标签的属性|
|html|`<html>`标签中的内容|
|head|`<head>`标签中的内容|
|title|`<title>`标签中的内容|
|metas|一组`<meta>`标签|
|styles|CSS声明|
|body_attribs|`<body>`标签的属性|
|body|`<body>`标签中的内容|
|navbar|导航栏|
|content|页面内容|
|scrpit|文档底部的js声明|
*如果应用需要向已经有内容的块中添加新内容, 必须使用 Jinja2 提供的 super() 函数*
```py
from flask_bootstrap import Bootstrap
from flask import Flask

app = Flask(__name__)
# bootstrap初始化会将应用实例作为参数传给构造函数
bootstrap = Bootstrap(app)
```
```html
<!-- 继承boostrap基模板 -->
{% extends "bootstrap/base.html" %} 
{% block title %}<h1>这里是title</h1>{% endbolck %}
{% block navbar %}<h1>这是导航栏</h1>{% endblock %}
{% block content %}<h1>这个是正文</h1>{% endblock %}
<!-- script块已有定义内容,  不可随意覆盖使用 -->
{% block script%}
{{super()}}
<script src='my_script.js'></script>
```

### 自定义错误页面
```py
@app.errorhandler(404)  # 错误处理函数
def page_not_found(e):  # 
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return reder_template('500.html'), 500
```
*html页面可以通过二次封装bootstrap基模板, 一般情况下页面导航来都是公用模块, 此时可以封装一个统一的导航栏成为一个新的基类模板*

### 链接
`url_for()`函数可以通过应用实例URL映射中保存的信息生成URL
```py
url_for(view_func)  # 传视图端点名
url_for(index, _external=True)  # 返回绝对路径 http://localhost:5000/
# 生成内部使用的链接 相对路径即可, 外部链接则需要绝对路径

# 生成动态URL,动态URL所需要的动态参数可直接传入
name = "haha"
url_for(user, name=name, _external=True)

# 传给 url_for() 的关键字参数不仅限于动态路由中的参数, 非动态的参数也会添加到查询字符串中
# 设name为动态参数 即 app.route("/<name>")
url_for(user, name="jj", version=3, code=4, page=20, _external=True)
# http://localhost:5000/jj?version=3&code=4&page=20
```

### 静态文件
*html文件引入静态资源的时候建议使用url_for生成动态路径,为了避免覆盖原有样式, 注意使用超继承*
```html
{% block head %}
{{super()}}
<style src="{{ url_for('static', filename='xixi.css') }}, type='text/css'">
{% endblock %}
```

### 使用Flask-Moment本地化日期和时间
官方使用手册: http://momentjs.com/docs/#/displaying/ 

*Moment.js个使用 JavaScript 开发的优秀客户端开源库;  
可以在浏览器中渲染日期和时间  
moment有format() . fromNow(). fromTime() . calendar() . valueOf() 和 unix() 等方法*

安装命令: `pip install flask-moment`
```py
# 初始化
from flask_moment import Moment
from flask import Flask
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
# js, Flask-Moment 还依赖 jQuery.js

@app.route("index")
def index():
    return render_template("index.html", current_time=datetime.utcnow())
```
```html
<!-- base.html -->
<!-- 前端需要在html基类模板中设置scripts -->
{% block scripts %}
{{super()}}
{{monment.include_moment()}}
{{moment.loacle("cn")}}
<!-- loacle声明需要将时间转为指定国家的时间 -->
{% endblock %}
```
```html
<!-- index.html -->
{{ moment(current_time).format('LLL') }}  
<!-- format渲染日期和时间. 参数决定了渲染的方式, 从 'L' 到 'LLLL' 分别对应不同的复杂度 -->
{{ moment(current_time).formNow(refresh=True) }}
<!-- 这个时间戳最开始显示为“a few seconds ago”, 但设定refresh=True 参数后, 其内容会随着时间的推移而更新.  -->
```


## Web表单
用户填写的信息通过`request.form` 访问
### flask-wtf
安装:`pip install flask-wtf`
```py
# 配置
import uuid
from flask import Flask


app = Flask(__name__)
# 防止CSRF跨站攻击 需要配置密钥, 常规需要配置到环境变量中. 本例为展示方便直接放在源码中
app.config["SECRET_KEY"] = uuid.uuid4()  # 62d08e22-de7b-4d4c-b3c1-6720be981bfd
```
```py
# 定义表单类
from flask_wtf import FlaskForm
from wtfroms import StringField, SubmitField
from wtforms.validators import DateRequired

class NameForm(FlaskForm):
    name = StringField("这个是格式错误时返回的msg", validators=[DateRequired()])
    # StringField 类表示属性为type="text" 的 HTML <input> 元素. 
    # validators指定一个由验证函数组成的列表
    submit = SubmitField('Submit')
    # SubmitField 类表示属性为type="submit" 的 HTML <input> 元素

@app.route("/", methods=["post", "get"])
def index():
    form = NameForm()
    return reder_template("index.html", form=form)
```
```html
<!-- 使用原生渲染时除了要写以下表格外还需要对其进行样式美化 -->
<form method="post">
<!-- form.hidden_tag() 元素. 这个元素生成一个隐藏的字段, 供 Flask-WTF 的 CSRF 防护机制使用.  -->
    {{ form.hidden_tag() }}
    {{ form.name.label }}{{ form.name(id='my-text-field') }}
    {{ form.submit() }}
</form>
```
```html
<!-- 使用flask-bootstrap, 效果与上方原生一样 -->
{% import "bootstrap/wth.html" as wtf %}
{{ wth.quick_form(form) }}
<!-- wtf.quick_form() 函数的参数为 Flask-WTF 表单对象 -->
```
**WTForms支持的HTML标准字段**
|函数|说明|
|-|-|
|BooleanField|复选框, True/False|
|DateField|文本, datetime.date格式|
|DateTimeField|文本字段, 值为 datetime.datetime 格式|
|DecimalField|文本字段, 值为 decimal.Decimal|
|FileField|文件上传字段|
|HiddenField|隐藏的文本字段|
|MultipleFileField|多文件上传字段|
|FieldList|一组指定类型的字段|
|FloatField|文本字段, 值为浮点数|
|FormField|把一个表单作为字段嵌入另一个表单|
|IntegerField|文本字段, 值为整数|
|PasswordField|密码文本字段|
|RadioField|一组单选按钮|
|SelectField|下拉列表|
|SelectMultipleField|下拉列表, 可选择多个值|
|SubmitField|表单提交按钮|
|StringField|文本字段|
|TextAreaField|多行文本字段|
**WTForms验证函数**
|函数|说明|
|-|-|
|DataRequired|确保转换类型后字段中有数据|
|Email|验证电子邮件地址|
|EqualTo|比较两个字段的值；常用于要求输入两次密码进行确认的情况|
|InputRequired|确保转换类型前字段中有数据|
|IPAddress|验证 IPv4 网络地址|
|Length|验证输入字符串的长度|
|MacAddress|验证 MAC 地址|
|NumberRange|验证输入的值在数字范围之内|
|Optional|允许字段中没有输入, 将跳过其他验证函数|
|Regexp|使用正则表达式验证输入值|
|URL|验证 URL|
|UUID|验证 UUID|
|AnyOf|确保输入值在一组可能的值中|
|NoneOf|确保输入值不在一组可能的值中|
**示例**
```py
@app.route('/index', methods=['GET', 'POST'])
def index1():
    name = None
    form = NameForm()
    if form.validate_on_submit():  # 数据能否被所有验证函数接受,validate_on_submit() 会调用名字字段上依附的DataRequired() 验证函数
        name = form.name.data
        form.name.data = ''  # 清空表单数据
    return render_template('index.html', form=form, name=name)
```
```html
<!-- 继承基类&使用web表单对象 -->
{% extends "base.html" %}
{% import "bootstrap/wtf.html" as wtf %}

{% block title %}Flasky{% endblock %}

{% block page_content %}
<div class="page-header">
    <h1>Hello, {% if name %}{{ name }}{% else %}Stranger{% endif %}!</h1>
</div>
{{ wtf.quick_form(form) }}
{% endblock %}
```

**结合重定向使用**
```py
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data  # 将用户数据存于用户会话(seesion)中
        return redirect(url_for('index'))  # 若不进行重定向, 用户在表单页刷新时会有警告(表单内容未清空)
    return render_template('index.html', form=form, name=session.get('name'))  # session可以当成字典一样使用
```

### 消息闪现
后台代码需要执行`flash(msg)` 前端模板最好在基模板中渲染闪现消息`get_flashed_messages()`, 因为这样所有页面都能显示需要显示的消息
```py
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))
```
```html
{% for message in get_flashed_messages() %}
<div class="alert alert-warning">  
<!-- 使用 Bootstrap 提供的 CSS alert 样式渲染警告消息 -->
    <button type="button" class="close" data-dismiss="alert">&times;</button>
    {{ message }}
</div>
{% endfor %}
```
