# 导入模块库
import logging


# 建立一个类
class create_logger:
    # 初始化函数，参数filename用来指定日志文件名，
    # 参数formatter传入日志格式化字符串，
    # 参数level设置日志输出级别
    def __init__(self, filename, formatter, level):
        self.filename = filename
        self.farmatter = formatter
        self.level = level

    # 建立一个logger对象
    def create_logger(self, logger_name):
        # 创建一个logger(记录器)
        log_obj = logging.getLogger(logger_name)
        # 设置日志输出级别
        log_obj.setLevel(self.level)
        # 创建一个文件handler，用于写入日志文件
        handler = logging.FileHandler(self.filename, mode='w', encoding="utf-8")
        # 设置到文件的日志输出级别
        handler.setLevel(self.level)
        # 将格式化字符串转换成loggin认可的形式
        formatter = logging.Formatter(self.farmatter)
        # 设置handler的日志的输出格式
        handler.setFormatter(formatter)
        # 将handler加入logger（记录器），
        # 这样记录器就可以将日志输出到指定的文件中
        log_obj.addHandler(handler)
        # 返回记录器对象
        return log_obj


# 主程序main
if __name__ == '__main__':
    # 设置格式化字符串
    v_formatter = "时间：%(asctime)s|| 文件名：%(filename)s||行号：%(lineno)d" \
                  "||级别：%(levelname)s||内容：%(message)s"
    # 指定日志文件
    v_filename = 'test_logging.log'
    # 指定日志输出级别
    v_level = logging.DEBUG
    # 实例化类
    logger = create_logger(v_filename, v_formatter, v_level)
    # 生成日志记录器
    logger_obj = logger.create_logger('test')
    # 输出相应的日志
    logger_obj.debug('这是一条debug级别的日志信息')
    logger_obj.info('这是一条info级别的日志信息')
    logger_obj.warning('这是一条warning级别的日志信息')
    try:
        open('不存在.jpg', 'rb')
    except Exception as e:
        # excepiton()可将参数中的内容写到日志文件
        logger_obj.exception("出现错误，错误信息是" + str(e))
