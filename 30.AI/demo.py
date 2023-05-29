from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage, ChatMessage
from langchain.prompts import ChatPromptTemplate, PromptTemplate, SystemMessagePromptTemplate, AIMessagePromptTemplate, HumanMessagePromptTemplate, ChatMessagePromptTemplate, FewShotPromptTemplate
from langchain.embeddings import OpenAIEmbeddings


OpenAI.openai_api_key = ""

# 常用于单次对话
llm = OpenAI(model_name="gpt-3.5-turbo", n=2, temperature=0.3)
llm.streaming = True
llm("给我讲个段子")  # 单个
llm.generate(["第一句", "第二句"])  # 多个

# 聊天
chat = ChatOpenAI()
messages = [
    SystemMessage(content="输出指定的结构体"),
    HumanMessage(content="认证接口")
]
chat(messages)
chat.generate([messages, messages])

# 提示模板
system_template = "你是一个{input_language}翻译成{output_language}的助手"
system_template_prompt = SystemMessagePromptTemplate.from_template(system_template)
human_template = "{text}"
human_template_prompt = HumanMessagePromptTemplate.from_template(human_template)
chat_prompt = ChatPromptTemplate.from_messages([system_template_prompt, human_template_prompt])
messages = chat_prompt.format_prompt(input_language="A", output_language="B", text="这个human")
chat(messages.to_messages())


# 嵌入
embeddings = OpenAIEmbeddings()
text = "dsadas"

query_result = embeddings.embed_query(text)
batch_query_result = embeddings.embed_documents([text])  # 批量向openai查向量


# 提示
prompt_template = "{first} + {second} = ?"
prompt = PromptTemplate(
    input_variables=["first", "second"],
    template=prompt_template
)

prompt_text = prompt.format(first="1", second="2")

llm = OpenAI(model_name="gpt-3.5-turbo", n=2, temperature=0.3)
print(llm(prompt_text))

## 少样本提示词

examples = [
    {"word": "开心", "antonym": "难过"},
    {"word": "高", "antonym": "矮"}
]

examples_template = """
单次: {word}
反义词: {antonym}
"""

example_prompt = PromptTemplate(
    input_variables=["word", "antonym"],
    template=examples_template
)


few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="给出每个单次的反义词",
    suffix="单次:{input}\\n反义词:",
    input_variables=["input"],
    example_separator="\\n"
)

prompt_text = few_shot_prompt.format(input="粗")
print(prompt_text)

# 给出每个单词的反义词
# 单词: 开心
# 反义词: 难过

# 单词: 高
# 反义词: 矮

# 单词: 粗
# 反义词:

# 调用OpenAI
llm = OpenAI(temperature=0.9)
print(llm(prompt_text))

# 链
from langchain.chains import LLMChain, SimpleSequentialChain

prompt_template = "{first} + {second} = ?"
prompt = PromptTemplate(
    input_variables=["first", "second"],
    template=prompt_template
)
llm = OpenAI(temperature=0.9)
chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run("1", "1"))

## 创造第二条链
second_prompt = PromptTemplate(
    input_variables=[],
    template="{result}+3=?"
)

chain_second = LLMChain(llm=llm, prompt=second_prompt)

overall_chain = SimpleSequentialChain(chains=[chain, chain_second], verbose=True)

print(overall_chain.run("1", "2"))

# agent代理
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)
tools = load_tools(["serpapi"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

agent.run("明天在北京穿什么衣服合适?")

"""
> Entering new AgentExecutor chain...
I need to find out what the weather will be like tomorrow in Beijing.
Action: Search
Action Input: "Beijing weather tomorrow"
Observation: Beijing, Beijing ; Current Weather. 2:41 AM. 61° ; TODAY'S WEATHER FORECAST. 5/10. 82° ; TONIGHT'S WEATHER FORECAST. 5/10. 57° ;
TOMORROW'S WEATHER FORECAST. 5/11.
Thought: It looks like it will be warm tomorrow, so I should wear something light.
Final Answer: 明天在北京穿薄衣服合适 。
> Finished chain.
"""

# 记忆
## 记忆有两种类型：短期和长期记忆。短期记忆一般指单一会话时传递数据，长期记忆则是处理多个会话时获取和更新信息。
