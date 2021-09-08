from hello import app
from time import sleep
with app.test_client() as c:
    response = c.get('/') # Perhaps here is where we'd call a Woodhouse endpoint
    assert response.data == b'Hello World!'
    sleep(240)
    assert response.status_code == 200
