# WwTrans 企微消息转发代理 Docker

[![Build](https://github.com/YunJian101/WwTrans/actions/workflows/build.yml/badge.svg)](https://github.com/YunJian101/WwTrans/actions/workflows/build.yml) [![Docker readme update](https://github.com/YunJian101/WwTrans/actions/workflows/readme_update.yml/badge.svg)](https://github.com/YunJian101/WwTrans/actions/workflows/readme_update.yml)

WwTrans 是一个基于 Docker 的企业微信消息转发代理服务，提供简洁的 Web 界面用于监控服务器公网地址状态。

## 功能特性

- 🚀 快速部署，一键启动
- 🌐 自动获取并显示服务器公网 IP
- 📅 记录公网地址更新时间
- 💾 IP 变化时自动保存，未变化时不写入
- 🎨 现代化 Web 界面，响应式设计
- 📱 支持 PC 和移动端访问

## 快速开始

### Docker 运行

```bash
docker run -d \
    --name WwTrans \
    --restart=always \
    -p 80:80 \
    alioth1/wwtrans:latest
```

### Docker Compose

```yaml
version: '3.3'
services:
    wwtrans:
        container_name: WwTrans
        restart: always
        ports:
            - '80:80'
        image: 'alioth1/wwtrans:latest'
```

## 访问服务

部署完成后，访问 `http://服务器IP` 即可查看服务状态页面。

页面会显示：
- 当前服务器公网 IP 地址
- 公网地址最近一次更新的时间
- 点击 IP 地址可复制到剪贴板

## 支持平台

Docker 镜像支持以下架构：

- linux/386
- linux/amd64
- linux/arm64/v8
- linux/arm/v7
- linux/arm/v6
- linux/ppc64le
- linux/s390x

## 项目说明

- **前端**：纯 HTML + CSS + JavaScript，无外部依赖
- **后端**：Nginx + CGI Shell 脚本
- **基础镜像**：Alpine Linux 3.23

## 许可证

本项目遵循开源许可证，详见 [LICENSE](LICENSE) 文件。

## 致谢

感谢原项目 [wxchat-Docker](https://github.com/DDSRem-Dev/wxchat-Docker) 提供的技术基础和灵感。

---

© 2025 WwTrans 企微消息转发服务 | Docker 部署版