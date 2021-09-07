from hello import app
with app.test_client() as c:
    response = c.get('/') # Perhaps here is where we'd call a Woodhouse endpoint
    assert response.data == b'Hello World!'
    assert response.status_code == 200
