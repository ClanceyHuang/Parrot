# Parrot
鹦鹉学舌，加载自己的聊天记录语料，通过机器学习训练"人工智障"客服聊天模型。

## 关于语料的说明

语料存放路径在`train_data/文件名.conv`

语料格式如下，其中读取识别原始文件中段落和行头的标示：
```
E
M 你好
M 你是xxx吗？
E
M 不是
M 那是什么？
E
```


大家可以使用小黄鸡的语料训练完成的模型文件`model_data.zip`进行聊天测试。

## 代码执行顺序

1. 在下载好代码和语料之后，将语料文件放入`train_data`目录下。

2. 按照`data_util.py`(数据预处理器)-->`execute.py`(执行器)-->`app.py`(应用模块)的顺序执行就可以了。

## 参考代码和文献

* http://blog.topspeedsnail.com/archives/10735/comment-page-1#comment-1161

* http://www.easyapple.net/?p=1384&from=singlemessage&isappinstalled=0

* https://github.com/zpppy/seqGan_chatbot

## 建议环境

系统及语言版本
```
ubuntu14.04 +
python3.5 +
```

核心包
```
tensorflow==2.0.0
flask==0.11.1
```

## 依赖配置

* 保存配置文件```pip freeze > requirements.txt```

* 加载配置文件```pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/```
