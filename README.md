# heroliss/fib

## 项目用途

两个 Fibonacci 实现示例：带缓存装饰器的递归 fib(n)，以及生成前 count 项的迭代器 fib2(count)。

## 当前状态

- 建议分类：Python Fibonacci 教学片段
- 生命周期：Dormant
- 最近 push：2016-08-07T07:51:44Z
- README 扫描状态：Missing

最新 push 为 2016-08-07，单次提交，长期冻结。适合标为教学/算法小片段。

## 实际运行方式

python fib.py 本身没有 main，不会输出。可在仓库根执行 python -c "from fib import fib, fib2; print(fib(10)); print(list(fib2(10)))"。

## 依赖与构建线索

Python 标准库；无 requirements、测试或许可证。

## 目录与证据

仓库只有 fib.py；包含 @buffer 缓存装饰器、递归 fib 和 fib2 生成器。

顶层目录/文件线索：

- `fib.py`

## 已知限制

- 本文档只依据 GitHub 元数据、README、构建文件、入口文件和目录证据整理，未进行完整构建或端到端运行验证。
- 不确定的运行环境、密码、服务器地址和兼容版本不在此处臆测。

## 需要确认

是否希望保留为算法笔记？

## 后续维护建议

1. 先确认“继续维护、完成冻结、历史保留、归档候选”中的一种状态。
2. 若继续保留，再补充一条可复现的运行验证记录和截图/输出。
3. 若确认完成或废弃，只保留简短历史说明，不需要改代码。

## 证据链接

- 仓库：[heroliss/fib](https://github.com/heroliss/fib)
- 默认分支：master
- 主要语言：Python
- stars / forks：0 / 0
- 扫描时间：2026-10-11T05:10:08Z
## 本地验证记录

在 Python 3.14 临时副本中已验证：`fib(10)` 得到 55，`list(fib2(10))` 得到 `[1,1,2,3,5,8,13,21,34,55]`；直接运行 `python fib.py` 没有输出，因为文件没有 main 入口。
