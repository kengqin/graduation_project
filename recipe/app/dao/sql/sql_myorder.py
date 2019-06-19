sql_myorder={
    "get_order_detail":"SELECT o.order_id,o.tourst_time,o.onum,o.order_start,s.tname,t.adult_price from `user` as u INNER JOIN order_ticket as o INNER JOIN scenic_spotty as s INNER JOIN ticket as t on u.id=o.user_id and o.scenic_id=s.tid and t.scenic_id=s.tid WHERE u.telephone={telephone}",
    'del_order_detail':"DELETE FROM order_ticket WHERE order_ticket.order_id={order_id}"
}