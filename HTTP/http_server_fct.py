#! /usr/bin/python
#---------------------------------------------


def send_get_response(data, type):
    try:
        self.send_response(200)
        self.send_header("Content-type", type)
        self.end_headers()
        self.wfile.write(data)
    except:
        pass

def retrieve_post_data(self):
    data = None
    self.send_response(200)
    try:
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = post_data.decode('utf8')
    except:
        print("[\033[1;31merror\033[0m] POST param retrieving failed")
    return data

def decipher_json(data):
    for key, value in data.items():
        lvl1 = key
        for key_, value_ in data[key].items():
            lvl2 = key_
            lvl3 = value_
    return [lvl1, lvl2, lvl3]
