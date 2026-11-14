[app]

title = TULAY
package.name = tulay
package.domain = org.karjak

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 35
android.minapi = 23
android.archs = arm64-v8a
android.permissions = INTERNET

[buildozer]

log_level = 2
warn_on_root = 1
