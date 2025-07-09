import importlib
import sys
import types
import pytest
import os

# Fixture to provide the helpers module with dummy dependencies
@pytest.fixture
def helpers(monkeypatch):
    # Ensure the project root is in sys.path for module imports
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    dummy_engine = types.SimpleNamespace(
        getProperty=lambda name: [types.SimpleNamespace(id="id")],
        setProperty=lambda name, value: None,
        say=lambda text: None,
        runAndWait=lambda: None,
    )
    dummy_pyttsx3 = types.SimpleNamespace(init=lambda: dummy_engine)
    dummy_geocoder = types.SimpleNamespace(ip=lambda arg: types.SimpleNamespace(latlng=[10, 20]))

    monkeypatch.setitem(sys.modules, "pyttsx3", dummy_pyttsx3)
    monkeypatch.setitem(sys.modules, "pyautogui", types.ModuleType("pyautogui"))
    monkeypatch.setitem(sys.modules, "psutil", types.ModuleType("psutil"))
    monkeypatch.setitem(sys.modules, "pyjokes", types.ModuleType("pyjokes"))
    monkeypatch.setitem(sys.modules, "requests", types.ModuleType("requests"))
    sr = types.ModuleType("speech_recognition")
    sr.Recognizer = lambda: None
    sr.Microphone = object
    monkeypatch.setitem(sys.modules, "speech_recognition", sr)
    monkeypatch.setitem(sys.modules, "geocoder", dummy_geocoder)

    helpers = importlib.import_module("helpers")
    importlib.reload(helpers)
    return helpers


def test_translate_known_word(helpers, monkeypatch):
    outputs = []
    monkeypatch.setattr(helpers, "speak", lambda text: outputs.append(text))
    helpers.translate("abandoned industrial site")
    assert outputs == [helpers.data["abandoned industrial site"]]


def test_weather(monkeypatch, helpers):
    outputs = []
    monkeypatch.setattr(helpers, "g", types.SimpleNamespace(latlng=[1, 2]))
    monkeypatch.setattr(helpers, "speak", lambda text: outputs.append(text))

    def fake_get(url):
        class Resp:
            def json(self):
                return {
                    "cod": 200,
                    "coord": {"lat": 1, "lon": 2},
                    "name": "TestCity",
                    "sys": {"country": "TC"},
                    "weather": [{"main": "Rain"}],
                    "wind": {"speed": 3},
                    "main": {"temp": 15, "humidity": 80},
                }
        return Resp()

    monkeypatch.setattr(helpers.requests, "get", fake_get, raising=False)
    helpers.weather()

    assert outputs == [
        "1latitude2longitude",
        "Current location is TestCityTCdia",
        "weather type Rain",
        "Wind speed is 3 metre per second",
        "Temperature: 15degree celcius",
        "Humidity is 80",
    ]
