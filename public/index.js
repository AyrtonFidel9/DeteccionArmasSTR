
const socket = io();


socket.on('connect', ()=>{
    console.log("Live stream vigilancia conectado")
})

socket.on('disconnect', ()=>{
    console.log("Live stream vigilancia conectado")
})

socket.on('video', (image) => {
    console.log(socket.id)
    console.log(image.data)
    var img = document.getElementById('play');

    img.src = "data:image/jpg;base64,"+image.data;
})

socket.on('notification', (value)=>{
    if(value.msg){
        document.getElementById('not').style.display ="block"
        document.getElementById('not').innerText = "!!!Arma detectada!!!";
    }
})


