# Latitude AI - Android APK

将 [dglatitude.cc](https://www.dglatitude.cc) 封装为原生 Android 应用。

## 📱 功能

- ✅ 原生 Android 应用体验
- ✅ 全屏 WebView 加载网页
- ✅ 适配深色/浅色模式
- ✅ 支持 arm64-v8a 和 armeabi-v7a 架构

## 🚀 快速开始

### 安装 APK

1. 前往 **Actions** 页面
2. 点击最新的 workflow run
3. 在 **Artifacts** 区域下载 `latitude-apk-arm64.zip`
4. 解压得到 `.apk` 文件，安装到手机

### 本地开发（需要 WSL/Linux）

```bash
# 安装依赖
pip install kivy buildozer

# 运行（桌面）
python main.py

# 构建 APK
buildozer android debug
```

## 🛠️ 技术栈

- [Kivy](https://kivy.org/) - Python UI 框架
- [Buildozer](https://buildozer.readthedocs.io/) - Android 打包工具
- [GitHub Actions](https://github.com/features/actions) - 自动化构建

## 📄 License

MIT License
