/**
 * Created by 相如 on 2019/5/22.
 */
/**
 *Created by Lenovo-HXL on 2019/1/17.
 */
// 导航
(function () {




    // 页面跳转
    window.sessionStorage.setItem('from', location.href);

    var token=window.localStorage && window.localStorage.getItem('token');
    var user_id=window.localStorage && window.localStorage.getItem('user_id');


    var nav_btn=document.querySelector("#nav_btn");
    var bs=document.querySelector("#bs-example-navbar-collapse-1");
    var ss=document.querySelectorAll(".ss");
    var outs= document.querySelector('#out');
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
        // nick_name.style.display="none";
        // out.style.display='none';
        // login.style.display="block";
        // register.style.display="block";
        // s1.style.display="block";
        location.href='../index.html'
    };
    // 登录注册
    // var login=document.querySelector(".login");
    // var register=document.querySelector(".register");
    // var s1 =document.querySelector(".s1");
    // var nick_name=document.querySelector(".nick_name");
    // var out =document.querySelector('.out');
    //     nick_name.style.display="none";
    //     out.style.display='none';
    //
    // var nickname=window.localStorage && window.localStorage.getItem('nickname');

    if (token) {
        getData("http://47.102.45.80:8080/api/user/checkToken/", null,{"token": token}, function (res) {
            if (res && res["status_code"] === "10003") {
                // login.style.display="none";
                // register.style.display="none";
                // s1.style.display="none";
                // nick_name.style.display="block";
                // nick_name.innerText=nickname;
                // out.style.display="block";
                // out.innerText='退出登录';
                // nick_name.onclick=function () {
                //     token=window.localStorage && window.localStorage.getItem('token');
                //     if(token){
                //         getData("http://47.102.45.80:8080/api/user/checkToken/", null,{"token": token}, function (res) {
                //             if (res && res["status_code"] === "10003") {
                //                 location.href = "./pages/person_center.html?user_id=" + user_id
                //             }else{
                //                 location.href="./pages/login.html"
                //             }
                //         })
                //     }else{
                //         location.href="./pages/login.html"
                //     }
                // }
            }else{
                // login.style.display="block";
                // register.style.display="block";

                // out.style.display="block";
                // out.innerText='退出登录';
                // nick_name.style.display="block";
            }
        });
    }

    var oWidth = parseFloat(document.body.clientWidth);
    window.onresize = ()=>{
        oWidth = parseFloat(document.body.clientWidth);
        if (document.body.clientWidth>=768){
            for (var s of ss){
                s.style.display="block";
            }
        }
    };




    // // 公司
    // var company_main=document.querySelector(".company_main");
    // getData(api+'sceipe/sceipe_first',null,null,function (res) {
    //     if(res && res['status_code']==='10008'){
    //         console.log(res['sceipe_first'])
    //         for(let r of res['sceipe_first']){
    //             // postData(api+'sceipe/sceipe_first_name',{'id':r['user_id']},null,function (res) {
    //             // if(res && res['status_code']==='10009'){
    //             //    r.name= res.name;
    //             // console.log(r)
    //             company_main.innerHTML+=`<div class="col-xs-12 col-sm-6 col-md-3 my_company" id="${r['id']}">
    //                 <div class="content">
    //                     <div class="company_image">
    //                         <img src="${r['src']}" alt="">
    //                     </div>
    //                     <!--<div class="company_logo">-->
    //                     <!--<img src="" alt="">-->
    //                     <!--</div>-->
    //                     <div class="company_name">
    //                         <span title="${r['name']}">${r["rname"]}</span>
    //                     </div>
    //                     <!--<div class="author">-->
    //                         <!--<span>hello</span>-->
    //                         <!--<span style="margin-right: 20px">收藏</span>-->
    //                     <!--</div>-->
    //                     <div class="zuozhe">
    //                        <div class="lefts">作者:${r.nickname}</div>
    //                        <!--<div class="rights">0人收藏</div>-->
    //                     </div>
    //                 </div>
    //             </div>`
    //             // }
    //             // })
    //             // var a=document.querySelectorAll(".my_company");
    //             // a.onclick=function () {
    //             //     // alert('ok')
    //             //     location.href="./pages/sceipe_detail.html?sceipe_id="+this.id;
    //             // }
    //         }
    //
    //         var my_companys=document.querySelectorAll(".my_company");
    //         console.log(my_companys)
    //         for (let a of my_companys) {
    //             // alert(2)
    //             a.onclick=function () {
    //                 // alert('ok')
    //                 location.href="./pages/sceipe_detail.html?sceipe_id="+this.id;
    //             }
    //         }
    //     }
    //
    // });
    // var company_main1=document.querySelector(".company_main1");
    // getData(api+'sceipe/sceipe_first_1',null,null,function (res) {
    //     if(res && res['status_code']==='10008'){
    //         for(let r of res['sceipe_first']){
    //             // postData(api+'sceipe/sceipe_first_name',{'id':r['user_id']},null,function (res) {
    //             // if(res && res['status_code']==='10009'){
    //             //    r.name= res.name;
    //             // console.log(r)
    //             company_main1.innerHTML+=`<div class="col-xs-12 col-sm-6 col-md-3 my_sceipe" id="${r["id"]}">
    //             <div class="content">
    //                 <div class="company_image">
    //                     <img src="${r['src']}" alt="">
    //                 </div>
    //                 <!--<div class="company_logo">-->
    //                 <!--<img src="" alt="">-->
    //                 <!--</div>-->
    //                 <div class="company_name">
    //                     <span title="${r['name']}">${r["rname"]}</span>
    //                 </div>
    //                 <!--<div class="author">-->
    //                 <!--<span>hello</span>-->
    //                 <!--<span style="margin-right: 20px">收藏</span>-->
    //                 <!--</div>-->
    //                 <div class="zuozhe">
    //                     <div class="lefts">作者:${r.nickname}</div>
    //                     <!--<div class="rights">0人收藏</div>-->
    //                 </div>
    //             </div>`
    //             // }
    //             // })
    //             // var a=document.querySelectorAll(".my_company");
    //             // a.onclick=function () {
    //             //     // alert('ok')
    //             //     location.href="./pages/sceipe_detail.html?sceipe_id="+this.id;
    //             // }
    //         }
    //
    //         var my_companys=document.querySelectorAll(".my_sceipe");
    //         console.log(my_companys)
    //         for (let a of my_companys) {
    //             // alert(2)
    //             a.onclick=function () {
    //                 // alert('ok')
    //                 location.href="./pages/sceipe_detail.html?sceipe_id="+this.id;
    //             }
    //         }
    //     }
    //
    // });


    //
    // // 日记
    // var user_icon02=document.querySelector(".user_icon02");
    // getData('http://47.102.45.80:8080/api/diary/diaryUserIcon/',null,null,function (res){
    //     if(res && res['status_code']==='10009'){
    //         for(let r of res['content']){
    //             user_icon02.innerHTML+=`<div class="col-xs-12 user_item" id="${r["id"]}">
    //                         <img src="${r["icon"]}" alt="">
    //                     </div>`
    //         }
    //
    //
    //         var user_items=document.querySelectorAll(".user_item");
    //         var first_diary_id=user_items[0].id;
    //         function getDiaryData(args) {
    //             getData("http://47.102.45.80:8080/api/diary/diaryItem/",{"diary_id":args},null,function (res) {
    //                 if (res && res['status_code']==='10009') {
    //                     var diary_text = document.querySelector(".diary_text");
    //                     var diary_title = document.querySelector(".diary_title span");
    //                     document.querySelector(".user_icon01 img").src=res["content"]["icon"];
    //                     diary_title.innerText=res["content"]["diary_title"];
    //                     document.querySelector(".style").innerText=res["content"]["style_name"];
    //                     document.querySelector(".diary_company_name").innerText=res["content"]["company"];
    //                     diary_text.innerText=res["content"]["diary_content"];
    //                     var imgs="";
    //                     for (var img of res["content"]["diary_img"]){
    //                         imgs +=`<img src="${img}">`
    //                     }
    //                     document.querySelector(".diary_image").innerHTML = imgs;
    //
    //                     // 字数限制
    //                     if (diary_text.innerText.length > 60) {
    //                         diary_text.innerText = diary_text.innerText.substring(0, 60) + "..."
    //                     }
    //                     if (diary_title.innerText.length > 15) {
    //                         diary_title.innerText = diary_title.innerText.substring(0, 15) + "..."
    //                     }
    //                 }else {
    //                     console.log(res["status_text"])
    //                 }
    //
    //             })
    //         }
    //         getDiaryData(first_diary_id);
    //         for (var user_item of user_items){
    //             user_item.onclick=function () {
    //                 var diary_id=this.id;
    //                 getDiaryData(diary_id)
    //             }
    //         }
    //     }else if(res['status_code']==='10008') {
    //         console.log(res["status_text"])
    //     }
    // });

    // var more_diary=document.querySelector(".more_diary a");
    //     // more_diary.onclick=function () {
    //     //     location.href="./pages/strategy_list.html?more_diary=true"
    //     // };
    //
    // // 攻略
    // var strategy_content_text=document.querySelector(".strategy_content_text");
    // var diary_content_text=document.querySelector(".diary_content_text");
    //
    // getData('http://47.102.45.80:8080/api/strategy/strategyTitle/',null,null,function (res) {
    //     if(res && res['status_code']==='10009'){
    //         for (var r of res["content"]){
    //             strategy_content_text.innerHTML+=`<a href="###" class="strategy_txt" id="${r["strategy_id"]}">${r["strategy_title"]}</a>`
    //         }
    //         var strategy_txts=document.querySelectorAll(".strategy_txt");
    //         for (var strategy_txt of strategy_txts){
    //             strategy_txt.onclick=function () {
    //                 location.href="./pages/strategy_info.html?strategy_id="+this.id;
    //             }
    //         }
    //         xzzs();
    //     }else{
    //         console.log(res["status_text"])
    //     }
    // });

    // getData('http://47.102.45.80:8080/api/diary/diaryTitle/',null,null,function (res) {
    //     if(res && res['status_code']==='10009'){
    //         for (var r of res["content"]){
    //             diary_content_text.innerHTML+=`<a href="#" class="diary_txt" id="${r["diary_id"]}">${r["diary_title"]}</a>`
    //         }
    //         var diary_txts=document.querySelectorAll(".diary_txt");
    //         for (var diary_txt of diary_txts){
    //             diary_txt.onclick=function () {
    //                 location.href="./pages/diary_info.html?diary_id="+this.id;
    //             }
    //         }
    //         xzzs();
    //     }else{
    //         console.log(res["status_text"])
    //     }
    // });

    /* 获取用户信息 */
    var lists=document.querySelector('.tab');
    getData(api+'user/select_alluser',null,null,function (res) {
        if(res && res.status_code=='10004'){
           for(var r of res.list.slice(0,9)){
               lists.innerHTML+=`<div class="lists">
                            <tr class="t" id="${r['id']}">
                            <td>${r['id']}</td>
                            <td>${r['name']}</td>
                            <td>${r['nickname']}</td>
                            <td>${r['telephone']}</td>
                            <td>${r['sex']}</td>
                            <td class="delete" style="cursor:pointer">修改</td>
                        </tr>

                        </div>`
           }
           var dele=document.querySelectorAll('.delete');
           // console.log(dele)
           for(let a of dele){
               // console.log(a)
               a.onclick=function () {
                   location.href='../pages/update_info.html?user_id='+a.parentNode.id

               }
           }
        }
    })
    var nick=document.querySelector('.nick');
    var searchs=document.querySelector('.searchs');
    searchs.onclick=function () {
        // console.log(nick.value)
        postData(api+'user/select_userinfo',{'user_id':nick.value},null,function (res) {
            if(res && res.status_code=='10004'){
                console.log(res.list)
                lists.innerHTML='';
                for(var r of res.list){
                    lists.innerHTML+=`<div class="lists">
                            <tr class="t" id="${r['id']}">
                            <td>${r['id']}</td>
                            <td>${r['name']}</td>
                            <td>${r['nickname']}</td>
                            <td>${r['telephone']}</td>
                            <td>${r['sex']}</td>
                            <td class="delete" style="cursor:pointer">修改</td>
                        </tr>

                        </div>`
                }
                var dele=document.querySelectorAll('.delete');
                console.log(dele)
                for(let a of dele){
                    console.log(a)
                    a.onclick=function () {
                        location.href='../pages/update_info.html?user_id='+a.parentNode.id;
                    }
                }
            }
        })
    }

    // 限制字数
    function xzzs() {
        //字数限制{
        var content_text=document.querySelectorAll(".content_text a");
        for (var a of content_text) {
            if (a.innerText.length > 13){
                a.innerText = a.innerText.substring(0, 13) + "..."
            }
        }
    }
    xzzs();

})();
