# Latitude AI - Android APK

将 [dglatitude.cc](https://www.dglatitude.cc) 封装为原生 Android 应用。

## 📱 功能

- ✅ 原生 Android WebView 体验
- ✅ 全屏加载 dglatitude.cc
- ✅ 支持 JavaScript 和本地存储
- ✅ arm64-v8a 架构支持

## 🚀 快速开始

### 安装 APK

1. 前往 **Actions** 页面
2. 点击最新的 workflow run
3. 在 **Artifacts** 区域下载 `latitude-ai-apk.zip`
4. 解压得到 `.apk` 文件，安装到手机

### 本地开发

需要 Linux 或 WSL 环境：

```bash
# 安装依赖
pip install buildozer cython

# 构建 APK
buildozer android debug
```

## 🛠️ 技术栈

- [Kivy](https://kivy.org/) - Python UI 框架
- [Pyjnius](https://pyjnius.readthedocs.io/) - Android Java 接口
- [Buildozer](https://buildozer.readthedocs.io/) - Android 打包工具
- [GitHub Actions](https://github.com/features/actions) - 自动化构建

## 📄 License

MIT License
