const skillValuesSubmit= document.querySelector('#skill-values');
const responsibilityValuesSubmit= document.querySelector('#responsibility-values');
const skillValuesArr = [];
const responsibilityValuesArr = [];
document.querySelector('#submit-form-btn').addEventListener('click', function(ev){
    let responsibilities = document.getElementsByClassName('responsibility-text');
    for(let i=0;i<responsibilities.length;i++){
        responsibilityValuesArr.push(responsibilities[i].textContent);
    }
    responsibilityValuesSubmit.value = responsibilityValuesArr.join('(*)');
    let skills = document.getElementsByClassName('skill-text');
    for(let i=0;i<skills.length;i++){
        skillValuesArr.push(skills[i].innerHTML);
    }
    skillValuesSubmit.value = skillValuesArr.join('(*)');
    console.log(responsibilityValuesSubmit.value);
    console.log(skillValuesSubmit.value);
});