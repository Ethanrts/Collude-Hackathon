function submit() {
    // alert(event);
    // event.preventDefault();
    let em = document.getElementById('email').value;
    let pw = document.getElementById('password').value;

    console.log(em);
    fetch('https://c1dc-169-235-64-155.ngrok.io/login?email=' + em + '&password=' + pw)
        .then(response => response.json())
        .then(function(response) {
            if (response.status) {
                document.getElementById('email');
                window.location = './welcome.html?status=' + response.status;

            } else {
                document.getElementById('email');
                window.location = './signin.html' + response.status;

            }
        })

}

function submit2() {
    // alert(event);
    // event.preventDefault();
    let emi = document.getElementById('email').value;
    let pwa = document.getElementById('password').value;
    let pwa2 = document.getElementById('password2').value;


    console.log(emi);
    console.log(pwa);
    console.log(pwa2);
    fetch('https://c1dc-169-235-64-155.ngrok.io/sign_up?email=' + emi + '&password=' + pwa + '&password2=' + pwa2)
        .then(response => response.json())
        .then(function(response) {
            if (response.status) {
                window.location = './welcome.html?status=' + response.status;
                document.getElementById('email');

            } else {
                document.getElementById('email')
                alert("Invalid Password");
                window.location = './signup.html';

            }
        })

}

function load() {
    // groceries = ['eg', 'sgtek']
    // read the groceries in the url
    document.getElementById('display').innerHTML = '<div class="lists">'

    for (let i = 0; i < groceries.length; i++) {
        document.getElementById('display').innerHTML += '<div>' + groceries[i] + '</div>';
    }

    document.getElementById('display').innerHTML += '</div>'

}