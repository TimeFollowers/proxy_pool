from flask import Flask,g
from RedisClient import RedisClient

__all__ = ['app']
app = Flask(__name__)

def get_conn():
    if not hasattr(g,'redis'):
        g.redis = RedisClient()
    return g.redis

@app.route("/")
def index():
    return "<h2>welcome to proxy pool system</h2>"

@app.route("/random")
def get_proxy():
    """
    获取随机可用代理
    :return: 随机代理
    """
    conn = get_conn()
    return conn.random()

@app.route("/count")
def get_counts():
    """
    获取代理池数量
    :return: 代理池总数量
    """
    conn = get_conn()
    return str(conn.count())

if __name__ == "__main__":
    app.run()