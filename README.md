# NewsPush
NewsPush

## 正在施工中

开发进度请查看: [changelog](./CHANGELOG.md)



## 使用方式
### 配置文件
- **token**: 项目根目录新建文件 `token.txt` 并在其中写入彩云天气的token
- **email**: 新建文件 `email_config.json`，并按照模板填写

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
