import React, {useState, useEffect} from 'react'
import {createRoot} from 'react-dom/client'
import './popup.css'

function App() {
    const [data, setData] = useState('');

    useEffect(() => {
        fetch('http://localhost:5000/get-date')
            .then(response => response.json())
            .then(data => setData(data.date))
            .catch(error => console.error('Error fetching date:', error));
    }, []);

    return (
        <div>
            <h1>Prayer Times in Tampa</h1>
            <p>Current Date: {data}
            
            
            </p>
        </div>
    );
}


const container = document.createElement('div');
document.body.appendChild(container);
const root = createRoot(container);
root.render(<App />);