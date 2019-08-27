TEST_CYLE = 20
GETTER_CYLE = 20
TESTER_ENABLED = True
GETTER_ENABLE = True
API_ENABLE = True
API_HOST = '0.0.0.0'
API_PORT = 5555

from multiprocessing import Process
from api import app
from Getter import Getter
from Tester import Tester
import time
class Scheduler():
    def schedule_tester(self,cycle=TEST_CYLE):
        """
        定时测试代理
        :param cycle:
        :return:
        """
        tester = Tester()
        while True:
            print("测试器开始运行")
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self,cycle=GETTER_CYLE):
        """
        定时获取代理
        :param cycle:
        :return:
        """
        getter = Getter()
        while True:
            print("开始抓取代理")
            getter.run()
            time.sleep(cycle)

    def schedule_api(self):
        """
        开启api
        :return:
        """
        app.run(API_HOST,API_PORT)

    def run(self):
        print("代理池开始运行")
        if TESTER_ENABLED:
            test_process = Process(target=self.schedule_tester)
            test_process.start()
        if GETTER_ENABLE:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()
        if API_ENABLE:
            api_process = Process(target=self.schedule_api)
            api_process.start()

if __name__ == "__main__":
    Scheduler().run()