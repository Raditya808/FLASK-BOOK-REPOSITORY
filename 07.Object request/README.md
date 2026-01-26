# Request

<p>Request To check User spec Pc / Laptop</p>



## Code 


```bash 
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
  headers = request.headers

  body = ['%s %s' % (key,value) for key,value in sorted(headers.items))
  ]
  body = '<br>'.join(body)

  return body
if __name__ =="__main__"
  app.run(debug=True)
```



## Browser output ON localhost


<img width="1919" height="798" alt="image" src="https://github.com/user-attachments/assets/228593a0-1018-4fe6-8f52-b9a0e5a97e08" />
