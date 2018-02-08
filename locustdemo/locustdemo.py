# -*- coding:utf-8 -*-

from locust import HttpLocust, TaskSet, task
import random


class RobotTaskSet(TaskSet):

    @task(1)
    def root(self):
        with self.client.get("/", catch_response=True) as response:
            print type(response)
            print dir(response)
            print response.content
            print response.status_code
            if response.status_code == 200:
                # response.failure("status code error!")
                response.success()

    @task(2)
    def get_libraries(self):
        self.client.get("/v1/libserver/libraries")


class RobotLocust(HttpLocust):
    task_set = RobotTaskSet
    min_wait = 5000
    max_wait = 15000


##example2
def get_library_keywords(l):
    libs = [
              "DataTime",
              "Reserved",
              "String",
              "Screenshot",
              "Process",
              "Telnet",
              "BuiltIn",
              "Collections",
              "Easter",
              "OperatingSystem"
            ]
    i = random.randint(0, len(libs)-1)
    l.client.get("/v1/libserver/library/keywords/%s" % libs[i])


def get_builtin_keyword(l):
    l.client.get("/v1/libserver/keyword/info?lib_name=BuiltIn&kw_name=Comment")


class RobotTaskSet2(TaskSet):
    tasks = {get_library_keywords: 3, get_builtin_keyword: 1}


class RobotLocust2(HttpLocust):
    task_set = RobotTaskSet2
    min_wait = 5000
    max_wait = 15000