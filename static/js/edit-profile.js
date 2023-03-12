const skillValuesSubmit= document.querySelector('#skill-values');
const skillValuesArr = [];
document.querySelector('#submit-form-btn').addEventListener('click', function(ev){
    //ev.preventDefault();
    let skills = document.getElementsByClassName('skill-text');
    for(let i=0;i<skills.length;i++){
        skillValuesArr.push(skills[i].innerHTML);
    }
    skillValuesSubmit.value = skillValuesArr.join('(*)');
    console.log(skillValuesSubmit.value);
});