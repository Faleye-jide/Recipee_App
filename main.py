from flask import Flask, render_template


recipe_app = Flask(__name__)



@recipe_app.route('/')
async def get_read():
    return render_template('index.html')
    
if __name__ == '__main__':
    recipe_app.run(port=9000)