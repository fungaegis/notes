## 简介

- 缺点: 不支持HTTP/1.1协议版本

tips:
- HTTP/1.1 相对1.0主要新增了
1. 缓存处理 
2. 带宽优化及网络连接的使用 
3. 错误通知的管理 
4. Host头处理(同ip虚拟主机)
5. 长连接(keep-alive减少客户端频繁的访问服务器)

### 解析过程
![](./images/gunicorn解析过程.jpg)
1. 从可读的socket中获取用户发送的请求内容，保存到buf中
```http
GET / HTTP/1.1\r\n
Host: localhost:8000\r\n
User-Agent: curl/7.47.0\r\n
Accept: */*\r\n
Content-Length: 16\r\n
Content-Type: application/x-www-form-urlencoed\r\n\r\n
name=123w4234234
```
- 第一行是request-line
- 最后一行是request-body
- 其余的是request-headers
2. 根据第一个\r\n，buf的内容可以分为两个部分:1. line 2. rbuf
3. 要判断line的长度是否超过了gunicorn配置的limit_request_line参数，超出的话，报错
4. line中是否包含了代理协议
    - 如果包含了，说明真正的request-line包含在rbuf中，如果对rbuf(把rbuf看成buf，进行上述的处理)进行分割
5. line就是合法的request-line，可以解析出：协议、请求的路径、版本号等
6. 可以解析出各个request header， 作为一个list返回即可
    - [('Host','localhost:8000'),('User-Agent','curl/7.47.0'),]