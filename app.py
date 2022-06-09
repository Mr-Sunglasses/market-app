from market import APP, api
from market.routes import API_TEST, Square, FindUser

api.add_resource(API_TEST, '/test')
api.add_resource(Square, '/square/<int:num>')
api.add_resource(FindUser, '/user/<string:username_given>')

if __name__ == '__main__':
    APP.run(debug=True, port=5500)

