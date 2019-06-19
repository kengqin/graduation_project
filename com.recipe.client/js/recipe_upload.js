/**
 * Created by 相如 on 2019/5/21.
 */
/**
 * Created by 相如 on 2019/5/18.
 */
(function () {
    // 页面跳转
    window.sessionStorage.setItem('from', location.href);

    var token = window.localStorage && window.localStorage.getItem('token');
    var user_id = window.localStorage && window.localStorage.getItem('user_id');


    var nav_btn = document.querySelector("#nav_btn");
    var bs = document.querySelector("#bs-example-navbar-collapse-1");
    var ss = document.querySelectorAll(".ss");
    var outs = document.querySelector('.out');
    var gang = document.querySelector('.gang');
    bs.style.display = "none";
    nav_btn.onclick = function () {
        if (bs.style.display === "none") {
            bs.style.display = "block";
        } else {
            bs.style.display = "none";
        }
        for (var s of ss) {
            s.style.display = "none";
        }
    };
    // 退出
    outs.onclick = function () {
        localStorage.clear();
        nick_name.style.display = "none";
        out.style.display = 'none';
        login.style.display = "block";
        register.style.display = "block";
        s1.style.display = "block";
        location.href = '../index.html'
    };
    // 登录注册
    var login = document.querySelector(".login");
    var register = document.querySelector(".register");
    var s1 = document.querySelector(".s1");
    var nick_name = document.querySelector(".nick_name");
    var out = document.querySelector('.out');
    nick_name.style.display = "none";
    out.style.display = 'none';

    var nickname = window.localStorage && window.localStorage.getItem('nickname');

    if (token) {
        getData("http://47.102.45.80:8080/api/user/checkToken/", null, {"token": token}, function (res) {
            if (res && res["status_code"] === "10003") {
                login.style.display = "none";
                register.style.display = "none";
                s1.style.display = "none";
                nick_name.style.display = "block";
                nick_name.innerText = nickname;
                out.style.display = "block";
                out.innerText = '退出登录';
                nick_name.onclick = function () {
                    token = window.localStorage && window.localStorage.getItem('token');
                    if (token) {
                        getData("http://47.102.45.80:8080/api/user/checkToken/", null, {"token": token}, function (res) {
                            if (res && res["status_code"] === "10003") {
                                location.href = "person_center.html?user_id=" + user_id
                            } else {
                                location.href = "login.html"
                            }
                        })
                    } else {
                        location.href = "login.html"
                    }
                }
                /* 删除用料 */
                // var delet=document.querySelector('.delete');
                var recipe = document.querySelector('.recipe');
                var add = document.querySelector('.add');
                // var detail=document.querySelector('.detail');
                let a = 1;
                var b;
                // b=document.querySelectorAll('.delete');
                add.onclick = function () {
                    // alert('ok')
                    a++;
                    // recipe.innerHTML +=` <div class="detail" id="${a}">
                    //         <input type="text" placeholder="请填写主料" style="background-color:#fff5d7;width:180px;height: 40px;padding: 10px;border: solid 1px rgba(0, 0, 0, 0.2)">
                    //         <input type="text" placeholder="请填写用量" style="background-color:#fff5d7;width:120px;height: 40px;padding: 10px;border: solid 1px rgba(0, 0, 0, 0.2)">
                    //         <span class="delete">×</span>
                    //     </div>`

                    var d = document.createElement('div');
                    d.style.paddingBottom = '5px';
                    d.className = 'detail'
                    d.id = a;
                    recipe.appendChild(d)
                    var e = document.createElement('input');
                    e.style.backgroundColor = '#fff5d7';
                    e.style.width = '180px';
                    e.style.height = '40px';
                    e.style.padding = '10px';
                    e.style.marginRight = '5px';
                    e.placeholder = '请填写主料'
                    e.style.border = 'solid 1px rgba(0, 0, 0, 0.2)';
                    d.appendChild(e)
                    var f = document.createElement('input');
                    f.style.backgroundColor = '#fff5d7';
                    f.style.width = '120px';
                    f.style.height = '40px';
                    f.style.padding = '10px';
                    f.placeholder = '请填写用量';
                    f.style.border = 'solid 1px rgba(0, 0, 0, 0.2)';
                    d.appendChild(f)
                    var g = document.createElement('span');
                    g.style.width = "20px";
                    g.style.height = '20px';
                    g.style.fontSize = '1.5em';
                    g.style.borderRadius = '80%';
                    g.style.backgroundColor = 'rgba(229,229,229,0.45)';
                    g.style.color = '#bababa';
                    g.style.cursor = 'pointer';
                    g.className = 'delete'
                    g.innerText = '×'
                    d.appendChild(g)
                    b = document.querySelectorAll('.delete');
                    console.log(b)
                    for (let c of b) {  //删除用料
                        c.onclick = function () {
                            // alert(c.parentNode.id)
                            document.getElementById(c.parentNode.id).parentNode.removeChild(document.getElementById(c.parentNode.id))
                        }
                    }
                };
                /* 删除 */
                // console.log(b)
                var details = document.querySelector('.delete');

                details.onclick = function () {
                    // alert(details.parentNode.id)
                }
                // var delet=document.querySelectorAll('.delete');

                /* 上传图片 */
                // console.log(res.key)
                // var img_recipe=document.querySelector('.img_recipe');
                // img_recipe.onchange=function (event) {
                //     var imgFile = event.target.files[0];
                //     postData(api+'user/upload',{"iconname":imgFile.name},null,function (res) {
                //         let file=res.filename; //返回的新文件名和token
                //         let domain=res.domain;
                //         let token = res.qiniu_token;
                //         let config = {
                //             useCdnDomain: false,
                //             disableStatisticsReport: true,
                //             retryCount: 6,
                //             region: qiniu.region.z0   //此处表示服务器所在的区域
                //         };
                //         let putExtra = {
                //             fname: "",
                //             params: {},
                //             mimeType: ["image/png", "image/jpeg", "image/gif", "image/jpg"]
                //         };
                //         // 添加上传dom面板
                //         putExtra.params["x:name"] = file.split(".")[0];
                //         let subscription;
                //         // 调用sdk上传接口获得相应的observable，控制上传和暂停
                //         let observable = qiniu.upload(imgFile, file, token, putExtra);
                //         subscription = observable.subscribe({
                //             next(res){
                //                 // ...
                //             },
                //             error(err){
                //                 alert('图片上传失败,错误信息:'+err)
                //             },
                //             complete(res){
                //                 window.sessionStorage.setItem('img',res.key)
                //                 console.log(res.key)
                //             }
                //         });
                //     })
                // }
                // function upImg(obj){
                //     var imgFile = obj.files[0];
                //     postData(api+'user/upload',{"iconname":imgFile.name},null,function (res) {
                //         let file=res.filename; //返回的新文件名和token
                //         let domain=res.domain;
                //         let token = res.qiniu_token;
                //
                //         let config = {
                //             useCdnDomain: false,
                //             disableStatisticsReport: true,
                //             retryCount: 6,
                //             region: qiniu.region.z0   //此处表示服务器所在的区域
                //         };
                //         let putExtra = {
                //             fname: "",
                //             params: {},
                //             mimeType: ["image/png", "image/jpeg", "image/gif", "image/jpg"]
                //         };
                //         // 添加上传dom面板
                //         putExtra.params["x:name"] = file.split(".")[0];
                //         let subscription;
                //         // 调用sdk上传接口获得相应的observable，控制上传和暂停
                //         let observable = qiniu.upload(imgFile, file, token, putExtra);
                //         subscription = observable.subscribe({
                //             next(res){
                //                 // ...
                //             },
                //             error(err){
                //                 alert('图片上传失败,错误信息:'+err)
                //             },
                //             complete(res){
                //                 window.sessionStorage.setItem('img',res.key)
                //             }
                //         });
                //     })
                //
                // }
                /* 提交 */
                var sub = document.querySelector('.sub');
                var listItem = [];
                var list = {'ingredients': '', 'amount': ''};
                // var proto = 0;
                var imgs=img
                sub.onclick = function () {
                    /* 获取食谱标题 */
                    var title=document.querySelector('.recipe_name');
                    console.log(title.value);

                    /* 获取食谱的自媒体标题 */
                    var describe=document.querySelector('.describe_recipe');
                    console.log(describe.value)

                    /* 获取操作步骤 */
                    var step=document.querySelector('.decrible');
                    console.log(step.value)
                    console.log(img)
                    /* 获取食料值 */
                    listItem = [];
                    var detail = document.querySelectorAll('.detail');
                    console.log(detail)
                    if(detail[0]){
                        for (var i of detail) {
                            // console.log(i)
                            // proto++;
                            if(i.children[0].value && i.children[1].value){
                                list['ingredients'] = i.children[0].value;
                                list['amount'] = i.children[1].value;
                                listItem.push(list)
                            }else{
                                alert('需要要上传的食材不能有空');
                                return false

                            }

                            list = {'ingredients': '', 'amount': ''}
                            // console.log(listItem)
                            // console.log(list[proto])
                        }
                    }else{
                        alert('食材不能为空')
                        return false
                    }

                    console.log(listItem)  // 食料值




                    /* 上传图片 */
                    // console.log(window.sessionStorage.getItem('img'));



                    /* 上传食谱 */
                    if( title.value && describe.value && listItem[0] && step.value && img){
                        // var recipe_id='';
                        postData(api+'user/insert_recipeinfo',{"rname":title.value,"describes":describe.value,"step":step.value,"listItem":listItem,"src":img,"user_id":user_id},null,function (res) {
                            if(res && res.status_code=='10004'){
                                // console.log(res.result)
                                // recipe_id=res.result
                                alert('上传成功！！');
                                location.reload()
                            }else{
                                alert(res.status_text)
                            }
                        })


                    }else if(!title.value) {
                        alert('请填写食谱标题')
                    }else if(!img){
                        alert('请上传食谱图片')
                    }else if(!describe.value){
                        alert('请填写自媒体标题')
                    }else if(!listItem){
                        alert('请填写食材')
                    }else if(!step.value){
                        alert('请填写具体步骤')
                    }else{
                        alert('请填写未完成的部分')
                    }

                }

            } else {
                login.style.display = "block";
                register.style.display = "block";
                s1.style.display = "block";
                nick_name.style.display = "none";
                alert('登录已失效');
            }
        });
    } else {
        alert('请登录~')
    }

})();
