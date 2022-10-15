# back-end_flask
Lab 1 
Застосунок надає наступні можливості:
1. Створення користувача
2. Створення категорії витрат
3. Створення запису про витрати

4. Отримання списку категорій
5. Отримання списку записів по певному користувачу
6. Отримання списку записів в категорії для певного користувача

Запити можна відправляти з Postman або через форму

Endpoints:

1 create user and records using form or postman
https://backendflask1.herokuapp.com/records (get all records or post)

2 to get all categories or post category
https://backendflask1.herokuapp.com/categories (post is possible via Postman or via form)

3 get all user's records by user's id
/users/<int:user_id>/records

4 get all user's records by user's id and by category (by postman)
/users/<int:user_id>/records
add a key 'category_id' and value(int) to the params

To install requirements recursively by following command
pip install -r requirements.txt
