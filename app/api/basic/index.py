from . import basic_blueprint


@basic_blueprint.route("/api/v1/hello", methods=["GET"])
def index():
	return "Hello World!"
