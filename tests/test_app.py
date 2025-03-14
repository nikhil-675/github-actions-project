from app.app import hello_world  # ✅ Clean import from the app package

def test_hello_world():
    assert hello_world() == "Hello, World!"
