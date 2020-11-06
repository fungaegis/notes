---
description: 在测试开发 devops 质量保证 工程效能领域踩坑中
---

# ReadMe

[![](https://img.shields.io/github/watchers/fungaegis/notes?label=watch&style=social)](https://github.com/fungaegis/notes/subscription) 
[![](https://img.shields.io/github/stars/fungaegis/notes?style=social)](https://github.com/fungaegis/notes) 
[![](https://img.shields.io/github/forks/fungaegis/notes?style=social)](https://github.com/fungaegis/notes/fork) 
[![](https://img.shields.io/github/followers/fungaegis?style=social)](https://github.com/fungaegis)



本文档多为实用性笔记,按笔者自己学习和实践的道路整理归档相关的资料.

有部分还未整理完,本文档持续更新中!


目录

统计时间 2020-09-27

|项目|子项目|进度|备注|
|-|-|-|-|
|算法|排列|已归档||
|算法|案例|已归档||
|flask|知识点|待完善|只归档纯后端|
|python|高阶知识点|已归档||
|python|通用库|未开展|暂缓开展|
|sql|sql必知必会|已归档||
|front|html|已归档||
|front|css|已归档||
|front|js|已归档||
|front|jquery|已归档|暂不复习|
|shell&linux|shell|已归档||
|shell&linux|linux|已归档||
|docker|docker|已归档||
|vue|vue|待完善||
|测试方法论|科普|已归档||
|测试方法论|方法论|待补充||
|测试方法论|管理|已归档||
|django|django|待完善|待实践|
|django|drf|待完善|待实践|
|gunicorn|gunicorn|待学习||
|k8s|k8s|待完善|待实践|
|nginx|nginx|待完善|待实践|
|测试框架|unittest|待完善||
|测试框架|pytest|待完善||
|自动化|web自动化|待完善|待实践分布式多容器|
|自动化|app自动化|待完善|待实践分布式多容器|
|自动化|api自动化|待完善||
|性能|jmeter|待完善|待实践|
|性能|基础知识|待完善||
|devops|方法论|待完善||
|devops|工具链|待学习||
|redis|redis|已归档||
|jenkins|jenkins|已归档||
|http|http知识点|已归档||
|http|图解http|待学习|暂缓|
|sonarqube|sonarqube|已归档|
|其他|正则表达式|已归档||
|其他|git|已归档||
|其他|mianshi|待完善||

---

|项目|子项目|进度|备注|
|-|-|-|-|
|nginx|nginx|待完善|待实践|
|k8s|k8s|待完善|待实践|
|测试框架|unittest|待完善||
|测试框架|pytest|待完善||
|自动化|web自动化|待完善|待实践分布式多容器|
|自动化|app自动化|待完善|待实践分布式多容器|
|自动化|api自动化|待完善||
|django|django|待完善|待实践|
|django|drf|待完善|待实践|
|vue|vue|待完善||
|flask|知识点|待完善|只归档纯后端|
|其他|mianshi|待完善||
|性能|jmeter|待完善|待实践|
|性能|基础知识|待完善||
|devops|方法论|待完善||
|devops|工具链|待学习||
|测试方法论|方法论|待补充||
|http|图解http|待学习|暂缓|


备忘录：
- https://studygolang.com/articles/27439?fr=sidebar： Artifactory集群作为文件共享中心
- jenkins pipeline share library 完善
- https://kubernetes.io/zh/docs/tutorials/kubernetes-basics/
- https://www.bilibili.com/video/BV1GT4y1A756?p=4


https://testerhome.com/articles/22085

k8s解决方案:
- 浏览器集群：浏览器集群化部署在k8s中，提升资源利用率并可同时提供数百浏览器的服务支持
- 持续集成：先知2项目中，编译，出包，部署，测试全部容器化并利用k8s自动化部署与运维，提升资源利用率并可同时提供70套测试环境的支持。同时今年的大部分测试服务也使用k8s部署
- 自动化：多数自动化测试项目中都引入了k8s client，在测试中操作k8s来完成较难的测试场景。
- 稳定性测试：扩展k8s的client-go来自定义k8s控制器，监控集群中所有的相关事件。同时对接普罗米修斯的push-gateway。弥补了普罗米修斯在实时监控能力上的不足(普罗米修斯是pull 架构，无法做到实时监控的效果) 这样再调用jenkins client，我们就创造了可以持续数周的自动化测试和监控效果。这种测试也成为浸泡测试，验证产品在长期的全链路业务测试下的稳定性。
- 混沌工程：自定义k8s operator(CRD+自定义控制器)， 自定义k8s admission webhoook, 在扩展一下k8s的client-go。 封装封装实现了故障注入，测试分析，恢复，监控这一套的自动化解决方案。


https://www.cnblogs.com/superhin/p/11478007.html



