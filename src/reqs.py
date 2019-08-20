from urllib.parse import urljoin
import requests


class Requests():
    def __init__(self, base_url):
        self.base_url = base_url

    def register(self, username, password):
        url = urljoin(self.base_url, "register")
        json_ = {"username": username, "password": password}

        r = requests.post(url, json=json_)
        return r.json()

    def login(self, username, password):
        url = urljoin(self.base_url, "login")
        json_ = {"username": username, "password": password}

        r = requests.post(url, json=json_)
        return r.json()

    def create_note(self, title, content, username, token):
        url = urljoin(self.base_url, "createNote")
        json_ = {
            "title":    title,
            "content":  content,
            "username": username,
            "token":    token
        }

        r = requests.post(url, json=json_)
        return r.json()

    def get_notes_list(self, username, token):
        url = urljoin(self.base_url, "getNotesList")
        json_ = {"username": username, "token": token}

        r = requests.post(url, json=json_)
        return r.json()

    def get_note(self, note_id, username, token):
        url = urljoin(self.base_url, "getNote")
        json_ = {"note_id": note_id, "username": username, "token": token}

        r = requests.post(url, json=json_)
        return r.json()

    def remove_note(self, note_id, username, token):
        url = urljoin(self.base_url, "removeNote")
        json_ = {"note_id": note_id, "username": username, "token": token}

        r = requests.delete(url, json=json_)
        return r.json()

    def modify_note(self, note_id, username, token, title, content):
        url = urljoin(self.base_url, "modifyNote")
        json_ = {
            "note_id":  note_id,
            "username": username,
            "token":    token,
            "title":    title,
            "content":  content
        }

        r = requests.put(url, json=json_)
        return r.json()


if __name__ == "__main__":
    r = Requests("http://srv02.mikr.us:40052")
    token = r.login("synnek", "luszownik1337")["token"]
    print(token)
    print(r.get_notes_list("synnek", token))
