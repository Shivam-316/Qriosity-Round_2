const progressBarFull = document.getElementById('progressBarFull');
const progressText = document.getElementById('progressText');
const data = JSON.parse(document.getElementById('data').textContent);
const choice_containers = Array.from(document.getElementsByClassName('choice-container'));
const choices = Array.from(document.getElementsByClassName('choice-text'));
const timer = document.getElementById('timer');
const question = document.getElementById('question');
const loader = document.getElementById('loader');
const game = document.getElementById('game');
let time_counter = time_taken = original_time = data.timer;
let acceptingAnswer = true;
let selectedChoice = null;

/*For Chocie Selection*/
choices.forEach((choice) => {
    choice.addEventListener('click', (e) => {
        if(acceptingAnswer){
            acceptingAnswer=false;
            time_taken -= time_counter; 
            selectedChoice = e.target;
            selectedChoice.parentElement.classList.add('choosen');
            choice_containers.forEach((choice_container)=>{
                choice_container.classList.remove('choice_hover')
            });
            const selectedAnswer = selectedChoice.textContent;
            let classToApply;
            $('#answer-form #id_answer').val(selectedAnswer);
            const form = $('#answer-form');
            $.ajax({
                type:'POST',
                url: form.attr("action"),
                data:form.serialize(),
                success: function(response){
                    if(response.isCorrect === false){
                        time_taken = original_time;
                    }
                },
                error: function (error) {
                    console.log(error);
                }
            });
        }
    });
});

/*For Timer*/
function checkTimer(){
    if(time_counter < 0){
        clearInterval(timer_async);
        nextQuestion();
    }
    else{
        Timer();
    }
}
function Timer(){
    timer.textContent = time_counter;
    time_counter-=1;
}

/*For Next Question*/
function nextQuestion(){
    game.classList.add('hidden');
    loader.classList.remove('hidden');
    $('#next-question-form #id_time').val(time_taken);
    const form = $('#next-question-form');
    $.ajax({
        type:'POST',
        url: form.attr("action"),
        data:form.serialize(),
        success: function(response){
            if(response.winner === true){
                location.reload();
            }
            else{
                set_quiz_data(response);
                setTimeout(function(){
                    loader.classList.add('hidden');
                    game.classList.remove('hidden');
                },1000);
                timer_async = setInterval(checkTimer, 1000);
                acceptingAnswer = true;
            }
        },
        error: function (error) {
            console.log(error);
        }
    });
}

function set_quiz_data(data){
    question.textContent = `Q. ${data.question}`;
    choices[0].textContent = data.A;
    choices[1].textContent = data.B;
    choices[2].textContent = data.C;
    choices[3].textContent = data.D;
    progressText.textContent = `Progress ${data.attempted}/${data.total_ques}`;
    progressBarFull.style.width = progressBarFull.textContent = `${data.progress}%`;
    time_counter = time_taken = original_time =data.timer
    if(selectedChoice !== null){
        selectedChoice.parentElement.classList.remove('choosen');
        selectedChoice=null;
    }
    choice_containers.forEach((choice_container)=>{
        choice_container.classList.add('choice_hover')
    });
}
set_quiz_data(data);
let timer_async = setInterval(checkTimer, 1000);