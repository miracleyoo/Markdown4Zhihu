# Markdown4Zhihu

这是一个可以将您的Markdown文件一键转换为知乎编辑器支持模式的仓库。

它会自动的处理图片，行内公式，多行公式，以及对表格的部分支持。当图片过大时，您可以选择加上`--compress`选项，对超过大小阈值（这里约为500K）的图片进行自动压缩。如果您的md文件和其图片文件夹在Data文件夹下，您本地的图片会自动转换为github上的raw链接。
上传知乎后一切都是那么美好。

## 使用方法

1. 首先，您应当仿照本仓库建立一个类似的您自己的仓库，它包括一个Data文件夹与根目录下的`zhihu-publisher.py`。当然，您也可以选择直接folk本仓库到您自己的账号下。

2. 然后，打开`zhihu-publisher.py`文件，在文件开头有这么一句：`GITHUB_REPO_PREFIX = "https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/"`请修改`miracleyoo`为您自己的GitHub用户名，如果仓库名字也有变化，请做出相应微调。

3. 这里我们假设您的文件名为`一个测试文档.md`，并将其和同名图片文件夹放到`Data`目录下，接着打开terminal(Linux/MacOS)或Git Bash(Windows)(或其他任何支持Git命令的终端)，输入以下命令：

`python zhihu-publisher.py --input="./Data/一个测试文档.md"`

4. OK，all set. 在`Data`目录下，你可以看到一个`一个测试文档_for_zhihu.md`的文件，将它上传至知乎编辑器即可。
