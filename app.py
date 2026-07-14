from flask import Flask, render_template, request
app = Flask(__name__, template_folder=&quot;.&quot;)
@app.route(&#39;/&#39;, methods=[&#39;GET&#39;, &#39;POST&#39;])
def index():
success_message = None
if request.method == &#39;POST&#39;:
name = request.form.get(&#39;name&#39;)
email = request.form.get(&#39;email&#39;)
phone = request.form.get(&#39;phone&#39;)
success_message = f&quot;Thank you for registering, {name}!&quot;
return render_template(&#39;index.html&#39;, success=success_message)
if __name__ == &#39;__main__&#39;:
app.run(host=&#39;0.0.0.0&#39;, port=5000)
