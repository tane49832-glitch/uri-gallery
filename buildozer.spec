[app]

# (string) Title of your application
title = Ruri Gallery

# (string) Package name
package.name = rurigallery

# (string) Package domain (needed for android packaging)
package.domain = com.secretbase

# (string) Source code directory
source.dir = .

# (list) Source files to include (let's include py and png files)
source.include_exts = py,png,jpg,kv,atlas

# (string) Application version (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) format used to package the app for release (aab or apk)
android.release_artifact = apk

# (str) format used to package the app for debug (apk)
android.debug_artifact = apk

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable AndroidX support. Required for newer libraries.
android.enable_androidx = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
