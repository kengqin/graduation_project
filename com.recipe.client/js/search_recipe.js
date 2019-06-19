/**
 * Created by 相如 on 2019/5/18.
 */
/**
 * Created by 相如 on 2019/5/16.
 */
(function(){

    var token =window.localStorage && window.localStorage.getItem('token');
    // 页面跳转
    window.sessionStorage.setItem('from', location.href);

    // var url = window.location.href;
    // var result = url.split("?")[1];
    // var keyValue = result.split("&");
    // var obj = {};
    // for (var i = 0; i < keyValue.length; i++) {
    //     var item = keyValue[i].split("=");
    //     obj[item[0]] = item[1];
    //     // sessionStorage.setItem("he", obj[item[0]])
    //
    // }
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

                // postData(api +'my_collection/select_counteron',{'user_id':user_id,"recipe_id":obj[item[0]]},null,function(res){
                //     if(res && res.status_code == '14000'){
                //         dianzan.style.color='orange';
                //     }else{
                //         dianzan.style.color='';
                //     }
                // })
                // postData(api +'my_collection/select_collegeon',{'user_id':user_id,"recipe_id":obj[item[0]]},null,function(res){
                //     if(res && res.status_code == '18000'){
                //         shoucang.style.color='orange';
                //     }else{
                //         shoucang.style.color='';
                //     }
                // })
            }else{
                login.style.display="block";
                register.style.display="block";
                s1.style.display="block";
                nick_name.style.display="none";

            }
        });
    }else{

    }


    /* 获取食谱列表 */
    var middle=document.querySelector('.middle_list');
    var a=[];
    getData(api+'sceipe/get_allinfo',null,null,function (res) {
        if(res && res.status_code == '10014'){
            console.log(res.list)
            a=res.list;
            for(var r of res.list.slice(0,5)){
                middle.innerHTML +=`<div class="middle" id="${r['id']}">
                <div class="recipe_img" >
                    <img src="${r['src']}" alt="" style="width:200px;height: 180px">
                </div>
                <div class="middle-right">
                    <h4>${r['describes']}</h4>
                    <div style="margin-top: 40px">
                        <span style="margin-right: 50px">${r['rname']}</span>
                        <span>作者:${r["nickname"]}</span>
                    </div>
                </div>
            </div>`
            }
            var middles=document.querySelectorAll('.middle');
            for (let a of middles) {
                // alert(2)
                a.onclick=function () {
                    // alert('ok')
                    location.href="sceipe_detail.html?sceipe_id="+this.id;
                }
            }

        }

        var add=document.querySelector('.add');
        var b=0;
        var num=5
        add.onclick=function () {
            b++;
            num=num+5;
           if(num < a.length){
               middle.innerHTML='';
               for(var r of a.slice(0,num)){
                   middle.innerHTML +=`<div class="middle" id="${r['id']}">
                <div class="recipe_img" >
                    <img src="${r['src']}" alt="" style="width:200px;height: 180px">
                </div>
                <div class="middle-right">
                    <h4>${r['describes']}</h4>
                    <div style="margin-top: 40px">
                        <span style="margin-right: 50px">${r['rname']}</span>
                        <span>作者:${r["nickname"]}</span>
                    </div>
                </div>
            </div>`
               }
               var middles=document.querySelectorAll('.middle');
               for (let a of middles) {
                   // alert(2)
                   a.onclick=function () {
                       // alert('ok')
                       location.href="sceipe_detail.html?sceipe_id="+this.id;
                   }
               }
           }else if((num-a.length)<=5 ){
               middle.innerHTML= '';
               add.innerText='没有更多了';
               for(var r of a.slice(0,num)){
                   middle.innerHTML +=`<div class="middle" id="${r['id']}">
                <div class="recipe_img" >
                    <img src="${r['src']}" alt="" style="width:200px;height: 180px">
                </div>
                <div class="middle-right">
                    <h4>${r['describes']}</h4>
                    <div style="margin-top: 40px">
                        <span style="margin-right: 50px">${r['rname']}</span>
                        <span>作者:${r["nickname"]}</span>
                    </div>
                </div>
            </div>`
               }
               var middles=document.querySelectorAll('.middle');
               for (let a of middles) {
                   // alert(2)
                   a.onclick=function () {
                       // alert('ok')
                       location.href="sceipe_detail.html?sceipe_id="+this.id;
                   }
               }
           }
        }
        var middles=document.querySelectorAll('.middle');
        for (let a of middles) {
            // alert(2)
            a.onclick=function () {
                // alert('ok')
                location.href="sceipe_detail.html?sceipe_id="+this.id;
            }
        }
    })

    var btn=document.querySelector('.btn');
    var text=document.querySelector('.text');
    btn.onclick=function(){
        // alert('a')
        // alert(text.value)
        if(text.value){
            postData(api+'sceipe/get_info_point',{"select":text.value},null,function(res){
                if(res && res.status_code== '10015'){
                    var add=document.querySelector('.add');
                    add.innerText=''
                    for(var r of res.list){
                        middle.innerHTML=  `<div class="middle" id="${r['id']}">
                <div class="recipe_img" >
                    <img src="${r['src']}" alt="" style="width:200px;height: 180px">
                </div>
                <div class="middle-right">
                    <h4>${r['describes']}</h4>
                    <div style="margin-top: 40px">
                        <span style="margin-right: 50px">${r['rname']}</span>
                        <span>作者:${r["nickname"]}</span>
                    </div>
                </div>
            </div>`
                    }
                    var middles=document.querySelectorAll('.middle');
                    for (let a of middles) {
                        // alert(2)
                        a.onclick=function () {
                            // alert('ok')
                            location.href="sceipe_detail.html?sceipe_id="+this.id;
                        }
                    }
                }else{
                    middle.innerHTML='';
                    var add=document.querySelector('.add');
                    add.innerText=''
                    alert('对不起未查询到结果~')
                    // location.reload()
                }

            })
        }else{
            alert('请输入食谱名')
        }


    }








})();