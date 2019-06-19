sql_sceipe={
    "select_sceipe_height":"SELECT r.id,r.rname,r.src,u.nickname FROM recipe as r inner join user as u on r.user_id = u.id LIMIT 8",
    "select_sceipe_height_1":"SELECT r.id,r.rname,r.src,u.nickname FROM recipe as r inner join user as u on r.user_id = u.id  LIMIT 7,14 ",
    "select_user_name":'select nickname from user where id={id};',
    "select_sceipe_info":"select * from recipe_ingredients where recipe_id = {recipe_id}",
    "select_recipe_detail":"select * from recipe_make where recipe_id ={recipe_id}",
    "get_recipe_info":"select d.src,d.describes,r.rname from detail as d inner join recipe as r on d.recipe_id=r.id where recipe_id ={recipe_id}",
    "search_sceipe":"select r.id,r.rname,u.nickname,r.src,d.describes from recipe as r inner join user as u on r.user_id = u.id inner join detail as d on r.id = d.recipe_id ",
    "search_recipe":"select r.id,r.rname,u.nickname,r.src,d.describes from recipe as r inner join user as u on r.user_id = u.id  inner join detail as d on r.id = d.recipe_id where  r.rname like '%{select}%'",
    "select_self":"select r.src ,r.rname, u.nickname,c.id,r.id as recipe_id  from counter as c inner join recipe as r on c.recipe_id=r.id inner join user as u on r.user_id=u.id where c.user_id ={user_id}",
    "select_selfcollege":"select r.src ,r.rname, u.nickname,c.id,r.id as recipe_id  from college as c inner join recipe as r on c.recipe_id=r.id inner join user as u on r.user_id=u.id where c.user_id = {user_id}",
    "get_nickname":"select u.nickname  from user as u inner join recipe as r on u.id = r.user_id where r.id={recipe_id};",



}