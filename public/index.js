
const socket = io();

const btnIniciar = document.getElementById('iniciar');
const notification = document.getElementById('notificacion');
btnIniciar.disabled = true;
var init = false;

socket.on('connect', ()=>{
    console.log("Live stream vigilancia conectado");
})

socket.on('disconnect', ()=>{
    console.log("Live stream vigilancia conectado");
})


socket.on('notification', (value)=>{
    if(value.msg){
        btnIniciar.disabled = false;
        document.getElementById('not').style.display ="block"
    }
});

function detener()
{
    socket.close();
}

function reanudar()
{
    init = true;
    socket.connect();

}

function cerrar()
{
    document.getElementById('not').style.display ="none";
}


socket.on('video', (image) => {
    console.log(socket.id)
    console.log(image.data)
    if(init)
    {
        var img = document.getElementById('play');
        img.src = "data:image/jpg;base64,"+image.data;
    }
})


