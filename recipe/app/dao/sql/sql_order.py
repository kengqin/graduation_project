
sql_order={
    "get_ticket":"select t.tname,a.adult_introduce,a.adult_price from scenic_spotty as t inner JOIN ticket as a on t.tid=a.scenic_id where t.tid={tid}",
    "order_create":"insert into order_ticket(order_id,scenic_id,user_id,order_time,tourst_time,onum,oname,otelephone,order_start) values ('{order_id}','{scenic_id}','{user_id}','{order_time}','{tourst_time}','{onum}','{oname}','{otelephone}','{order_start}')",
    "getUserById": "select id from user where telephone={telephone} limit 1",
    "getOrderinfo":"select scenic_id,user_id,order_time,onum from order_ticket where order_id={order_id};",
    "get_ticket_1": "select t.tname,a.adult_introduce,a.adult_price from scenic_spotty as t inner JOIN ticket as a on t.tid=a.scenic_id where t.tid={tid}",
    "update_ticket":"update order_ticket set order_start = {order_start} WHERE order_id={order_id};",
    "select_ticket":"select order_start from order_ticket WHERE order_id={order_id};"
}