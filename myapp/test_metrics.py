#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
1、调整各个节点实际数据
2、结合前端展示，分析进度
3、有时间部署 grafana 剩余组件的 dashboard
'''
test=[
    {
        "consul集群":{
            "集群状态":"健康",
            "运行时长":157632021,
            "节点个数":4.0
        }
    },
    {
        "consul节点1":{
            "节点状态":"健康",
            "运行时长":157632021,
            "cpu使用率":0.15,
            "mem使用率":20
        }
    },
    {
        "consul节点2":{
            "节点状态":"健康",
            "运行时长":157632021,
            "cpu使用率":0.16,
            "mem使用率":25
        }
    },
    {
        "consul节点3":{
            "节点状态":"异常",
            "运行时长":0,
            "cpu使用率":0,
            "mem使用率":0
        }
    },
    {
        "consul节点4":{
            "节点状态":"健康",
            "运行时长":152632021,
            "cpu使用率":0.12,
            "mem使用率":19
        }
    },
    {
        "nginx组件":{
            "组件状态":"健康",
            "运行时长":1930284,
            "节点个数":2.0
        }
    },
    {
        "nginx节点1":{
            "节点状态":"健康",
            "运行时长":152632021,
            "cpu使用率":0.18,
            "mem使用率":11
        }
    },
    {
        "nginx节点2":{
            "节点状态":"健康",
            "运行时长":112632021,
            "cpu使用率":0.02,
            "mem使用率":7.3
        }
    },
    {
        "tomcat组件":{
            "组件状态":"健康",
            "运行时长":1930284,
            "节点个数":3.0
        }
    },
    {
        "tomcat节点1":{
            "节点状态":"健康",
            "运行时长":112632021,
            "cpu使用率":0.02,
            "mem使用率":7.3
        }
    },
    {
        "tomcat节点2":{
            "节点状态":"健康",
            "运行时长":112632021,
            "cpu使用率":0.02,
            "mem使用率":7.3
        }
    },
    {
        "tomcat节点3":{
            "节点状态":"异常",
            "运行时长":112632021,
            "cpu使用率":0.02,
            "mem使用率":7.3
        }
    },
    {
        "prometheus组件":{
            "服务状态":"健康",
            "运行时长":12110235,
            "节点个数":2.0
        }
    },
    {
        "prometheus节点1":{
            "节点状态":"健康",
            "运行时长":112632021,
            "cpu使用率":0.15,
            "mem使用率":10
        }
    },
    {
        "prometheus节点2":{
            "节点状态":"异常",
            "运行时长":112632021,
            "cpu使用率":0.02,
            "mem使用率":7.3
        }
    },
    {
        "grafana组件":{
            "服务状态":"健康",
            "运行时长":12110235,
            "节点个数":2.0
        }
    },
    {
        "grafana节点1":{
            "节点状态":"健康",
            "运行时长":112632021,
            "cpu使用率":0.15,
            "mem使用率":10
        }
    },
    {
        "grafana节点2":{
            "节点状态":"异常",
            "运行时长":112632021,
            "cpu使用率":0.02,
            "mem使用率":7.3
        }
    },
    {
        "mysql":{
            "节点状态":"健康",
            "运行时长":112632021,
            "cpu使用率":1.6,
            "mem使用率":20
        }
    },
    {
        "knox":{
            "节点状态":"健康",
            "运行时长":112632021,
            "cpu使用率":1.6,
            "mem使用率":20
        }
    },
    {
        "keycloak":{
            "节点状态":"健康",
            "运行时长":112632021,
            "cpu使用率":1.6,
            "mem使用率":20
        }
    },
    {
        "ambari-server":{
            "节点状态":"健康",
            "运行时长":112632021,
            "cpu使用率":1.6,
            "mem使用率":20
        }
    },
    {
        "ambari-agent组件":{
            "服务状态":"健康",
            "运行时长":112632021,
            "节点个数":2.0
        }
    },
    {
        "ambari-agent节点1":{
            "节点状态":"健康",
            "运行时长":112632021,
            "cpu使用率":0.15,
            "mem使用率":10
        }
    },
    {
        "ambari-agent节点2":{
            "节点状态":"异常",
            "运行时长":112632021,
            "cpu使用率":0.02,
            "mem使用率":7.3
        }
    }
]