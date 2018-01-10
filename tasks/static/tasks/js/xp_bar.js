const completed_tasks = parseInt(document.currentScript.getAttribute('tasks-completed'));
const level = Math.floor(completed_tasks/10); //Should correspond to colour
const progress_bar = document.getElementsByClassName('progress-bar')[0];
                //1 Level = 10 tasks by default (adjustable?)
switch(level) {
  case 0:
    progress_bar.style.backgroundColor = "#9E9E9E";
    progress_bar.parentNode.style.backgroundColor = "#F1F1F1";
    break;
  case 1:
    progress_bar.style.backgroundColor = "#A0B0BF";
    progress_bar.parentNode.style.backgroundColor = "#DDEEFF";
    
    break;
  case 2:
    progress_bar.style.backgroundColor = "#7A3BE3";
    progress_bar.parentNode.style.backgroundColor = "#B082FF";
    break;
  case 3:
    progress_bar.style.backgroundColor = "#C01FD0";
    progress_bar.parentNode.style.backgroundColor = "#F489FF";
    break;
  default:
    progress_bar.style.backgroundColor = "#D44040";
    progress_bar.parentNode.style.backgroundColor = "#FF9B9B";
    break;
}

//Colours:
//L1: #9E9E9E
//L2: #A0B0BF
//L3: #7A3BE3
//L4: #C01FD0
//L5: #D44040
//Announce winners monthly, then reset exp

progress_bar.style.width = String(((completed_tasks%10)/10)*100)+"%"