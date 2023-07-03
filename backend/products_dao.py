from sql_connection import get_sql_connection
def get_all_dishes(connection):
    
    cursor = connection.cursor()

    query = ("SELECT dishes.product_id, dishes.dish_name, dishes.uom_id, dishes.price_per_unit, dishes.course_type , unit_of_measure.uom_name FROM dishes INNER JOIN unit_of_measure on dishes.uom_id=unit_of_measure.uom_id") 

    cursor.execute(query)
    response=[]

    for (product_id, dish_name, uom_id, price_per_unit, course_type, uom_name ) in cursor:
       response.append(
           {
               'product_id': product_id,
               'dish_name': dish_name,
               'uom_id': uom_id,
               'price_per_unit': price_per_unit,
               'course_type': course_type,
               'uom_name': uom_name

           }
        
           
       )

    return response

def insert_new_dish(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO dishes "
             "(dish_name, uom_id, price_per_unit, course_type)"
             "VALUES (%s, %s, %s, %s)")
    data = (product['dish_name'], product['uom_id'], product['price_per_unit'], product['course_name'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid
def delete_dish(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM dishes where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection=get_sql_connection()
    print(insert_new_dish(connection,{
        'dish_name': 'Blue Lagoon',
        'uom_id': '1',
        'price_per_unit':120,
        'course_name': 'Beverages'

    }))

