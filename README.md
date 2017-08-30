Pygments Server
==
I needed a good way to generate pygments-compatible syntax highlighted html blocks from clientside JavaScript, and couldn't find anything suitable.

Run the server, then post JSON in the form of
```json
{
  "lang": "Java",
  "code": "System.out.println(func(1, \"cat\"))"
}
```
And you'll receive back a highlighted html block. The language key is optional, as pygments can somewhat guess the language, but its recomennded that you include it.

See: [here](https://github.com/richleland/pygments-css) for compatible css styles.

You can find my server at `https://pygments.austinschwartz.com/` if you want to use that instead

Install
==
1. virtualenv pygmentsserver
2. source pygmentsserver/bin/activate
3. pip install -r requirements.txt
4. Then run server.py or `pip install gunicorn` and `gunicorn --bind 0.0.0.0:PORT wsgi:app`

Note
==
This is very similar to [Trevor Turk's Pygments server](https://github.com/trevorturk/pygments) although it doesn't depend on GAE, uses a much more recent pygments, and supports language guessing.

License
==
MIT license, see license file
