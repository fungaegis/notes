# jenkins&allure结合
jenkins与allure之间的支持非常好，基于jenkins运行的allure还支持历史对比，历史回溯等，非常方便每次测试用例的执行
步骤一：
- jenkins运行allure的机子安装allure服务、python库、pytest插件库 [安装教程1](https://www.jianshu.com/p/40a5a005ce01)
- 进入Jenkins的插件管理安装：Allure
- 进入jenkins的全局设置，找到 Allure Commandline
- 填写相关信息
- 进入到job的设置页面，在 构建后操作中找到 allure



# jenkins&pytest的参数化构建

在创建jenkins的job时，依使用情况的不同，有些时候我们希望job能通过builder去指定一些参数从而进行构建的
在这个时候我们就用上了jenkins的参数化构建

勾选 参数化构建过程 👉 选择需要的参数化模式。 本实例用的是 选项参数。
![参数化模式选择](https://upload-images.jianshu.io/upload_images/20499241-c7fa50ae83ae881a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

参数可添加多个同类型或不同类型，本实例围绕的一个场景是：多环境多产品线的构建选择
所以添加了两个参数化，并分别命名为 env（环境） product（产品线）
注意：此处 名称 为之后引用该参数的变量名
- linux系列系统的shell的用法是： \$var
- win系列系统的doc/powershell的用法是：  %var%
- git等源码管理用法是： ${var}

![](https://upload-images.jianshu.io/upload_images/20499241-8561ec39ecc9ad31.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
设置后 在构建页面呈现的效果如下：设置了两个参数化所以出现了两个下拉框
![构建页](https://upload-images.jianshu.io/upload_images/20499241-77bba7d0002825cf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
构建中因为jenkins服务器使用的是linux系统，所以选择了 执行shell
我们的自动化脚本支持命令行传参运行[python3 十一、命令行参数](https://www.jianshu.com/p/e3bcf1041c3f)
具体实现教程可以看看

这里解释下为什么要如下图那般执行这么多shell命令
- 第一条 cd到脚本文件夹
- 第二条 因为我们还采用了excel作为数据源存了用例，也存了执行结果。所以每次执行完excel都会被修改，所以每次修改后将修改临时保存
- 第三条 临时保存的文件其实在新的运行后也是会被迭代掉的，所以在每次运行前将所有临时保存的记录清空
- 第四条 切换到我们指定的分支，此处的埋笔就是第二三条命令，只有处理完变动才能进行切换
- 第五条 拉取最新的远端仓库代码
- 第六条 参数化执行脚本

![](https://upload-images.jianshu.io/upload_images/20499241-890a89d5ce4f500c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

jenkins job的构建首页，可以看到有打包好的allure文件和右侧历史运行情况（成功、故障、失败）
左侧的构建历史可以查看每次构建的allure文件，可以做到追溯历史

![](https://upload-images.jianshu.io/upload_images/20499241-13cf6fcd728ad14d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
