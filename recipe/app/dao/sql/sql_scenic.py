sql_user={
    "getdatabyid":"select tname from scenic_spotty where tid={tid}",
    "getdatabyid2":"select tintroduce from scenic_spotty where tid={tid}",
    "getdatabyid3":"select taddress from scenic_spotty WHERE tid={tid}",
    "getdatabyid4":"select open_time from scenic_spotty where tid={tid}",
    "getdatabyid5":"select adult_price from ticket where scenic_id={id}",
    "getdatabyid6":"select adult_introduce from ticket where scenic_id={id}",
    "getdatabyid13":"select Market_value from ticket where scenic_id={id}",
    "getdatabyid14":"select image_ponit from scenic_spotty where tid={tid}",
    "getdatabyid15":"select image_ad1 from scenic_spotty where tid={tid}",
    "getdatabyid16":"select image_ad2 from scenic_spotty where tid={tid}",
    "get_u_id":"select id from user where telephone={telephone}",
    "into":"insert into college (user_id,scenic_id) values ('{user_id}','{scenic_id}')",
"getnewid":"select c.id from college as c inner join user as u on c.user_id = u.id where telephone={telephone} and scenic_id={scenic_id}",
    "shanchu":"delete from college where scenic_id={scenic_id}",
    "select_comment":"select c.comm,c.comment_time,c.order_id,u.telephone  from comment as c inner join user as u on c.user_id = u.id where scenic_id={scenic_id} order by c.comment_time desc,c.id desc"
}