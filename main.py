from website import create_app

app = create_app()  

if __name__ == '__main__':
    app.run(debug=True,port=5000)  # Set debug=True for development, change to False in production