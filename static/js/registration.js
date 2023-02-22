const firstNameElement = document.getElementById('first-name');
const lastNameElement = document.getElementById('last-name');
const emailElement = document.getElementById('email');
const passwordElement = document.getElementById('password');
const submitElement = document.getElementById('submit-form-btn');

firstNameElement.addEventListener('input', validate_first_name);

function validate_first_name(event){
    const firstNameValue = event.target.value;
    const regex = /^[a-zA-Z]+$/;
    const isValid = regex.test(firstNameValue);
    if(isValid){
      firstNameElement.classList.remove('invalid');
    } else {
      firstNameElement.classList.add('invalid');
    }
}
/*
submitElement.addEventListener('click', validate);
function validate(ev) {
    ev.preventDefault();
    function validateFirstName(firstName) {
        if (firstName.length < 3) {
            console.log('Incorrect first name');
            return false;
        }
        return true;
    }
    function validateLastName(lastName) {
        if (lastName.length < 3) {
            console.log('Incorrect last name');
            return false;
        }
        return true;
    }
    function validateEmail(email) {
        regex = /^\w+([.-]?\w+)@\w+([.-]?\w+)(.\w{2,3})+$/;
        if (!email.match(regex)) {
            console.log('Incorrect email')
            return false;
        }
        return true;
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
    function validatePassword(password) {
        if (password.length < 8 || !checkNumbers(password) || !checkUpperCase(password) || !checkLowerCase(password)) {
            console.log('Incorrect password');
            return false;
        }
        return true;
    }
    let firstName = firstNameElement.value;
    let lastName = lastNameElement.value;
    let email = emailElement.value;
    let password = passwordElement.value;
    validateFirstName(firstName);
    validateLastName(lastName);
    validateEmail(email);
    validatePassword(password);
}
*/