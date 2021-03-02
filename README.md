# メール送信を自動化するためのプログラム

- メールを送信する作業を自動化
- メールを要求するくせに返信しないやつ対策で`Disposition-Notification-To`付与のメールを送信

## use clss
```
    arg = {
        "host":host,  # mail server
        "port": port, # port number
        "add": add,   # send from address
        "to_add": add, # send to address
        "title": title, # mail Subject
        "body": body # mail body
    }

    mail = Mail(arg)
    mail.send_mail()

```

