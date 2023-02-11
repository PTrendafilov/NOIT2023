const popularSkills = [
  "Web Development",
  "Mobile Development",
  "Data Science",
  "Digital Marketing",
  "Graphic Design",
  "Writing",
  "Translation",
  "Content Creation",
  "Video Editing",
  "App Development",
  "JavaScript",
  "Python",
  "Java",
  "C++",
  "Ruby",
  "PHP",
  "C#",
  "Swift",
  "Go",
  "Kotlin",
  "React",
  "Angular",
  "Vue.js",
  "Ruby on Rails",
  "Django",
  "Laravel",
  "Express.js",
  "CSS",
  "HTML",
  "JS",
  'Machine Learning',
  'Chat GPT',
  'Open AI',
  'Deep Learning',
  'Neural Networks',
  'Data Analysis',
  'Web Scraping',
  'Selenium',
  'Data Scraping',
  'Tensorflow',
  'Design',
  'UI Design',
  'UX Design',
  'Animations',
  'Unity',
  'Visual Basic',
  'Quality Assurance',
  'Flask',
  'Game Development',
  'Wordpress',
  'Copywriting',
  'Video Editing',
  'Programming',
  'Problem Solving',
  'Subtitling',
  'SEO',
  'Android',
  'iOS',
  'Digital Marketing',
  'Developing',
  'SQL',
  'Cybersecurity',
  'Data Visualization',
  'Marketing',
  'Editing',
  'Data Entry',
];

const skillTextbox = document.querySelector('#skill-textbox');
//console.log(skillTextbox.parentElement)
const optionsContainer = document.createElement('ul');
optionsContainer.setAttribute('id', 'options-skills-autocomplete');
optionsContainer.style.display = 'none';
skillTextbox.parentElement.parentElement.appendChild(optionsContainer);

skillTextbox.addEventListener('input', function () {
  const val = this.value;
  const options = popularSkills.filter(function (skill) {
    return skill.toLowerCase().startsWith(val.toLowerCase());
  });
  optionsContainer.innerHTML = '';
  options.forEach(function (option) {
    const optionElement = document.createElement('li');
    optionElement.textContent = option;
    optionElement.classList.add('skills-autocomplete-option');
    optionElement.addEventListener("click", addOption);
    if (skillTextbox.value.length !== 0) {
      optionsContainer.appendChild(optionElement);
    }

  });
  if (options.length > 0 && options.length != popularSkills.length) {
    optionsContainer.style.display = 'block';
  } else {
    optionsContainer.style.display = 'none';

  }
});
const addSkillBtn = document.querySelector('#add-skill');
function addOption(ev){
  //console.log(ev.target);
  skillTextbox.value = ev.target.textContent;
  addSkillBtn.click()
}