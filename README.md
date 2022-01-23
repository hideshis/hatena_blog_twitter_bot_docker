# hatena_blog_twitter_bot_docker
hatena_blog_twitter_botをdocker上で実行する。
はてなブログの最新記事10件から1件を無作為に選択し、そのURLをツイートする。

```
docker build -t my-python-app .
docker run -it --rm --name my-running-app my-python-app
```