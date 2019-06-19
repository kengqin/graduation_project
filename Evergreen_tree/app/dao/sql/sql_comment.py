sql_comment={
    "get_comment":"SELECT o.order_id,o.tourst_time,o.onum,o.order_start,s.tname,t.adult_price from `user` as u INNER JOIN order_ticket as o INNER JOIN scenic_spotty as s INNER JOIN ticket as t on u.telephone=o.otelephone and o.scenic_id=s.tid and t.scenic_id=s.tid WHERE u.telephone={telephone}",
    "select_comment":"select c.order_id,c.comm,s.tname from comment as c inner join user as u on c.user_id=u.id inner JOIN scenic_spotty as s on c.scenic_id=s.tid where telephone='{telephone}'",
    "comment_se":"select c.comm from comment as c inner join user as u on c.user_id=u.id inner JOIN scenic_spotty as s on c.scenic_id=s.tid where order_id={order_id}",
    "del_comment":"delete from comment where order_id={order_id}",
    "get_sceipe_comment":"select c.id,c.comm,c.comment_time,u.nickname from comment as c inner join user as u on c.user_id = u.id where recipe_id = {recipe_id} ORDER BY c.id desc",
    "insert_sceipe_comment":"insert into comment(user_id ,comm,comment_time,recipe_id) values({user_id},'{comm}','{comment_time}',{recipe_id})",

}