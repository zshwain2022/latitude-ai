"""
Latitude AI - Android APK
将 https://www.dglatitude.cc 封装为原生 Android 应用
使用 Android 原生 WebView
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.utils import platform
from kivy.clock import Clock

if platform == 'android':
    from jnius import autoclass, cast
    from android.runnable import run_on_ui_thread
    
    # Android classes
    WebView = autoclass('android.webkit.WebView')
    WebViewClient = autoclass('android.webkit.WebViewClient')
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    LayoutParams = autoclass('android.view.ViewGroup$LayoutParams')
    View = autoclass('android.view.View')
    Color = autoclass('android.graphics.Color')


class LatitudeApp(App):
    def build(self):
        self.webview = None
        self.layout = Widget()
        
        # Schedule WebView creation after layout is ready
        Clock.schedule_once(self.create_webview, 0)
        
        return self.layout
    
    def on_pause(self):
        """App 进入后台时暂停 WebView"""
        if platform == 'android' and self.webview:
            self.webview.onPause()
        return True
    
    def on_resume(self):
        """App 恢复时恢复 WebView"""
        if platform == 'android' and self.webview:
            self.webview.onResume()
    
    @run_on_ui_thread
    def create_webview(self, *args):
        """在 UI 线程创建 Android WebView"""
        if platform != 'android':
            print("WebView only available on Android")
            return
        
        activity = PythonActivity.mActivity
        
        # Create WebView
        self.webview = WebView(activity)
        self.webview.setWebViewClient(WebViewClient())
        
        # Enable JavaScript
        settings = self.webview.getSettings()
        settings.setJavaScriptEnabled(True)
        settings.setDomStorageEnabled(True)
        settings.setCacheMode(settings.LOAD_DEFAULT)
        
        # Load the website
        self.webview.loadUrl('https://www.dglatitude.cc')
        
        # Add WebView to the activity's content view
        # Get the root view and add WebView to it
        root_layout = activity.findViewById(0x1020002)  # android.R.id.content
        
        if root_layout:
            # Remove any existing views
            root_layout.removeAllViews()
            
            # Add WebView with full screen layout
            params = LayoutParams(
                LayoutParams.MATCH_PARENT,
                LayoutParams.MATCH_PARENT
            )
            root_layout.addView(self.webview, params)
        else:
            # Fallback: set as content view directly
            activity.setContentView(self.webview)


if __name__ == '__main__':
    LatitudeApp().run()
