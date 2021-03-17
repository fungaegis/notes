https://www.cnblogs.com/yoyoketang/p/9035341.html

在caps配置中,声明app安装
```py
desired_caps = {
                'platformName': 'Android',
                'deviceName': '127.0.0.1:62001',
                'platformVersion': '4.4.2',
                'app': appPath("baidu.apk"),
                'appPackage': 'com.baidu.yuedu',
                'appActivity': 'com.baidu.yuedu.splash.SplashActivity',
                'noReset': 'true',
                }
```

`driver.install_app("C:\\Users\\yifliu\\Desktop\\weibo10.4.0.apk")#安装APP，需指定apk安装包路径`