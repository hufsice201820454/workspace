const drawbutton = document.getElementById('drawbutton');
const messagediv = document.getElementById('message');

function drawLottery(){
    return new Promise((resole, reject) => {
        setTimeout(()=>{
            const isWinner = Math.random() < 0.5;
            isWinner ? resolve("당첨되었습니다.") : reject("꽝! 다음 기회에...");
        }, 1000);
    });
}

drawbutton.addEventListener('click', async () =>{
    messagediv.textContent = "1초 후에 당첨 결과가 발표됩니다.";
    messagediv.className = 'message';

    try{
        const result = await drawLottery();
        messagediv.textContent = result;
        messagediv.classList.add('success');
    } catch (error){
        messagediv.textContent = error;
        messagediv.classList.add('failure');
    }
    // drawLottery()
    //     .then(result =>{
    //         messagediv.textContent = result;
    //         messagediv.classList.add('success');
    //     })
    //     .catch(error => {
    //         messagediv.textContent = error;
    //         messagediv.classList.add('failure');
    //     });

    
});