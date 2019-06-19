/**
 * Created by 相如 on 2019/5/18.
 */
/**
 * Created by 相如 on 2019/5/18.
 */
(function(){
    // 页面跳转
    window.sessionStorage.setItem('from', location.href);

    var token=window.localStorage && window.localStorage.getItem('token');
    var user_id=window.localStorage && window.localStorage.getItem('user_id');


    var nav_btn=document.querySelector("#nav_btn");
    var bs=document.querySelector("#bs-example-navbar-collapse-1");
    var ss=document.querySelectorAll(".ss");
    var outs= document.querySelector('.out');
    var gang=document.querySelector('.gang');
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
        location.href='../index.html'
    };
    // 登录注册
    var login=document.querySelector(".login");
    var register=document.querySelector(".register");
    var s1 =document.querySelector(".s1");
    var nick_name=document.querySelector(".nick_name");
    var out =document.querySelector('.out');
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
                                location.href="login.html"
                            }
                        })
                    }else{
                        location.href="login.html"
                    }
                }

                /* 获取收藏记录 */

                /* 获取点赞列表 */
                var lists=document.querySelector('.b-middle');
                var a=[];
                // console.log(user_id)
                postData(api+'sceipe/get_selfcollege',{"user_id":user_id},null,function(res){
                    console.log(res.list)
                    if(res && res.status_code == '10017'){
                        // console.log(res.list)
                        a=res.list;
                        if(a.length<=5){
                            var add =document.querySelector('.add');
                            add.innerText='';
                        }
                        // console.log(a);
                        for(var r of res.list.slice(0,5)){
                            lists.innerHTML +=`<div class="b-middles" id="${r['recipe_id']}">
                    <div style="width: 200px;height: 150px">
                        <img src="${r['src']}" alt="" style="width:150px;height:150px;">
                    </div>
                    <div class="middle-rights">
                        <!--<h4>这道菜真的好吃</h4>-->
                        <div style="margin-top: 40px">
                            <!--<h4>${r['describe']}</h4>-->
                            <div style="margin-top: 20px">
                                <span style="margin-right: 50px">菜谱:${r['rname']}</span>
                                <span>作者:${r["nickname"]}</span>
                            </div>
                        </div>
                    </div>
                    <div class="btns">
                        删除收藏
                    </div>
                </div>`

                        }

                        var middles=document.querySelectorAll('.b-middles');
                        var btns=document.querySelectorAll('.btns')
                        for (let a of middles) {
                            // alert(2)
                            a.onclick=function () {
                                location.href="sceipe_detail.html?sceipe_id="+this.id;
                            }

                        }
                        for(let b of btns){
                            b.onclick=function () {
                                var b1=b.parentNode.id;
                                postData(api+'my_collection/delete_collegeon',{"user_id": user_id,"recipe_id":b1},null,function(res){
                                    if(res && res.status_code=='16000'){
                                        alert(res.status_text);
                                        location.reload()
                                    }else{

                                    }
                                })
                                event.stopPropagation();
                            }
                        }

                    }else{
                        var add =document.querySelector('.add');
                        add.innerText='没有数据哦'
                    }


                });
                var add =document.querySelector('.add');
                var num=5;
                add.onclick=function(){
                    num=num+5;
                    lists.innerHTML='';
                    if(num<a.length){

                        for(var r of a.slice(0,num)){
                            lists.innerHTML+=`<div class="b-middles" id="${r['recipe_id']}">
                    <div style="width: 200px;height: 150px">
                        <img src="${r['src']}" alt="" style="width:150px;height:150px;">
                    </div>
                    <div class="middle-rights">
                        <!--<h4>这道菜真的好吃</h4>-->
                        <div style="margin-top: 40px">
                            <!--<h4>${r['describe']}</h4>-->
                            <div style="margin-top: 20px">
                                <span style="margin-right: 50px">菜谱:${r['rname']}</span>
                                <span>作者:${r["nickname"]}</span>
                            </div>
                        </div>
                    </div>
                    <div class="btns">
                        删除收藏
                    </div>
                </div>`
                        }
                        var middles=document.querySelectorAll('.b-middles');
                        var btns=document.querySelectorAll('.btns')
                        for (let a of middles) {
                            // alert(2)
                            a.onclick=function () {
                                location.href="sceipe_detail.html?sceipe_id="+this.id;
                            }

                        }
                        for(let b of btns){
                            b.onclick=function () {
                                var b1=b.parentNode.id;
                                postData(api+'my_collection/delete_collegeon',{"user_id": user_id,"recipe_id":b1},null,function(res){
                                    if(res && res.status_code=='16000'){
                                        alert(res.status_text);
                                        location.reload()
                                    }else{

                                    }
                                })
                                event.stopPropagation();
                            }
                        }

                    }else if((num-a.length)<=5){
                        lists.innerHTML='';
                        add.innerText='没有更多了'
                        for(var r of a.slice(0,num)){
                            lists.innerHTML+=`<div class="b-middles" id="${r['recipe_id']}">
                    <div style="width: 200px;height: 150px">
                        <img src="${r['src']}" alt="" style="width:150px;height:150px;">
                    </div>
                    <div class="middle-rights">
                        <!--<h4>这道菜真的好吃</h4>-->
                        <div style="margin-top: 40px">
                            <!--<h4>${r['describe']}</h4>-->
                            <div style="margin-top: 20px">
                                <span style="margin-right: 50px">菜谱:${r['rname']}</span>
                                <span>作者:${r["nickname"]}</span>
                            </div>
                        </div>
                    </div>
                    <div class="btns">
                        删除收藏
                    </div>
                </div>`
                        }

                        var middles=document.querySelectorAll('.b-middles');
                        var btns=document.querySelectorAll('.btns')
                        for (let a of middles) {
                            // alert(2)
                            a.onclick=function () {
                                location.href="sceipe_detail.html?sceipe_id="+this.id;
                            }

                        }
                        for(let b of btns){
                            b.onclick=function () {
                                var b1=b.parentNode.id;
                                postData(api+'my_collection/delete_collegeon',{"user_id": user_id,"recipe_id":b1},null,function(res){
                                    if(res && res.status_code=='16000'){
                                        alert(res.status_text);
                                        location.reload()
                                    }else{

                                    }
                                })
                                event.stopPropagation();
                            }
                        }
                    }


                }
                var middles=document.querySelectorAll('.b-middles');
                var btns=document.querySelectorAll('.btns')
                for (let a of middles) {
                    // alert(2)
                    a.onclick=function () {
                        location.href="sceipe_detail.html?sceipe_id="+this.id;
                    }

                }
                for(let b of btns){
                    b.onclick=function () {
                        var b1=b.parentNode.id;
                        postData(api+'my_collection/delete_collegeon',{"user_id": user_id,"recipe_id":b1},null,function(res){
                            if(res && res.status_code=='16000'){
                                alert(res.status_text);
                                location.reload()
                            }else{

                            }
                        })
                        event.stopPropagation();
                    }
                }


            }else{
                login.style.display="block";
                register.style.display="block";
                s1.style.display="block";
                nick_name.style.display="none";
            }
        });
    }










})();