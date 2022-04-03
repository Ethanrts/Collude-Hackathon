function submit() {
    userInohyht = document.getElementById('user').value;
    console.log(userInohyht)
    fetch('https://610c-169-235-64-155.ngrok.io?username=' + userInohyht)
    .then(response => response.json())
    .then(function (response) {
        console.log('server response', response);
        if(response.content) document.getElementById('user').style.backgroundColor = 'green';
    })


    userInohyht = document.getElementById('pass').value;
    console.log(userInohyht)
    fetch('https://610c-169-235-64-155.ngrok.io?username=' + userInohyht)
    .then(response => response.json())
    .then(function (response) {
        console.log('server response', response);
        if(response.content) document.getElementById('pass').style.backgroundColor = 'green';
    })
}
