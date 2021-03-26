const timers = JSON.parse(document.getElementById('timers').textContent);
const starttime = Date.parse(timers.start) / 1000;
const endtime = Date.parse(timers.end) / 1000;

function makeTimer() {
    let now = new Date();
    now = Date.parse(now) / 1000;
    const button = $('#button');
    if(now > starttime && now < endtime){
        if(button.hasClass('disabled')){
            button.removeClass('disabled');
        }
    }
    else if(!button.hasClass('disabled')){
        button.addClass('disabled');
    }
    if(now < starttime){
        timeLeft = starttime - now;
        let days = Math.floor(timeLeft / 86400); 
        let hours = Math.floor((timeLeft - (days * 86400)) / 3600);
        let minutes = Math.floor((timeLeft - (days * 86400) - (hours * 3600 )) / 60);
        let seconds = Math.floor((timeLeft - (days * 86400) - (hours * 3600) - (minutes * 60)));

        if (days < "10") { days = "0" + days; }
        if (hours < "10") { hours = "0" + hours; }
        if (minutes < "10") { minutes = "0" + minutes; }
        if (seconds < "10") { seconds = "0" + seconds; }

        $("#days").html(`<span class='timerSpan'>${days} <span class="dhms"> Days<span/></span>`);
        $("#hours").html(`<span class='timerSpan'>${hours} <span class="dhms"> Hours<span/></span>`);
        $("#minutes").html(`<span class='timerSpan'>${minutes} <span class="dhms"> Minutes<span/></span>`);
        $("#seconds").html(`<span class='timerSpan'>${seconds} <span class="dhms"> Seconds<span/></span>`);
    }
    else{
        $("#days").html(`<span class='timerSpan'>00 <span class="dhms"> Days<span/></span>`);
        $("#hours").html(`<span class='timerSpan'>00 <span class="dhms"> Hours<span/></span>`);
        $("#minutes").html(`<span class='timerSpan'>00 <span class="dhms"> Minutes<span/></span>`);
        $("#seconds").html(`<span class='timerSpan'>00 <span class="dhms"> Seconds<span/></span>`);
    }
}
makeTimer();
$('#button').click(function (e) {
    e.preventDefault();
    if ($(this).hasClass('disabled'))
      return false;
    else
      window.location.href = $(this).attr('href');
});
setInterval(function() { makeTimer(); }, 1000);