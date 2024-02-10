function sendMessage() {
    let nombre = $("#nombre").val();
    let detalle = $("#detalle").val();
    let patente = $("#patente").val();
    let tipo = $("#tipo").val();
    let imagen = $('#imageInput').prop('files')[0];

    // Crear un objeto FormData para enviar datos de formulario y archivos
    let formData = new FormData();
    formData.append('nombre', nombre);
    formData.append('detalle', detalle);
    formData.append('patente', patente);
    formData.append('tipo', tipo);
    formData.append('imagen', imagen);

    $.ajax({
        url: 'http://127.0.0.1:5000/enviar_mensaje_con_foto',
        type: 'POST',
        data: formData,
        contentType: false, // No establecer el tipo de contenido para FormData
        processData: false, // No procesar datos para FormData
        success: function(response) {
            // Manejar la respuesta del servidor
            console.log(response);
        },
        error: function(xhr, status, error) {
            // Manejar errores
            console.error(error);
        }
    });
}