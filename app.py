#!/usr/bin/env python
# encoding: utf-8
"""
:file      :   app.py
:author    :   ClanceyHuang 
:name      :   app.py
:refer     :   unknown
:desc      :   ...
:version   :   Python3.x
:contact   :   ClanceyHuang@outlook.com
:copyright :   © 2017 by ClanceyHuang(Kirk).
:license   :   MIT, see LICENSE for more details.
"""

# here put the import lib
from flask import Flask, render_template, request, jsonify, current_app
import execute
import time
import threading
import jieba


def heartbeat():
    """定义心跳检测函数"""
    print(
        time.strftime("%Y-%m-%d %H:%M:%S - heartbeat",
                      time.localtime(time.time())))
    timer = threading.Timer(60, heartbeat)
    timer.start()


timer = threading.Timer(60, heartbeat)
timer.start()
"""
ElementTree 在 Python 标准库中有两种实现。
一种是纯 Python 实现例如 xml.etree.ElementTree ，另外一种是速度快一点的 xml.etree.cElementTree 。
尽量使用 C 语言实现的那种，因为它速度更快，而且消耗的内存更少。
"""

app = Flask(__name__, static_url_path="/static")
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


@app.route("/message", methods=["POST"])
def reply():
    """定义应答函数，用于获取输入信息并返回相应的答案
    jsonify:是用于处理序列化json数据的函数，就是将数据组装成json格式返回。http://flask.pocoo.org/docs/0.12/api/#module-flask.json
    """
    # 从请求中获取参数信息
    req_msg = request.form["msg"]
    # 将语句使用结巴分词进行分词
    req_msg = " ".join(jieba.cut(req_msg))

    # 调用decode_line对生成回答信息

    res_msg = execute.predict(req_msg)
    # 将unk值的词用微笑符号袋贴
    res_msg = res_msg.replace("_UNK", "^_^")
    res_msg = res_msg.strip()

    # 如果接受到的内容为空，则给出相应的回复
    if res_msg == " " or res_msg == "":
        res_msg = "我们聊点啥呢？"
    return jsonify({'text': res_msg})


# @app.route("/")
# def index():
#     return render_template("index.html")

if __name__ == "__main__":
    """启动APP"""
    app.run(host="127.0.0.1", port=8888)
