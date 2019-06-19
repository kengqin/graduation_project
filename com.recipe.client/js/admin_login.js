/**
 * Created by 相如 on 2019/5/15.
 */

(function () {

    var tel=document.querySelector('#txt_telephone');
    var tel_error=document.querySelector('#tel_error');
    var password=document.querySelector('#txt_password');
    var password_error=document.querySelector('#password_error');
    var login_btn=document.querySelector('#btn_login')

    //查看密码
    // document.querySelector('#eye-check').onclick=function() {
    //     if (password.type=='password') {
    //         password.type='text';
    //     }else {
    //         password.type='password'
    //     }
    // };


    //登录ajax
    login_btn.onclick=function () {
        if(checkPassword() && checkTelphone()){
            //    开始提交后台
            var user={"telephone":tel.value,"password":password.value};
            postData(api+'user/admin_login',user,null,function (res) {
                if(res && res.status_code=='10003'){
                    // localStorage.setItem('token',res.token);
                    localStorage.setItem('admin_id',res.id);
                    localStorage.setItem('admin_telephone',res.telephone);
                    localStorage.setItem('admin_role',res.role);
                    // localStorage.setItem('nickname',res.nickname);

                    // if(sessionStorage.getItem('from')){
                    //     location.href=sessionStorage.getItem('from');
                    // }else {
                        location.href='admin_index.html';
                    // }

                }else if(res && res.status_code=='10004'){
                    tel_error.innerText=res.status_text;

                }else if(res && res.status_code=='10005') {
                    password_error.innerText=res.status_text;
                }else {
                    console.log(res.status_text)
                }
            })
        }
    };


    //检查手机号
    function checkTelphone() {
        var regMobile=/^[A-Za-z0-9]{5,}$/;
        if(tel.value){
           if(regMobile.test(tel.value)){
               tel_error.innerText='';
               return true
           }else{
               tel_error.innerText='管理员账号必须大于五位'
               return false;
           }
            return true
        }else {
            tel_error.innerText='管理员账号不能为空';
            return false;
        }
    }


    //检查密码
    function checkPassword() {
        var regMobile=/^\w{5,}$/;
        if(password.value){
            if(regMobile.test(password.value)){
                password_error.innerText='';
                return true;
            }else {
                password_error.innerText='*密码必须大于六位';
                return false;
            }
            return true
        }else {
            password_error.innerText='密码不能为空';
            return false;
        }
    }

    //自动检查手机号
    tel.onchange=function () {
        // telephone_error=''
        checkTelphone();
    };

    //自动检查密码
    password.onchange=function () {
        checkPassword();

    };

})();




