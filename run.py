from app import create_app

if __name__ == "__main__":
	application = create_app()
	application.app_context().push()
	application.run(debug=True)
