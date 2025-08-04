import { isNotEmpty } from "./validator.js";


//    <div class="mb-3">
//       <label for="inputID" class="form-label">ID</label>
//       <input type="text" class="form-control" id="inputID" placeholder="아이디 입력">
//     </div>
//     <div class="mb-3">
//       <label for="inputPassword" class="form-label">Password</label>
//       <input type="password" class="form-control" id="inputPassword" placeholder="비밀번호 입력">
//     </div>
//     <div class="btn-group-custom">
//       <button type="submit" class="btn btn-primary w-50">로그인</button> 아이디 버튼
//       <button type="button" class="btn btn-secondary w-50">회원가입</button>

const button = document.getElementById("button");
button.addEventListener("click", () =>{
    const id = document.getElementById("inputID");
    const pwd = document.getElementById("inputPassword");
    
    console.log(id.value, pwd.value)
    if (isNotEmpty(id.value, "id") && isNotEmpty(pwd.value, "pwd")){
        window.location.href = "https://www.google.com"; 
    }

})

//함수 import받기