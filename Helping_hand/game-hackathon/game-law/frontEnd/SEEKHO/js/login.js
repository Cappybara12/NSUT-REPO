let phoneNumber = document.getElementById('form3Example3')
let otp = document.getElementById('form3Example4')
let passwordHolder = document.getElementById('passwordHolder')
let submitButton = document.getElementById('submitButton')
let userId = 0
let token= ""

function validatePhoneNumber(input_str) {
    let re = /^\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{4})$/;
  
    return re.test(input_str);
  }

let handleSignInClick=()=>{
    if(submitButton.value=='otp'){
        console.log("clicked")
        console.log(Number(phoneNumber.value))
        let data=JSON.stringify({"phone":Number(phoneNumber.value)})
        console.log(data)
        if(validatePhoneNumber(phoneNumber.value)){
            fetch('https://22a7-2401-4900-445e-6beb-40a8-b8d8-19e-d0a0.in.ngrok.io/aaoseekhein/v1/signin',{
                headers: {
                'Content-Type': 'application/json;charset=utf-8',
                'Accept': 'application/json;charset=utf-8'
                },
                body:data,
                method:'post',
            })
            .then(response=>response.json())
            .then(resData=>{
                passwordHolder.hidden = false
                submitButton.innerText='Sign-In'
                submitButton.value='Sign-In'
                console.log(resData) 
                userId = resData.userid
            })
            .catch((err)=>{
                console.log(err)
            })
        }
    }
    else{
        console.log("clicked")
        console.log(Number(otp.value))
        let data=JSON.stringify({"user":Number(userId),"otp":Number(otp.value)})
        console.log(data)
        fetch('https://22a7-2401-4900-445e-6beb-40a8-b8d8-19e-d0a0.in.ngrok.io/aaoseekhein/v1/gettoken',{
                headers: {
                'Content-Type': 'application/json;charset=utf-8',
                'Accept': 'application/json;charset=utf-8'
                },
                body:data,
                method:'post',
            })
            .then(response=>response.json())
            .then(data=>{
                console.log(data) 
                token = data.token
                window.location.href = "./index.html";
                localStorage.setItem("token",token)
                localStorage.setItem("userId",userId)

            })
            .catch((err)=>{
                console.log(err)
            })
        console.log(otp.value)
    }
}

console.log(userId,token)