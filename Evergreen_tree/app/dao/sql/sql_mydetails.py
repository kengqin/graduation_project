sql_mydetails = {
    "get_order_detail": "SELECT o.order_time,o.tourst_time,o.onum,o.oname,o.otelephone,o.order_start,o.card,s.tname,s.tid,s.tintroduce,t.adult_price FROM order_ticket AS o INNER JOIN scenic_spotty AS s INNER JOIN ticket as t ON s.tid=o.scenic_id and s.tid=t.scenic_id WHERE o.order_id={order_id} LIMIT 1",
    "insert_comment":"insert into comment(order_id,user_id,comm,comment_time,scenic_id)values ({order_id},{user_id},'{comm}','{comment_time}',{scenic_id}) ",
    "select_user_id":"select id from user where telephone={telephone}",
    "update_order_ticket":"update order_ticket set order_start = {order_start} WHERE order_id={order_id};"
}
