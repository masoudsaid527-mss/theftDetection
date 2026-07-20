// =====================================
// APP.JS
// GLOBAL FRONTEND FUNCTIONS
// =====================================



// =====================================
// MOBILE MENU
// =====================================


const menuButton = document.querySelector(".menu-btn");
const navigation = document.querySelector("nav");


if(menuButton && navigation){


    menuButton.addEventListener("click", () => {


        if(navigation.style.display === "block"){


            navigation.style.display = "none";


        }else{


            navigation.style.display = "block";


        }


    });


}







// =====================================
// FAQ
// =====================================


const faqButtons = document.querySelectorAll(".faq-question");


faqButtons.forEach(button=>{


    button.addEventListener("click",()=>{


        const answer = button.nextElementSibling;



        if(answer.style.display==="block"){


            answer.style.display="none";


        }else{


            answer.style.display="block";


        }


    });


});







// =====================================
// CONTACT FORM
// =====================================


const form=document.querySelector("form");


if(form){


form.addEventListener("submit",function(e){


    e.preventDefault();



    alert(
        "Your message has been sent successfully."
    );



    form.reset();



});


}







// =====================================
// AUTHENTICATION SYSTEM
// =====================================



// GET CURRENT USER

function getCurrentUser(){


    const user = localStorage.getItem(
        "loggedInUser"
    );


    if(user){


        return JSON.parse(user);


    }



    return null;


}








// CHECK LOGIN

function checkLogin(){


    const user = getCurrentUser();



    if(!user){


        window.location.href =
        "../login.html";


    }


}







// SHOW USER NAME

function showUsername(){


    const user = getCurrentUser();


    const username =
    document.getElementById(
        "username"
    );



    if(user && username){


        username.innerHTML =
        user.email;


    }


}







// LOGOUT

function logout(){



    localStorage.removeItem(
        "loggedInUser"
    );


    localStorage.removeItem(
        "userRole"
    );



    window.location.href =
    "../login.html";


}







// AUTO LOAD

document.addEventListener(
"DOMContentLoaded",
()=>{


    showUsername();


});