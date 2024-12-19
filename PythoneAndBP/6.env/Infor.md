进入环境

```
cd testing/Scripts
activate
cd producting/Scripts
activate
```

安装后端依赖

```
cd ../
pip install -r package.txt
```

查看依赖是否安装完成

```
pip list
```

让后端跑起来

```
uvicorn main:app --reload
```
