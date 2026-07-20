// =====================================
// CITIZEN DASHBOARD.JS
// =====================================


// =====================================
// CHECK LOGIN
// =====================================

document.addEventListener(
"DOMContentLoaded",
function(){


    checkLogin();


    loadUser();


    loadCases();


    loadNotifications();


});





// =====================================
// GET USER
// =====================================


function loadUser(){


    const user = getCurrentUser();



    if(user){


        const username =
        document.getElementById(
            "username"
        );



        const email =
        document.getElementById(
            "email"
        );



        if(username){

            username.innerHTML =
            user.username || user.email;

        }



        if(email){

            email.innerHTML =
            user.email;

        }


    }


}







// =====================================
// LOAD CASES
// =====================================


function loadCases(){



    fetch(
        "http://127.0.0.1:8000/api/cases/"
    )



    .then(response=>response.json())



    .then(data=>{



        let cases = data.length;



        const caseCount =
        document.getElementById(
            "caseCount"
        );



        if(caseCount){


            caseCount.innerHTML =
            cases;


        }



    })



    .catch(error=>{


        console.log(
            "Cases error:",
            error
        );


    });



}







// =====================================
// LOAD NOTIFICATIONS
// =====================================


function loadNotifications(){



    fetch(
        "http://127.0.0.1:8000/api/notifications/"
    )



    .then(response=>response.json())



    .then(data=>{



        const notificationCount =
        document.getElementById(
            "notificationCount"
        );



        if(notificationCount){


            notificationCount.innerHTML =
            data.length;


        }



    })



    .catch(error=>{


        console.log(
            "Notification error:",
            error
        );


    });



}







// =====================================
// NAVIGATION BUTTONS
// =====================================



function openProfile(){


    window.location.href =
    "profile.html";


}





function reportTheft(){


    window.location.href =
    "report.html";


}





function myCases(){


    window.location.href =
    "cases.html";


}






// =====================================
// LOGOUT
// =====================================


function logoutUser(){


    localStorage.removeItem(
        "loggedInUser"
    );


    localStorage.removeItem(
        "userRole"
    );


    window.location.href =
    "../login.html";


}