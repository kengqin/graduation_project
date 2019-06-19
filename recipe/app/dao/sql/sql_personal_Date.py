sql_personal_date={
    "get_personal_date":"SELECT u.nickname,u.email,u.`name`,u.card_id,u.sex,u.qq FROM `user` AS u WHERE u.telephone={telephone} LIMIT 1",
    "change_personal_date":"UPDATE `user` AS u SET u.telephone='{telephone}',u.sex='{sex}',u.qq='{qq}',u.card_id='{card_id}',u.email='{email}',u.`name`='{name}',u.nickname='{nickname}' WHERE telephone={telephone}"
}