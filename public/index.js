
const socket = io();

const btnIniciar = document.getElementById('iniciar');
btnIniciar.disabled = true;
var init = false;

socket.on('connect', ()=>{
    console.log("Live stream vigilancia conectado");
})

socket.on('disconnect', ()=>{
    console.log("Live stream vigilancia conectado");
})

socket.on('video', (image) => {
    console.log(socket.id)
    console.log(image.data)
    if(init)
    {
        var img = document.getElementById('play');
        img.src = "data:image/jpg;base64,"+image.data;
    }
})

socket.on('notification', (value)=>{
    if(value.msg){
        btnIniciar.disabled = false;
        document.getElementById('not').style.display ="block"
        document.getElementById('not').innerText = "!!!Arma detectada!!!";
    }
})

function detener()
{
    socket.close();
}

function reanudar()
{
    init = True;
    socket.connect();
}

function cerrar()
{
    document.getElementById('not').style.display ="none"
}


