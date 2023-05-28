# NewsPush
在这个信息爆炸的时代,人们容易被大量信息淹没。
你是否也遇到过以下情况:
希望了解一些重要新闻事件和热点话题,却总是被广告和视频轻易分散注意力,等回过神来已经没有多余的时间?
这时,我们就需要一款定点新闻推送服务了。
***该仓库实现了一款基于邮箱的新闻推送服务:***
目前支持:
1. 知乎热榜  
2. 百度贴吧热榜 
3. 一财网 
4. 财新网
5. 新浪财经 
6. 历史上的今天
7. 高楼迷 
8. 起点中文网  
9. 纵横中文网
10. 咖啡日报
11. 开发者头条
12. IT之家
排名不分先后,欢迎赞助帮助我们提高排名:心: 
***未来计划支持的特性:***
- 基于企业微信的微信消息推送
如果您有想要添加的特性或者在使用本工具时遇到的问题,欢迎提出 [拉取请求](https://github.com/IronManStank/NewsPush/pulls) 或 [问题](https://github.com/IronManStank/NewsPush/issues/new/choose) !
## 开发日志 
开发进度请查看: [更新日志](./CHANGELOG.md) 
## 使用方式 
### 通过 Github Action 
1. [复刻](https://github.com/IronManStank/NewsPush/fork) 本仓库 
2. 启用 Github Action 
3. 设置 scrects:参数请参考 ***命令行参数***部分 
4. 测试:进入复刻后的仓库,进入 Actions 手动运行 
### 配置文件
- ***token***: 项目根目录新建文件`token.txt`,在其中填入彩云天气的token。彩云天气token申请教程请自行搜索。 
- ***email***:在`tools/emailpush`下新建文件`email_config.json`,按照模板填写。

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

### 命令行参数 
可使用 python main.py --help 查看命令行帮助信息。 
在使用 Github Action 时,需要在仓库的`secrets`中添加以下参数:
- ETOKEN: 此token为彩云天气API token 
- SENDER: 内容为邮件发送者邮箱 
- USERS: 内容为邮件接收者邮箱,多个邮箱请用 , 分隔 
- TOKEN: 值为发送者邮箱token,开启IMAP或POP3服务后获得 
- CITY: 选择的城市天气 
**注:彩云天气token不是必要条件,但它会影响实际使用体验**
