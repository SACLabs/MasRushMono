# MAS Kernel

## Actor

## Node

## Gate

## Router

## Graph

## MAS Node design
根据外界需求，产品经理写详细的需求文档，接着架构师做系统设计，项目经理把这个项目分成具体的任务分给工程师，工程师写具体的代码，写完所有代码后，测试工程师进行代码测试。
Product Manager: 制定初步需求
Architect: 负责系统设计
Engineer: 实现代码
QA Engineer: 负责进行详细的质量测试
Project Manager: 管理项目进度并调整资源
Boss (Client): 提供项目验收与反馈

[ 计划与需求分析 节点 ]
              |
              |--> [ demand解析: Input: 需求定义（test + descript + refer src）; Output: 需求文档 ]
              |
[ 架构设计与开发 节点]
              |--> [ 架构/系统设计: Input: 需求定义, 需求文档; Output: 系统设计说明 ]
              |       &emsp;|
              |       &emsp;|--> [ 工程开发: Input: 需求定义, 需求文档, 系统设计说明; Output: 功能代码 ]
              |
[ 测试与验收 节点]
              |
              |--> [ 质量检测: Input: 需求定义, 需求文档, 系统设计说明, 代码实现; Output: 测试报告 ]
              |
              |--> [ 验收: Input: 需求定义, 需求文档, 系统设计说明, 代码实现, 测试报告; Output: 产品验收和反馈]
