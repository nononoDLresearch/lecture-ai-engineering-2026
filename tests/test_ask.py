from google.genai import types

from app import ask as ask_module


def test_ask_sends_and_extends_conversation_history(monkeypatch):
    history = [types.Content(role="user", parts=[types.Part.from_text(text="最初の質問")])]
    calls = []

    class FakeModels:
        def generate_content(self, **kwargs):
            calls.append(kwargs)
            return type("Response", (), {"usage_metadata": None, "text": "回答"})()

    class FakeClient:
        models = FakeModels()

    monkeypatch.setattr(ask_module.genai, "Client", lambda **kwargs: FakeClient())

    assert ask_module.ask("続きの質問", history) == "回答"

    sent_contents = calls[0]["contents"]
    assert [part.text for message in sent_contents for part in message.parts] == [
        "最初の質問",
        "続きの質問",
    ]
    assert [part.text for message in history[-2:] for part in message.parts] == [
        "続きの質問",
        "回答",
    ]