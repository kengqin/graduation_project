import app.dao.order_mydetails as mydetails



def get_order_mydetails(order_id):
    if order_id:
        result=mydetails.get_order_mydetail(order_id)

        res_1=result[0]["order_time"].split()

        result[0]["order_time"]=res_1[0]
        # print(result)
        return result
def insert_order_mydetails(order_id):
    if order_id:
        result=mydetails.insert_order_mydetail(order_id)
        # print(result)
        return result

if __name__ == '__main__':
    a={"order_id":'201902192001568'}
    get_order_mydetails(a)