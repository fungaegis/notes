# 组件
## models 模型
简介: 为第三方模型提供通用接口, 支持以下三种类型的模型
1. LLMs(大语言模型)
2. 聊天模型
3. 文本嵌入模型
## prompts 提示
简介: 提示工程相关使用
1. 提示模板
2. 聊天提示模板
3. 示例选择器
4. 输出解析器
## memory 记忆
简介: 用来在对话过程中存储上下文
## indexes 索引
结构化文档, 用以更好与LLMs交互, 以及对向量数据库的操控
1. 加载器
2. 分割器
3. 检索
4. 向量存储
## chains 链
把一个个独立的组件链接在一起
- LLMChain: 由PromptTemplate、模型和可选的输出解析器组成. 链接收多个输入变量, 使用PromptTemplate生成提示, 传递给模型, 最后使用输出解析器把模型返回值转化成预期格式
- 索引相关链
- 提示选择器

## agents 代理
- 工具: 用来方便模型和其他资源交互
- 代理: 围绕模型的包装器，接收用户输入，决定模型的行为
- 工具集: 解决特定问题的工具集合
- 代理执行器: 代理和一组工具，调用代理

|Apify | 一个数据抓取平台|
|--- | ---|
|ArXiv | arXiv是一个收集物理学、数学、计算机科学、生物学与数理经济学的论文预印本的网站|
|AWS Lambda | Amazon serverless计算服务|
|Shell工具 | 执行shell命令|
|Bing Search | Bing搜索|
|ChatGPT插件 | |
|DuckDuckGo | DuckDuckGo搜索|
|Google Places | Google地点|
|Google Search | Google搜索|
|Google Serper API | 一个从google搜索提取数据的API|
|Gradio Tools | Gradio应用|
|IFTTT Webhooks | 一个新生的网络服务平台，通过其他不同平台的条件来决定是否执行下一条命令|
|OpenWeatherMap | 天气查询|
|Python REPL | 执行python代码|
|Requests | 发送网络请求|
|SceneXplain | 一个访问ImageCaptioning的工具，通过url就可以获取图像描述|
|Wikipedia | 查询wiki数据|
|Wolfram Alpha | 一个计算平台，可以计算复杂的数学问题|
|YouTubeSearchTool | 视频搜索|
|Zapier | 一个工作流程自动化平台|

|工具 | 介绍|
|--- | ---|
|Apify | 一个数据抓取平台|
|ArXiv | arXiv是一个收集物理学、数学、计算机科学、生物学与数理经济学的论文预印本的网站|
|AWS Lambda | Amazon serverless计算服务|
|Shell工具 | 执行shell命令|
|Bing Search | Bing搜索|
|ChatGPT插件 | |
|DuckDuckGo | DuckDuckGo搜索|
|Google Places | Google地点|
|Google Search | Google搜索|
|Google Serper API | 一个从google搜索提取数据的API|
|Gradio Tools | Gradio应用|
|IFTTT Webhooks | 一个新生的网络服务平台，通过其他不同平台的条件来决定是否执行下一条命令|
|OpenWeatherMap | 天气查询|
|Python REPL | 执行python代码|
|Requests | 发送网络请求|
|SceneXplain | 一个访问ImageCaptioning的工具，通过url就可以获取图像描述|
|Wikipedia | 查询wiki数据|
|Wolfram Alpha | 一个计算平台，可以计算复杂的数学问题|
|YouTubeSearchTool | 视频搜索|
|Zapier | 一个工作流程自动化平台|

