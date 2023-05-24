# 项目启动命令

## 常规启动

```shell
uvicorn app:app --reload
```

## 上线启动

```shell
uvicorn app:app --reload --host 0.0.0.0 --port 9000
```
