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
requirements = python3,kivy,plyer,sdl2_ttf==2.20.2,pyjnius,android

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

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
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) XML rules for auto backup
android.backup_rules =

# (str) The name of the JNI library to use for Android
android.jni_ignored_src =

# (list) Android permission list
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# (int) Target Android API version
android.target_api = 33

# (list) White list of Java classes that can be used in Python via pyjnius
android.add_jars =

# (list) Java class to add as an activity to the manifest.
android.add_activites =

# (str) OUYA Console category. Should be one of GAME or APP
# ouya.category = APP

# (str) Filename of OUYA console icon. It must exist in source dir.
# ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
android.intent_filters =

# (str) launchMode to set for the main activity
android.launch_mode = singleTop

# (list) Android additional libraries to copy into libs/armeabi
android.add_libs_armeabi =
android.add_libs_armeabi_v7a =
android.add_libs_arm64_v8a =
android.add_libs_x86 =
android.add_libs_x86_64 =

# (bool) Indicate if the screen should stay on while on USB power
android.wakelock = False

# (bool) Enable WebView-like behavior that helps when developing apps
android.embed_boot_into_start_activity = True

# (str) Activity background color in #AARRGGBB format
android.activity_background_color = #FFFFFF

# (str) Path to a custom android.jar
android.android_jar =

# (str) Used for package identifier naming convention
android.naming_convention =

# (bool) Android: copy libs instead of using addLibs with services
android.copy_libs = 1

# (str) The architecture of your device
android.arch = arm64-v8a

# (list) List of service declarations
services =

# (bool) Use --private data storage (True) or --dir public storage (False)
android.storage_type = files

#
# iOS specific
#

# (str) Name of the certificate to use for signing the debug version
#ios.certificate =

# (str) Name of the signing profile to use
#ios.profiles =

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

# (str) Path to build spec file
spec = buildozer.spec

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

# (str) GitHub repository URL
#publish.github_repo =

# (str) GitHub token for authentication
#publish.github_token =

# (str) PyPI repository URL
#publish.pypi_url =

# (str) PyPI token for authentication
#publish.pypi_token =

# (str) Additional arguments for publishing
#publish_extra_args =
