import time
import logging
from app import app


logging.basicConfig(
                level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S')

if __name__ == '__main__':
    for item in range(100, 1):
        task_add = app.send_task('add', args=(item, item),)
        task_divide = app.send_task('divide', args=(item, item-1),)
        result_add = task_add.get()
        result_divide = task_divide.get()
        logging.info(result_add)
        logging.info(result_divide)
        time.sleep(5)