import logging

# 创建一个FileHandler对象，
# 为了解决中文乱码问题，将文件编码设置为 “utf-8”。
handler = logging.FileHandler(filename="test.log", encoding="utf-8")
# 进行日志相关设置，将日志输出到test.log文件中，
# 通过format设置日志文件的内容和格式，
# 通过datefmt设置日期时间的显示形式，
# 通过level设置了日志输出级别
logging.basicConfig(handlers=[handler],
                    format="时间：%(asctime)s|| 文件名：%(filename)s||行号：%(lineno)d"
                           "||级别：%(levelname)s||内容：%(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S", level=logging.INFO)
logging.debug('这是一条debug级别的日志信息')
logging.info('这是一条info级别的日志信息')
logging.warning('这是一条warning级别的日志信息')
logging.error('这是一条error级别的日志信息')
logging.critical('这是一条critica级别的日志信息')
try:
    print('这是一个错误的语句', 66 / 0)
except Exception as e:
    # excepiton()可将参数中的内容写到日志文件
    logging.exception("出现错误，错误信息是" + str(e))
