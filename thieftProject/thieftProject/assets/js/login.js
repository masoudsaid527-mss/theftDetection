// =====================================
// GET ELEMENTS
// =====================================

const loginForm = document.getElementById("loginForm");

const email = document.getElementById("email");

const password = document.getElementById("password");



// =====================================
// VALIDATE EMAIL
// =====================================

function validateEmail(value) {

    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);

}



// =====================================
// ERROR FUNCTIONS
// =====================================

function showError(id) {

    const element = document.getElementById(id);

    if (element) {
        element.style.display = "block";
    }

}


function hideError(id) {

    const element = document.getElementById(id);

    if (element) {
        element.style.display = "none";
    }

}



// =====================================
// LOGIN FUNCTION
// =====================================

if (loginForm) {


    loginForm.addEventListener("submit", function(e) {


        e.preventDefault();



        let valid = true;



        // =============================
        // CHECK EMAIL
        // =============================

        if (!validateEmail(email.value.trim())) {


            showError("emailError");

            valid = false;


        } else {


            hideError("emailError");


        }





        // =============================
        // CHECK PASSWORD
        // =============================

        if (password.value.trim() === "") {


            showError("passwordError");

            valid = false;


        } else {


            hideError("passwordError");


        }




        // STOP IF INVALID

        if (!valid) {

            return;

        }





        // =============================
        // SEND LOGIN DATA
        // =============================

        const loginData = {


            email: email.value.trim(),

            password: password.value


        };





        fetch("http://127.0.0.1:8000/api/login/", {


            method: "POST",


            headers: {


                "Content-Type": "application/json"

            },


            body: JSON.stringify(loginData)


        })





        .then(response => {


            return response.json().then(data => ({


                status: response.status,

                data: data


            }));


        })






        .then(result => {


            console.log(result);



            // =============================
            // SUCCESS LOGIN
            // =============================

            if (result.status === 200) {


                alert("Login successful");



                // Save user information

                if (result.data.user) {


                    localStorage.setItem(

                        "loggedInUser",

                        JSON.stringify(result.data.user)

                    );



                    localStorage.setItem(

                        "userRole",

                        result.data.user.role

                    );


                }





                // Redirect

                const dashboards = {
                    citizen: "citizen/dashboard.html",
                    police: "police/dashboard.html",
                    admin: "admin/dashboard.html",
                    policymaker: "policymaker/dashboard.html"
                };
                const destination = dashboards[result.data.user && result.data.user.role];

                if (destination) {
                    window.location.href = destination;
                } else {
                    localStorage.removeItem("loggedInUser");
                    localStorage.removeItem("userRole");
                    alert("This account does not have a valid role. Please contact an administrator.");
                }



            }





            // =============================
            // LOGIN FAILED
            // =============================

            else {


                alert(

                    result.data.error ||

                    "Invalid email or password"

                );


            }



        })






        .catch(error => {


            console.error(
                "Error:",
                error
            );


            alert(
                "Cannot connect to server"
            );


        });





    });


}
