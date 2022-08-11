# 小姐姐下载器

_⚠ 本项目为学习项目，如果侵犯了您的权益，请及时联系删除_
> 使用 scrapy 框架下载小姐姐的图片

## 先决条件 ：

- [Proxy_Pool](https://github.com/jhao104/proxy_pool)
- [Scrapy](https://scrapy.org/)
- [Pillow](https://python-pillow.org/)

## 涉及的知识点

- scrapy 代理的使用
- 随机 UA 的使用
- 图片的下载

## 使用方法

1. 部署 proxy_pool

```shell
git clone https://github.com/jhao104/proxy_pool.git
cd proxy_pool
docker compose up -d
# 保持默认部署端口为 5010 如果有能力也可修改，但请对应修改本项目的相关端口
```

2. 下载本项目并切换到项目目录

```shell
git clone https://github.com/allinu/NiceGirls.git
cd NiceGirls
```

3. 创建虚拟环境

```shell
# 根据你的喜好自行创建
```

4. 安装项目依赖

```shell
pip install -U pip && pip install scrapy pillow
```

5. 运行对应的爬虫

```shell
# 青春、唯美
scrapy crawl vmgirls
# or
# 性感
scrapy crawl photos18
```

## 协议

    NiceGirls allinu
    Copyright © 2022 allinu

    Permission is hereby granted, free of charge, to any person obtaining
    a copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included
    in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
    DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
    OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

