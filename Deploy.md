# 开发教程

### 一、准备工作

1. Fork 本仓库到自己 Github 仓库下
2. 将代码 Clone 到本地，并确定已经安装好 node / npm 环境
3. 执行 `npm i` 安装模块依赖，然后执行 `npm run dev` 看是否可以跑起来

### 二、文档格式说明

1. 假如可以跑起来，可以去 `src/pages/posts` 只留一个 markdown 文件用于格式参考，或者加入自己的文件，文档说明如下
2. 第一行的文档建议是一个图片的展示，这样代码会自动取第一行为你的头图，也可以已通过 front matter 规范用 pic 字段表示，假如都没有填写，会使用默认的图片
3. 中间空一行，第三行是文档的描述，可以用 `small` 标签包裹，用于文字的描述部分，也可用 front matter 规范中 desc 字段表示，假如没有，会使用默认描述
4. 关于文档的时间，也是默认通过 node 取到文档的创建时间，假如不想要这个，也可用 front matter 规范中 date 字段表示
5. 关于文章的标题，可以用 `数字-标题` 的方式，方便很多地方的统一处理

### 部署说明

1. 由于 astro 最终打包出来是静态的文件，按理所有支持资源部署的平台都支持的，比如说 Github Pages、Vercel、Netlify 都可以的，此次重点推荐用 Vercel 部署，很简单高效，其他的平台可以参考 [astro](https://docs.astro.build/en/guides/deploy/) 文档，以下说明的是 Vercel 的部署教程
2. 首先确保 Fork 的代码已经传到 Github 中了, 然后进入 [Vercel](https://vercel.com/new) 选择 `Continue with GitHub`，将对应的仓库 import 进去
3. 导入后，确定 FRAMEWORK PRESET 是 Astro（[截图](https://gw.alipayobjects.com/zos/k/ic/0BffKE.png)），一般会默认选中，没有的话请选择这个，选择后，点击 Deploy 即可，稍等片刻，等待部署
4. 过了一会儿部署完成了，参考[截图](https://gw.alipayobjects.com/zos/k/e3/QLS7dG.png)位置，就是你的域名地址好了，点击进去就可以访问了，是不是很简单

### 新增功能
1. 评论使用[Waline](https://waline.js.org/),按教程配置即可
2. TOC
3. busuanzi pv统计
4. 只有README.md有变动(新建文章的场景)时, github actions触发 `vercel --prod`

> 注意第4点, 能看到这里,说明你很大概率已经在vercel创建好了对应的项目。考虑到通常开发者都会直接用vercel-cli直接本地发布，并且vercel给的用量也够。 因此第四点并不是一个很有价值的功能

### 项目配置
config.json配置如下填写即可
```json
{
  "title": "测试狗",
  "author": "thinkerchan",
  "description": "测试狗周刊",
  "keywords": "测试狗,testdog,testdog.cn",
  "icon": "https://t-qiniu.linkroutes.com/uPic/XgSVmb.jpg",
  "pic": "",
  "homePage": "https://post.testdog.cn",
  "blogPage": "",
  "twitterId": "thinkerchan",
  "githubId": "thinkerchan",
  "repo": "thinkerchan/weekly",
  "cmtURL":"https://cmt.testdog.cn", // 不配置则不显示评论
  "pv": true
}
```

文档设置toc
```
---
toc: true
---

xxxxxxxx
```

### github actions
> 本仓库使用github actions主要是为了自动更新readme.md，这个不是必要的。不了解Github actions可查看[文档](https://docs.github.com/zh/actions/quickstart)

直接按下操作即可:
1. 先在 https://github.com/settings/tokens/new 创建一个秘钥, 在`Select scopes`中把 `repo`和`workflow`勾上, 保存. 然后复制生成的那个明文秘钥，格式类似: ghp_xxxxxxxxxxx , 注意不要泄露。

2. 回到 https://github.com/你的仓库/settings/secrets/actions 中, 点击`new repository secret` 创建一个名为`GH_TOKEN`的变量, 值为步骤1中的秘钥

3. 回到 https://github.com/你的仓库/settings/actions, 找到 `Workflow permissions`, 选中 `读和写权限` 保存即可

4. 同理, 先获取[Vercel token](https://vercel.com/account/tokens), 按照步骤2创建一个名为`VERCEL_TOKEN`的变量

### 其他
考虑到也有人可能会同步到自己的微信公众号, 可以使用这个md转公众号文章工具 https://thinkerchan.com/md/dist/

---
感谢
- [tw93](https://github.com/tw93/weekly)
- [我](https://github.com/thinkerchan/weekly)