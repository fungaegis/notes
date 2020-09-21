## 1. 简介:
1. Kubernetes是一个容器编排平台, 用于管理容器的工作负载和服务
2. 如果想要将 Docker 应用于庞大的业务实现，是存在困难的编排、管理和调度问题。于是，我们迫切需要一套管理系统，对 Docker 及容器进行更高级更灵活的管理。
3. k8s 把数量众多的服务器重新抽象为一个统一的资源池

特性:
- 快速部署应用
- 快速扩展应用
- 无缝对接新的应用功能
- 节省资源，优化硬件资源的使用
- 可移植: 支持公有云，私有云，混合云，多重云 multi-cloud
- 可拓展: 模块化，插件化，可挂载，可组合
- 自动化: 自动部署，自动重启，自动复制，自动伸缩/扩展

### 1.2 云架构

- Iaas: 基础设施即服务(一台云服务器)
- Paas: 平台即服务(数据库)
- Saas: 软件即服务(现成的软件)

### 1.3 k8s架构

k8s是一(master)对多(slave)的分布式架构

Master节点结构:
- apiserver网关: 负责与node进行交互，用户的指令请求(kubectl restapi webui)
- scheduler调度器: 把请求资源调度到某一个 Node 节点
- controller 控制器: 维护 K8s 资源对象
- etcd 存储资源对象

Node节点结构:
- kubelet: 节点上的资源操作指令由kubelet来执行
    - 负责本地 Pod 的维护
- kube-proxy 代理服务(虚拟网卡): 服务间(Pod)负载均衡
- Pod: k8s 管理的基本单元（最小单元）
    - Pod 内部是容器
    - k8s 不直接管理容器，而是管理 Pod
    - 容器的存储在 Node 节点，容器是存储在 Pod 内部的
    - Pod 内部可以有一个容器，或者多个容器
    - 由多个docker容器（常规1个） + pause容器组成(pause用来传达管理其他容器的指令)
- Docker: 容器引擎
- Fluentd 日志收集服务

### deployment 维持pod数量
`kubectl run container_name --image image_name --port 80`: 启动镜像并维持服务
`kubectl get deployments.`: 查看pod资源
`kubectl edit deployments pod_name`: 修改配置文件
`replicas`: 配置文件中用来修改副本数

### service: 多个pod抽象为一个服务
kube-proxy 整个集群层面抽象出一个虚拟交换机，如果有多个pod会自动进行负载均衡，分发。
以上这个过程生成 service资源

`kubectl expose depolyment pod --target-port 80 --type NodePort`: 创建service
`kubectl get svc`: 获取services，可以查看服务的虚拟ip

### 互相通信
内部的dns会自动将ip与service名字绑定
互相访问只要输入名字即可

### ingress
虚拟ip映射到公网
1. 获取配置文件 https://github.com/sunwu51/notebook/tree/master/19.07
2. 创建ing-dep.yml文件粘贴
3. `kubectl apply -f ing-dep.yml` 创建
4. 创建ing-config文件粘贴
5.  `kubectl apply -f ing-config.yml`创建
6. 外界访问 ing-config中的

## 2. 基本命令

`kubectl cluster-info`: 查看master地址和版本
`kubectl get pod`: 获取pod列表

``
``
``
``
``
``

