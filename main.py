"""
Latitude AI - Android APK
将 https://www.dglatitude.cc 封装为原生 Android 应用
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.utils import platform

# 设置窗口标题和状态栏颜色
Window.clearcolor = (1, 1, 1, 1)

if platform == 'android':
    from jnius import autoclass
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    activity = PythonActivity.mActivity
    window = activity.getWindow()
    # 状态栏颜色 (深蓝色)
    from android.graphics import Color
    window.setStatusBarColor(Color.parseColor('#1a73e8'))


class MainLayout(BoxLayout):
    pass


class LatitudeApp(App):
    title = 'Latitude AI'

    def build(self):
        return MainLayout()

    def on_start(self):
        """应用启动时加载网页"""
        if hasattr(self.root, 'ids') and 'webview' in self.root.ids:
            self.root.ids.webview.url = 'https://www.dglatitude.cc'


if __name__ == '__main__':
    LatitudeApp().run()
