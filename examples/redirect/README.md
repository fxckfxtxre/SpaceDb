## Use
1. 
   #### Run ./main.py
   ```bash
   $ python main.py
   ```
2. 
   #### Go to localhost:2312
   ```bash
   GET > http://localhost:2312/new?url=https://www.youtube.com > 200 > {"url": "http://localhost:2312/ENWjq"}
   ```
3. 
   #### Redirect
   ```bash
   GET > http://localhost:2312/ENWjq > 302 > https://www.youtube.com
   ```
