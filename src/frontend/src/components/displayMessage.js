import { useState, useEffect } from 'react'

function DisplayMessage() {
    // The initial state will be an empty string
    const [message, setMessage] = useState('')

    // Call Flask backend to get current message
    useEffect(() => {
        fetch("updateMessage")
            .then(
                response => response.json()
                    .then(
                        data => {
                            setMessage(data)
                        }
                    )
            )
    }, ''
    );

    return (
        <div>
            <h1>{message}</h1>
            <h4>
                <a href="https://medium.com/@ianfergusonrva" target="_blank" rel="noreferrer">Follow me on Medium</a> for more
            </h4>
        </div>
    )
}

export default DisplayMessage;