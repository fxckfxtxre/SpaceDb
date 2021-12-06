<p align="center"><img src="https://i.ibb.co/Lnhyr3s/image.png" /></p>

<p align="center">
  <a href="https://pypi.org/project/spacedb"><img alt="PyPI" src="https://img.shields.io/pypi/v/spacedb?color=brightgreen"></a>
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/fxckfxtxre/spacedb?color=blueviolet&label=size">
  <img alt="GitHub" src="https://img.shields.io/github/license/fxckfxtxre/spacedb?color=critical">
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/fxckfxtxre/spacedb?color=orange">
</p>

<p align="center">
  <img alt="GitHub repo size" src="https://img.shields.io/discord/904729539362586674?color=blue&label=discord">
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/fxckfxtxre/stratz?color=ff69b4">
</p>


## Features

- Easy to use
- Encoding support
- Json friendly
- Light weight and fastest
- Support all python types

## Instalation

#### Via **pip**
```bash
$ pip install spacedb
```

#### Via **github**
```bash
$ git clone https://github.com/fxckfxtxre/SpaceDB.git
$ cd SpaceDB
$ python setup.py
```

## Docs

- Initialization:
  ```python
  db = spacedb.Storage(<name>, <[args]>, <encoding>)
  example = spacedb.Storage("cars", ["name", "power", "color"], "base64")

  #Note: encoding in 1.1.0v supports base64 or json
  ```

- Add
  ```python
  db.add(<arg>=<value>, ...)
  example.add(name="ferrari", power=1000, color="red")
  ```

- Delete
  ```python
  db.delete(<arg>=<value>, ...)
  example.delete(power=1000)

  #Note: also use 2 and more args
  example.delete(color="red", power=1000) #its work
  ```

- Update
  #### Update data
  ```python
  db.update({<new args>}, <old arg>, ...)
  example.update({"name": "bmw"}, name="ferrari")

  #Note: also use 2 and more args
  example.update({"name": "bmw", "power": 750}, name="ferrari", color="red")
  ```

- Search
  #### Return first data by your query
  ```python
  db.search(<arg>=<value>, ...)
  example.search(name="ferrari") #return data or none

  #Note: also use 2 and more args
  example.search(name="ferrari", color="red")
  ```

- Search All
  #### As opposed to **search** this method returned **all** data by your query
  ```python
  db.search_all(<arg>=<value>, ...)
  example.search_all(name="ferrari") #return [data, data] or none
  ```
  

- Unique
  #### **Check** unique
  ```python
  db.unique(<arg>=<value>, ...)
  example.unique(name="ferrari") #if unique return true else false

  #Note: also use 2 and more args
  example.unique(name="ferrari", power=1000)
  ```

- Data
  #### **All** data from database
  ```python
  db.data() #return all data from db
  ```

## Examples
- [Redirect app](https://github.com/fxckfxtxre/SpaceDb/tree/main/examples/redirect)