#简单修改
#简单修改2
#简单修改gitee
import redis

# 方案1：连接本地Redis（需要先启动Redis服务器）
# r = redis.Redis(host='localhost', port=6379, db=0)

# 方案2：添加连接检查
try:
    r = redis.Redis(host='localhost', port=6379, db=0, socket_connect_timeout=5)
    # 测试连接
    r.ping()
    print("Redis连接成功!")
except redis.ConnectionError:
    print("Redis连接失败! 请确保Redis服务器正在运行。")
    print("解决方案:")
    print("1. 安装并启动Redis服务器")
    print("2. 使用Docker: docker run -p 6379:6379 -d redis")
    print("3. 检查Redis是否在端口6379上运行")
    exit(1)

# 字符串操作
r.set("name", "Alice")          # 设置键值
print(r.get("name"))            # 输出: b'Alice'（返回bytes类型）

# 哈希操作
r.hset("user:1", "name", "Bob") # 设置哈希字段
print(r.hget("user:1", "name")) # 输出: b'Bob'

# 列表操作
r.lpush("tasks", "task1")       # 左插入列表
print(r.lrange("tasks", 0, -1)) # 输出: [b'task1']

# 集合操作
r.sadd("tags", "python", "redis") # 添加集合元素
print(r.smembers("tags"))        # 输出: {b'python', b'redis'}