Vue框架
一、简介
1.什么是Vue.js
●前端三大主流框架之一
。Angular.js、React.js、Vue.js
●简单小巧
。使用gzip压缩之后，只有20kb左右
。入门容易
●自动进行响应式更新
。只需关注前端业务逻辑，无需操作DOM
●高级特性
。解耦视图与数据(mvvm)
。可复用组件(组件化)
。前端路由(axios)
。状态管理(vuex)
。虚拟DOM
2.MVVM模式
●M
。模型
。从后端获取的数据
●V
。视图
。界面展示
●VM
。视图模型
。核心控制
3.组件化
二、前端工程化、组件化
●模块化
。以不同的组件，来划分不同的功能模块
●复用
●高效
●解耦

1. 创建前端vue工程

●安装Node.js
。https://nodejs.org/dist/v10.16.3/node-v10.16.3-x64.msi
。node-V
。npm-V
●使用淘宝ηpm镜像源
npm insta1l-g cnpm --registry=https://registry.npm.taobao.org

2. 安装vue-cli脚手架

#使用npm
npm install-g @vue/cli
#或者使用淘'inpm镜像源
cnpm insta11-g @vue/c1i

3. webpack
是前端压缩打包的工具

4. 使用vs code或者WebStorm创建I程项目
三、基础知识
1.插值表达式&绑定属性
2.v-if和v-show
3.v-for
4.使用UI框架来实现
4.1 element ui

#使用淘宝cnpm安装
cnpm i element-ui -S
#导入element-ui
//导入ElementUI 和Css文件
import ElementUI from 'element-ui'；
import 'element-ui/1ib/theme-chalk/index.css'；

#在创建Vue实例之前需要将element-ui插件加入到Vue中
Vue.use(ElementUI)；


5.v-on绑定事件

●监听和响应事件
●v-on可以缩写为@

6.v-model

●数据双向绑定
●只能在input、textarea、select元素上使用

7.vue实例生命周期

●created
。在vue实例化之后执行
。还未挂载到DOM和渲染到模板
●mounted
。挂载到DOM之后
![](.\image\vue的生命周期图.png)

四、组件
1.组件声明
- 局部组件
- 全局组件

2.组件传值

●子组件接收父组件的数据
    。使用props属性指定，从父组件接收的数据
●子组件给父组件传数据

3.slot插槽

●插槽
●命名插槽
●插槽作用域

五、路由
1.简介

●创建单页面应用
●官方路由组件，实现前端路由功能

2.安装

● npm insta1l vue-router

3.简单路由

●创建路由规则文件
●将router挂载到Vue实例中
●路由参数类型
。路径参数
。查询字符串参数
●路由跳转
。使用router-link
。to属性可以为path路径、命名路由以及路径参数和查询字符串参数
●element ui中的案例

只会向静态服务器发起一次请求，之后页面通过首次获取的js执行

4.嵌套路由
●在父路由下再添加子路由(router-view)
六、axios
1.简介
●非常流行的请求库
●vue发起异步请求的标配

2.安装
●npm insta11 axios -S

3.案例
dogs api：https://dog.ceo/api/breeds/image/random
●基本操作
●优化操作