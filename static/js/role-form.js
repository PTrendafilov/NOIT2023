const clientInput = document.getElementById('input-client');
const freelancerInput = document.getElementById('input-freelancer');
const teamleaderInput = document.getElementById(id='input-teamleader');
const submitFormBtn = document.getElementById('submit-form-btn');
const inputs = document.getElementsByClassName('role-input');
freelancerInput.addEventListener("click", function(){
    submitFormBtn.value = 'Включи се като ученик';
    for(let i=0; i < inputs.length; i++){
        inputs[i].parentElement.classList.remove('clicked');
    }
    freelancerInput.parentElement.classList.add('clicked');
});
clientInput.addEventListener("click", function(){
    submitFormBtn.value = 'Включи се като бизнес';
    for(let i=0; i < inputs.length; i++){
        inputs[i].parentElement.classList.remove('clicked');
    }
    clientInput.parentElement.classList.add('clicked');
});
teamleaderInput.addEventListener("click", function(){
    submitFormBtn.value = 'Включи се като ментор';
    for(let i=0; i < inputs.length; i++){
        inputs[i].parentElement.classList.remove('clicked');
    }
    teamleaderInput.parentElement.classList.add('clicked');
});