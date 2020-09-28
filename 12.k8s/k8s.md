## 参考资料
https://zhuanlan.zhihu.com/p/162928436
在线k8s：https://www.katacoda.com/

## 1. 简介:
1. Kubernetes是一个容器编排平台, 用于管理容器的工作负载和服务
2. 如果想要将 Docker 应用于庞大的业务实现，是存在困难的编排、管理和调度问题。于是，我们迫切需要一套管理系统，对 Docker 及容器进行更高级更灵活的管理。
3. k8s 把数量众多的服务器重新抽象为一个统一的资源池

应用:
- 快速部署应用
- 快速扩展应用
- 无缝对接新的应用功能
- 节省资源，优化硬件资源的使用

特点:
- 可移植: 支持公有云，私有云，混合云，多重云 multi-cloud
- 可拓展: 模块化，插件化，可挂载，可组合
- 自动化: 自动部署，自动重启，自动复制，自动伸缩/扩展

### 1.2 云架构
- 云和 K8s 是什么关系
    - 云就是使用容器构建的一套服务集群网络，云由很多的大量容器构成。K8s 就是用来管理云中的容器。

- 云原生有如下特点：
    - 容器化，所有服务都必须部署在容器中
    - 微服务，Web 服务架构式服务架构
    - CI/CD
    - DevOps

- Iaas: 基础设施即服务(一台云服务器)
- Paas: 平台即服务(数据库)
- Saas: 软件即服务(现成的软件)

### 1.3 k8s架构

k8s是一(master)对多(slave)的分布式架构

Master节点结构:
- apiserver网关: 1.负责与node进行交互 2.用户的指令请求(kubectl restapi webui) 所有的指令请求都要过网关
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

## 2. 核心组件
### 2.1 Pod (容器组)
- Pod 也是一个容器，这个容器中装的是 Docker 创建的容器，Pod 用来封装容器的一个容器，Pod 是一个虚拟化分组；
- Pod 相当于独立主机，可以封装一个或者多个容器(常规只推荐一个)
- Pod 有自己的 IP 地址、主机名，相当于一台独立沙箱环境

- Web 服务集群如何实现？
    - 实现服务集群：只需要复制多方 Pod 的副本即可，这也是 K8s 管理的先进之处，K8s 如果继续扩容，只需要控制 Pod 的数量即可，缩容道理类似。

- Pod 底层网络，数据存储是如何进行的？
    - Pod 内部容器创建之前，必须先创建 Pause 容器；
    - 服务容器之间访问 localhost ，相当于访问本地服务一样，性能非常高。

### 2.2 ReplicaSet 副本控制器(副本集)
控制 Pod 副本「服务集群」的数量，永远与预期设定的数量保持一致即可。当有 Pod 服务宕机时候，副本控制器将会立马重新创建一个新的 Pod，永远保证副本为设置数量。


### 2.3 Deployment 部署对象
- 服务更新:
    - 部署模型：
    - ReplicaSet 不支持滚动更新，Deployment 对象支持滚动更新，通常和 ReplicaSet 一起使用；
    - Deployment 管理 ReplicaSet，RS 重新建立新的 RS，创建新的 Pod

### 2.4 StatefulSet
- 对于 K8s 来说，不能使用 Deployment 部署有状态服务
- 对于有状态服务的部署，使用 StatefulSet 进行有状态服务的部署。

- 什么是有状态服务？
    1. 有实时的数据需要存储
    2. 有状态服务集群中，把某一个服务抽离出去，一段时间后再加入机器网络，如果集群网络无法使用
什么是无状态服务？

- 没有实时的数据需要存储
    1. 无状态服务集群中，把某一个服务抽离出去，一段时间后再加入机器网络，对集群服务没有任何影响

- 为了解决有状态服务使用容器化部署的一个问题。
- 部署模型
- 有状态服务

StatefulSet 保证 Pod 重新建立后，Hostname 不会发生变化，Pod 就可以通过 Hostname 来关联数据。

### 2.5 deployment 维持pod数量
- `kubectl run container_name --image image_name --port 80 --replicas=2`: 运行镜像并维持2个pod
- `kubectl get deployments`: 查看deployments
- `kubectl edit deployments pod_name`: 修改配置文件
- `replicas`: 配置文件中用来修改副本数

### 2.6 service: 多个pod抽象为一个服务
kube-proxy 整个集群层面抽象出一个虚拟交换机，如果有多个pod会自动进行负载均衡，分发。
以上这个过程生成 service资源

- `kubectl expose depolyment pod --target-port 80 --type NodePort`: 创建service
- `kubectl get svc`: 获取services，可以查看服务的虚拟ip

### 2.7 互相通信
内部的dns会自动将ip与service名字绑定
互相访问只要输入名字即可

### 2.8 ingress
虚拟ip映射到公网
1. 获取配置文件 https://github.com/sunwu51/notebook/tree/master/19.07
2. 创建ing-dep.yml文件
3. `kubectl apply -f ing-dep.yml` 创建
4. 创建ing-config 文件
5. `kubectl apply -f ing-config.yml`创建
6. 外界访问 ing-config中的

## 2. 常用命令
- `kubectl version`: 查看k8s的版本
- `kubectl cluster-info`: 查看master地址和版本
- `kubectl get pod`: 获取pod列表
- `kubectl get nodes`: 获取node节点信息
- `kubectl delete pods pod_name`: 删除pod
- `kubectl delete deployment deployment_name`: 删除deployment,会将所有的pod都删除
- `kubectl create -f xx.yaml`: 用配置文件创建deployment

