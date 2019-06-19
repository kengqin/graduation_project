/**
 * Created by 相如 on 2019/5/16.
 */
(function(){
    var dianzan=document.querySelector('.dianzan');
    var dianzan1=document.querySelector('.dianzan1');
    var shoucang=document.querySelector('.shoucang');
    var shoucang1=document.querySelector('.shoucang1');
    var token =window.localStorage && window.localStorage.getItem('token');
    // 页面跳转
    window.sessionStorage.setItem('from', location.href);

    var url = window.location.href;
    var result = url.split("?")[1];
    var keyValue = result.split("&");
    var obj = {};
    for (var i = 0; i < keyValue.length; i++) {
        var item = keyValue[i].split("=");
        obj[item[0]] = item[1];
        // sessionStorage.setItem("he", obj[item[0]])

    }
    // var token=window.localStorage && window.localStorage.getItem('token');
    var user_id=window.localStorage && window.localStorage.getItem('user_id');
    // var recipe_id=parseInt(location.href.split("?recipe_id=")[1]);
    // console.log(recipe_id)
    var nav_btn=document.querySelector("#nav_btn");
    var bs=document.querySelector("#bs-example-navbar-collapse-1");
    var ss=document.querySelectorAll(".ss");
    var outs= document.querySelector('.out');
    // var gang=document.querySelector('.gang');
    bs.style.display="none";
    nav_btn.onclick=function () {
        if (bs.style.display==="none"){
            bs.style.display="block";
        }else {
            bs.style.display="none";
        }
        for (var s of ss){
            s.style.display="none";
        }
    };
    // 退出
    outs.onclick=function(){

        localStorage.clear();
        nick_name.style.display="none";
        out.style.display='none';
        login.style.display="block";
        register.style.display="block";
        s1.style.display="block";
        location.href="sceipe_detail.html?sceipe_id="+obj[item[0]];

    };
    // 登录注册
    var login=document.querySelector(".login");
    var register=document.querySelector(".register");
    var s1 =document.querySelector(".s1");
    var nick_name=document.querySelector(".nick_name");
    var out =document.querySelector('.out');
    var remove=document.querySelector('.remove');
    nick_name.style.display="none";
    out.style.display='none';

    var nickname=window.localStorage && window.localStorage.getItem('nickname');

    if (token) {
        getData("http://47.102.45.80:8080/api/user/checkToken/", null,{"token": token}, function (res) {
            if (res && res["status_code"] === "10003") {
                login.style.display="none";
                register.style.display="none";
                s1.style.display="none";
                nick_name.style.display="block";
                nick_name.innerText=nickname;
                out.style.display="block";
                out.innerText='退出登录';

                nick_name.onclick=function () {
                    token=window.localStorage && window.localStorage.getItem('token');
                    if(token){
                        getData("http://47.102.45.80:8080/api/user/checkToken/", null,{"token": token}, function (res) {
                            if (res && res["status_code"] === "10003") {
                                location.href = "person_center.html?user_id=" + user_id
                            }else{
                                location.href="./pages/login.html"
                            }
                        })
                    }else{
                        location.href="./pages/login.html"
                    }
                }
                dianzan.style.display='block';
                shoucang.style.display='block';
                dianzan1.style.display='none';
                shoucang1.style.display='none';
                postData(api +'my_collection/select_counteron',{'user_id':user_id,"recipe_id":obj[item[0]]},null,function(res){
                    if(res && res.status_code == '14000'){
                        dianzan.style.color='orange';
                    }else{
                        dianzan.style.color='';
                    }
                })
                postData(api +'my_collection/select_collegeon',{'user_id':user_id,"recipe_id":obj[item[0]]},null,function(res){
                    if(res && res.status_code == '18000'){
                        shoucang.style.color='orange';
                    }else{
                        shoucang.style.color='';
                    }
                })
            }else{
                login.style.display="block";
                register.style.display="block";
                s1.style.display="block";
                nick_name.style.display="none";
                dianzan.style.display='none';
                shoucang.style.display='none';
                dianzan1.style.display='block';
                shoucang1.style.display='block';
            }
        });
    }else{
        dianzan.style.display='none';
        shoucang.style.display='none';
        dianzan1.style.display='block';
        shoucang1.style.display='block';
    }

    /* 点赞 */
    dianzan.onclick=function(){
        postData(api +'my_collection/select_counteron',{'user_id':user_id,"recipe_id":obj[item[0]]},null,function(res){
            if(res && res.status_code == '14000'){
                postData(api+'my_collection/delete_counteron',{'user_id':user_id,"recipe_id":obj[item[0]]},null,function(res){
                    if(res && res.status_code=='16000'){
                        dianzan.style.color='';
                        location.reload();
                        }})
            }else{
                postData(api+'my_collection/insert_counteron',{'user_id':user_id,"recipe_id":obj[item[0]]},null,function (res) {
                    if(res && res.status_code == '15000'){
                        dianzan.style.color='orange';
                        location.reload();
                    }})
            }
        })
    }
    shoucang.onclick=function(){
        postData(api +'my_collection/select_collegeon',{'user_id':user_id,"recipe_id":obj[item[0]]},null,function(res){
            if(res && res.status_code == '18000'){
                postData(api+'my_collection/delete_collegeon',{'user_id':user_id,"recipe_id":obj[item[0]]},null,function(res){
                    if(res && res.status_code=='16000'){
                        shoucang.style.color='';
                        location.reload();
                    }})
            }else{
                postData(api+'my_collection/insert_collegeon',{'user_id':user_id,"recipe_id":obj[item[0]]},null,function (res) {
                    if(res && res.status_code == '15000'){
                        shoucang.style.color='orange';
                        location.reload();
                    }})
            }
        })
    }
    /* 未登录时点赞*/
    dianzan1.onclick=function () {
        alert('请您先登录~')
    }
    shoucang1.onclick=function () {
        alert('请您先登录~')
    }

    /* 收藏总数 */
    var counter=document.querySelector('.shoucangshu');
    postData(api+'my_collection/select_college',{"recipe_id":obj[item[0]]},null,function (res) {
        if(res && res.status_code == '12000'){
            // console.log(res.college)
            counter.innerHTML= ` <span>${res.college['college']}个收藏</span> `;
        }else{
            counter.innerHTML= ` <span>${res.college['college']}0</span> `;
        }
    })
    /* 用户收藏总数 */
    var counte=document.querySelector('#college');
    postData(api+'my_collection/get_coll',{"recipe_id":obj[item[0]]},null,function (res) {
        if(res && res.status_code == '16000'){
            // console.log(res.college)
            counte.innerHTML= ` 总收藏数<span style="font-weight: 700;font-size: 1.5em" >${res['c']}</span> `;
        }else{
            counte.innerHTML= ` 总收藏数<span style="font-weight: 700;font-size: 1.5em" >0</span> `;
        }
    })
    /* 点赞总数 */
    var counters=document.querySelector('.dianzanshu');
    postData(api+'my_collection/select_counter',{"recipe_id":obj[item[0]]},null,function (res) {
        if(res && res.status_code == '13000'){
            // console.log(res.counter)
            counters.innerHTML= ` <span>${res.counter['counter']}个点赞</span> `;
        }else{
            counters.innerHTML= ` <span>${res.counter['counter']}0</span> `;
        }
    })
    /* 用户点赞总数 */
    var count=document.querySelector('#counte');
    postData(api+'my_collection/get_coun',{"recipe_id":obj[item[0]]},null,function (res) {
        if(res && res.status_code == '16000'){
            // console.log(res.counter)
            count.innerHTML= `总点赞数&nbsp;<span style="font-weight: 700;font-size: 1.5em">${res['c']}</span> `;
        }else{
            count.innerHTML= `总点赞数&nbsp;<span style="font-weight: 700;font-size: 1.5em">0</span> `;
        }
    })
    /* 获取菜谱用户 */
    var name =document.querySelector('.top-user');
    postData(api+'sceipe/get_nickname',{"recipe_id":obj[item[0]]},null,function(res){
        if(res && res.status_code =='10018'){
            console.log(res.list)
            name.innerText='美食达人用户:'+res.list['nickname'];
        }
    })
    /* 获取用户总评论数 */
    var com=document.querySelector('#con');
    postData(api+'my_collection/get_commets',{"recipe_id":obj[item[0]]},null,function(res){
        if(res && res.status_code == '16000'){
            com.innerText='('+res.result['c']+')'
        }else{
            com.innerText='(0)';
        }
    })
    /*  评论 */
    var textarea=document.querySelector('#textarea');
    remove.onclick=function(){
        if(token){
            postData(api+'orders/cashier', {"token": token},null, function (res) {
                if (res && res.status_code == '10003') {
                    var content = textarea.value.replace(/\n|\r\n/g,"<br>");
                    if(content){
                        postData(api+'comment/insert_recipe_comment',{"user_id":user_id,"recipe_id":obj[item[0]],"comm":content},null,function (res) {
                            if(res && res.status_code =='11000'){
                                content='';
                                alert(res.status_text);
                                location.reload();

                            }else{
                                alert(res.status_text);
                            }
                        })
                        // console.log(content)
                    }else{
                        alert('请输入评论哦')
                    }
                }else{
                    alert("登录已失效!请重新登录后重试！")
                }
            })
        }else{
            alert('请登录后再评论哦~')
        }
    }

    /*  获取评论  */
    var comment_a=document.querySelector('.comment_a');
    var num=5;
    postData(api+'comment/recipe_comment',{"recipe_id":obj[item[0]]},null,function (res) {
        if(res && res.status_code =='10801'){
            // console.log(res.comment.slice(0,5))
            if(res.comment.length<=5){
                var b=document.querySelector('.more');
                b.innerText='';
            }
           for(var a of res.comment.slice(0,5)){
                comment_a.innerHTML+=`<div class="comment_article">
                        <div class="username">
                            <span>美食达人:${a.nickname}</span>
                            <span style="color:grey;margin-left:20px;">${a.comment_time}</span>
                        </div>
                        <div class="comment_text">
                            <!--<h4>回复内容:</h4>-->
                            <div class="comm">
                                ${a.comm}
                            </div>
                        </div>
                        <!--<div style="width: 100%;height:1px;background-color:rgba(0,0,0,0.08);margin-top: 10px">-->

                        <!--</div>-->
                    </div>`
            }
        }else{
            var b=document.querySelector('.more');
            b.innerText='';
        }
    });
    var more=document.querySelector('.more');
    var a=0;
    more.onclick=function(){
        a++;
        num=num+5;
        postData(api+'comment/recipe_comment',{"recipe_id":obj[item[0]]},null,function (res) {
            if(res && res.status_code =='10801') {
                console.log(res.comment.length/5);
                if(num<res.comment.length){
                    comment_a.innerHTML='';
                    for (var a of res.comment.slice(0, num)) {
                        comment_a.innerHTML+= `<div class="comment_article">
                        <div class="username">
                            <span>美食达人:${a.nickname}</span>
                            <span style="color:grey;margin-left:20px;">${a.comment_time}</span>
                        </div>
                        <div class="comment_text">
                            <!--<h4>回复内容:</h4>-->
                            <div class="comm">
                                ${a.comm}
                            </div>
                        </div>
                        <!--<div style="width: 100%;height:1px;background-color:rgba(0,0,0,0.08);margin-top: 10px">-->

                        <!--</div>-->
                    </div>`
                    }
                }else if((num-res.comment.length)<=5 ){
                    comment_a.innerHTML= '';
                    more.innerText='没有更多了';
                    for (var a of res.comment.slice(0, num)) {
                        comment_a.innerHTML+= `<div class="comment_article">
                        <div class="username">
                            <span>美食达人:${a.nickname}</span>
                            <span style="color:grey;margin-left:20px;">${a.comment_time}</span>
                        </div>
                        <div class="comment_text">
                            <!--<h4>回复内容:</h4>-->
                            <div class="comm">
                                ${a.comm}
                            </div>
                        </div>
                        <!--<div style="width: 100%;height:1px;background-color:rgba(0,0,0,0.08);margin-top: 10px">-->

                        <!--</div>-->
                    </div>`
                    }

                }

            }
            });
    }

    /* 菜谱详细信息 */
    var material=document.querySelector('.material');
    postData(api+'sceipe/get_sceipeinfo',{"recipe_id": obj[item[0]]},null,function(res){
        if(res && res.status_code == '10011'){
            for(var r of res.list){
                material.innerHTML += `<li class="material_li">
                        <ul class="material_subul">
                            <li class="material_subli material_name" title="${r['ingredients']}" style="font-weight: bold;color:#333;background:#fff;">${r['ingredients']}</li>
                            <li class="material_subli" title="${r['amount']}" style="font-weight: 400;color:#666;background:#fff;">${r['amount']}</li>
                        </ul>
                    </li>`
            }
        }
    })

    /* 获取菜谱步骤 */
    var acticle=document.querySelector('.acticle');
    postData(api+'sceipe/get_sceipedetail',{"recipe_id": obj[item[0]]},null,function (res) {
        if(res && res.status_code == '10012'){
            console.log(res.list)
            acticle.innerText=res.list[0]['step'];
        }
    })

    /*   获取菜谱基本信息  */
    var picture=document.querySelector('.picture');
    var recipe_title=document.querySelector('.recipe_title');
    var dis=document.querySelector('.dis');
    postData(api+'sceipe/get_sceipedetailinfo',{"recipe_id": obj[item[0]]},null,function (res) {
        if(res && res.status_code == '10013'){
            console.log(res.list)
            picture.src=res.list[0]['src'];
            recipe_title.innerText=res.list[0]['rname'];
            // dis.innerText=res.list[0]['describes'];
        }
    })

})();