from waitress import serve
import server
import generate
serve(server.app, host='0.0.0.0', port=80)
# serve(generate.app, host='0.0.0.0', port=5000)