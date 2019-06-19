/**
 * Created by 相如 on 2019/5/20.
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
                /* 获取个人信息 */
                var nicknames=document.querySelector('#user_nickname');
                var name=document.querySelector('#user_realname');
                var mail=document.querySelector('#user_mailbox');
                var rdman=document.querySelector('#rdman');
                var rdwoman=document.querySelector('#rdwoman');
                var age=document.querySelector('#use_age');
                var qq=document.querySelector('#use_qq');
                var sub=document.querySelector('#submit_all');

                postData(api+'user/userinfo',{"user_id":user_id},null,function(res){
                    if(res && res.status_code == '10004'){
                        console.log(res.id)
                        nicknames.value=res.id['nickname'];
                        name.value=res.id['name'];
                        mail.value=res.id['email'];
                        age.value=res.id['age'];
                        qq.value=res.id['qq'];
                        if(res.id['sex']=='男'){
                            rdman.checked=true;
                            rdwoman.checked=false
                        }else if(res.id['sex']=='女'){
                            rdwoman.checked=true;
                            rdman.checked=false
                        }else{
                            rdman.checked=false
                            rdwoman.checked=false
                        }
                    }
                })

                /*  修改个人信息 */
                var sex='';
                sub.onclick=function(){
                    if(nicknames.value){

                        if(rdman.checked){
                            sex='男'
                        }else if(rdwoman.checked){
                            sex='女'
                        }else{
                            sex=''
                        }
                        // if(name.value){
                        //
                        // }else{
                        //     name.value=''
                        // }
                        // if(mail.value){
                        //
                        // }else{
                        //     mail.value=''
                        // }
                        // if(qq.value){
                        //
                        // }else{
                        //     qq.value=''
                        // }
                        // if(age.value){
                        //
                        // }else{
                        //     age.value=''
                        // }
                        postData(api+'user/update_userinfo',{"nickname":nicknames.value,"name":name.value,"email":mail.value,"qq":qq.value,"sex":sex,"age":age.value,"user_id":user_id},null,function(res){
                            if(res && res.status_code == '10004'){
                                // alert(nicknames.value)
                                localStorage.setItem('nickname',nicknames.value);
                                nick_name.innerText=nicknames.value
                                alert('修改成功！');
                                // location.reload()
                            }else{

                            }


                        })
                    }else{
                        alert('用户昵称不能为空')
                    }
                }





            }else{
                login.style.display="block";
                register.style.display="block";
                s1.style.display="block";
                nick_name.style.display="none";
                alert('登录已失效');
            }
        });
    }else{
        alert('请登录~')
    }









})();