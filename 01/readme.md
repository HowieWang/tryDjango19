## 01 配置django环境和建立工程

Generally the topics will include:
- Django Project Setup
- Class Based Views (& some Function Based Views)
- Models, Model Forms, Forms, Form Validation
- Integrate Bootstrap front-end framework.
- Django Registration Redux for Authentication/Registration
- And More


建立工作目录
mkdir code 
cd code 

建立虚拟环境
cc 3todo python=3 django=1.9 
coa 3todo

建立工程
python manage.py startproject 3todo

测试
python manage.py runserver
打开浏览器【查看是否正确，截图】

【理解主要文件含义？】

- manage.py
- settings.py 
- urls.py 
- wsgi.py 
- __init__.py 

测试admin页面，强大的后台瞬间展现
注意看刚才运行runserver时候是不是有个提示【migrate的意思？截个图】

建立数据库
python manage.py migrate
建立管理员账户
python manage.py createsuperuser

【重新查看浏览器，截图页面/admin】