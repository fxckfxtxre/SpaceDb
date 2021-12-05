import os.path
import base64
import json


class Storage(object):
    def __init__(self, path, rule, encoding="base64") -> None:
        self.encoding = encoding
        self.path = path.replace(".spacedb", "")

        if not os.path.exists(path + ".spacedb"):
            self.__new(rule)

    def unique(self, **rule):
        query = self.search(**rule)

        if query:
            return False
        
        return True
    
    def data(self):
        return self.__read()["data"]

    def add(self, **rule):
        send = {}
        for r in self.__read()["rule"]:
            if r in rule:
                send[r] = rule[r]

            else:
                raise Exception("Invalid rule arguments")

        data = self.__read()
        data["data"].append(send)

        self.__write(data)

        return True

    def delete(self, **rule):
        c = len(rule)
        data = self.__read()
        
        for i in data["data"]:
            c2 = 0
            for ii in i:
                try:
                    if i[ii] == rule[ii]:
                        c2 += 1
                except KeyError:
                    pass

            if c2 == c:
                data["data"].remove(i)
                self.__write(data)

                return True

        return False

    def update(self, new, **rule):
        query = self.search(**rule)
        data = self.__read()
        
        if query:
            for i in new:
                query[i] = new[i]
            
            self.add(**query)
            self.delete(**rule)
            
            return True

        return False

    def search(self, **rule):
        c = len(rule)
        
        for i in self.__read()["data"]:
            c2 = 0
            for ii in i:
                try:
                    if i[ii] == rule[ii]:
                        c2 += 1
                except KeyError:
                    pass

            if c2 == c:
                return i

        return None
    
    def search_all(self, **rule):
        s = []
        c = len(rule)
        
        for i in self.__read()["data"]:
            c2 = 0
            for ii in i:
                try:
                    if i[ii] == rule[ii]:
                        c2 += 1
                except KeyError:
                    pass

            if c2 == c:
                s.append(i)

        if len(s) > 0:
            return s

        return None

    def __new(self, rule):
        if self.encoding == "base64":
            self.__write({
                "rule": rule,
                "data": [],
                "encoding": "base64",
                "db": "spacedb"
            })
        else:
            self.__write({
                "rule": rule,
                "data": [],
                "encoding": "utf-8",
                "db": "spacedb"
            })

    def __decode(self, data):
        data = data.encode("utf-8")
        data = base64.b64decode(data)
        data = data.decode("utf-8")

        return data

    def __encode(self, data):
        data = data.encode("utf-8")
        data = base64.b64encode(data)
        data = data.decode("utf-8")

        return data

    def __read(self):
        if self.encoding == "base64":
            with open(self.path + ".spacedb") as db:
                
                return json.loads(self.__decode(db.read()))
        else:
            with open(self.path + ".spacedb") as db:
                
                return json.load(db)

    def __write(self, obj):
        if self.encoding == "base64":
            with open(self.path + ".spacedb", "w", encoding="utf-8") as db:
                db.write(self.__encode(json.dumps(obj)))
                
                return True
        else:
            with open(self.path + ".spacedb", "w", encoding="utf-8") as db:
                json.dump(obj, db)
                
                return True