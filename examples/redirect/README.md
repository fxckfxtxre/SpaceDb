## Use
1. 
   #### Run ./main.py
   ```bash
   $ python main.py
   ```
2. 
   #### Create short link
   ```bash
   GET > http://localhost:2312/new?url=https://www.youtube.com > 200 > {"url": "http://localhost:2312/ENWjq"}
   ```
3. 
   #### And... Redirect
   ```bash
   GET > http://localhost:2312/ENWjq > 302 > https://www.youtube.com
   ```
