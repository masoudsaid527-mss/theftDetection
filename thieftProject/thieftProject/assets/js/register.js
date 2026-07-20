// =====================================
// GET ELEMENTS
// =====================================


const registerForm = document.getElementById("registerForm");
// Submit button: rely on the form's native submit event
const submitBtn = document.getElementById("submit");
// No special click handler needed; the form's `submit` event handles everything.
// Keeping only native behavior prevents calling `.submit()` on a non-form element.
if (submitBtn && registerForm) {
    // Intentionally empty.
}


const fullname = document.getElementById("fullname");

const email = document.getElementById("email");

const phone = document.getElementById("phone");

const nid = document.getElementById("nid");

const password = document.getElementById("password");

const confirmPassword = document.getElementById("confirmPassword");

const strengthBar = document.getElementById("strengthBar");
const role = document.getElementById("role");
const terms = document.getElementById("terms");
const registerStatus = document.getElementById("registerStatus");






// =====================================
// VALIDATE EMAIL
// =====================================


function validateEmail(value){

    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);

}






// =====================================
// ERROR FUNCTIONS
// =====================================


function showError(id){

    const error = document.getElementById(id);

    if(error){

        error.style.display="block";

    }

}



function hideError(id){

    const error = document.getElementById(id);

    if(error){

        error.style.display="none";

    }

}

function setStatus(message = "") {
    if (registerStatus) {
        registerStatus.textContent = message;
        registerStatus.style.display = message ? "block" : "none";
    }
}






// =====================================
// PASSWORD STRENGTH
// =====================================


if(password){


    password.addEventListener("input",function(){


        let strength = 0;


        let value = password.value;



        if(value.length >= 6){

            strength++;

        }


        if(/[A-Z]/.test(value)){

            strength++;

        }


        if(/[0-9]/.test(value)){

            strength++;

        }


        if(/[^A-Za-z0-9]/.test(value)){

            strength++;

        }





        if(strengthBar){


            if(strength === 0){

                strengthBar.style.width="0%";

            }


            else if(strength === 1){

                strengthBar.style.width="25%";

            }


            else if(strength === 2){

                strengthBar.style.width="50%";

            }


            else if(strength === 3){

                strengthBar.style.width="75%";

            }


            else{

                strengthBar.style.width="100%";

            }


        }



    });


}








// =====================================
// REGISTER SUBMIT
// =====================================


if (registerForm) {

    registerForm.addEventListener("submit", function (e) {


    e.preventDefault();

    setStatus();



    let valid = true;






    // FULL NAME

    if(fullname.value.trim()===""){


        showError("nameError");

        valid=false;


    }

    else{


        hideError("nameError");


    }








    // EMAIL

    if(!validateEmail(email.value)){


        showError("emailError");

        valid=false;


    }

    else{


        hideError("emailError");


    }








    // PHONE

    if(phone.value.trim()===""){


        showError("phoneError");

        valid=false;


    }

    else{


        hideError("phoneError");


    }








    // NATIONAL ID

    if(nid.value.trim()===""){


        showError("nidError");

        valid=false;


    }

    else{


        hideError("nidError");


    }








    // PASSWORD

    if(password.value.length < 6){


        showError("passwordError");

        valid=false;


    }

    else{


        hideError("passwordError");


    }








    // CONFIRM PASSWORD

    if(password.value !== confirmPassword.value){


        showError("confirmError");

        valid=false;


    }

    else{


        hideError("confirmError");


    }

    // ACCOUNT TYPE
    if (!role.value) {
        showError("roleError");
        valid = false;
    } else {
        hideError("roleError");
    }

    // TERMS
    if (!terms.checked) {
        showError("termsError");
        valid = false;
    } else {
        hideError("termsError");
    }

    // ==============================
    // SEND TO DJANGO API
    // ==============================


    if(valid){

        submitBtn.disabled = true;
        submitBtn.textContent = "Creating account...";



        const userData = {


            full_name: fullname.value.trim(),


            email: email.value.trim(),


            phone: phone.value.trim(),


            national_id: nid.value.trim(),


            password: password.value,


            confirm_password: confirmPassword.value,

            role: role.value



        };





        fetch(
            "http://127.0.0.1:8000/api/register/",
            {


            method:"POST",


            headers:{


                "Content-Type":"application/json"


            },


            body:JSON.stringify(userData)



        })





        .then(async response => {
            const data = await response.json().catch(() => ({}));
            if (!response.ok) {
                throw new Error(data.error || "Registration failed");
            }
            return data;
        })





        .then(data => {



            console.log(data);




            if(data.message === "Registration successful."){



                alert(
                    "Registration successful. Please login."
                );



                window.location.href="login.html";



            }



            else{


                setStatus(data.error || "Registration failed.");


            }




        })






        .catch(error => {



            console.error(error);
            setStatus(error.message || "Cannot connect to server. Start the Django server and try again.");



        })
        .finally(() => {
            submitBtn.disabled = false;
            submitBtn.textContent = "Create Account";
        });




    }





});



}
