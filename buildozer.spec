[app]

# (str) Title of your application
title = Latitude AI

# (str) Package name
package.name = latitudeai

# (str) Package domain (needed for android/ios packaging)
package.domain = com.latitude

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json,txt

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
# 注意: 移除了 sdl2_ttf 版本限制，使用默认版本
requirements = python3,kivy,pyjnius,android

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Android API level to use (minimum)
android.api = 33

# (int) Minimum SDK required
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip trying to update the Android sdk
android.skip_update = False

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (str) The Android arch to build for
android.archs = arm64-v8a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (list) Android permission list
# 添加了 Internet 权限
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE

# (int) Target Android API version
android.target_api = 33

# (str) launchMode to set for the main activity
android.launch_mode = singleTask

# (bool) Indicate if the screen should stay on while on USB power
android.wakelock = False

# (str) Activity background color in #AARRGGBB format
android.activity_background_color = #FFFFFFFF

# (str) Extra command line arguments to pass to the build process
android.extra_manifest_xml = 
android.extra_manifest_application_arguments = 

# (str) Extra arguments to pass to the gradle build
android.gradle_options = 

# (list) Java classes to add as activities to the manifest
android.add_activities = 

# (list) Android AAR archives to add
android.add_aars = 

# (list) Android gradle dependencies to add
android.gradle_dependencies = 

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme
android.apptheme = @android:style/Theme.NoTitleBar

# (list) Pattern to whitelist for the whole project
android.whitelist = 

# (bool) If True, show verbose output from the build process
android.verbose = True

# (str) The format used to package the app for release mode (aab or apk or aar)
android.release_artifact = apk

# (str) The format used to package the app for debug mode (apk or aar)
android.debug_artifact = apk

#
# iOS specific
#

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios

# (bool) If True, skip confirmation for ios deployment
#ios.deploy_confirmation = 1

#
# macOS specific
#

# (str) Changes to the entitlements file
macos.entitlements =

# (str) Changes to the Info.plist file
macos.info_plist =

#
# Web specific
#

# (bool) Disable web-specific functionality
web.disable_auto_reload = False


[build]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Build output directory
output_dir = bin

# (str) The cache directory
cache_dir = .cache

# (str) The distribution directory
dist_dir = dist

# (list) List of extensions to watch for changes and rebuild
watch_exts = py,kv

# (str) Command to run when watching for file changes
watch_cmd = python3 main.py

# (str) Extra arguments to pass to buildozer
extra_args =

# (str) Android NDK path
android.ndk_path =

# (str) Android SDK path
android.sdk_path =

# (str) ANT directory (set by default)
android.ant_path =

# (str) JAVA JDK path
javaexec = java

# (str) Path to the hostpython installation
hostpython =

# (str) Additional arguments to pass to ndk-build
android.ndk_args =

# (bool) Copy files instead of symlink
copy_files = 1

# (str) The directory where the final APK will be placed
apk_output_dir = output

# (str) The filename pattern for the generated APK
apk_filename_pattern = {app.name}-{version}-{arch}

# (str) Extra environment variables to pass to the build process
env_persist =

# (str) Temporary directory for build operations
tmp_dir = /tmp/buildozer_{app.name}_{timestamp}


[publish]

# (str) The publish method to use (none, github, pypi, etc.)
publish_method = none
