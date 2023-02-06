# NewsPush

当今世界，人人处于信息茧房之中。你是否遇到以下情况:

想要了解一些国家大事和热点新闻，却被广告和视频悄悄偷走时间和精力。等到回过头来的时候才发现自己的剩余时间所剩无几？

这个时候，我们就需要定点推送服务了。

**本仓库可实现基于邮箱的新闻推送服务：**

现支持：

```
知乎热榜
百度贴吧热榜
第一财经
财新网
新浪财经新闻
历史上的今天
高楼迷
起点中文网
纵横中文网
咖啡日报
开发者头条
IT之家
```

排名不分先后，如有赞助可置顶❤️

**未来预计支持特性：**

- 基于企业微信的微信消息推送

关于其他想要添加的特性或者是使用本程序中遇到的问题欢迎 `Pull Requests`或`Issues`！

## 正在施工中

开发进度请查看: [changelog](./CHANGELOG.md)

## 使用方式

### 配置文件

- **token**: 项目根目录新建文件 `token.txt` 并在其中写入彩云天气的token。关于彩云天气的token申请教程请自行百度。
- **email**: 在`tools/emailpush`下新建文件 `email_config.json`，并按照模板填写

```json
{
    "sender": "asd@qq.com",
    "token": "m*********ji",
    "receivers": [
        "1******0@qq.com",
        "a*****q@icloud.com"
    ],
    "header": {
        "HeaderFrom": "Personal Intelligence System",
        "HeaderTo": "BOSS"
    },
    "subject": "Email test",
    "message": "This is a test email."
}
```

注：彩云天气token不是必备项，但是会影响实际使用体验。

### 命令行解析方式

在使用命令行解析方式的时候，需要向仓库的`secrets`中添加以下参数：

- `ETOKEN`: 该token为彩云天气api token.
- `SENDER`: 内容为邮件发送者邮箱。
- `USERS`: 内容为邮件接收者邮箱【可为多个，','分割】。
- `TOKEN`: 值为发送者邮箱token，开启IMAP或POP3服务后获得。

注：彩云天气token不是必备项，但是会影响实际使用体验。
