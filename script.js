function sendMessage() {
    fetch('/send-message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            channel_id: '1200971345173938267',
            message: 'Hello from Discord bot!',
        }),
    })
        .then(response => response.text())
        .then(data => {
            console.log(data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}