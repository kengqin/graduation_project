/**
 * Created by 相如 on 2019/5/22.
 */

// 导航
(function () {




    // 页面跳转
    window.sessionStorage.setItem('from', location.href);

    var token=window.localStorage && window.localStorage.getItem('token');
    var user_id=window.localStorage && window.localStorage.getItem('user_id');

    var url = window.location.href;
    var result = url.split("?")[1];
    var keyValue = result.split("&");
    var obj = {};
    for (var i = 0; i < keyValue.length; i++) {
        var item = keyValue[i].split("=");
        obj[item[0]] = item[1];
        // sessionStorage.setItem("he", obj[item[0]])

    }
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

    // if (token) {
    //     getData("http://47.102.45.80:8080/api/user/checkToken/", null,{"token": token}, function (res) {
    //         if (res && res["status_code"] === "10003") {
    //             // login.style.display="none";
    //             // register.style.display="none";
    //             // s1.style.display="none";
    //             // nick_name.style.display="block";
    //             // nick_name.innerText=nickname;
    //             // out.style.display="block";
    //             // out.innerText='退出登录';
    //             // nick_name.onclick=function () {
    //             //     token=window.localStorage && window.localStorage.getItem('token');
    //             //     if(token){
    //             //         getData("http://47.102.45.80:8080/api/user/checkToken/", null,{"token": token}, function (res) {
    //             //             if (res && res["status_code"] === "10003") {
    //             //                 location.href = "./pages/person_center.html?user_id=" + user_id
    //             //             }else{
    //             //                 location.href="./pages/login.html"
    //             //             }
    //             //         })
    //             //     }else{
    //             //         location.href="./pages/login.html"
    //             //     }
    //             // }
    //         }else{
    //             // login.style.display="block";
    //             // register.style.display="block";
    //
    //             // out.style.display="block";
    //             // out.innerText='退出登录';
    //             // nick_name.style.display="block";
    //         }
    //     });
    // }

    var oWidth = parseFloat(document.body.clientWidth);
    window.onresize = ()=>{
        oWidth = parseFloat(document.body.clientWidth);
        if (document.body.clientWidth>=768){
            for (var s of ss){
                s.style.display="block";
            }
        }
    };



    var nickname=document.querySelector('.nickname');
    var name=document.querySelector('.name');
    var telephones=document.querySelector('.telephones')
    var doman=document.querySelector('#rdman')
    var woman=document.querySelector('#rdwoman');

    // var b={"nickname":nickname.value,"name":name.value,"telephone":telephone.value,"sex":sex.value,"user_id":obj[item[0]]}


    /*  修改用户信息  */
    postData(api+'user/selet_info',{"user_id":obj[item[0]] },null,function(res){
        if(res && res.status_code == '10004'){
            // alert(nicknames.value)
            // localStorage.setItem('nickname',nicknames.value);
            // nick_name.innerText=nicknames.value
            nickname.value=res.list['nickname'];
            name.value=res.list['name'];
            console.log(res.list['telephone'])
            telephones.value=res.list['telephone']
            if(res.list['sex']=='男'){
                doman.checked=true;
                woman.checked=false;
            }else if(res.list['sex']=='女'){
                doman.checked=false;
                woman.checked=true;

            }else{
                doman.checked=false
                woman.checked=false
            }
            // alert('修改成功！');
            // location.reload()
        }else{

        }


    })
    var subs=document.querySelector('.sub');
    var sex='';
    subs.onclick=function(){
        if(nickname.value && telephones.value ){
            if(rdman.checked){
                sex='男'
            }else if(rdwoman.checked){
                sex='女'
            }else{
                sex=''
            }
            postData(api+'user/updates',{'name':name.value,'nickname':nickname.value,'telephone':telephones.value,'sex':sex,'user_id':obj[item[0]]},null,function (res) {
                if(res && res.status_code ==='10004'){
                    alert(res.status_text)
                }
            })
        }
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

