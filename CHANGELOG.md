# 更新日志

## [1.0.1] - 2025-02-04

### 新增
- 新增环境变量 `SHOW_PUBLIC_IP` 控制公网地址显示
- 默认值为 `true`（显示公网IP）
- 设置为 `false` 时隐藏公网地址显示区域
- 更新 README.md 添加环境变量说明文档

### 修改
- 优化 Dockerfile，移除过时的 `version` 字段
- 修复 fcgiwrap socket 路径配置
- 添加 dos2unix 处理脚本文件换行符问题
- 优化前端逻辑，根据环境变量动态显示/隐藏公网地址
