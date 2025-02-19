"""
演示Socket服务器开发
"""
import socket
# 创建socket对象
socket_server = socket.socket()
# 绑定ip地址和端口
socket_server.bind(('127.0.0.1', 8888))
# 监听端口
socket_server.listen(1)
# listen方法内接收一个整数参数，表示接收链接的数量
# 等待客户端链接
# result = socket_server.accept()
# conn = result[0]        #客户端和服务端的链接对象
# address = result[1]     #客户端的地址信息
conn, address = socket_server.accept()
#accept方法返回的是二元元组（链接对象， 客户端地址信息）
# 可以通过  变量1, 变量2 = socket_server.accept()的形式，接收这个二元元组
# accept（）方法是阻塞方法，等待客户端的链接，如果没有链接就卡在这一步不向下进行

print(f"接收到了客户端的链接，客户端的信息是:{address}")

while True:
    # 接收客户端信息,要使用客户端课服务端的本次链接对象，而非socket_server对象
    data :str = conn.recv(1024).decode("utf-8")
    # recv接收的参数是缓冲区大小，一般给1024即可
    # recv方法的返回值是一个字节数组也就是bytes对象，不是字符串，可以通过decode方法通过UTF-8编码将字节数组转化为字符串对象
    print(f"客户端发来的消息是{data}")

    msg = input("请输入你和客户端回复的消息:")
    if msg == 'exit':
        break
    conn.send(msg.encode("utf-8")) #encode可以将字符串编码为字节数组对象
    # conn.send(msg)
# 关闭链接
conn.close()
socket_server.close()



