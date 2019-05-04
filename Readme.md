# 获取Menherachan的背景图

前端时间，微博图床加入了防盗链，导致我博客的背景图不能正常显示了，原先使用的是随机Menhera Api。 他会随机返回一个微博图床的url。而现在无法显示了，将会返回403错误码。

## 获取Menhera背景图

通过api批量下载Menhera背景图，并且去除背景色。

api来自 https://api.ixiaowai.cn/mcapi/mcapi.php

你需要安装 requests 和 pillow 库。

完成之后，将会在 `convert` 文件夹中显示去除背景色的图片。

然后你可以使用多种方式，在服务端重写一个api，达成之前的效果。

