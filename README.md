 
# interfaceTest
   Python开发接口测试框架，将结果以html的形式进行结果分析
    
# config.ini文件配置
 需要用户对根据配置文件的内容进行填写
```python
 
[DATABASE]
host = 10.10.12.191
username = XXXXXXXXX
password = XXXXXX
port = XXXX
database = XXXX

[HTTPS]
baseurl = https://10.10.12.196
port = 443
timeout = 5.0

[EMAIL]
mail_host = smtp.exmail.qq.com
mail_user = XXXXXXXX
mail_pass = XXXXXX
mail_port = 25
sender = XXXXXX
receiver = XXXXXXX
subject = APP-SPC800 接口自动化测试结果
content = "APP-SPC800 接口自动化测试报告"
on_off = 1  # 1:to send test result report; 0: not send test result report
```
