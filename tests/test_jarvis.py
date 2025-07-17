import importlib
import os
import sys
import types
import pytest

# Fixture to provide the Jarvis module with dummy dependencies
@pytest.fixture
def jarvis(monkeypatch):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    outputs = []

    dummy_engine = types.SimpleNamespace(
        getProperty=lambda name: [types.SimpleNamespace(id="id0"), types.SimpleNamespace(id="id1")],
        setProperty=lambda name, value: None,
        say=lambda text: None,
        runAndWait=lambda: None,
    )
    dummy_pyttsx3 = types.SimpleNamespace(init=lambda: dummy_engine)

    dummy_wikipedia = types.SimpleNamespace(summary=lambda q, sentences=2: f"summary:{q}")

    sr = types.ModuleType("speech_recognition")
    sr.Recognizer = lambda: None
    sr.Microphone = object

    dummy_webbrowser = types.SimpleNamespace(
        register=lambda *a, **k: None,
        get=lambda *a, **k: types.SimpleNamespace(open_new_tab=lambda url: outputs.append(url)),
        open=lambda url: outputs.append(url),
        BackgroundBrowser=lambda path: None,
    )

    dummy_smtplib = types.SimpleNamespace(
        SMTP=lambda *a, **k: types.SimpleNamespace(
            ehlo=lambda: None,
            starttls=lambda: None,
            login=lambda *a, **k: None,
            sendmail=lambda *a, **k: None,
            close=lambda: None,
        )
    )

    dummy_news = types.SimpleNamespace(speak_news=lambda: outputs.append("news"), getNewsUrl=lambda: "http://news")
    dummy_OCR = types.SimpleNamespace(OCR=lambda: None)
    dummy_helpers = types.SimpleNamespace(
        speak=lambda text: outputs.append(text),
        weather=lambda: outputs.append("weather"),
        takeCommand=lambda: "dummy",
        cpu=lambda: outputs.append("cpu"),
        joke=lambda: outputs.append("joke"),
        screenshot=lambda: outputs.append("screenshot"),
    )
    dummy_translate_mod = types.SimpleNamespace(translate=lambda word: outputs.append(f"translate:{word}"))
    dummy_youtube = types.SimpleNamespace(youtube=lambda q: outputs.append(f"youtube:{q}"))
    dummy_getpass = types.SimpleNamespace(getuser=lambda: "tester")
    dummy_cv2 = types.ModuleType("cv2")

    monkeypatch.setitem(sys.modules, "pyttsx3", dummy_pyttsx3)
    monkeypatch.setitem(sys.modules, "wikipedia", dummy_wikipedia)
    monkeypatch.setitem(sys.modules, "speech_recognition", sr)
    monkeypatch.setitem(sys.modules, "webbrowser", dummy_webbrowser)
    monkeypatch.setitem(sys.modules, "smtplib", dummy_smtplib)
    monkeypatch.setitem(sys.modules, "news", dummy_news)
    monkeypatch.setitem(sys.modules, "OCR", dummy_OCR)
    monkeypatch.setitem(sys.modules, "helpers", dummy_helpers)
    monkeypatch.setitem(sys.modules, "diction", dummy_translate_mod)
    monkeypatch.setitem(sys.modules, "youtube", dummy_youtube)
    monkeypatch.setitem(sys.modules, "getpass", dummy_getpass)
    monkeypatch.setitem(sys.modules, "cv2", dummy_cv2)

    jarvis_module = importlib.import_module("jarvis")
    importlib.reload(jarvis_module)

    return jarvis_module.Jarvis(), outputs


def test_execute_query_cpu(jarvis):
    j, outputs = jarvis
    j.execute_query("cpu")
    assert "cpu" in outputs


def test_execute_query_wikipedia(jarvis):
    j, outputs = jarvis
    j.execute_query("wikipedia python")
    assert outputs[:3] == ["Searching Wikipedia....", "According to Wikipedia", "summary: python"]


def test_execute_query_are_you_there(jarvis):
    j, outputs = jarvis
    j.execute_query("jarvis are you there")
    assert outputs[-1] == "Yes Sir, at your service"
