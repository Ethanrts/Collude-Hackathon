function submit() {
    // alert(event);
    // event.preventDefault();
    let em = document.getElementById('email').value;
    let pw = document.getElementById('password').value;

    console.log(em);
    fetch('https://1e5f-169-235-64-155.ngrok.io/login?email=' + em + '&password=' + pw)
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
    fetch('https://1e5f-169-235-64-155.ngrok.io/sign_up?email=' + emi + '&password=' + pwa + '&password2=' + pwa2)
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
    fetch('https://1e5f-169-235-64-155.ngrok.io/list')
        .then(response => response.json())
        .then(function(response) {
            console.log(response)
            document.getElementById('display').innerHTML = '';
            Object.keys(response).forEach(function(category) {
                document.getElementById('display').innerHTML += '<div> <p><strong>' + category + '</strong></p>';
                response[category].forEach(function(item) {
                    document.getElementById('display').innerHTML += '<p onclick="add(`' + item + '`)">' + item + '</p>';
                });
                document.getElementById('display').innerHTML += '</div>';
            })
        })
    document.getElementById('display').innerHTML = '<div class="lists">'

    for (let i = 0; i < groceries.length; i++) {
        document.getElementById('display').innerHTML += '<div>' + groceries[i] + '</div>';
    }

    document.getElementById('display').innerHTML += '</div>'

}
clickedStuff = []

function add(item) {
    clickedStuff.push(item);
    console.log('user clicked', clickedStuff);
}

function submit3() {
    // fetch('https://1e5f-169-235-64-155.ngrok.io/result')
    //     .then(response => response.json())
    //     .then(function(response) {
    //         for (i = 0; i < clickedStuff.length; i++) {
    //             document.write(clickedStuff[i] + "<br />");
    //         }

    //     })
    window.location = './result.html?cart=' + JSON.stringify(clickedStuff);
}

function resultLoad() {
    const queryString = window.location.search;

    const urlParams = new URLSearchParams(queryString);
    const flist = JSON.parse(urlParams.get('cart'))

    console.log(flist)
    flist.forEach(function(ingredient) {

        document.getElementById('flist').innerHTML += '<div>' + ingredient + '</div>'
    })

}