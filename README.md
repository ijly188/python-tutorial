# python-tutorial

test

# 參考
https://coderzcolumn.com/tutorials/python/logging-config-simple-guide-to-configure-loggers-from-dictionary-and-config-files-in-python
https://www.gushiciku.cn/pl/24ek/zh-tw
https://zhung.com.tw/article/python%E4%B8%AD%E7%9A%84log%E5%88%A9%E5%99%A8-%E4%BD%BF%E7%94%A8logging%E6%A8%A1%E7%B5%84%E4%BE%86%E6%95%B4%E7%90%86print%E8%A8%8A%E6%81%AF/
https://stackoverflow.max-everyday.com/2017/10/python-logging/
https://blog.perwagnernielsen.dk/django_logging.html
https://titangene.github.io/article/python-logging.html


# 測試 grep/awk 撈accessLog指令
grep accessLog log.txt | awk '{print $1 " " $2 " - " $11 " - " $12 " - " $13}'