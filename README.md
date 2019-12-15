# Markdown4Zhihu

这是一个可以将您的Markdown文件一键转换为知乎编辑器支持模式的仓库。

它会自动的处理图片，行内公式，多行公式，以及对表格的部分支持。如果您的md文件和其图片文件夹在Data文件夹下，您本地的图片会自动转换为github上的raw链接。
上传知乎后一切都是那么美好。

## 使用方法

这里我们假设您的文件名为`一个测试文档.md`，并将其和同名图片文件夹放到`Data`目录下，接着打开terminal(Linux/MacOS)或Git Bash(Windows)(或其他任何支持Git命令的终端)，输入以下命令：

`python zhihu-publisher.py --input="./Data/一个测试文档.md"`

OK，all set. 在`Data`目录下，你可以看到一个`一个测试文档_for_zhihu.md`的文件，将它上传至知乎编辑器即可。
