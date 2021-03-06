import sublime

from .path import OVERLAY_ROOT


def with_ignored_overlay(fun):
    def decorator(*args, **kwargs):
        disable_overlay()
        try:
            fun(*args, **kwargs)
        finally:
            enable_overlay()

    return decorator


def disable_overlay():
    prefs = sublime.load_settings("Preferences.sublime-settings")
    ignored = prefs.get("ignored_packages", [])
    if OVERLAY_ROOT not in ignored:
        prefs.set("ignored_packages", ignored + [OVERLAY_ROOT])


def enable_overlay():
    prefs = sublime.load_settings("Preferences.sublime-settings")
    ignored = prefs.get("ignored_packages", [])
    if OVERLAY_ROOT in ignored:
        ignored.remove(OVERLAY_ROOT)
        prefs.set("ignored_packages", ignored)
