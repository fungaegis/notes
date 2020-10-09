参考资料
1. http://docs.kubernetes.org.cn/
2. 在线k8s：https://www.katacoda.com/

# 1. 简介:
1. Kubernetes是一个容器编排平台, 用于管理容器的工作负载和服务
2. 如果想要将 Docker 应用于庞大的业务实现，是存在困难的编排、管理和调度问题。于是，我们迫切需要一套管理系统，对 Docker 及容器进行更高级更灵活的管理。
3. k8s 把数量众多的服务器重新抽象为一个统一的资源池
4. k8s 自己也是运行在一堆 pod 上

应用:
- 快速部署应用
- 快速扩展应用
- 无缝对接新的应用功能
- 节省资源，优化硬件资源的使用

特点:
- 可移植: 支持公有云，私有云，混合云，多重云 multi-cloud
- 可拓展: 模块化，插件化，可挂载，可组合
- 自动化: 自动部署，自动重启，自动复制，自动伸缩/扩展

## 1.2 云架构
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

## 1.3 k8s架构

k8s是一(master)对多(slave)的分布式架构

Master节点结构:
- apiserver网关: 整个系统的对外接口，供客户端和其它组件调用
- scheduler调度器: 对集群内部的资源进行调度
- controller 控制器: 负责管理控制器
- etcd 存储资源对象

Node节点结构:
- kubelet: 节点上的资源操作指令由kubelet来执行(监视指派到它所在Node上的Pod，包括创建、修改、监控、删除等)
- kube-proxy 代理服务(虚拟网卡): 服务间(Pod)负载均衡
- Pod: k8s 管理的基本单元（最小单元）
    - k8s 不直接管理容器，而是管理 Pod
    - 容器的存储在 Node 节点，容器是存储在 Pod 内部的
    - Pod 内部可以有一个容器，或者多个容器
    - 由多个docker容器（常规1个） + pause容器组成(pause用来传达管理其他容器的指令)
- Docker: 容器引擎
- Fluentd: 主要负责日志收集、存储与查询

# 2. 基础知识

- 命名空间: 是 k8s 中”组“的概念，提供同一服务的 pod 就应该被放置同一命名空间下

## 2.1 命令

### 1. 查看

#### 1. kubectl get 查看资源

- `kubectl get pod`: 查看所有pod(容器组)

- `kubectl get pod -n kube-system -o wide`: 查看系统服务pod
    - `-n`: 指定 命名空间(k8s 所有的 pod 都被放置在 kube-system 命名空间下)
    - `-o wide`: 查看更多的信息

- `kubectl get get svc`: 查看服务(service)
- `kubectl get get rs`: 查看副本控制器(ReplicaSet副本集)
- `kubectl get get deploy`: 查看部署(Deployment)
- `kubectl get get secret`: 查看秘钥(secret)
- ``: 持久化数据卷


```py
root@xixi:~# kubectl get pod -n kube-system
--------------------------------------------------------------------------
NAME                                    READY   STATUS    RESTARTS   AGE
coredns-4c5785cbcc-8ck7s                1/1     Running   2          169d
coredns-4c5785cbcc-zsmvg                1/1     Running   2          169d
heapster-4b9b6b6597-6l9gd               1/1     Running   3          169d
kube-flannel-ds-amd64-bmkdv             1/1     Running   11         371d
kubernetes-dashboard-59d6887fdf-pdfrd   1/1     Running   0          158d
metrics-server-79558644c6-ngj4g         1/1     Running   2          169d
prometheus-68f6cf7cfd-87sh2             1/1     Running   1          169d
```

- NAME：第一列是 pod 的名字，k8s 可以为 pod 随机分配一个五位数的后缀。
- READY：第二列是 pod 中已经就绪的 docker 容器的数量，上文中我们提到了，pod 封装了一个或多个 docker 容器。在这里，1/1的含义为就绪1个容器/共计1个容器。
- STATUS：第三列是 pod 的当前状态，下面是一些常见的状态：

|状态名	|含义|
|-|-|
|Running|运行中|
|Error|异常，无法提供服务|
|Pending|准备中，暂时无法提供服务|
|Terminaling|结束中，即将被移除|
|Unknown|未知状态，多发生于节点宕机|
|PullImageBackOff|镜像拉取失败|
- RESTART：k8s 可以自动重启 pod，这一行就是标记了 pod 一共重启了多少次。
- AGE：pod 一共存在了多长时间。

#### 2. kubectl describe 查看详情

`-n`: 指定 命名空间

- `kubectl describe secrets 秘钥名`: 查看指定秘钥详情 
    - Example:`kubectl describe secrets admin-user-token-666wc -n kube-system` 查看dashboard token
- `kubectl describe pod 容器组名`: 查看指定容器详情
    - Example: `kubectl describe pod redis-master-fd5b55b33-t95lr` 查看redis pod 的详情
- ``: 
- ``: 
- ``: 
- ``: 
- ``: 
- ``: 

```py
root@devops40:~# kubectl describe pod redis-master-fd5b55b33-t95lr
------------------------------------------------------------------
# 实例名字
Name:           redis-master-fd5b55b33-t95lr
# 命名空间
Namespace:      default
# 工作节点
Node:           172.16.5.11/172.16.5.11
# 启动时间
Start Time:     Tue, 14 Apr 2020 09:18:11 +0800
# 标签
Labels:         app=redis
                pod-template-hash=fd5b55b33
                role=master
# 注解
Annotations:    <none>
# 状态
Status:         Running
# pod的ip
IP:             172.20.0.97
# 控制资源
Controlled By:  ReplicaSet/redis-master-fd5b55b33
Containers:
  redis-master:
    Container ID:   docker://b63482e57bc593648629a6d5c76f30a38f074a4e562ec9c3b9ec067d4d45f7
    Image:          redis:2.8.23
    Image ID:       docker-pullable://redis@sha256:e507029ca6a11b85f8ff16d7ff73ae54582f16fd757e64431f5ca6d27a13c
    Port:           6379/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Fri, 24 Apr 2020 17:24:46 +0800
    Last State:     Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Fri, 24 Apr 2020 17:22:52 +0800
      Finished:     Fri, 24 Apr 2020 17:23:39 +0800
    Ready:          True
    Restart Count:  2
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-f0wln (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  default-token-f0wln:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-f0wln
    Optional:    false
QoS Class:       BestEffort
Node-Selectors:  <none>
Tolerations:     <none>
Events:          <none>
```
- 当pod运行异常时,可以在describe末尾处的Events看到相关信息

#### 3. kubectl logs 查看日志
`kubectl logs -f -n kube-system prometheus-68f6cf7cfd-87sh2`

### 2. 创建

- yaml文件创建

- 简易创建

#### 1. kubectl create 创建资源


## 2.2 常用命令
- `kubectl version`: 查看k8s的版本
- `kubectl cluster-info`: 查看master地址和版本
- `kubectl get pod`: 获取pod列表
- `kubectl get nodes`: 获取node节点信息
- `kubectl delete pods pod_name`: 删除pod
- `kubectl delete deployment deployment_name`: 删除deployment,会将所有的pod都删除
- `kubectl create -f xx.yaml`: 用配置文件创建deployment

# 3. 核心组件
## 3.1 Pod (容器组)
- Pod 也是一个容器，这个容器中装的是 Docker 创建的容器，Pod 用来封装容器的一个容器，Pod 是一个虚拟化分组；
- Pod 相当于独立主机，可以封装一个或者多个容器(常规只推荐一个)
- Pod 有自己的 IP 地址、主机名，相当于一台独立沙箱环境

- Web 服务集群如何实现？
    - 实现服务集群：只需要复制多方 Pod 的副本即可，这也是 K8s 管理的先进之处，K8s 如果继续扩容，只需要控制 Pod 的数量即可，缩容道理类似。

- Pod 底层网络，数据存储是如何进行的？
    - Pod 内部容器创建之前，必须先创建 Pause 容器；
    - 服务容器之间访问 localhost ，相当于访问本地服务一样，性能非常高。

## 3.2 ReplicaSet 副本控制器(副本集)
控制 Pod 副本「服务集群」的数量，永远与预期设定的数量保持一致即可。当有 Pod 服务宕机时候，副本控制器将会立马重新创建一个新的 Pod，永远保证副本为设置数量。


## 3.3 Deployment 部署对象
- 服务更新:
    - 部署模型：
    - ReplicaSet 不支持滚动更新，Deployment 对象支持滚动更新，通常和 ReplicaSet 一起使用；
    - Deployment 管理 ReplicaSet，RS 重新建立新的 RS，创建新的 Pod

## 3.4 StatefulSet
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

## 3.5 deployment 维持pod数量
- `kubectl run container_name --image image_name --port 80 --replicas=2`: 运行镜像并维持2个pod
- `kubectl get deployments`: 查看deployments
- `kubectl edit deployments pod_name`: 修改配置文件
- `replicas`: 配置文件中用来修改副本数

## 3.6 service: 多个pod抽象为一个服务
kube-proxy 整个集群层面抽象出一个虚拟交换机，如果有多个pod会自动进行负载均衡，分发。
以上这个过程生成 service资源

- `kubectl expose depolyment pod --target-port 80 --type NodePort`: 创建service
- `kubectl get svc`: 获取services，可以查看服务的虚拟ip

## 3.7 互相通信
内部的dns会自动将ip与service名字绑定
互相访问只要输入名字即可

## 3.8 ingress
虚拟ip映射到公网
1. 获取配置文件 https://github.com/sunwu51/notebook/tree/master/19.07
2. 创建ing-dep.yml文件
3. `kubectl apply -f ing-dep.yml` 创建
4. 创建ing-config 文件
5. `kubectl apply -f ing-config.yml`创建
6. 外界访问 ing-config中的



