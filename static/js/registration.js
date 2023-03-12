const firstNameElement = document.getElementById('first-name');
const lastNameElement = document.getElementById('last-name');
const emailElement = document.getElementById('email');
const passwordElement = document.getElementById('password');
const submitElement = document.getElementById('submit-form-btn');
const usernameElement = document.getElementById('username');

usernameElement.addEventListener('input', validateUsername);
firstNameElement.addEventListener('input', validateFirstName);
lastNameElement.addEventListener('input', validateLastName);
emailElement.addEventListener('input', validateEmail);
passwordElement.addEventListener('input', validatePassword);

function validateUsername(){
    if (usernameElement.value.length < 3) {
        usernameElement.nextElementSibling.setAttribute('class', '');
        usernameElement.nextElementSibling.setAttribute('class', 'fa-solid fa-exclamation');
        usernameElement.classList.add('invalid');
        usernameElement.classList.remove('valid');


    } else {
        usernameElement.nextElementSibling.setAttribute('class', '');
        usernameElement.nextElementSibling.setAttribute('class', 'fa fa-regular fa-circle-check');
        usernameElement.classList.remove('invalid');
        usernameElement.classList.add('valid');
    }
}

function validateFirstName() {
    if (firstNameElement.value.length < 3) {
        firstNameElement.nextElementSibling.setAttribute('class', '');
        firstNameElement.nextElementSibling.setAttribute('class', 'fa-solid fa-exclamation');
        firstNameElement.classList.add('invalid');
        firstNameElement.classList.remove('valid');


    } else {
        firstNameElement.nextElementSibling.setAttribute('class', '');
        firstNameElement.nextElementSibling.setAttribute('class', 'fa fa-regular fa-circle-check');
        firstNameElement.classList.remove('invalid');
        firstNameElement.classList.add('valid');
    }
}

function validateLastName() {
    if (lastNameElement.value.length < 3) {
        lastNameElement.nextElementSibling.setAttribute('class', '');
        lastNameElement.nextElementSibling.setAttribute('class', 'fa-solid fa-exclamation');
        lastNameElement.classList.add('invalid');
        lastNameElement.classList.remove('valid');
    } else {
        lastNameElement.nextElementSibling.setAttribute('class', '');
        lastNameElement.nextElementSibling.setAttribute('class', 'fa fa-regular fa-circle-check');
        lastNameElement.classList.remove('invalid');
        lastNameElement.classList.add('valid');

    }
}

function validateEmail() {
    regex = /^\w+([.-]?\w+)@\w+([.-]?\w+)(.\w{2,3})+$/;
    if (!emailElement.value.match(regex)) {
        emailElement.nextElementSibling.setAttribute('class', '');
        emailElement.nextElementSibling.setAttribute('class', 'fa-solid fa-exclamation');
        emailElement.classList.add('invalid');
        emailElement.classList.remove('valid');
    } else {
        emailElement.nextElementSibling.setAttribute('class', '');
        emailElement.nextElementSibling.setAttribute('class', 'fa fa-regular fa-circle-check');
        emailElement.classList.remove('invalid');
        emailElement.classList.add('valid');
    }
}
let lowerCaseLetters = /[a-z]/g;
let upperCaseLetters = /[A-Z]/g;
let number = /[0-9]/g;

function checkLowerCase(password) {
    if (!password.match(lowerCaseLetters)) {
        console.log('You must have lowercase letters');
        return false;
    }
    return true;
}

function checkUpperCase(password) {
    if (!password.match(upperCaseLetters)) {
        console.log('You must have uppercase letters');
        return false;
    }
    return true;
}

function checkNumbers(password) {
    if (!password.match(number)) {
        console.log('You must have numbers');
        return false;
    }
    return true;
}

function validatePassword() {
    if (passwordElement.value.length < 8 || !checkNumbers(passwordElement.value) || !checkUpperCase(passwordElement.value) || !checkLowerCase(passwordElement.value)) {
        passwordElement.nextElementSibling.setAttribute('class', '');
        passwordElement.nextElementSibling.setAttribute('class', 'fa-solid fa-exclamation');
        passwordElement.classList.add('invalid');
        passwordElement.classList.remove('valid');
    } else {
        passwordElement.nextElementSibling.setAttribute('class', '');
        passwordElement.nextElementSibling.setAttribute('class', 'fa fa-regular fa-circle-check');
        passwordElement.classList.remove('invalid');
        passwordElement.classList.add('valid');
    }
}